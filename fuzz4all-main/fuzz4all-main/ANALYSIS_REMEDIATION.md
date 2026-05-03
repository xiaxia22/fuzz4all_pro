# Fuzz4All 毕设成果分析与整改方案

> 分析日期：2026-05-03  
> 分析对象：`outputs/targeted10`（10类Java API模糊测试结果）  
> 分析范围：系统源代码 `Fuzz4All/`（非直接修改结果文件）

---

## 一、当前成果指标

| 类别 | 生成数 | SAFE | ERROR(运行时) | TIMEOUT | FAILURE | **通过率** |
|------|--------|------|------------|---------|---------|-----------|
| java.base_java_io_BufferedInputStream | 60 | 7 | 7 | 2 | 44 | **10.6%** |
| java.base_java_io_File | 50 | 27 | 0 | 0 | 23 | **54.0%** |
| java.base_java_lang_Thread | 54 | 8 | 0 | 3 | 39 | **14.8%** |
| java.base_java_lang_reflect_Method | 60 | 6 | 9 | 0 | 45 | **10.3%** |
| java.base_java_net_Socket | 52 | 17 | 9 | 0 | 34 | **32.7%** |
| java.base_java_net_URI | 60 | 40 | 5 | 0 | 15 | **72.7%** |
| java.base_java_time_Duration | 60 | 9 | 9 | 0 | 42 | **15.3%** |
| java.base_javax_crypto_Cipher | 52 | 3 | 6 | 0 | 41 | **5.8%** |
| java.desktop_java_beans_PropertyChangeSupport | 60 | 8 | 0 | 0 | 52 | **13.3%** |
| java.management_java_lang_management_ManagementFactory | 60 | 39 | 0 | 0 | 21 | **65.0%** |
| **合计** | **568** | **164** | **45** | **5** | **356** | **28.9%** |

**毕设达标目标**：整体通过率 ≥ 50%，最低单类 ≥ 30%，Tier1（>50%）类别 ≥ 6/10

---

## 二、根本原因分析（代码层）

通过阅读全部源代码，识别出以下影响多个类别的系统性 Bug 和设计缺陷：

---

### BUG 1：受检异常未被识别，反馈规则无法生成
**文件**：`Fuzz4All/target/JAVA/JAVA.py`，第 125-130 行  
**影响类别**：Cipher（致命），Socket，Duration，ManagementFactory，Reflect

`extract_javac_error_categories()` 只检测了 `IOException` 和 `FileNotFoundException` 两种受检异常：

```python
# 当前代码（不完整）
if "unreported exception IOException" in normalized:
    categories.append("unchecked_ioexception")
if "unreported exception FileNotFoundException" in normalized:
    categories.append("unchecked_ioexception")
```

当 Cipher 报错 `unreported exception NoSuchPaddingException`、`unreported exception InvalidKeyException` 时，代码完全检测不到，落入最后的 `_sanitize_feedback()` 路径，无法生成结构化规则。这是 Cipher 通过率为 5.8% 的直接原因——反馈循环失去了修正能力。

**修复**：改为通用正则，检测任何 `unreported exception XxxException` 错误。

---

### BUG 2：`parse_validation_message()` 日志级别传参错误
**文件**：`Fuzz4All/target/target.py`，第 1233-1248 行  
**影响**：所有类别的 FAILURE/ERROR 日志均以错误级别写入

```python
# 当前代码（BUG：LEVEL.VERBOSE 作为第3个参数传给 format() 而非 logo()）
self.v_logger.logo(
    "{} failed validation with error message: {}".format(
        file_name, message, LEVEL.VERBOSE  # ← str.format() 忽略多余参数！
    )
)
# logo() 使用默认级别 LEVEL.INFO，而非 VERBOSE
```

结果：FAILURE 消息以 INFO 级别记录，导致日志分类混乱，在低详细度模式下信息过多。

---

### BUG 3：`feedback_history` 被裁剪为 `max_feedback_rules` 长度
**文件**：`Fuzz4All/target/target.py`，第 1157-1158 行  
**影响**：所有类别的历史信息丢失过快

```python
# 当前代码
self.feedback_history = self.feedback_history[-self.max_feedback_rules :]
# max_feedback_rules 默认 5，只保留最近 5 条历史
```

`feedback_history` 的语义是完整的历史记录（与 `failure_rules` 是当前活跃规则不同），不应被严格限制。这会导致早期出现的重要错误信息从历史中消失，影响后续 prompt 刷新时的上下文质量。

---

### DESIGN ISSUE 4：提示词评分对 0-SAFE 提示词的惩罚不足
**文件**：`Fuzz4All/target/target.py`，第 908-913 行  
**影响**：自动提示词选择在 SAFE 率低的类别上效果差

```python
# 当前评分公式
score = (
    safe_count * 3              # SAFE 样本奖励
    + structured_failure_count  # 结构化失败也奖励 +1
    - syntax_failure_count * 2  # 语法错误惩罚
)
```

问题：对于 Cipher 这样所有 52 个样本都是"结构化失败"（unreported exception）的类别，一个 0-SAFE 的坏提示词可以得分 52，而一个有 5 个 SAFE 样本的好提示词得分只有 5×3 + 47 = 62。差距很小，甚至更差的提示词可能在某次评估中因随机性胜出。

**修复**：提高 SAFE 权重，使 SAFE 样本的贡献更显著。

---

### DESIGN ISSUE 5：`_is_viable_generated_code()` 截断检测不足
**文件**：`Fuzz4All/target/JAVA/JAVA.py`，第 87-99 行  
**影响**：截断/格式错误的代码会进入编译阶段浪费时间

当前检测规则过少：
```python
if re.search(r"\bvalid$", normalized):
    return False
if normalized.endswith(("write(", "try {", "Buffered")):
    return False
```

遗漏了大量常见截断模式，如方法名含 `%s` 占位符、以 `.` 结尾的方法调用、不完整的参数列表等。

---

### DESIGN ISSUE 6：SECURITY 配置文件缺少关键加密异常的 import
**文件**：`Fuzz4All/mutation/profile_loader.py`，第 228-233 行  
**影响**：Cipher 类别

当前 SECURITY 的 repair_rules.imports 只包含两个异常类：
```python
"imports": [
    "java.security.InvalidKeyException;",
    "java.security.InvalidAlgorithmParameterException;",
],
```

缺少 `javax.crypto.NoSuchPaddingException`（注：实际上此类在 `javax.crypto` 包中）、`java.security.NoSuchAlgorithmException`、`javax.crypto.IllegalBlockSizeException`、`javax.crypto.BadPaddingException`。当修复 BUG 1 后生成的代码开始使用 `catch(SpecificException e)` 而不是 `catch(Exception e)` 时，这些 import 就很有必要了。

---

## 三、代码整改计划

### 改动 1：JAVA.py — 通用受检异常检测（最高优先级）

**位置**：`Fuzz4All/target/JAVA/JAVA.py:125-130`

```python
# 改动前（仅检测IO异常）
if "unreported exception IOException" in normalized:
    categories.append("unchecked_ioexception")
if "unreported exception FileNotFoundException" in normalized:
    categories.append("unchecked_ioexception")

# 改动后（检测所有受检异常）
if "unreported exception IOException" in normalized:
    categories.append("unchecked_ioexception")
if "unreported exception FileNotFoundException" in normalized:
    categories.append("unchecked_ioexception")
# 新增：检测任意受检异常（Cipher、crypto、reflection等均覆盖）
if re.search(r"unreported exception [A-Za-z]+Exception", normalized):
    if "unchecked_ioexception" not in categories:
        categories.append("unchecked_exception")
```

同时在 `map_error_categories_to_rules()` 中新增规则映射：
```python
if "unchecked_exception" in categories:
    rules.append(
        "Wrap all API method calls in a single "
        "try { ... } catch (Exception e) { e.printStackTrace(); } block, "
        "since they may throw checked exceptions."
    )
```

**预期效果**：Cipher 通过率从 5.8% 提升至 ~50%+，Socket、Duration 也受益。

---

### 改动 2：JAVA.py — 增强代码可行性检测

**位置**：`Fuzz4All/target/JAVA/JAVA.py:87-99`，`_is_viable_generated_code()`

增加以下截断/错误模式检测：
- 方法名含 `%s` 等格式化占位符（反射类别的典型幻觉）
- 以 `(`, `)`, `,` 结尾（参数列表未闭合）
- 方法调用以 `.` 结尾

---

### 改动 3：target.py — 修复 `parse_validation_message()` 日志 Bug

**位置**：`Fuzz4All/target/target.py:1233-1248`

```python
# 改动前（BUG）
self.v_logger.logo(
    "{} failed validation with error message: {}".format(
        file_name, message, LEVEL.VERBOSE   # LEVEL 传到了 format() 里
    )
)

# 改动后
self.v_logger.logo(
    "{} failed validation with error message: {}".format(file_name, message),
    LEVEL.VERBOSE   # 正确传给 logo() 的 level 参数
)
```

---

### 改动 4：target.py — 修复 `feedback_history` 裁剪 Bug

**位置**：`Fuzz4All/target/target.py:1157-1158`

```python
# 改动前（裁剪过激）
self.feedback_history = self.feedback_history[-self.max_feedback_rules :]

# 改动后（保留更多历史，改用更大的窗口）
self.feedback_history = self.feedback_history[-50:]
```

---

### 改动 5：target.py — 改进提示词评分公式

**位置**：`Fuzz4All/target/target.py:908-913`

```python
# 改动前（SAFE 权重过低）
score = (
    safe_count * 3
    + structured_failure_count
    - syntax_failure_count * 2
)

# 改动后（SAFE 权重提升，结构化失败仅辅助）
score = (
    safe_count * 5
    + structured_failure_count
    - syntax_failure_count * 3
)
return max(score, 0)
```

**说明**：safe_count 权重从 3→5，syntax_failure 惩罚从 -2→-3，使有 SAFE 样本的提示词更有优势，语法错误更严重扣分。

---

### 改动 6：profile_loader.py — 补充 SECURITY 类别 import

**位置**：`Fuzz4All/mutation/profile_loader.py:228-233`，SECURITY 的 `repair_rules.imports`

```python
# 改动前（缺少关键crypto异常import）
"imports": [
    "java.security.InvalidKeyException;",
    "java.security.InvalidAlgorithmParameterException;",
],

# 改动后
"imports": [
    "javax.crypto.NoSuchPaddingException;",
    "java.security.NoSuchAlgorithmException;",
    "javax.crypto.IllegalBlockSizeException;",
    "javax.crypto.BadPaddingException;",
    "java.security.InvalidKeyException;",
    "java.security.InvalidAlgorithmParameterException;",
],
```

---

## 四、改动影响预测

| 改动 | 主要受益类别 | 预期效果 |
|------|------------|---------|
| 改动1：通用异常检测 | Cipher, Socket, Duration | Cipher: 5.8%→~50%; 反馈规则对所有抛受检异常的API生效 |
| 改动2：截断检测增强 | Reflect（%s方法名）, Thread | 减少明显无效代码进入编译，加速反馈循环 |
| 改动3：日志Bug修复 | 所有类别 | 日志分类正确，VERBOSE消息不再污染INFO输出 |
| 改动4：history保留更多 | 所有类别（特别是长运行任务） | 提示词刷新时有更完整的历史上下文 |
| 改动5：评分改进 | Cipher, BufferedInputStream（0-SAFE类别） | 自动提示词选择偏向真正有效的提示词 |
| 改动6：SECURITY imports | Cipher | 修复后若代码用具名catch，import自动补全 |

---

## 五、展示页面开发方案

### 5.1 技术选型
纯静态 HTML/CSS/JS，无需服务器，浏览器直接打开即可展示，适合答辩投影。
- **图表**：Chart.js (CDN)
- **代码高亮**：Prism.js (CDN)
- **样式**：自定义 CSS（深色科技风）

### 5.2 页面结构

```
index.html
├── Header（项目标题 + 副标题）
│
├── Section 1：系统介绍（System Overview）
│   ├── 项目背景卡片（一段话介绍）
│   ├── 系统架构图（静态图片）
│   └── 五步工作流程（横向时间轴）
│       1. Auto-Prompting → 2. LLM Generation → 3. Mutation
│       → 4. Compilation Validation → 5. Feedback Loop
│
├── Section 2：流程证据（Process Evidence）
│   ├── Prompt 演化对比（before/after代码框）
│   ├── 学习到的规则示例（卡片列表）
│   └── 生成代码样本（代码高亮 + 编译结果标签）
│
├── Section 3：测试结果（Results Dashboard）
│   ├── 指标总览（4张卡片：总生成数/通过率/类别数/有效种子）
│   ├── 各类别通过率柱状图（Chart.js）
│   ├── 结果分布饼图（SAFE/FAIL/ERROR/TIMEOUT）
│   └── 类别详情表格（展开可查看错误类型分布）
│
└── Footer（署名/学校/时间）
```

### 5.3 需要你提供的内容（否则我用占位符）

| 内容 | 是否必须 | 说明 |
|------|---------|------|
| 毕设题目（中文） | **必须** | 用于页面 H1 标题 |
| 一段系统简介（100-200字） | **必须** | Section 1 背景介绍 |
| 系统架构图（PNG/JPG） | 可选 | 否则用文字流程图代替 |
| 学校/姓名 | 可选 | 用于 footer |
| 截图/运行证据图片 | 可选 | Section 2 证据展示 |

> 只需提供题目和简介，我就可以立即帮你生成完整的 index.html。
> 结果数据我会直接从 outputs/targeted10 自动读取。

---

## 六、整改后预期效果

| 类别 | 当前 | 预期整改后 |
|------|------|----------|
| Cipher | 5.8% | ~50% |
| BufferedInputStream | 10.6% | ~40% |
| PropertyChangeSupport | 13.3% | ~35% |
| Reflect/Method | 10.3% | ~30% |
| Thread | 14.8% | ~35% |
| Duration | 15.3% | ~40% |
| Socket | 32.7% | ~50% |
| File | 54.0% | ~65% |
| URI | 72.7% | ~75% |
| ManagementFactory | 65.0% | ~70% |
| **整体** | **28.9%** | **~49%** |
