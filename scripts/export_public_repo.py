#!/usr/bin/env python3
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / "efficient ml paper reading" / "2026-08-20" / "_manager" / "LATEST_PAPER_TODO.json"

DIRECTIONS = [
    ("01-llm-serving", "LLM Serving", ["serving", "serve", "scheduler", "scheduling", "slo", "batching", "prefill", "decode", "inference system", "goodput", "throughput"]),
    ("02-speculative-decoding", "Speculative Decoding", ["speculative", "draft", "verify", "specdec", "self-spec", "parallel decoding"]),
    ("03-kv-cache-long-context", "KV Cache / Long Context", ["kv cache", "kv-cache", "kvcache", "long-context", "long context", "prefix cache", "cache reuse", "offload", "migration"]),
    ("04-quantization", "Quantization", ["quant", "low-bit", "low bit", "w4a", "int4", "int8", "fp4", "mxfp", "microscaling", "ptq", "qat"]),
    ("05-sparsity-pruning", "Sparsity / Pruning", ["sparse", "sparsity", "prun", "token selection", "token dropping", "token pruning"]),
    ("06-efficient-attention", "Efficient Attention", ["attention", "flashattention", "linear attention", "local attention", "sparse attention"]),
    ("07-moe-systems", "MoE Systems / Accelerators", ["moe", "mixture of experts", "expert parallel", "expert routing", "expert replication"]),
    ("08-gpu-kernel-compiler", "GPU Kernel / DSL / Compiler", ["kernel", "compiler", "triton", "cuda", "gemm", "gpu", "dsl", "fusion", "tensor core"]),
    ("09-distributed-training-inference", "Distributed Training / Inference", ["distributed", "parallelism", "pipeline parallel", "tensor parallel", "collective", "communication", "multi-gpu", "cluster", "training system"]),
    ("10-multimodal-mllm-serving", "Multimodal / MLLM Serving", ["multimodal", "mllm", "vlm", "vision-language", "omni", "visual token"]),
    ("11-video-image-generation", "Video / Image Generation", ["video generation", "image generation", "autoregressive image", "video model", "videolm"]),
    ("12-diffusion-flow", "Diffusion / Flow Acceleration", ["diffusion", "dit", "flow matching", "rectified flow", "denoising"]),
    ("13-efficient-reasoning-agents", "Efficient Reasoning / Agents", ["reasoning", "agent", "agentic", "rollout", "test-time", "test time", "reinforcement learning"]),
    ("14-physical-ai-vla-wam", "VLA / WAM / Physical AI", ["vla", "vision-language-action", "world action", "wam", "robot", "embodied", "action generation", "autonomous driving", "humanoid"]),
    ("15-edge-cloud-heterogeneous", "Edge / Cloud / Heterogeneous AI", ["edge", "device", "heterogeneous", "cpu-gpu", "npu", "mobile", "cloud-edge", "cxl", "pim", "on-device", "memory hierarchy"]),
]


def norm_title(s):
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def esc(s):
    return str(s or "").replace("|", "\\|").replace("\n", " ").strip()


def link_for(r):
    arxiv = (r.get("arxiv") or "").strip()
    if arxiv:
        return f"https://arxiv.org/abs/{arxiv}"
    for key in ("official_url", "official_page"):
        v = (r.get(key) or "").strip()
        if v.startswith("http"):
            return v
    doi = (r.get("doi") or "").strip()
    if doi:
        return f"https://doi.org/{doi}"
    v = (r.get("pdf_source") or "").strip()
    if v.startswith("http"):
        return v
    return ""


def code_for(r):
    for key in ("repo", "github", "code_url", "project_repo", "official_repo"):
        v = (r.get(key) or "").strip()
        if v.startswith("http"):
            return v
    return ""


def classify(r):
    blob = " ".join([r.get("title", ""), r.get("topic", ""), r.get("venue", ""), r.get("why", "")]).lower()
    hits = []
    for slug, name, kws in DIRECTIONS:
        if any(k in blob for k in kws):
            hits.append((slug, name))
    if not hits:
        # Keep every paper visible even when taxonomy metadata is still coarse.
        hits = [("15-edge-cloud-heterogeneous", "Edge / Cloud / Heterogeneous AI")]
    return hits


def markdown_table(records):
    out = ["| Paper | Venue | Topic | Paper | Code |", "|---|---|---|---|---|"]
    for r in records:
        title = esc(r.get("title"))
        venue = esc(r.get("venue") or r.get("window") or "Fresh / preprint")
        topic = esc(r.get("topic"))
        paper = link_for(r)
        code = code_for(r)
        paper_cell = f"[Link]({paper})" if paper else "—"
        code_cell = f"[Repo]({code})" if code else "—"
        out.append(f"| **{title}** | {venue} | {topic} | {paper_cell} | {code_cell} |")
    return "\n".join(out)


def main():
    d = json.loads(SOURCE.read_text())
    raw = d.get("formal_high_value_records", [])
    seen = set()
    records = []
    for r in raw:
        key = (r.get("arxiv") or "").strip() or (r.get("doi") or "").strip().lower() or norm_title(r.get("title"))
        if not key or key in seen:
            continue
        seen.add(key)
        x = {
            "title": r.get("title", ""),
            "venue": r.get("venue", ""),
            "topic": r.get("topic", ""),
            "arxiv": r.get("arxiv", ""),
            "doi": r.get("doi", ""),
            "official_id": r.get("official_id", ""),
            "paper_url": link_for(r),
            "code_url": code_for(r),
            "formal_class": r.get("formal_class", ""),
            "decision": r.get("decision", r.get("priority", "")),
            "why": r.get("why", r.get("reason", "")),
        }
        x["directions"] = [name for _, name in classify(r)]
        records.append(x)

    records.sort(key=lambda r: ((r.get("venue") or "zzz").lower(), r["title"].lower()))
    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "papers").mkdir(exist_ok=True)

    (ROOT / "data" / "papers.json").write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n")
    with (ROOT / "data" / "papers.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["title", "venue", "topic", "arxiv", "doi", "paper_url", "code_url", "formal_class", "decision", "directions"])
        w.writeheader()
        for r in records:
            row = {k: r.get(k, "") for k in w.fieldnames}
            row["directions"] = "; ".join(r["directions"])
            w.writerow(row)

    venue_groups = defaultdict(list)
    for r in records:
        venue_groups[r.get("venue") or "Fresh / Preprint"].append(r)
    all_md = [
        "# 📚 Complete Paper List",
        "",
        f"> **{len(records)} quality-gated papers** exported from the validated canonical literature census. PDF binaries are not stored here; links point to primary paper sources whenever resolved.",
        "",
        "[← Research Map](README.md) · [Machine-readable JSON](../data/papers.json) · [CSV](../data/papers.csv)",
        "",
    ]
    for venue, rs in sorted(venue_groups.items(), key=lambda kv: (-len(kv[1]), kv[0].lower())):
        all_md += [f"## {venue} · {len(rs)}", "", markdown_table(rs), ""]
    (ROOT / "papers" / "ALL_PAPERS.md").write_text("\n".join(all_md))

    latest = [r for r in records if r.get("formal_class") == "STRONG_CURRENT"]
    latest_md = [
        "# 🆕 Latest Strong Papers",
        "",
        f"> **{len(latest)} currently retained strong papers** from the latest discovery stream.",
        "",
        markdown_table(latest),
        "",
    ]
    (ROOT / "papers" / "LATEST.md").write_text("\n".join(latest_md))

    bydir = defaultdict(list)
    for r in records:
        rr = dict(r)
        # classify again on public fields to get slugs
        source_stub = {"title": r["title"], "topic": r["topic"], "venue": r["venue"], "why": r.get("why", "")}
        for slug, name in classify(source_stub):
            bydir[slug].append(rr)

    nav_rows = []
    for idx, (slug, name, _) in enumerate(DIRECTIONS, 1):
        rs = sorted(bydir[slug], key=lambda r: ((r.get("venue") or "zzz").lower(), r["title"].lower()))
        md = [
            f"# {idx:02d} · {name}",
            "",
            f"> **{len(rs)} papers** currently mapped to this direction. Cross-direction duplication is intentional when a paper has multiple technical roles.",
            "",
            "[← Research Map](README.md) · [Complete Paper List](ALL_PAPERS.md)",
            "",
            markdown_table(rs),
            "",
        ]
        (ROOT / "papers" / f"{slug}.md").write_text("\n".join(md))
        nav_rows.append((idx, slug, name, len(rs)))

    readme = [
        "# 🧭 Research Map",
        "",
        f"> **{len(records)} quality-gated papers · 15 research directions · primary paper links · official code links when verified**",
        "",
        "<div align=\"center\">",
        "",
        "[**📚 Browse all papers**](ALL_PAPERS.md) · [**🆕 Latest strong papers**](LATEST.md) · [**🧩 JSON**](../data/papers.json) · [**📊 CSV**](../data/papers.csv)",
        "",
        "</div>",
        "",
        "## Explore by direction",
        "",
        "| # | Research direction | Papers |",
        "|---:|---|---:|",
    ]
    for idx, slug, name, n in nav_rows:
        readme.append(f"| {idx:02d} | [**{name}**]({slug}.md) | **{n}** |")
    readme += [
        "",
        "> Counts are multi-label and therefore do not sum to the unique-paper total. A canonical paper can intentionally appear in several directions.",
        "",
        "## Reading tiers",
        "",
        "- ⭐⭐⭐⭐⭐ **Must Read** — field-defining or indispensable canonical work",
        "- ⭐⭐⭐⭐ **Important** — major route node with strong systems/architecture impact",
        "- ⭐⭐⭐ **Valuable** — meaningful contribution or important branch",
        "- 🧭 **Watch** — promising work still awaiting stronger evidence/adoption",
        "",
        "The next enrichment pass adds verified official repositories, open-source status, GitHub-star snapshots, and explicit technical lineage annotations paper by paper.",
        "",
    ]
    (ROOT / "papers" / "README.md").write_text("\n".join(readme))

    stats = {
        "unique_papers": len(records),
        "latest_strong": len(latest),
        "papers_with_primary_link": sum(bool(r["paper_url"]) for r in records),
        "papers_with_verified_code_link": sum(bool(r["code_url"]) for r in records),
        "venues": len(set(r.get("venue") or "Fresh / Preprint" for r in records)),
        "direction_counts": {name: len(bydir[slug]) for slug, name, _ in DIRECTIONS},
        "source_date_beijing": d.get("date_beijing", ""),
        "updated_at_beijing": d.get("updated_at_beijing", ""),
    }
    (ROOT / "data" / "stats.json").write_text(json.dumps(stats, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(stats, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
