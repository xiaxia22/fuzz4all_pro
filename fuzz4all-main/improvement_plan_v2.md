# 改进方案 v2 — 弱类收口与 10 类统一回归

> 目标：一次性把 CALLBACK/JVM_MGMT 弱类拉起，FILE/REFLECT 稳定化，
> 形成可提交的 10 类统一回归结果。
>
> 执行原则：只做最小必要改动，不改架构，改完即验。

---

## 一、诊断修正（对照原方案的偏差）

| 原方案描述 | 实际情况 | 影响 |
|---|---|---|
| CALLBACK 要补 reject "indexed helper / proxy-helper 幻觉" | 已有 `addIndexedPropertyChangeListener` 拦截，但 `fireIndexedPropertyChange`、`createPropertyChangeListenerProxy`、`hasListeners()` 无参版均未拦截，targeted8 仍有这些幻觉 | 补充方向对，但内容不够，直接执行方案不能解决问题 |
| JVM_MGMT reject "MBeanProxy、明显非 JDK 管理 helper" | filter_rules 当前为空，且 `MBeanProxy`/`getPlatformMBeans()`/`MemoryPoolMXBeans`/`PlatformMXBean` 均未被拦截 | 这是 JVM_MGMT 失效的核心，必须精确到 token |
| REFLECT 归为"波动类"需大改 | targeted7/8 的 Method 样本结构基本合法，偶发幻觉已被现有规则覆盖大半 | 优先级应低于 CALLBACK/JVM_MGMT，降低改动范围 |
| "structural garbage filter" 作为独立层 | brace 平衡检查和 truncated 检查已在代码中，缺的是类型级幻觉 token 拦截，与 filter_rules 对应即可 | 不需要新增独立层，补 reject_tokens/patterns 即可 |
| 文档未提温度参数 | CALLBACK/JVM_MGMT yaml 均 temperature=1.0，是幻觉率高的直接因素 | 需要降温 |
| 文档未提 duplicate import 问题 | targeted7/8 均有重复 import（ManagementFactory、PropertyChangeSupport 各两行）| 需要在 `_repair_java_code` 中加去重 |

---

## 二、必须完成的代码改动（5 处，按优先级排序）

### 改动 1：`profile_loader.py` — CALLBACK filter_rules 补全

**文件**：`Fuzz4All/mutation/profile_loader.py`

在 `CALLBACK` profile 的 `filter_rules` 中添加：

```python
"filter_rules": {
    "reject_tokens": [
        "fireIndexedPropertyChange",
        "createPropertyChangeListenerProxy",
        "PropertyChangeListenerProxy(",
    ],
    "reject_patterns": [
        r"addIndexedPropertyChangeListener",
        r"removeIndexedPropertyChangeListener",
        r"hasListeners\s*\(\s*\)",            # 无参版不存在
        r"new\s+PropertyChangeListenerProxy\s*\([^)]*,[^)]*,[^)]*,",  # 4参数构造
        r"java\.nio\.[A-Za-z]+\s*\.\s*asByteArrayOutputStream",       # 幻觉链
    ],
},
```

**理由**：targeted7/8 中出现的幻觉模式全部来自上述几个点，现有的两条 pattern 不足以覆盖。

---

### 改动 2：`profile_loader.py` — JVM_MGMT filter_rules 从空补全

**文件**：`Fuzz4All/mutation/profile_loader.py`

将 `JVM_MGMT` profile 的 `filter_rules` 从空改为：

```python
"filter_rules": {
    "reject_tokens": [
        "MBeanProxy",           # javax.management.MBeanProxy 不存在
        "MemoryPoolMXBeans",    # 错误类型名，正确是 List<MemoryPoolMXBean>
        "PlatformMXBean",       # 不存在，正确是 PlatformManagedObject
        "getPlatformMBeanName", # 幻觉方法
    ],
    "reject_patterns": [
        r"ManagementFactory\.getPlatformMBeans\s*\(\s*\)",        # 无参版不存在
        r"getPlatformMBeanServerInfo\s*\(\s*\)",                   # 幻觉方法
        r"newPlatformMXBeanProxy\s*\(\s*null\s*,\s*[^,]+,\s*null\s*\)",  # 3参数全null
    ],
},
```

**理由**：这是 JVM_MGMT 接近 0 SAFE 的直接原因，每一条都能在 targeted7/8 输出中找到对应幻觉。

---

### 改动 3：`target.py` — 生成代码去重 import

**文件**：`Fuzz4All/target/target.py`

在 `_repair_java_code` 方法内，在现有修复逻辑末尾加一步 import 去重：

```python
# Deduplicate import lines while preserving order
seen_imports = set()
deduped_lines = []
for line in repaired.split("\n"):
    stripped = line.strip()
    if stripped.startswith("import "):
        if stripped in seen_imports:
            continue
        seen_imports.add(stripped)
    deduped_lines.append(line)
repaired = "\n".join(deduped_lines)
```

**理由**：targeted7/8 均出现重复 import，不影响编译但说明 seed 质量下降，会干扰 SAFE 统计和 prompt 评分。

---

### 改动 4：`config/targeted/*.yaml` — CALLBACK/JVM_MGMT 降温

**文件**：
- `config/targeted/java.desktop_java_beans_PropertyChangeSupport.yaml`
- `config/targeted/java.management_java_lang_management_ManagementFactory.yaml`

将这两个文件中的 `temperature: 1` 改为 `temperature: 0.8`，并将 `max_feedback_rules` 从 5 改为 7：

```yaml
llm:
  temperature: 0.8          # 从 1 降到 0.8，减少幻觉率
  ...
target:
  max_feedback_rules: 7     # 从 5 改为 7，允许更多针对性约束
```

**理由**：Qwen2.5-Coder-7B 在 temperature=1.0 下对这两类 API 幻觉率显著高于其他类。降到 0.8 可在不损失多样性的情况下明显降低无效输出比例。

---

### 改动 5：`JAVA.py` — 补充 `nonexistent_type` 错误类别

**文件**：`Fuzz4All/target/JAVA/JAVA.py`

在 `extract_javac_error_categories` 末尾添加：

```python
# Type-level hallucinations: "cannot find symbol" for a class/type name
if "cannot find symbol" in normalized and re.search(
    r"symbol:\s+class\s+[A-Za-z_][A-Za-z0-9_]*", normalized
):
    categories.append("nonexistent_type")
```

在 `map_error_categories_to_rules` 中添加对应规则：

```python
if "nonexistent_type" in categories:
    rules.append(
        f"Use only documented JDK public types; do not reference undocumented or invented class names."
    )
    if primary_tag == "JVM_MGMT":
        rules.append(
            f"For {target_api}, valid types include: ManagementFactory, MemoryMXBean, ThreadMXBean, "
            f"ClassLoadingMXBean, RuntimeMXBean, MemoryUsage, MemoryPoolMXBean, ObjectName, MBeanServer. "
            f"Do not use MBeanProxy, PlatformMXBean, MemoryPoolMXBeans, or other invented management types."
        )
    elif primary_tag == "CALLBACK":
        rules.append(
            f"For {target_api}, valid types include: PropertyChangeSupport, PropertyChangeListener, "
            f"PropertyChangeEvent, PropertyChangeListenerProxy(String, PropertyChangeListener). "
            f"Do not use indexed listener types or invent proxy/helper classes."
        )
```

**理由**：`MBeanProxy`/`MemoryPoolMXBeans`/`PlatformMXBean` 这类幻觉类型会触发 `symbol: class` 错误，当前没有分类规则对应，导致反馈规则是通用的而非分类级的。

---

## 三、不需要改动的部分（维持现状）

| 组件 | 判断 | 理由 |
|---|---|---|
| `target.py` `_ensure_java_import()` | 保持 | 词边界匹配已稳定工作 |
| `target.py` refresh 链路 | 保持 | `refresh_status_round_*` / `refresh_decision_round_*` 证据链完整 |
| `java_mutator.py` | 保持 | 分类级 operator 已覆盖所有 10 类，RESOURCE 已泛化到 Closeable 系列 |
| `profile_loader.py` SECURITY/CONCURRENT/NETWORK/TIME/UTILITY | 保持 | 这些强类运行稳定，不改 |
| `JAVA.py` 现有错误类别 | 保持并扩充 | 已有约 20 个类别，结构合理，只补缺口 |
| 其他 9 个代表 API 的 yaml | 保持 | 只改 CALLBACK/JVM_MGMT 两个弱类的温度 |

---

## 四、验证方案

### 第一步：弱类专项验证（先跑，不跑全量）

只跑这 4 个：
- `java.desktop_java_beans_PropertyChangeSupport`
- `java.management_java_lang_management_ManagementFactory`
- `java.base_java_lang_reflect_Method`（REFLECT 波动检验）
- `java.base_java_io_File`（FILE 稳定性检验）

**达标标准：**

| API | 达标条件 |
|---|---|
| PropertyChangeSupport | SAFE > 0，且 manifest 中不再出现 `fireIndexedPropertyChange`/`MBeanProxy` 类幻觉 |
| ManagementFactory | SAFE > 0，且不再出现 `cannot find symbol: class MBeanProxy` / `PlatformMXBean` 错误 |
| Method | SAFE 比例稳定，runtime_rules 中不再大量出现 `nonexistent_type` |
| File | SAFE 比例不低于 targeted7 的水平，不出现大幅退化 |

### 第二步：10 类统一回归

固定跑全部 10 个代表 API。统一检查以下 6 项：

1. `primary_tag` 和 `mutation_profile` 正确命中
2. manifest 中出现对应分类 operator（如 `callback_duplicate_registration_mutation`）
3. SAFE / FAILURE / ERROR 分布（SAFE > 0 为最低要求）
4. `runtime_rules_1.txt` 中的规则是分类级的（非通用）
5. `refresh_status_round_*` 有可观察的 best_prompt 更新记录
6. 不再出现 targeted7/8 中的已知幻觉模式（逐类对比）

### 第三步：形成可提交版结论

满足以下条件视为可提交：

- 10 类全部命中正确 primary_tag 和 mutation_profile ✓
- 10 类全部出现对应分类 operator ✓
- 强类（SECURITY/CONCURRENT/NETWORK/UTILITY/TIME/RESOURCE）稳定 ✓
- 波动类（FILE/REFLECT）不再大起大落 ✓
- 弱类（CALLBACK/JVM_MGMT）摆脱 SAFE=0 ✓
- refresh 闭环有可观察证据 ✓

---

## 五、改动优先级和执行顺序

```
改动1（CALLBACK filter）→ 改动2（JVM_MGMT filter）→ 改动3（去重import）
→ 改动4（降温度/加规则上限）→ 改动5（JAVA.py nonexistent_type）
→ 第一步验证 → 第二步 10 类回归 → 第三步结论
```

改动 1-5 可以一次性完成，不存在依赖关系。

---

## 六、最终系统的完整数据流（确认不变）

```
API 文档 → 离线 5D 分类 → primary_tag + mutation_profile
→ 运行时装载 profile + operator（filter_rules 过滤幻觉种子）
→ DeepSeek autoprompt 生成初始 prompt
→ Qwen 生成 seed（temperature=0.8 for 弱类）
→ 分类 operator 变异 seed
→ javac 编译 + 运行反馈 → extract_javac_error_categories
→ map_error_categories_to_rules（含 nonexistent_type 分类规则）
→ DeepSeek 更新 runtime_prompt + runtime_rules
→ 下一轮继续迭代
→ 10 类代表 API 输出可解释、可复现、可写报告的结果
```
