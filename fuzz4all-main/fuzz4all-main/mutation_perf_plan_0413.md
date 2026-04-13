# `java.base_java_io_BufferedOutputStreamnew413` 检查与后续方案

## 1. 这次 `new413` 输出是否符合预期

已检查目录：

- `outputs/targeted/java.base_java_io_BufferedOutputStreamnew413`

结论：

1. 第一阶段改动已经稳定生效。
2. 第二阶段代码已经接入，但这次运行本身没有触发真正的 prompt refresh。

### 1.1 已实现的结果

这次输出里已经出现：

- `prompts/runtime_prompt_1.txt`
- `prompts/runtime_prompt_2.txt`
- `prompts/runtime_rules_1.txt`
- `prompts/runtime_rules_2.txt`

并且 `log.txt` 中出现了：

- `Prompt updated from structured feedback (rules: 5, safe examples: 2).`

这说明：

- 编译日志已经被结构化规则吸收
- runtime prompt 已经开始演化
- 第一阶段闭环是通的

### 1.2 为什么这次没有看到 `refreshed_*`

原因不是第二阶段失效，而是这次运行没有达到触发阈值。

当前配置：

- `batch_size = 30`
- 当前输出共有 `0.fuzz` 到 `59.fuzz`，共 60 个样本
- 也就是只完成了 2 轮 `update()`
- 当前 `prompt_refresh_interval = 5`

因此：

- 只会产生 `runtime_prompt_*`
- 不会进入 `refresh_prompt_from_feedback()`
- 所以没有 `refreshed_request_round_*`、`refreshed_prompt_round_*`、`accepted_refreshed_prompt_round_*`

这和代码逻辑是完全一致的。

### 1.3 如何验证第二阶段是否真的工作

要让第二阶段在运行中真正出现，建议任选一个方式：

1. 把样本量继续提高到至少 150
   - 因为 `150 / 30 = 5` 轮更新，正好达到 refresh 阈值
2. 或者临时把 `prompt_refresh_interval` 从 `5` 改为 `2`
   - 这样 60 个样本就会触发一次 refresh

更建议先用方法 2 验证第二阶段是否通，再恢复成 `5` 或更高。

## 2. 初始化为什么这么慢

从你的截图和当前代码逻辑看，慢点主要发生在：

- `[INFO] Use auto-prompting prompt ...`
- `Generating prompts ...`

也就是初始化阶段的 autoprompt 候选生成与评分。

### 2.1 现在的初始化成本结构

当前配置中：

- `autoprompt_candidates = 3`
- 还有 1 个 `greedy_prompt`

所以初始化会评估总共 4 个 prompt。

而每个 prompt 会调用：

- `validate_prompt(prompt)`

这个函数又会：

1. 用当前 LLM 生成 `batch_size` 个样本
2. 对每个样本逐个调用 `javac` 验证
3. 统计 SAFE 数量作为 prompt score

你当前 `batch_size = 30`，而 Ollama 路径下 `_generate_with_prompt()` 还是串行的：

```python
for _ in range(batch_size):
    response = ollama.chat(...)
```

因此初始化阶段总请求数大致是：

- `4 prompts * 30 samples = 120 次 Ollama 生成`

如果单次生成平均 6 到 8 秒，那么：

- `120 * 7s ≈ 840s`
- 也就是 14 分钟左右

这和你实际观察到的 15 分钟非常吻合。

### 2.2 第二阶段会把这个问题放大

一旦第二阶段 refresh 真正触发，它会再次做一套类似流程：

1. 生成 refresh request
2. 让 autoprompt 模型产生 `greedy + candidates`
3. 对这些新 prompt 再做 `validate_prompt()`

如果不优化，第二阶段每触发一次都可能再额外吃掉一轮高成本初始化时间。

所以：

- 第二阶段功能逻辑是对的
- 但性能上必须收敛，否则真正跑长任务时会明显拖慢主 fuzzing

## 3. 初始化变慢的根本原因

不是 `javac` 慢，也不是日志写入慢，而是三件事叠加：

1. prompt 候选数量偏多
2. prompt 评分样本数直接复用了主 fuzzing 的 `batch_size=30`
3. Ollama 生成是串行，不是并行

所以本质问题是：

- “用于 prompt 选择的评估成本”和“用于正式 fuzzing 的生成成本”被绑定在一起了

这是当前最应该拆开的点。

## 4. 性能优化方案计划

这里先给方案，不直接改，等你确认后再动。

### 方案 A：为 prompt 评分单独引入更小的 batch

新增两个配置项：

- `autoprompt_validation_batch_size`
- `runtime_refresh_validation_batch_size`

建议默认：

- 初始化 autoprompt 评分：`6` 或 `8`
- runtime refresh 评分：`4` 或 `6`

理由：

- prompt 评分不需要和正式 fuzzing 一样生成 30 个样本
- 评分只要能大致区分候选 prompt 即可
- 这样初始化可以从 120 次生成降到 24 或 32 次

这是最有效、最稳的优化。

### 方案 B：降低 refresh 阶段候选数

当前：

- `prompt_refresh_candidates = 3`

建议：

- runtime refresh 用 `1` 或 `2`

理由：

- refresh 是运行中的增量优化，不需要像初始 prompt 选择那样广搜
- 候选越少，越不阻塞 fuzzing 主流程

### 方案 C：对 Ollama prompt 评分阶段设置更短生成长度

当前：

- `max_length = 1024`

建议：

- prompt 评分阶段单独设置 `validation_max_length = 384` 或 `512`

理由：

- prompt 评分只关心“能否生成可编译样本”
- 不需要每次都放到正式 fuzzing 那样的长度

### 方案 D：只在“规则变化明显”时才触发 refresh

可增加判断：

- 只有当 `failure_rules` 和上次相比出现新增/替换时
- 才进行 `refresh_prompt_from_feedback()`

理由：

- 避免重复用几乎同一批规则做重写
- 降低无效 refresh

### 方案 E：给 prompt score 做哈希缓存

可缓存：

- prompt 文本 hash -> score

理由：

- 如果 refresh 后某个 prompt 和已有 prompt 相同或近似，不要重复评估

### 我建议的优化顺序

先做：

1. A：评分 batch 拆小
2. B：refresh 候选数减少
3. D：规则变化才 refresh

后做：

4. C：评分长度单独收短
5. E：score cache

## 5. 已完成的 API 分类脚本

我已经新增并跑通：

- `scripts/classify_java_apis.py`

输出文件：

- `outputs/api_classification/java_api_5d_classification.json`
- `outputs/api_classification/java_api_5d_classification.csv`
- `outputs/api_classification/java_api_5d_summary.md`

实际结果：

- 全量分类了 `4410` 个 Java API 文档
- 脚本能够保证所有文档至少落到一个标签
- 主标签和多标签结果都已输出

### 5.1 分类规则来源

我从以下两个 `.doc` 中提取了关键标签线索：

- `api_classify.doc`
- `五维全息分类漏斗 .doc`

虽然它们是旧式 `.doc` 二进制格式，但我已经成功抽到了里面最关键的文本片段，包括：

- `RESOURCE`
- `BUFFER`
- `MARK_SUPPORT`
- `BATCH_OP`
- `CALLBACK`
- `CONCURRENT`
- `TIME`
- `FILE`
- `SECURITY`
- `REFLECT`
- `GENERIC`

另外还保留了扩展标签：

- `NETWORK`
- `JVM_MGMT`
- `UTILITY`

### 5.2 五维分类在脚本中的落地方式

脚本不是只看文件名，而是按五个维度综合打分：

1. `package`
2. `type`
3. `interface`
4. `field`
5. `method`
6. `boundary`

这里实际实现为“5 维漏斗 + 边界维度补充”，用于增强稳定性。

每个 API 的输出包含：

- `primary_tag`
- `all_tags`
- `scores`
- `dimensions` 中的命中证据

### 5.3 当前分类示例

当前分类结果中：

- `BufferedOutputStream -> RESOURCE`
- `BufferedInputStream -> RESOURCE`
- `SSLSession -> SECURITY`
- `Thread -> CONCURRENT`
- `File -> FILE`

这已经可以作为后续变异策略的稳定输入。

## 6. 基于分类结果的变异实施方案

这里先给设计，不直接改 fuzzing 主逻辑。

核心思想：

- 不再只靠通用 mutate/combine/equivalent
- 而是让“变异操作”由目标 API 的分类标签驱动

也就是：

- `target API classification -> mutation profile -> operator selection -> code mutation`

## 7. 变异系统的建议结构

### 7.1 新增一个分类结果加载层

建议未来新增：

- `Fuzz4All/util/api_classifier.py`

职责：

1. 读取 `outputs/api_classification/java_api_5d_classification.json`
2. 根据 `target_string` 或文档路径找到当前 API 的分类结果
3. 返回：
   - `primary_tag`
   - `all_tags`
   - `scores`

### 7.2 新增一个 Java 变异画像层

建议未来新增：

- `Fuzz4All/target/JAVA/mutation_profiles.py`

职责：

把标签映射成“可执行的变异画像”。

例如：

#### `RESOURCE`

变异方向：

- 生命周期交错：`write -> flush -> close -> write`
- try-with-resources 变体
- 嵌套资源
- `null` 底层流
- 构造后早关闭/重复关闭

#### `BUFFER`

变异方向：

- 缓冲区大小变化：`1`, `2`, `8`, `1024`, `Integer.MAX_VALUE`
- 大数组与小数组交替
- 连续小写入/大块写入混合
- 边界容量附近切换

#### `BATCH_OP`

变异方向：

- `write(byte[], off, len)` 中的 `off/len`
- `off=0`
- `len=0`
- `off+len == length`
- `off+len > length`

#### `MARK_SUPPORT`

变异方向：

- `mark/reset`
- 不同 `marklimit`
- `reset` 前后状态切换

#### `CONCURRENT`

变异方向：

- 线程间交错调用
- 多 producer / consumer
- lock/unlock 变种
- future cancel / timeout

#### `CALLBACK`

变异方向：

- 空 listener
- 重复注册/注销
- 回调中回调

#### `SECURITY`

变异方向：

- 非法 provider
- 弱算法 / 不支持算法
- `null` key / invalid key size
- 权限或 context 边界

#### `FILE`

变异方向：

- 非法路径
- 相对路径穿越
- 空路径
- 特殊字符路径

#### `TIME`

变异方向：

- 极值时间
- 时区边界
- epoch 前后

#### `REFLECT`

变异方向：

- private/public 切换
- 非法 method name
- 参数列表不匹配

#### `NETWORK`

变异方向：

- 非法 host/port
- timeout
- 连接状态交错

#### `UTILITY` / `GENERIC`

变异方向：

- `null`
- `0`
- `-1`
- `MAX/MIN`
- 空字符串 / Unicode

## 8. `BufferedOutputStream` 的变异重点

当前分类结果：

- `primary_tag = RESOURCE`
- 次级高分标签：
  - `BATCH_OP`
  - `BUFFER`

因此这个 API 最适合的变异重点应该是：

1. 资源生命周期变异
2. `write(byte[], off, len)` 参数边界变异
3. 缓冲区大小变异
4. 嵌套流结构变异
5. checked exception 结构变异

也就是说，对 `BufferedOutputStream` 来说，最值钱的不是“随便改代码”，而是围绕这三个主轴：

- lifecycle
- off/len
- buffer-size

## 9. 变异逻辑未来应加在哪里

### 建议不要直接改 `Target.update()`

理由：

- `Target.update()` 是 prompt 层逻辑
- 变异算子更适合放在 target 侧

### 建议优先改 `JAVATarget.update_strategy()` 或新增 Java 专用变异入口

推荐未来结构：

1. 保留现有 `update_strategy()` 的大框架
2. 在 `JAVATarget` 中增加：
   - `build_mutation_profile()`
   - `select_mutation_operators()`
   - `render_mutation_instruction()`

然后让 Java 的 prompt 更新从：

- “等价 / 变异 / 合并”

升级成：

- “根据 API 分类画像选择资源/批量参数/缓冲边界类变异”

## 10. 我建议的下一步改动顺序

如果你认可这份方案，建议这样推进：

### 第一步：性能优化

先改初始化和 refresh 评分成本：

1. 新增 `autoprompt_validation_batch_size`
2. 新增 `runtime_refresh_validation_batch_size`
3. 减少 refresh candidates
4. 只在规则变化时才 refresh

理由：

- 不先控速，第二阶段越完整越慢

### 第二步：分类结果接入运行时

新增一个读取分类结果的轻量模块，让当前 target 能拿到：

- `primary_tag`
- `top secondary tags`

### 第三步：只做 prompt 级变异提示，不直接做 AST/源码重写

先让分类标签驱动 prompt instruction，例如：

- “please mutate around resource lifecycle”
- “please explore off/len boundary combinations”
- “please vary constructor buffer size”

这样：

- 成本低
- 风险低
- 容易观察是否有用

### 第四步：再考虑更强的代码级算子

只有当 prompt 级变异已经明显有效时，再考虑：

- 模板替换
- 局部结构重写
- 代码片段拼接

## 11. 最终判断

### 对 `new413` 的判断

符合当前阶段预期。

已经实现：

- 第一阶段结构化反馈闭环
- 第二阶段代码接入

尚未观察到：

- 第二阶段运行时 refresh 的实际输出

原因是：

- 这次样本数不足以触发 refresh，而不是代码失效

### 对“慢”的判断

初始化慢是结构性问题，不是偶发问题。

如果不做性能收敛，后面第二阶段真正开始多轮 refresh 后，整体运行时间会继续上升。

### 对变异方向的判断

最合适的路线不是立刻改复杂源码变异器，而是：

1. 先用五维分类结果建立 API mutation profile
2. 再让 profile 驱动 prompt 级变异
3. 最后再考虑代码级变异

这是最稳、最容易验证收益的路径。
