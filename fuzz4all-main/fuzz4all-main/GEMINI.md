现在这套系统已经不是原始 Fuzz4All 了，主线已经改成了：

config/documentation：每个 API 一份文档
outputs/api_classification：先离线做 5D 分类
config/targeted：每个 API 一份 target 配置
Fuzz4All/mutation：按分类加载 profile 和通用变异因子
Fuzz4All/target：生成、编译、反馈、refresh 闭环
outputs/targeted*：每轮验证结果
也就是说，你现在的项目已经具备了“API 文档驱动 + 分类驱动变异 + 编译反馈优化”的雏形，而且很多关键环节已经跑通了。

按目录和代码说现在做到了什么

1. config/documentation
这里现在已经不是“语言特性文档”，而是每个 API 的单独文档。
这是整套方案的输入源。

作用：

DeepSeek/autoprompt 读这里
离线分类也读这里
target 配置里的 path_documentation 都指向这里
当前状态：

已完成
已经成为你整套系统的标准输入层
2. outputs/api_classification
这里是离线 5D 分类结果。

关键文件：

java_api_5d_classification.json
java_api_5d_classification.csv
java_api_5d_summary.md
作用：

给每个 API 打：
primary_tag
all_tags
mutation_profile
priority_operators
risk_points
运行时 profile loader 会读它
当前状态：

已完成，并且已经做过一轮较大修正
现在主标签已经能比较稳定区分：
SECURITY
FILE
REFLECT
CONCURRENT
CALLBACK
TIME
NETWORK
UTILITY
JVM_MGMT
RESOURCE
这是整套系统的“离线知识层”
还要继续做的：

小幅调权重可以继续做
但它已经不是当前最大瓶颈了
3. config/targeted
这里现在是每个 API 一份 target 配置。

关键变化：

你已经不再是少数手写 yaml
而是把 documentation 对应的大量 API 都生成成了 target
文件名和 API 对齐，便于批量跑
作用：

决定单个 API 怎么 fuzz
决定是否启用 mutation、refresh、autoprompt
决定 target 文档、target_string、prompt 约束等
当前状态：

大规模配置已经生成完
代表 API 的配置已经被调成“收敛验证版”
生成脚本 generate_targeted_configs.ps1 现在也支持按分类自动给默认模板
这很重要：

现在不是只手工修几个 yaml
而是以后新生成 target 也会自动继承分类模板
还要继续做的：

如果后面分类策略稳定，可以再批量重生成一次全量 target
让全量 API 都继承最新分类模板
4. Fuzz4All/mutation/profile_loader.py
这是离线分类结果 -> 运行时 mutation profile 的桥。

作用：

读取 java_api_5d_classification.json
决定某个 API 当前属于哪个 primary_tag
决定使用哪个 mutation_profile
决定激活哪些 active_profiles
组合出当前可用的 operator 集
当前状态：

已经是整套系统的核心之一
现在已经支持多类 profile：
security_provider_flow
reflection_dispatch
file_path_state
concurrent_sequence
callback_registration_flow
time_boundary_mix
network_endpoint_state
utility_value_boundary
jvm_mgmt_runtime_state
resource_buffer_batch
mark_reset_sequence
还加了运行时纠偏逻辑，避免旧分类结果直接掉进 generic_java
当前问题：

还可以继续微调弱类的 active profile 组合
但总体上已经“能用”
5. Fuzz4All/mutation/java_mutator.py
这是真正执行分类变异因子的地方。

作用：

按 priority_operators 对 seed 做 mutation
生成每条 mutation 样例
把 category-specific operator 真正落到代码上
当前已经有的能力：

security_*
file_*
reflect_*
concurrent_*
callback_*
time_*
network_*
utility_*
jvm_mgmt_*
resource_*
mark_support_*
generic_*
当前状态：

强类已经足够支撑验证
弱类也已经有第一版通用算子
RESOURCE 我们已经补了一轮，让它不再只偏输出流，而能更像输入流/读流
当前问题：

RESOURCE 还没有完全把 read/mark/reset 类算子转化成很多有效样例
CALLBACK、JVM_MGMT 虽然有算子，但生成质量还是受 seed 影响很大
6. Fuzz4All/target/JAVA/JAVA.py
这是Java 目标的验证与反馈归因层。

作用：

把生成代码写回文件
调 javac
归类错误类型
把错误类型转成分类级规则
提供 structured feedback 给 prompt 刷新
当前状态：

已经从原来很局部的 BufferedOutputStream 风格，改成了通用 Java API 反馈器
支持按 primary_tag 追加分类级规则：
SECURITY
FILE
REFLECT
CONCURRENT
CALLBACK
TIME
NETWORK
JVM_MGMT
MARK_SUPPORT
UTILITY
RESOURCE
我们最近刚做的最关键改动：

把“方法不存在”和“重载/参数不匹配”拆开归因
这很关键，因为：

以前 CALLBACK 会把合法的 add/remove/fire 也误判成 undocumented
现在应该能更准确地区分：
API 根本不存在
API 存在但参数错了
当前问题：

这块已经接近正确形态了
但真正效果还要靠下一轮服务器结果验证
7. Fuzz4All/target/target.py
这是总控闭环层。

作用：

初始化模型
做 auto_prompt
生成代码
写 best_prompt.txt
做 runtime feedback 汇总
决定什么时候 refresh
写 runtime prompt / runtime rules / refresh 结果
当前状态：

主闭环已经有了：
best_prompt.txt
runtime_prompt_*.txt
runtime_rules_*.txt
mutation_manifest.jsonl
我们还补了：
refresh_status_round_*.txt
refresh_decision_round_*.txt
accepted_refreshed_prompt_round_*.txt
也就是说：

现在 prompt refresh 已经不再是“黑箱”
你后面能直接看出：
为什么某轮没 refresh
为什么 refresh 被接受/拒绝
当前问题：

首轮 autoprompt 还很慢，尤其 DeepSeek 网络慢时
这不是主设计错了，而是初始化太重
8. outputs/targeted*
这里是你一轮轮实验结果的证据。

你已经跑过：

newtargeted
outputs002
targeted1
targeted2
targeted4
targeted5
targeted6
从这些结果可以看到系统的演化：

早期阶段
都掉到 generic_java
说明分类没有真正驱动运行时
中期阶段
targeted2 / targeted4
SECURITY / FILE / REFLECT / CONCURRENT 已经跑通
说明主链打通了
后期阶段
targeted5
新增 NETWORK / UTILITY / TIME / RESOURCE / CALLBACK / JVM_MGMT
说明 10 类代表集基本铺开了
最新阶段
targeted6
说明分类级收紧逻辑是生效的
但弱类质量还没完全到位
现在到底做到了什么

如果一句话概括：

你已经完成了“分类驱动 fuzz 架构”的主体改造，并且强类已经基本跑通，弱类正在收尾。

再具体一点：

已经做到的
每个 API 有独立文档输入
每个 API 有离线分类结果
每个 API 有对应 target 配置
运行时能按分类加载 mutation profile
强类已经能稳定出现分类专属 operator
编译日志能提炼成分类级反馈规则
runtime prompt 会根据 SAFE 和失败规则更新
refresh 过程已经可观察
还没完全做到的
CALLBACK 还没稳定产出 SAFE
JVM_MGMT 还没稳定产出 SAFE
RESOURCE 虽然提升了，但资源类定制算子贡献还不够强
首轮 autoprompt 初始化太慢
还没有一轮“10 类都达标”的最终实验结果
接下来还需要做什么

现在不应该再大范围改分类体系了，后面应该收口到这几件事：

1. 解决首轮 autoprompt 太慢
这是当前最直接卡住你的问题。

可选方向：

调试时首轮跳过 DeepSeek autoprompt
或给 auto_prompt 增加“快速模式”
或允许先用分类模板 prompt，后续再 refresh
这是现在最应该先处理的工程问题。

2. 把 CALLBACK 拉起来
重点：

验证新的错误归因拆分是否生效
看它是否不再把合法 overload 全当不存在
目标是让它出现一批 SAFE
3. 把 JVM_MGMT 拉起来
重点：

看新 seed 是否更集中于标准 MXBean query 入口
减少发明伪方法
至少让它从 0 SAFE 变成可用
4. 再提升 RESOURCE
重点：

看读流/mark/reset/skip/available 类变异是否真的开始产出
不再主要靠 resource_exception_shell
5. 做最终 10 类代表集验证
最终应该固定 10 个代表 API：

SECURITY：Cipher
FILE：File
REFLECT：Method
CONCURRENT：Thread
CALLBACK：PropertyChangeSupport
TIME：Duration
NETWORK：Socket
UTILITY：URI
JVM_MGMT：ManagementFactory
RESOURCE：BufferedInputStream
然后统一看：

primary_tag
mutation_profile
operator 分布
SAFE / FAILURE
refresh 证据
最终系统效果应该是什么样

理想的最终效果不是“能跑几个 API”，而是下面这个整体系统：

输入层
config/documentation 里放 API 文档
系统自动分类、自动生成 target
离线知识层
outputs/api_classification 为每个 API 输出：
主标签
复合画像
风险点
变异优先级
在线生成层
DeepSeek 先根据 API 文档生成高质量 prompt
Qwen/Ollama 根据 prompt 生成 seed
分类变异层
系统根据 API 分类自动选择 profile
通用分类算子对 seed 变异
不是按单 API 硬编码，而是按类生效
反馈优化层
seed 和 mutation 一起编译验证
javac 日志被归因为结构化规则
DeepSeek 根据规则和 SAFE 样例刷新 prompt
prompt 发生多轮迭代，而不是一次性写死
输出层
每个目标目录里最终应稳定出现：

best_prompt.txt
runtime_prompt_*.txt
runtime_rules_*.txt
refresh_status_round_*.txt
refresh_decision_round_*.txt
accepted_refreshed_prompt_round_*.txt
mutation_manifest.jsonl
大量 SAFE 和可解释的失败样例
验证层
10 类代表 API 都能进入正确分类画像
都能出现对应 operator
强类有稳定 SAFE
弱类至少有可用 SAFE
refresh 有证据
能做实验对比和论文结果分析