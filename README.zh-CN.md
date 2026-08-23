<div align="center">

# ⚡ Efficient ML Landscape

### 面向 **Efficient ML · AI Infrastructure · Physical AI** 的持续研究地图

<p>
  <a href="README.md"><b>English</b></a>
  ·
  <a href="docs/METHODOLOGY.md">方法论</a>
  ·
  <a href="papers/README.md">研究地图</a>
  ·
  <a href="papers/LATEST_30D.md"><b>最近 30 天</b></a>
  ·
  <a href="papers/CLASSICAL.md">经典论文</a>
  ·
  <a href="papers/ALL_PAPERS.md">论文库</a>
  ·
  <a href="groups/README.md">研究团队</a>
  ·
  <a href="venues/README.md">Venue 地图</a>
</p>

<p>
  <img src="https://img.shields.io/badge/Papers-700-7c3aed?style=for-the-badge" alt="700 papers" />
  <img src="https://img.shields.io/badge/Primary%20Links-681-059669?style=for-the-badge" alt="681 primary links" />
  <img src="https://img.shields.io/badge/Research%20Tracks-15-2563eb?style=for-the-badge" alt="15 research tracks" />
  <img src="https://img.shields.io/badge/Physical%20AI-Protected-f59e0b?style=for-the-badge" alt="Physical AI protected" />
</p>

<p>
  <img src="https://img.shields.io/github/stars/WangZhican/efficient-ml-landscape?style=flat-square" alt="GitHub stars" />
  <img src="https://img.shields.io/github/last-commit/WangZhican/efficient-ml-landscape?style=flat-square" alt="Last commit" />
  <img src="https://img.shields.io/github/repo-size/WangZhican/efficient-ml-landscape?style=flat-square" alt="Repo size" />
</p>

**重要论文 · 技术路线 · 研究团队 · 系统 Venue · 官方代码 · Coverage Audit，一站式整理。**

### [🆕 追踪最近 30 天最新论文 →](papers/LATEST_30D.md)

### [🏛️ 浏览经典 / 历史论文库 →](papers/CLASSICAL.md)

### [📚 打开完整论文库 →](papers/ALL_PAPERS.md)

### [🧭 按 15 个研究方向浏览 →](papers/README.md)

</div>

---

## 📊 当前论文库

| 指标 | 当前公开版本 |
|---|---:|
| **质量门控后的唯一论文** | **700** |
| **最近 30 天追踪总数** | **194** |
| **最近 30 天质量门控论文** | **46** |
| **最近 30 天 Watchlist** | **45** |
| **最近 30 天低优先级相关论文** | **103** |
| **经典 / 历史论文** | **654** |
| **已有可信一手论文链接** | **681** |
| **最新 Strong 论文** | **45** |
| **研究方向** | **15** |
| **已出现的 Venue/Source 标签** | **46** |

> [!IMPORTANT]
> **Paper list 是这个仓库的核心。** 公开视图明确拆成 **滚动最近 30 天** 和 **经典 / 历史 canonical census** 两部分。最近 30 天采用更偏 recall 的策略：**内容相关决定是否可见，质量决定 P0/P1/P2 优先级**；经典库仍保持高质量门槛。

---

## ✨ 这个仓库和普通 Awesome List 有什么区别？

它不是把论文标题平铺在一起，而是尽量恢复领域真正的研究结构：

> **问题 → 技术路线 → 代表论文 → 后续演进 → 系统影响 → 开源采用**

没有固定论文数量上限。**经典库**仍按技术贡献、影响力、研究路线价值、系统/架构/部署价值和一手证据做高门槛筛选；**最近 30 天**则先保证相关工作不漏掉，再按 P0 Strong / P1 Watch / P2 Relevant-Low-Priority 分级。技术贡献接近时，官方开源、社区采用度和 GitHub stars 会得到额外加权。

> [!NOTE]
> **公开仓库不存放论文 PDF。** 每篇论文只链接到 arXiv、官方 proceedings、DOI、作者/项目主页等可信一手来源，以及存在时的官方代码仓库。

---

## 🧭 15 个研究方向

<table>
<tr>
<td width="33%" valign="top">

### 🖥️ Serving & Runtime
- [LLM Serving](papers/01-llm-serving.md)
- [Speculative Decoding](papers/02-speculative-decoding.md)
- [KV Cache / Long Context](papers/03-kv-cache-long-context.md)
- [Multimodal / MLLM Serving](papers/10-multimodal-mllm-serving.md)
- [Edge / Cloud / Heterogeneous AI](papers/15-edge-cloud-heterogeneous.md)

</td>
<td width="33%" valign="top">

### 🧠 Model Efficiency
- [Quantization](papers/04-quantization.md)
- [Sparsity / Pruning](papers/05-sparsity-pruning.md)
- [Efficient Attention](papers/06-efficient-attention.md)
- [MoE Systems / Accelerators](papers/07-moe-systems.md)
- [Efficient Reasoning / Agents](papers/13-efficient-reasoning-agents.md)

</td>
<td width="33%" valign="top">

### ⚙️ Systems & Generation
- [GPU Kernel / DSL / Compiler](papers/08-gpu-kernel-compiler.md)
- [Distributed Training / Inference](papers/09-distributed-training-inference.md)
- [Video / Image Generation](papers/11-video-image-generation.md)
- [Diffusion / Flow Acceleration](papers/12-diffusion-flow.md)
- [VLA / WAM / Physical AI](papers/14-physical-ai-vla-wam.md)

</td>
</tr>
</table>

<div align="center">

### **15 个方向，一张互相连接的研究地图**

[**进入研究地图 →**](papers/README.md) · [**浏览全部论文 →**](papers/ALL_PAPERS.md)

</div>

---

## 🤖 Physical AI 是一级方向

Physical AI 不会被埋在普通 multimodal 分类里，而是长期独立保护，显式覆盖：

`VLA / WAM serving` · `cache / quant / sparsity` · `action-head / flow / diffusion` · `streaming agent` · `cloud-edge` · `runtime / infrastructure`

重点不仅是模型算法，也包括 **serving、runtime、调度、异构部署、state reuse、real-time control loop 和 hardware-aware execution**。

---

## 📚 每篇论文会提供什么？

| 字段 | 内容 |
|---|---|
| **Paper** | 标题、可核验时的作者、年份、Venue |
| **Research role** | 所属方向、子方向以及在技术路线中的位置 |
| **Why it matters** | 核心贡献与影响力摘要 |
| **Primary source** | arXiv / 官方 proceedings / DOI / 官方项目页 |
| **Code** | 核验后的官方 repo / project implementation |
| **Open source** | 是否公开代码、模型或 runtime |
| **Adoption** | 有意义时记录 GitHub stars，并附核验时间 |
| **Priority** | Canonical / Must-read / Important / Watch |
| **Lineage** | 前驱、后继与竞争路线 |

真正重要的论文允许出现在多个方向，只要它在不同路线中承担不同技术角色，而不会为了全局去重破坏研究脉络。

---

## 🗺️ 仓库导航

| 区域 | 用途 |
|---|---|
| [`papers/ALL_PAPERS.md`](papers/ALL_PAPERS.md) | **完整公开论文总表** |
| [`papers/`](papers/README.md) | 15 个方向的路线图与分类论文表 |
| [`groups/`](groups/README.md) | 高校实验室、公司、startup 与 OSS ecosystem |
| [`venues/`](venues/README.md) | Venue/source census 与系统覆盖地图 |
| [`data/papers.json`](data/papers.json) | 机器可读论文数据库 |
| [`data/papers.csv`](data/papers.csv) | 适合表格软件使用的公开导出 |
| [`docs/`](docs/) | 方法论、审计规则、研究路线与 changelog |
| `scripts/` | Markdown / JSON / CSV 导出与一致性校验 |

---

## 🔎 收录原则

目标是最大化 **研究价值，而不是列表长度**。

**优先收录**

- 技术原创性和影响力强的工作；
- 具有 systems / architecture / deployment 价值的工作；
- 有官方开源代码、模型或 runtime 的工作；
- 社区采用广、GitHub star 信号强的工作；
- 创建、改变或巩固重要研究路线的工作；
- 能够由一手来源可靠核验的工作。

**避免**

- 为了凑数量而收录；
- 没有不同技术角色的无意义重复；
- 把第三方 reproduction 冒充官方 repo；
- 仅关键词命中但与 Efficient ML 关系很弱的工作；
- 把“搜索过”误写成“覆盖完成”。

---

## ✅ Coverage 需要证明，而不是感觉

<div align="center">

### `SEARCHED  ≠  COVERED  ≠  SATURATED`

</div>

内部 census 会显式跟踪 freshness window、venue coverage、major-group coverage、historical recall 和 canonical citation neighborhood。只有完成系统性的 **zero-new confirmation round** 才会声明 saturation；“已经收了很多论文”本身不是充分证据。

完整规则见：**[docs/METHODOLOGY.md](docs/METHODOLOGY.md)**。

---

## 🚧 当前增强阶段

论文底库已经公开。接下来持续在 424 篇论文之上增加：

**官方 repo 核验 → 开源状态 → GitHub stars → Must-Read 等级 → 技术 lineage → group/venue 关联 → 路线总结**

这样先保证论文列表立即可用，同时避免把没有验证过的 repo 或 metadata 当成事实发布。

---

<div align="center">

### 🌟 给真正想理解“研究地图”，而不是只收藏论文的人。

如果这个仓库对你有帮助，可以 Star 一下，后续重要路线更新会持续同步。

</div>
