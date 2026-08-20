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
  <a href="groups/README.md">Groups</a>
  ·
  <a href="venues/README.md">Venues</a>
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

**Influential papers, technical lineages, major research groups, systems venues, official repositories, and auditable coverage — in one place.**

</div>

---

## ✨ What makes this different?

This is **not a flat awesome-list** and not a paper dump. The goal is to reconstruct the field as a navigable research graph:

> **problem → technical route → canonical paper → follow-up lineage → systems impact → open-source adoption**

Every retained work is quality-gated. There is **no fixed paper-count quota**. When technical value is comparable, official open source, stronger community adoption, and higher GitHub stars receive additional weight.

> [!NOTE]
> **No paper PDFs are stored in this public repository.** Paper entries link to primary sources such as arXiv, official proceedings, DOI pages, and author/project pages, plus the official code repository when available.

---

## 🧭 Research Atlas

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

### **15 directions · one connected research map**

[**Explore the research map →**](papers/README.md)

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
| **Paper** | Title, authors, year, venue |
| **Research role** | Direction, sub-direction, and technical position in the roadmap |
| **Why it matters** | Concise contribution and influence summary |
| **Primary source** | arXiv / official proceedings / DOI / official project page |
| **Code** | Official repository or project implementation when available |
| **Open source** | Code / model / runtime availability |
| **Adoption** | GitHub stars when meaningful and timestamped |
| **Priority** | Canonical / must-read / important / watch |
| **Lineage** | Predecessors, follow-ups, and competing routes |

A major paper may intentionally appear in multiple directions when it plays a genuinely different technical role in each roadmap.

---

## 🗺️ Repository map

| Area | Purpose |
|---|---|
| [`papers/`](papers/README.md) | Direction-by-direction research roadmaps and curated papers |
| [`groups/`](groups/README.md) | Major academic labs, companies, startups, and OSS ecosystems |
| [`venues/`](venues/README.md) | Venue/source census and systematic coverage map |
| [`data/`](data/README.md) | Machine-readable public metadata |
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

## 🚧 Current phase

The public repository is being bootstrapped from a continuously maintained internal literature census. Records enter the public view only after:

**identifier deduplication → primary-source validation → technical classification → repo/project verification → public export**

This keeps the public-facing map cleaner than the raw discovery stream.

---

<div align="center">

### 🌟 Built for researchers who want the **map**, not just the papers.

If this repository helps your research, consider starring it so you can find the latest updates easily.

</div>
