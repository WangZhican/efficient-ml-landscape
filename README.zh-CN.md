# Efficient ML Landscape

一个持续维护的 Efficient ML / AI Infrastructure 研究地图。重点覆盖 2024 年至今的重要工作，并仅在确有必要时保留少量更早的经典论文。

> **公开仓库不存放论文 PDF。** 每条论文记录只提供可信的一手论文链接，以及存在时的官方代码 / 项目仓库链接。

## 15 个长期方向

1. LLM Serving
2. Speculative Decoding
3. KV Cache / Long Context
4. Quantization
5. Sparsity / Pruning
6. Efficient Attention
7. MoE Systems / Accelerators
8. GPU Kernel / DSL / Compiler
9. Distributed Training / Inference
10. Multimodal / MLLM Serving
11. Video / Image Generation Acceleration
12. Diffusion / Flow Acceleration
13. Efficient Reasoning / Agent Systems
14. VLA / WAM / Physical AI Serving
15. Edge / Cloud / Heterogeneous AI Systems

## 仓库内容

- `papers/`：按方向和子方向整理的论文路线图
- `groups/`：重要高校课题组、研究院、公司与开源生态
- `venues/`：重要会议与来源覆盖地图
- `data/`：机器可读的论文 / group / venue 数据
- `docs/`：收录标准、去重、coverage / saturation 与审计方法
- `scripts/`：用于从权威数据库导出 Markdown / JSON / CSV 并做一致性校验的脚本

## 每篇论文的公开字段

在信息可核验时，至少提供：标题、作者、年份、venue、方向、子方向、技术角色、核心贡献、论文一手链接、官方 repo / project 链接、是否开源、GitHub stars、推荐等级、与前后工作的技术关系。

同一篇重要论文允许出现在多个方向，只要它在各方向承担不同的技术角色；不会为了全局去重而破坏研究路线。

## 收录原则

没有固定论文数量上限。只按技术贡献、影响力、研究路线价值、系统 / 架构 / 部署价值和一手证据决定是否收录。在技术贡献相近时，优先官方开源代码 / 模型 / runtime、社区采用更广以及 GitHub stars 更高的工作。

## Coverage 与 Saturation

`SEARCHED != COVERED != SATURATED`。

访问过某个来源不代表完成覆盖；完成一轮覆盖也不代表已经饱和。只有经过系统的 zero-new confirmation round，才能声明 saturation。论文数量很多本身不构成“没有明显遗漏”的证据。

## Physical AI

Physical AI 是长期保护方向，独立覆盖 VLA/WAM serving、cache / quantization / sparsity、action-head / flow / diffusion、streaming agent、cloud-edge 和 runtime / infrastructure。

## 当前状态

仓库正在从内部持续维护的高召回文献 census 中生成公开版。只有完成 identifier 去重、论文来源核验和 repo 链接核验的记录才会进入公开仓库。
