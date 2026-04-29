# Fuzz4All Java Targeting — 改动说明与运行指南

> 本文档说明本次优化改动的内容、原因、运行方式和预期结果。
> 改动日期：2026-04-29 | 涉及提交：`440a720`

---

## 目录

1. [项目快速入门](#1-项目快速入门)
2. [本次改动总览](#2-本次改动总览)
3. [逐项改动说明](#3-逐项改动说明)
4. [如何运行](#4-如何运行)
5. [预期运行结果](#5-预期运行结果)
6. [常见问题排查](#6-常见问题排查)

---

## 1. 项目快速入门

Fuzz4All 是一个用大语言模型（LLM）驱动的 fuzzer，本项目在此基础上对 **Java 标准库 API** 进行定向 fuzz：

- LLM 根据 API 文档生成 Java 测试程序
- `javac` 编译验证，可选 `java` 运行时执行
- 根据编译/运行时错误自动提炼"规则"，刷新 LLM 提示词
- 对每个 API 按 5 维分类（RESOURCE、BUFFER、SECURITY 等）选择最匹配的变异算子

**目录结构（关键部分）：**

```
Fuzz4All/
├── fuzz.py                  # 主入口
├── make_target.py           # 根据 YAML 构造目标对象
├── target/
│   ├── target.py            # 基类：prompt 管理、变异调度、反馈闭环
│   └── JAVA/JAVA.py         # Java 子类：javac/java 验证、错误分类
└── mutation/
    ├── java_mutator.py      # 11 类变异算子
    └── profile_loader.py    # 5D 分类结果 → 变异 profile 映射

config/targeted/             # 每个 API 对应一个 YAML 配置
outputs/                     # fuzz 输出目录（自动创建）
```

---

## 2. 本次改动总览

| # | 改动文件 | 改动类型 | 一句话说明 |
|---|---------|---------|-----------|
| 1 | `target.py` | 删除死代码 | 移除 `update_strategy()` 及三个废弃 prompt 变量 |
| 2 | `target.py` | Bug 修复 | `generate_model()` 使用配置的 `max_length` 而非硬编码 1024 |
| 3 | `target.py` + `JAVA.py` | 重构 | Java 专用过滤逻辑下移至子类，修复误杀合法代码的 bug |
| 4 | `JAVA.py` | 新功能 | 实现 `runtime_feedback_mode`：编译成功后可选执行，捕获运行时异常 |
| 5 | `make_target.py` | Bug 修复 | `target_name` 按语言给出正确默认值（Java 默认 `javac`） |
| 6 | `java_mutator.py` | 核心重构 | RESOURCE 算子从硬编码3个类名改为动态识别任意资源类 |
| 7 | `profile_loader.py` | Bug 修复 | `mutation_profile_override` 区分 profile 名与分类标签两种语义 |
| 8 | `profile_loader.py` | 精度提升 | REFLECT 分类移除宽泛假阳性词 |
| 9 | 3 个 YAML 配置 | 补全 | 显式写入 `target_name: javac` |
| 10 | `当前进度与预期结果.md` | 文档修正 | 修正目录名和抽象方法描述的错误 |

---

## 3. 逐项改动说明

---

### 改动 1：删除死代码 `update_strategy()` 及关联变量

**文件：** `Fuzz4All/target/target.py`

**改了什么：**
- 删除 `__init__` 中的 `self.se_prompt`、`self.m_prompt`、`self.c_prompt` 三个变量的初始化
- 删除 `initialize()` 中将它们加入 EOS token 列表的代码
- 删除整个 `update_strategy()` 方法（约 15 行）

**为什么改：**

`update_strategy()` 是原始 Fuzz4All 论文的"in-context learning"机制——通过在 prompt 末尾追加指令（"请生成一个语义等价的程序"、"请变异前一个程序"）来引导 LLM。

当前架构已用 `_create_feedback_prompt()` 完全替代了这个机制：`update()` 直接根据编译失败规则和安全样例重建整个 prompt。`update_strategy()` 从未在任何调用链中被调用，但代码、变量、EOS token 全部保留，导致：

1. 阅读代码的人误以为两套机制同时工作
2. 三个 prompt 字符串被无谓地加入 EOS 列表，生成时会对 tokenizer 造成干扰（尽管 LLM 极少输出这些字符串）

**改前：**
```python
# __init__ 中
self.se_prompt = self.wrap_in_comment("Please create a semantically equivalent program...")
self.m_prompt  = self.wrap_in_comment("Please create a mutated program...")
self.c_prompt  = self.wrap_in_comment("Please combine the two previous programs...")
self.p_strategy = kwargs["prompt_strategy"]

# initialize() 中
eos = [
    self.prompt_used["separator"],
    "<eom>",
    self.se_prompt,   # ← 废弃
    self.m_prompt,    # ← 废弃
    self.c_prompt,    # ← 废弃
]
```

**改后：**
```python
# __init__ 中
self.p_strategy = kwargs["prompt_strategy"]  # 仅保留 -1 禁用开关

# initialize() 中
eos = [
    self.prompt_used["separator"],
    "<eom>",
]
```

> **注意：** `p_strategy == -1` 的"禁用所有更新"开关保留未动，YAML 中 `prompt_strategy: -1` 可以关闭 prompt 自动更新。

---

### 改动 2：`generate_model()` 使用配置的 `max_length`

**文件：** `Fuzz4All/target/target.py`（第 1057 行附近）

**改了什么：**
将主生成循环中的 `max_length=1024` 改为 `max_length=self.max_length`。

**为什么改：**

`self.max_length` 在 `Target.__init__` 中从 YAML 的 `llm.max_length` 读取，是用户可配置项。但 `generate_model()` 无论 YAML 写什么都硬编码使用 1024，使得该配置项对主循环生成完全无效。autoprompt 验证和 runtime refresh 各自使用了正确的配置值，只有主循环漏掉了。

**改前：**
```python
def generate_model(self) -> List[str]:
    return self._generate_with_prompt(
        self.prompt,
        batch_size=self.batch_size,
        temperature=self.temperature,
        max_length=1024,           # ← 硬编码，忽略配置
    )
```

**改后：**
```python
def generate_model(self) -> List[str]:
    return self._generate_with_prompt(
        self.prompt,
        batch_size=self.batch_size,
        temperature=self.temperature,
        max_length=self.max_length, # ← 使用 YAML llm.max_length
    )
```

---

### 改动 3：Java 专用过滤逻辑下移至子类，修复 `valid` 误判

**文件：** `Fuzz4All/target/target.py` + `Fuzz4All/target/JAVA/JAVA.py`

**改了什么：**

`target.py` 基类的 `_is_viable_generated_code()` 简化为仅做括号平衡检查（语言无关）：

```python
# target.py（基类）
def _is_viable_generated_code(self, code: str) -> bool:
    normalized = " ".join((code or "").split())
    if normalized.count("{") != normalized.count("}"):
        return False
    return True
```

`JAVA.py` 新增覆写方法，包含完整的 Java 专用检查：

```python
# JAVA.py（子类）
def _is_viable_generated_code(self, code: str) -> bool:
    if not super()._is_viable_generated_code(code):
        return False
    normalized = " ".join((code or "").split())
    if self._profile_rejects_generated_code(normalized):
        return False
    # 用词边界正则检查截断末尾，避免误杀含 "invalid" 的合法代码
    if re.search(r"\bvalid$", normalized):
        return False
    if normalized.endswith(("write(", "try {", "Buffered")):
        return False
    return True
```

**为什么改：**

原始代码中，含 Java 专用逻辑（`"Buffered"`、`".write("`）的检查放在**通用基类**中，被 C/C++/Go 等所有语言目标共享，逻辑上不正确。

更严重的问题是 `endswith("valid")` 这个检查：

- 原意是拒绝截断代码（如以 `isValid` 结尾但没有分号，说明 LLM 没生成完）
- 但 `endswith("valid")` 同时也匹配以 `"invalid"` 结尾的代码（因为 `"invalid"` 以 `"valid"` 为后缀）
- 改用 `re.search(r"\bvalid$", normalized)` 做词边界匹配，`"invalid"` 不再被误杀

---

### 改动 4：实现 `runtime_feedback_mode` 运行时执行验证

**文件：** `Fuzz4All/target/JAVA/JAVA.py`

**改了什么：**

`validate_individual()` 编译成功后，若配置 `runtime_feedback_mode` 不为 `compile_only`，则用 `java -cp <dir> <ClassName>` 执行编译产物，捕获运行时异常。

```python
# 编译成功后
if getattr(self, "runtime_feedback_mode", "compile_only") != "compile_only":
    class_dir = str(Path(write_back_name).parent)
    class_name = Path(write_back_name).stem
    run_cmd = f"java -cp {class_dir} {class_name}"
    try:
        run_result = subprocess.run(run_cmd, shell=True, capture_output=True,
                                    encoding="utf-8", timeout=5, text=True)
        if run_result.returncode != 0:
            return FResult.ERROR, run_result.stderr  # 运行时异常 = 潜在 bug
    except subprocess.TimeoutExpired:
        return FResult.TIMED_OUT, "java runtime"
```

**为什么改：**

YAML 配置中 `runtime_feedback_mode: normalized` 已存在于所有自动生成的配置文件，但原始代码 `validate_individual()` 只运行 `javac`，从不执行。这意味着：

- 编译通过（`SAFE`）的程序不会被运行
- `ArrayIndexOutOfBoundsException`、`NullPointerException`、`IllegalArgumentException` 等 JVM 级别的 bug 无法被发现
- `runtime_feedback_mode` 配置项是声明但无实现的功能

**两种模式说明：**

| YAML 配置值 | 行为 |
|-------------|------|
| `runtime_feedback_mode: compile_only` | 只做 `javac` 编译，不执行（原有行为） |
| `runtime_feedback_mode: normalized` | 编译 + `java` 执行，运行时异常报为 `FResult.ERROR` |

---

### 改动 5：修复 `target_name` 默认值

**文件：** `Fuzz4All/make_target.py`

**改了什么：**

```python
# 改前
"target_name": fuzzing.get("target_name", "target"),  # 默认值毫无意义

# 改后
_default_target_names = {
    "java": "javac",
    "cpp":  "g++",
    "c":    "gcc",
    "go":   "go",
    "smt2": "cvc5",
    "qiskit": "python",
}
"target_name": fuzzing.get("target_name", _default_target_names.get(_language, "target")),
```

**为什么改：**

所有自动生成的 YAML 配置（`config/targeted/` 下 50+ 个文件）均未包含 `target_name` 字段。原默认值是字符串 `"target"`，对 Java 而言编译命令会变成：

```
target --source 21 --enable-preview --target 21 /tmp/xxx.java
```

这会直接报 "command not found"，而报错信息完全不提示真正原因，极难排查。每次运行都需要在命令行手动传 `--target javac`，遗忘即报错。

---

### 改动 6：RESOURCE 变异算子从硬编码改为动态识别

**文件：** `Fuzz4All/mutation/java_mutator.py`

**改了什么：**

新增辅助方法 `_find_resource_vars()`，用正则从代码中动态提取所有资源类型变量，重写三个核心算子：

```python
# 新增：动态识别任意 *InputStream/*OutputStream/*Reader/*Writer 变量
_RESOURCE_VAR_RE = re.compile(
    r"\b([A-Za-z][A-Za-z0-9]*(?:InputStream|OutputStream|Reader|Writer))"
    r"\s+([A-Za-z_][A-Za-z0-9_]*)\s*="
)

def _find_resource_vars(self, code: str) -> List[Tuple[str, str]]:
    """返回代码中所有资源变量的 [(类名, 变量名), ...] 列表"""
    seen, results = set(), []
    for m in _RESOURCE_VAR_RE.finditer(code):
        key = (m.group(1), m.group(2))
        if key not in seen:
            seen.add(key)
            results.append(key)
    return results
```

**为什么改（这是本次最重要的改动）：**

改动前，`resource_constructor_edge` 和 `resource_lifecycle_sequence` 内部是这样的：

```python
resource_types = [
    "BufferedOutputStream",
    "BufferedInputStream",
    "BufferedReader",
]
for resource_type in resource_types:
    ...
```

只有这三个类才能被 RESOURCE 算子覆盖。当系统将 RESOURCE profile 应用到 `FileInputStream`、`PrintWriter`、`GZIPOutputStream`、`ByteArrayOutputStream` 等其他 API 时，算子对代码进行模式匹配，一个都找不到，**静默返回空列表**——不报错，但也产生零变异。

这直接破坏了"11类分类感知变异"的核心目标：RESOURCE 类 API 在理论上应该获得生命周期、缓冲区大小、包装深度等维度的专项测试，实际上只有 3 个类能真正受益，其余几十个 API 都退化成无变异状态。

**三个算子的改动逻辑：**

| 算子 | 改前 | 改后 |
|------|------|------|
| `resource_constructor_edge` | 逐个处理 3 个硬编码类名 | `_find_resource_vars()` 动态发现所有资源变量，对每个类型尝试注入/替换 size 参数 |
| `resource_lifecycle_sequence` | 分别搜索 3 个固定变量名 | 动态发现，根据 `is_output` / `is_input` 插入对应的 flush/close/mark/reset/skip |
| `resource_wrapper_depth` | 3 个独立 `(pattern, replacements)` 元组 | 动态发现，按 output/input 方向选择包装策略 |

---

### 改动 7：修复 `mutation_profile_override` 命名空间混淆

**文件：** `Fuzz4All/mutation/profile_loader.py`

**改了什么：**

将 profile_override 的处理逻辑分成两条语义明确的分支：

```python
if profile_override:
    if profile_override in MUTATION_PROFILE_DEFINITIONS:
        # 填的是 profile 名（如 "resource_buffer_batch"）：直接用
        mutation_profile = profile_override
    elif profile_override in PROFILE_ORDER:
        # 填的是分类标签（如 "RESOURCE"）：更新 primary_tag 并重新推导 profile
        primary_tag = profile_override
        all_tags = [profile_override] + [t for t in all_tags if t != profile_override]
        mutation_profile = _derive_mutation_profile(
            primary_tag, all_tags, classification_scores, target_api, doc_path
        )
    else:
        mutation_profile = derived_mutation_profile  # 无效值，回退
else:
    mutation_profile = (matched.get("mutation_profile") or derived_mutation_profile)
```

**为什么改：**

原代码：

```python
mutation_profile = profile_override or (...)   # 若 override 非空，直接用
if profile_override and profile_override in PROFILE_ORDER:  # PROFILE_ORDER 是分类标签名列表
    primary_tag = profile_override
```

两个命名空间完全不同：
- `PROFILE_ORDER` 的值：`["RESOURCE", "BUFFER", "FILE", ...]`（分类标签）
- `MUTATION_PROFILE_DEFINITIONS` 的键：`["resource_buffer_batch", "file_path_state", ...]`（profile 名）

用户在 YAML 中写 `mutation_profile_override: "resource_buffer_batch"`（profile 名）时：
- 第一行把 `mutation_profile` 设为 `"resource_buffer_batch"` ✓
- 第二行 `"resource_buffer_batch" in PROFILE_ORDER` 为 False → if 分支不执行
- 结果：`mutation_profile` 正确，但 `primary_tag` 没有跟着更新，分类与 profile 不一致

用户写 `mutation_profile_override: "RESOURCE"`（分类标签）时：
- 第一行把 `mutation_profile` 设为 `"RESOURCE"` ✗（`"RESOURCE"` 不是合法 profile 名）
- `_resolve_active_profiles("RESOURCE", ...)` 在 `MUTATION_PROFILE_DEFINITIONS` 中找不到对应，行为不确定

覆盖功能对任何输入都无法正确工作。

---

### 改动 8：移除 REFLECT 分类的假阳性关键词

**文件：** `Fuzz4All/mutation/profile_loader.py`

**改了什么：**

```python
# 改前
("REFLECT", [".reflect", "method", "field", "constructor", "proxy", "accessibleobject", "invocation"]),

# 改后
("REFLECT", [".reflect", ".lang.reflect", "accessibleobject", "invocationhandler", "proxy"]),
```

**为什么改：**

`_context_domain_hints()` 用字符串 `in` 检查（子串匹配）来识别 API 类别。`"method"`、`"field"`、`"constructor"` 是极其通用的词：

- 任何 API 的文档描述中几乎都含有"method"这个词
- `PropertyChangeSupport`、`ManagementFactory` 这类与反射毫无关系的 API 会被错误地提示为 REFLECT 类
- 后果：这些 API 被分配反射相关的变异算子（`reflect_accessibility_flip_mutation` 等），而这些算子对它们产生零有效变异

保留的关键词（`.reflect`、`.lang.reflect`、`accessibleobject`、`invocationhandler`）足够精确，只在真正的反射 API 上触发。

---

### 改动 9：三个 YAML 配置添加 `target_name: javac`

**文件：**
- `config/targeted/java.base_java_io_BufferedInputStream.yaml`
- `config/targeted/java.desktop_java_beans_PropertyChangeSupport.yaml`
- `config/targeted/java.management_java_lang_management_ManagementFactory.yaml`

**改了什么：** 在 `fuzzing:` 节添加 `target_name: javac`。

**为什么改：** 见改动 5。同时这三个文件是当前活跃的配置，需要立即修正确保能直接运行（无需命令行 `--target javac` 参数）。

---

### 改动 10：修正文档错误

**文件：** `当前进度与预期结果.md`

| 位置 | 改前 | 改后 |
|------|------|------|
| 项目结构说明 | `configs/: YAML configuration files` | `config/: YAML configuration files` |
| 新语言开发说明 | 需要实现 `generate()`, `update()`, `validate_individual()` | 需要实现 `filter()`, `clean()`, `clean_code()`, `wrap_prompt()`, `wrap_in_comment()`, `validate_individual()`, `write_back_file()`；注明 `generate()` 和 `update()` 在基类中已有完整实现，不应覆写 |

---

## 4. 如何运行

### 4.1 环境准备

```bash
# 创建 conda 环境
conda create -n fuzz4all python=3.10
conda activate fuzz4all

# 安装依赖
pip install -r requirements.txt
pip install -e .

# 确认 Java 工具链
javac -version   # 需要 Java 21+
java -version
```

### 4.2 配置环境变量

```bash
# 必填：LLM 设置（选择其一）

# 方案 A：HuggingFace 本地 GPU（推荐）
export FUZZING_MODEL="Qwen/Qwen2.5-Coder-7B-Instruct"
export FUZZING_DEVICE="gpu"
export FUZZING_BATCH_SIZE=30

# 方案 B：Ollama 本地（无 GPU）
export FUZZING_MODEL="ollama/qwen2.5-coder:7b"
export FUZZING_DEVICE="cpu"
export FUZZING_BATCH_SIZE=5

# 可选：autoprompt 和 runtime prompt 刷新（推荐填写）
export DEEPSEEK_API_KEY=sk-xxxx   # 或 OPENAI_API_KEY
```

### 4.3 运行单个 API 的定向 fuzz

**最小运行示例（BufferedInputStream，5个样本，用于验证环境）：**

```bash
python Fuzz4All/fuzz.py \
  --config config/targeted/java.base_java_io_BufferedInputStream.yaml \
  main_with_config \
  --folder outputs/test_run \
  --model_name Qwen/Qwen2.5-Coder-7B-Instruct
```

> 改动后：配置文件已含 `target_name: javac`，无需再手动传 `--target javac`。

**正式运行（按 YAML 配置，24 小时，60 样本）：**

```bash
python Fuzz4All/fuzz.py \
  --config config/targeted/java.base_java_io_BufferedInputStream.yaml \
  main_with_config \
  --folder outputs/targeted/java.base_java_io_BufferedInputStream \
  --model_name Qwen/Qwen2.5-Coder-7B-Instruct
```

### 4.4 开启运行时执行验证

在 YAML 配置的 `target:` 节确认：

```yaml
target:
  runtime_feedback_mode: normalized   # 编译 + 执行（改动后此项生效）
  # runtime_feedback_mode: compile_only  # 只编译（原有行为）
```

### 4.5 使用 profile_override 指定变异策略

在 YAML 配置的 `target:` 节添加（两种写法均正确，改动后）：

```yaml
target:
  # 写法 A：指定 profile 名（直接用该 profile）
  mutation_profile_override: "resource_buffer_batch"

  # 写法 B：指定分类标签（自动推导对应 profile）
  mutation_profile_override: "RESOURCE"
```

### 4.6 批量运行所有 API

```bash
for yaml in config/targeted/*.yaml; do
  api_name=$(basename "$yaml" .yaml)
  python Fuzz4All/fuzz.py \
    --config "$yaml" \
    main_with_config \
    --folder "outputs/targeted/$api_name" \
    --model_name Qwen/Qwen2.5-Coder-7B-Instruct &
done
```

---

## 5. 预期运行结果

### 5.1 启动阶段输出

```
=== Target Config ===
language: java
target_name: javac          ← 改动5：现在显示正确的 javac
max_length: 1024
...
====================
Initializing ... this may take a while ...
Loading model ...
HuggingFace model loaded
Mutation enabled with primary tag RESOURCE and profile resource_buffer_batch
(active_profiles=['RESOURCE', 'BUFFER', 'BATCH_OP', 'MARK_SUPPORT'], operators=[...]).
Initial prompt prepared (XXX chars).
Done
```

### 5.2 主循环输出

```
Fuzzing • [████████░░░░] 45%  27/60 • 0:12:34
```

每个 batch 处理后，`log.txt` 中可见：

```
Prompt updated from structured feedback (rules: 3, safe examples: 2).
```

若有错误案例被发现：

```
outputs/targeted/java.base_java_io_BufferedInputStream/42.fuzz has potential error!
```

### 5.3 输出文件结构

```
outputs/targeted/java.base_java_io_BufferedInputStream/
├── 0.fuzz ~ 59.fuzz      # 生成的 Java 程序
├── mutation_manifest.jsonl  # 每个样本的元数据（改动后：含 compile_result、operator 等）
├── log.txt                  # 系统日志（prompt 刷新、error 发现）
├── log_generation.txt       # LLM 交互日志
├── log_validation.txt       # 编译/运行验证日志
└── prompts/
    ├── best_prompt.txt       # 当前最优 prompt
    ├── best_initial_prompt.txt
    ├── runtime_prompt_N.txt  # 各轮 prompt 快照
    └── refresh_decision_round_N.txt  # prompt 刷新决策记录
```

### 5.4 mutation_manifest.jsonl 样例

```json
{
  "source_type": "mutated",
  "operator": "resource_constructor_edge",
  "parent_index": 3,
  "target_api": "FileInputStream",          ← 改动6：FileInputStream 也能被变异了
  "mutation_profile": "resource_buffer_batch",
  "primary_tag": "RESOURCE",
  "compile_result": "SAFE",
  "feedback_summary": [],
  "sanitized_message": ""
}
```

```json
{
  "source_type": "generated",
  "operator": "llm_seed",
  "compile_result": "ERROR",               ← 改动4：运行时异常现在会被捕获
  "sanitized_message": "Exception in thread \"main\" java.lang.ArrayIndexOutOfBoundsException: ..."
}
```

### 5.5 各指标的健康范围

| 指标 | 正常范围 | 说明 |
|------|---------|------|
| `compile_result: SAFE` 占比 | 15% ~ 50% | 太低说明 prompt 质量差或 API 很复杂 |
| `compile_result: FAILURE` 占比 | 40% ~ 75% | 编译失败，会提炼成规则反馈给 LLM |
| `compile_result: ERROR` 占比 | 0% ~ 5% | 潜在 bug，需人工确认 |
| 变异样本占总样本比例 | 20% ~ 60% | 取决于 `mutation_budget_per_seed` |
| `resource_constructor_edge` 变异成功率 | > 0%（**改动后**）| 改动前对非 Buffered 类型一直是 0% |

---

## 6. 常见问题排查

**Q: 启动时报 "cannot find symbol: target"**

原因：`target_name` 未设置或设置错误。
解法：确认 YAML 的 `fuzzing:` 节有 `target_name: javac`（改动后默认已正确，无需手动加）。

---

**Q: 所有样本 `compile_result` 全是 FAILURE，没有 SAFE**

可能原因：
1. `DEEPSEEK_API_KEY` 未设置，autoprompt 回退为纯文档 prompt，质量较低
2. `max_length` 太短，LLM 没有生成完整的 Java 程序

解法：设置 API key 或增大 `llm.max_length`（如 2048）。

---

**Q: `resource_constructor_edge` 在 manifest 中从未出现**

改动后不应再发生。若仍出现，检查目标 API 的代码中是否有匹配 `*InputStream/*OutputStream/*Reader/*Writer` 的变量声明。如果目标 API 用的是更高层的抽象（如 `Readable`、`Closeable`），需在 `_RESOURCE_VAR_RE` 中扩展接口名。

---

**Q: `runtime_feedback_mode: normalized` 导致 fuzz 很慢**

原因：每个 SAFE 样本还需额外运行一次 JVM（5 秒超时）。
解法：将超时调短（改 `JAVA.py` 中的 `timeout=5`），或对不需要运行时验证的 API 改为 `compile_only`。

---

**Q: `profile_override` 设置后没有效果**

确认填写的是合法值：
- 合法 profile 名：`resource_buffer_batch`、`file_path_state`、`security_provider_flow` 等（见 `profile_loader.py` `MUTATION_PROFILE_DEFINITIONS`）
- 合法分类标签：`RESOURCE`、`BUFFER`、`FILE`、`CONCURRENT`、`SECURITY`、`REFLECT`、`CALLBACK`、`TIME`、`NETWORK`、`UTILITY`、`JVM_MGMT`、`MARK_SUPPORT`、`GENERIC`

改动后两种写法均可正确工作。
