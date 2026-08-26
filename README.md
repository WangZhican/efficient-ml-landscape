<div align="center">

# ⚡ Efficient ML Landscape

### A curated research atlas for **Efficient ML · AI Infrastructure · Physical AI**

<p>
  <a href="README.zh-CN.md"><b>中文</b></a>
  ·
  <a href="docs/METHODOLOGY.md">Methodology</a>
  ·
  <a href="papers/README.md">Research Map</a>
  ·
  <a href="papers/LATEST_30D.md"><b>Latest 30 Days</b></a>
  ·
  <a href="papers/CLASSICAL.md">Classical</a>
  ·
  <a href="papers/ALL_PAPERS.md">Paper Library</a>
  ·
  <a href="groups/README.md">Groups</a>
  ·
  <a href="venues/README.md">Venues</a>
</p>

<p>
  <img src="https://img.shields.io/badge/Papers-1039-7c3aed?style=for-the-badge" alt="1039 papers" />
  <img src="https://img.shields.io/badge/Primary%20Links-1017-059669?style=for-the-badge" alt="1017 primary links" />
  <img src="https://img.shields.io/badge/Research%20Tracks-15-2563eb?style=for-the-badge" alt="15 research tracks" />
  <img src="https://img.shields.io/badge/Physical%20AI-Protected-f59e0b?style=for-the-badge" alt="Physical AI protected" />
</p>

<p>
  <img src="https://img.shields.io/github/stars/WangZhican/efficient-ml-landscape?style=flat-square" alt="GitHub stars" />
  <img src="https://img.shields.io/github/last-commit/WangZhican/efficient-ml-landscape?style=flat-square" alt="Last commit" />
  <img src="https://img.shields.io/github/repo-size/WangZhican/efficient-ml-landscape?style=flat-square" alt="Repo size" />
</p>

**Influential papers, technical lineages, major research groups, systems venues, official repositories, and auditable coverage — in one place.**

### [🆕 Track the latest 30 days →](papers/LATEST_30D.md)

### [🏛️ Browse the classical / historical census →](papers/CLASSICAL.md)

### [📚 Open the complete paper library →](papers/ALL_PAPERS.md)

### [🧭 Explore by 15 research directions →](papers/README.md)

</div>

---

## 📊 Library at a glance

| Metric | Current public view |
|---|---:|
| **Quality-gated unique papers** | **1039** |
| **Latest 30-day tracked total** | **279** |
| **Latest 30-day quality-gated papers** | **50** |
| **Latest watchlist** | **108** |
| **Latest relevant low-priority** | **121** |
| **Classical / historical papers** | **989** |
| **Papers with resolved primary-source links** | **1017** |
| **Latest strong papers** | **45** |
| **Research directions** | **15** |
| **Venue/source labels represented** | **46** |

> [!IMPORTANT]
> The paper library is split into a **rolling Latest 30 Days view** for active tracking and a **Classical / Historical view** for the long-term canonical census. The latest tracker is deliberately broader: **topical relevance decides visibility, while quality decides P0/P1/P2 priority**. The classical census remains quality-gated.

---

## ✨ What makes this different?

This is **not a flat awesome-list** and not a paper dump. The goal is to reconstruct the field as a navigable research graph:

> **problem → technical route → canonical paper → follow-up lineage → systems impact → open-source adoption**

The **Classical / Historical** library is quality-gated. The **Latest 30 Days** tracker is coverage-oriented: directly relevant work is retained as P0/P1/P2 rather than disappearing below a single quality threshold. There is **no fixed paper-count quota**. When technical value is comparable, official open source, stronger community adoption, and higher GitHub stars receive additional weight.

> [!NOTE]
> **No paper PDFs are stored in this public repository.** Paper entries link to primary sources such as arXiv, official proceedings, DOI pages, and author/project pages, plus the official code repository when available.

---

## 🧭 Research Atlas

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

### **15 directions · one connected research map**

[**Explore the research map →**](papers/README.md) · [**Browse every paper →**](papers/ALL_PAPERS.md)

</div>

---

## 🤖 Physical AI is a first-class track

Physical AI is intentionally protected from being buried inside a generic multimodal category. The map explicitly follows:

`VLA / WAM serving` · `cache / quant / sparsity` · `action-head / flow / diffusion` · `streaming agents` · `cloud-edge execution` · `runtime / infrastructure co-design`

The emphasis is not only on model algorithms, but also on **serving, runtime, scheduling, heterogeneous deployment, state reuse, real-time control loops, and hardware-aware execution**.

---

## 📚 What each paper record contains

| Field | What you get |
|---|---|
| **Paper** | Title, authors when available, year, venue |
| **Research role** | Direction, sub-direction, and technical position in the roadmap |
| **Why it matters** | Concise contribution and influence summary when validated |
| **Primary source** | arXiv / official proceedings / DOI / official project page |
| **Code** | Official repository or project implementation when verified |
| **Open source** | Code / model / runtime availability |
| **Adoption** | GitHub stars when meaningful and timestamped |
| **Priority** | Canonical / must-read / important / watch |
| **Lineage** | Predecessors, follow-ups, and competing routes |

A major paper may intentionally appear in multiple directions when it plays a genuinely different technical role in each roadmap.

---

## 🗺️ Repository map

| Area | Purpose |
|---|---|
| [`papers/ALL_PAPERS.md`](papers/ALL_PAPERS.md) | **Complete public paper list** |
| [`papers/`](papers/README.md) | Direction-by-direction research roadmaps and curated papers |
| [`groups/`](groups/README.md) | Major academic labs, companies, startups, and OSS ecosystems |
| [`venues/`](venues/README.md) | Venue/source census and systematic coverage map |
| [`data/papers.json`](data/papers.json) | Machine-readable public paper database |
| [`data/papers.csv`](data/papers.csv) | Spreadsheet-friendly public export |
| [`docs/`](docs/) | Methodology, audit rules, roadmap notes, and changelog |
| `scripts/` | Exporters, validators, and metadata synchronization tools |

---

## 🔎 Selection philosophy

We optimize for **research value rather than list size**.

**Prefer**

- technically original and influential work;
- systems / architecture / deployment relevance;
- official open-source code, models, or runtimes;
- strong adoption and meaningful GitHub-star signal;
- papers that create, redirect, or consolidate an important research route;
- first-party evidence.

**Avoid**

- quota-driven padding;
- duplicate records with no distinct technical role;
- third-party repositories presented as official implementations;
- weak keyword matches with little Efficient-ML relevance;
- claiming coverage simply because a source was visited once.

---

## ✅ Coverage is audited, not assumed

<div align="center">

### `SEARCHED  ≠  COVERED  ≠  SATURATED`

</div>

The underlying census tracks freshness windows, venue coverage, major-group coverage, historical recall, and canonical citation neighborhoods. Saturation is only claimed after systematic **zero-new confirmation rounds**; a large paper count by itself is not evidence that the map is complete.

Read the full methodology: **[docs/METHODOLOGY.md](docs/METHODOLOGY.md)**.

---

## 🚧 Current enrichment phase

The paper base is now public. The next layer is being added continuously:

**official repo verification → open-source status → GitHub-star snapshots → must-read tiers → technical lineage → group/venue links → route summaries**

This separation keeps the paper census immediately useful while preventing unverified repository links or metadata from being published as fact.

---

<div align="center">

### 🌟 Built for researchers who want the **map**, not just the papers.

If this repository helps your research, consider starring it so you can find the latest updates easily.

</div>
