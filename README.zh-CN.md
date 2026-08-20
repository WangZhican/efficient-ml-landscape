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
  <a href="groups/README.md">研究团队</a>
  ·
  <a href="venues/README.md">Venue 地图</a>
</p>

<p>
  <img src="https://img.shields.io/badge/Research%20Tracks-15-2563eb?style=for-the-badge" alt="15 research tracks" />
  <img src="https://img.shields.io/badge/Papers-Quality--Gated-7c3aed?style=for-the-badge" alt="Quality-gated papers" />
  <img src="https://img.shields.io/badge/PDFs-Links%20Only-059669?style=for-the-badge" alt="Links only" />
  <img src="https://img.shields.io/badge/Physical%20AI-Protected-f59e0b?style=for-the-badge" alt="Physical AI protected" />
</p>

<p>
  <img src="https://img.shields.io/github/stars/WangZhican/efficient-ml-landscape?style=flat-square" alt="GitHub stars" />
  <img src="https://img.shields.io/github/last-commit/WangZhican/efficient-ml-landscape?style=flat-square" alt="Last commit" />
  <img src="https://img.shields.io/github/repo-size/WangZhican/efficient-ml-landscape?style=flat-square" alt="Repo size" />
</p>

**重要论文 · 技术路线 · 研究团队 · 系统 Venue · 官方代码 · Coverage Audit，一站式整理。**

</div>

---

## ✨ 这个仓库和普通 Awesome List 有什么区别？

它不是把论文标题平铺在一起，而是尽量恢复领域真正的研究结构：

> **问题 → 技术路线 → 代表论文 → 后续演进 → 系统影响 → 开源采用**

没有固定论文数量上限。是否收录只由技术贡献、影响力、研究路线价值、系统/架构/部署价值和一手证据决定；技术贡献接近时，官方开源、社区采用度和 GitHub stars 会得到额外加权。

> [!NOTE]
> **公开仓库不存放论文 PDF。** 每篇论文只链接到 arXiv、官方 proceedings、DOI、作者/项目主页等可信一手来源，以及存在时的官方代码仓库。

---

## 🧭 15 个研究方向

<table>
<tr>
<td width="33%" valign="top">

### 🖥️ Serving & Runtime
- LLM Serving
- Speculative Decoding
- KV Cache / Long Context
- Multimodal / MLLM Serving
- Edge / Cloud / Heterogeneous AI

</td>
<td width="33%" valign="top">

### 🧠 Model Efficiency
- Quantization
- Sparsity / Pruning
- Efficient Attention
- MoE Systems / Accelerators
- Efficient Reasoning / Agents

</td>
<td width="33%" valign="top">

### ⚙️ Systems & Generation
- GPU Kernel / DSL / Compiler
- Distributed Training / Inference
- Video / Image Generation
- Diffusion / Flow Acceleration
- VLA / WAM / Physical AI

</td>
</tr>
</table>

<div align="center">

### **15 个方向，一张互相连接的研究地图**

[**进入完整研究地图 →**](papers/README.md)

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
| **Paper** | 标题、作者、年份、Venue |
| **Research role** | 所属方向、子方向以及在技术路线中的位置 |
| **Why it matters** | 核心贡献与影响力摘要 |
| **Primary source** | arXiv / 官方 proceedings / DOI / 官方项目页 |
| **Code** | 官方 repo / project implementation |
| **Open source** | 是否公开代码、模型或 runtime |
| **Adoption** | 有意义时记录 GitHub stars，并附核验时间 |
| **Priority** | Canonical / Must-read / Important / Watch |
| **Lineage** | 前驱、后继与竞争路线 |

真正重要的论文允许出现在多个方向，只要它在不同路线中承担不同技术角色，而不会为了全局去重破坏研究脉络。

---

## 🗺️ 仓库导航

| 区域 | 用途 |
|---|---|
| [`papers/`](papers/README.md) | 15 个方向的路线图和精选论文 |
| [`groups/`](groups/README.md) | 高校实验室、公司、startup 与 OSS ecosystem |
| [`venues/`](venues/README.md) | Venue/source census 与系统覆盖地图 |
| [`data/`](data/README.md) | 机器可读的公开 metadata |
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

## 🚧 当前阶段

公开仓库正在由内部持续维护的高召回文献 census 生成。论文只有经过：

**identifier 去重 → 一手来源核验 → 技术分类 → repo/project 核验 → public export**

之后才进入公开视图，因此公开版本会比原始 discovery stream 更干净、更适合作为长期研究索引。

---

<div align="center">

### 🌟 给真正想理解“研究地图”，而不是只收藏论文的人。

如果这个仓库对你有帮助，可以 Star 一下，后续重要路线更新会持续同步。

</div>
