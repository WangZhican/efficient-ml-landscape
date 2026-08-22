#!/usr/bin/env python3
import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

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
    out = ["| Priority | Paper | Venue | Topic | Paper | Code |", "|---|---|---|---|---|---|"]
    for r in records:
        tier = esc(r.get("tracking_tier") or ("Canonical" if r.get("formal_class") == "CANONICAL_HIGH_VALUE" else "P0"))
        title = esc(r.get("title"))
        venue = esc(r.get("venue") or r.get("window") or "Fresh / preprint")
        topic = esc(r.get("topic"))
        paper = link_for(r)
        code = code_for(r)
        paper_cell = f"[Link]({paper})" if paper else "—"
        code_cell = f"[Repo]({code})" if code else "—"
        out.append(f"| **{tier}** | **{title}** | {venue} | {topic} | {paper_cell} | {code_cell} |")
    return "\n".join(out)


def parse_iso(s):
    if not s:
        return None
    try:
        return datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except ValueError:
        return None


def load_recent_arxiv_index(source):
    scan = source.parent / "ARXIV_30D_SCAN.json"
    if not scan.exists():
        return {}
    try:
        d = json.loads(scan.read_text())
    except (OSError, json.JSONDecodeError):
        return {}
    return {r.get("arxiv", ""): r for r in d.get("candidates", []) if r.get("arxiv")}


def is_latest_30d(raw_record, recent_arxiv, source_date):
    if raw_record.get("formal_class") == "STRONG_CURRENT":
        return True
    arxiv = (raw_record.get("arxiv") or "").strip()
    meta = recent_arxiv.get(arxiv, {})
    published = parse_iso(meta.get("published"))
    if published:
        cutoff = datetime.combine(source_date, datetime.min.time(), tzinfo=timezone(timedelta(hours=8))) - timedelta(days=30)
        return published.astimezone(cutoff.tzinfo) >= cutoff
    if source_date.year == 2026 and source_date.month == 8 and arxiv.startswith("2608."):
        return True
    return False


def public_watch_record(r):
    x = {
        "title": r.get("title", ""),
        "venue": r.get("venue", ""),
        "topic": r.get("topic", ""),
        "arxiv": r.get("arxiv", ""),
        "doi": r.get("doi", ""),
        "official_id": r.get("official_id", ""),
        "paper_url": link_for(r),
        "code_url": code_for(r),
        "formal_class": "WATCH",
        "decision": "WATCH",
        "tracking_tier": "P1 · Watch",
        "why": r.get("why", r.get("reason", "")),
        "published_at": r.get("published_utc", r.get("published_at", "")),
        "updated_at": r.get("updated_utc", r.get("updated_at", "")),
        "is_latest_30d": True,
    }
    x["directions"] = [name for _, name in classify(r)]
    return x


def public_low_priority_record(r):
    x = {
        "title": r.get("title", ""),
        "venue": r.get("venue", ""),
        "topic": r.get("topic", ""),
        "arxiv": r.get("arxiv", ""),
        "doi": r.get("doi", ""),
        "official_id": r.get("official_id", ""),
        "paper_url": link_for(r),
        "code_url": code_for(r),
        "formal_class": "RELEVANT_LOW_PRIORITY",
        "decision": "P2_RELEVANT_LOW_PRIORITY",
        "tracking_tier": "P2 · Relevant",
        "why": r.get("why", r.get("reason", "")),
        "published_at": r.get("published_utc", r.get("published_at", "")),
        "updated_at": r.get("updated_utc", r.get("updated_at", "")),
        "is_latest_30d": True,
    }
    x["directions"] = [name for _, name in classify(r)]
    return x


def write_csv(path, records):
    fields = ["tracking_tier", "title", "venue", "topic", "arxiv", "doi", "paper_url", "code_url", "formal_class", "decision", "published_at", "directions"]
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        for r in records:
            row = {k: r.get(k, "") for k in fields}
            row["directions"] = "; ".join(r.get("directions", []))
            w.writerow(row)


def refresh_landing_counts(path, stats):
    if not path.exists():
        return
    text = path.read_text()
    text = re.sub(r"(badge/Papers-)\d+(-7c3aed)", rf"\g<1>{stats['unique_papers']}\2", text)
    text = re.sub(r'alt="\d+ papers"', f'alt="{stats["unique_papers"]} papers"', text)
    text = re.sub(r"(badge/Primary%20Links-)\d+(-059669)", rf"\g<1>{stats['papers_with_primary_link']}\2", text)
    text = re.sub(r'alt="\d+ primary links"', f'alt="{stats["papers_with_primary_link"]} primary links"', text)
    labels = {
        "Quality-gated unique papers": stats["unique_papers"],
        "Latest 30-day tracked total": stats["latest_30d_tracked_total"],
        "Latest 30-day quality-gated papers": stats["latest_30d_quality_gated"],
        "Latest watchlist": stats["latest_30d_watchlist"],
        "Latest relevant low-priority": stats["latest_30d_relevant_low_priority"],
        "Classical / historical papers": stats["classical_papers"],
        "Papers with resolved primary-source links": stats["papers_with_primary_link"],
        "Latest strong papers": stats["latest_strong"],
        "质量门控后的唯一论文": stats["unique_papers"],
        "最近 30 天追踪总数": stats["latest_30d_tracked_total"],
        "最近 30 天质量门控论文": stats["latest_30d_quality_gated"],
        "最近 30 天 Watchlist": stats["latest_30d_watchlist"],
        "最近 30 天低优先级相关论文": stats["latest_30d_relevant_low_priority"],
        "经典 / 历史论文": stats["classical_papers"],
        "已有可信一手论文链接": stats["papers_with_primary_link"],
        "最新 Strong 论文": stats["latest_strong"],
    }
    for label, value in labels.items():
        pattern = rf"(\| \*\*{re.escape(label)}\*\* \| \*\*)\d+(\*\* \|)"
        text = re.sub(pattern, rf"\g<1>{value}\2", text)
    path.write_text(text)


def main():
    parser = argparse.ArgumentParser(description="Export a public-safe Efficient ML paper index from a validated JSON source.")
    parser.add_argument("--source", required=True, type=Path, help="Path to the validated source JSON.")
    args = parser.parse_args()
    d = json.loads(args.source.read_text())
    source_date = datetime.fromisoformat(d.get("date_beijing") or args.source.parent.parent.name).date()
    recent_arxiv = load_recent_arxiv_index(args.source)
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
        meta = recent_arxiv.get((r.get("arxiv") or "").strip(), {})
        x["published_at"] = meta.get("published", "")
        x["updated_at"] = meta.get("updated", "")
        x["is_latest_30d"] = is_latest_30d(r, recent_arxiv, source_date)
        x["tracking_tier"] = "P0 · Strong" if x["is_latest_30d"] else "Canonical"
        x["directions"] = [name for _, name in classify(r)]
        records.append(x)

    records.sort(key=lambda r: ((r.get("venue") or "zzz").lower(), r["title"].lower()))
    latest30 = sorted(
        [r for r in records if r.get("is_latest_30d")],
        key=lambda r: (r.get("published_at") or "", r["title"].lower()),
        reverse=True,
    )
    classical = [r for r in records if not r.get("is_latest_30d")]
    watch = []
    watch_seen = set()
    for r in d.get("watchlist", []):
        key = (r.get("arxiv") or "").strip() or (r.get("doi") or "").strip().lower() or norm_title(r.get("title"))
        if not key or key in watch_seen:
            continue
        watch_seen.add(key)
        x = public_watch_record(r)
        meta = recent_arxiv.get((r.get("arxiv") or "").strip(), {})
        x["published_at"] = x.get("published_at") or meta.get("published", "")
        x["updated_at"] = x.get("updated_at") or meta.get("updated", "")
        watch.append(x)

    low_priority = []
    low_seen = set()
    blocked = seen | watch_seen
    for r in d.get("recent_relevant_low_priority", []):
        key = (r.get("arxiv") or "").strip() or (r.get("doi") or "").strip().lower() or norm_title(r.get("title"))
        if not key or key in blocked or key in low_seen:
            continue
        low_seen.add(key)
        x = public_low_priority_record(r)
        meta = recent_arxiv.get((r.get("arxiv") or "").strip(), {})
        x["published_at"] = x.get("published_at") or meta.get("published", "")
        x["updated_at"] = x.get("updated_at") or meta.get("updated", "")
        low_priority.append(x)

    watch.sort(key=lambda r: (r.get("published_at") or "", r["title"].lower()), reverse=True)
    low_priority.sort(key=lambda r: (r.get("published_at") or "", r["title"].lower()), reverse=True)
    latest_tracking = latest30 + watch + low_priority

    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "papers").mkdir(exist_ok=True)

    (ROOT / "data" / "papers.json").write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n")
    write_csv(ROOT / "data" / "papers.csv", records)
    write_csv(ROOT / "data" / "latest_30d.csv", latest_tracking)
    write_csv(ROOT / "data" / "classical.csv", classical)
    (ROOT / "data" / "latest_30d.json").write_text(json.dumps({
        "window_end_beijing": str(source_date),
        "window_start_beijing": str(source_date - timedelta(days=30)),
        "tracking_philosophy": "Topical relevance decides visibility; quality decides P0/P1/P2 tier.",
        "tracked_total": len(latest_tracking),
        "p0_strong_or_canonical": latest30,
        "p1_watchlist": watch,
        "p2_relevant_low_priority": low_priority,
        "tracking_records": latest_tracking,
    }, ensure_ascii=False, indent=2) + "\n")
    (ROOT / "data" / "classical.json").write_text(json.dumps(classical, ensure_ascii=False, indent=2) + "\n")

    venue_groups = defaultdict(list)
    for r in classical:
        venue_groups[r.get("venue") or "Fresh / Preprint"].append(r)
    all_md = [
        "# 📚 Paper Library",
        "",
        f"> **{len(records)} quality-gated papers** form the canonical library. The rolling latest-30-day tracker is broader: **{len(latest_tracking)} visible papers = {len(latest30)} P0 + {len(watch)} P1 + {len(low_priority)} P2**. Recent topical relevance determines visibility; quality determines tier.",
        "",
        "[← Research Map](README.md) · [🆕 Latest 30 Days](LATEST_30D.md) · [🏛️ Classical](CLASSICAL.md) · [JSON](../data/papers.json) · [CSV](../data/papers.csv)",
        "",
        f"## 🆕 P0 · Strong / Canonical recent · {len(latest30)}",
        "",
        markdown_table(latest30),
        "",
        f"## 🧭 P1 · Watch · {len(watch)}",
        "",
        "> Clearly relevant and promising, but still awaiting stronger novelty, evidence, venue, or adoption validation.",
        "",
        markdown_table(watch),
        "",
        f"## 📎 P2 · Relevant, lower priority · {len(low_priority)}",
        "",
        "> Directly in scope and therefore retained for recall, even when current quality/impact evidence is not strong enough for Watch or Canonical promotion.",
        "",
        markdown_table(low_priority),
        "",
        f"## 🏛️ Classical / Historical · {len(classical)}",
        "",
    ]
    for venue, rs in sorted(venue_groups.items(), key=lambda kv: (-len(kv[1]), kv[0].lower())):
        all_md += [f"### {venue} · {len(rs)}", "", markdown_table(rs), ""]
    (ROOT / "papers" / "ALL_PAPERS.md").write_text("\n".join(all_md))

    latest_md = [
        "# 🆕 Latest 30 Days",
        "",
        f"> Rolling 30-day view ending **{source_date}**: **{len(latest_tracking)} tracked papers = {len(latest30)} P0 + {len(watch)} P1 + {len(low_priority)} P2**. Topical relevance determines visibility; quality determines priority. The classical census remains stricter.",
        "",
        "[← Paper Library](ALL_PAPERS.md) · [🏛️ Classical](CLASSICAL.md) · [JSON](../data/latest_30d.json) · [CSV](../data/latest_30d.csv)",
        "",
        "## P0 · Strong / Canonical recent papers",
        "",
        markdown_table(latest30),
        "",
        "## P1 · Watch",
        "",
        "> Directly relevant and promising, but still awaiting stronger novelty/evidence/adoption validation.",
        "",
        markdown_table(watch),
        "",
        "## P2 · Relevant, lower priority",
        "",
        "> Directly in scope and retained so recent recall is not sacrificed by a high quality threshold. These entries can be upgraded to P1/P0 after deeper review.",
        "",
        markdown_table(low_priority),
        "",
    ]
    (ROOT / "papers" / "LATEST_30D.md").write_text("\n".join(latest_md))
    (ROOT / "papers" / "LATEST.md").write_text("\n".join(latest_md))

    classical_md = [
        "# 🏛️ Classical / Historical Efficient ML",
        "",
        f"> **{len(classical)} quality-gated papers** outside the rolling 30-day freshness window. Use Latest 30 Days for active tracking.",
        "",
        "[← Paper Library](ALL_PAPERS.md) · [🆕 Latest 30 Days](LATEST_30D.md) · [JSON](../data/classical.json) · [CSV](../data/classical.csv)",
        "",
    ]
    for venue, rs in sorted(venue_groups.items(), key=lambda kv: (-len(kv[1]), kv[0].lower())):
        classical_md += [f"## {venue} · {len(rs)}", "", markdown_table(rs), ""]
    (ROOT / "papers" / "CLASSICAL.md").write_text("\n".join(classical_md))

    bydir = defaultdict(list)
    bydir_latest = defaultdict(list)
    bydir_classical = defaultdict(list)
    for r in records:
        rr = dict(r)
        source_stub = {"title": r["title"], "topic": r["topic"], "venue": r["venue"], "why": r.get("why", "")}
        for slug, name in classify(source_stub):
            bydir[slug].append(rr)
            if r.get("is_latest_30d"):
                bydir_latest[slug].append(rr)
            else:
                bydir_classical[slug].append(rr)
    for r in watch + low_priority:
        rr = dict(r)
        source_stub = {"title": r["title"], "topic": r["topic"], "venue": r.get("venue", ""), "why": r.get("why", "")}
        for slug, name in classify(source_stub):
            bydir_latest[slug].append(rr)

    nav_rows = []
    for idx, (slug, name, _) in enumerate(DIRECTIONS, 1):
        rs_latest = sorted(bydir_latest[slug], key=lambda r: (r.get("published_at") or "", r["title"].lower()), reverse=True)
        rs_classical = sorted(bydir_classical[slug], key=lambda r: ((r.get("venue") or "zzz").lower(), r["title"].lower()))
        canonical_total = len(bydir[slug])
        md = [
            f"# {idx:02d} · {name}",
            "",
            f"> **{canonical_total} canonical papers** mapped here, plus a broader **{len(rs_latest)}-paper Latest-30-Day tracker** using P0/P1/P2 tiers. Cross-direction duplication is intentional when a paper has multiple technical roles.",
            "",
            "[← Research Map](README.md) · [🆕 Latest 30 Days](LATEST_30D.md) · [🏛️ Classical](CLASSICAL.md) · [Paper Library](ALL_PAPERS.md)",
            "",
            f"## 🆕 Latest 30 Days · {len(rs_latest)} tracked",
            "",
            markdown_table(rs_latest),
            "",
            f"## 🏛️ Classical / Historical · {len(rs_classical)} canonical",
            "",
            markdown_table(rs_classical),
            "",
        ]
        (ROOT / "papers" / f"{slug}.md").write_text("\n".join(md))
        nav_rows.append((idx, slug, name, canonical_total, len(rs_latest)))

    readme = [
        "# 🧭 Research Map",
        "",
        f"> **{len(records)} quality-gated papers · 15 research directions · primary paper links · official code links when verified**",
        "",
        "<div align=\"center\">",
        "",
        f"[**🆕 Latest 30 Days · {len(latest_tracking)} tracked**](LATEST_30D.md) · [**🏛️ Classical · {len(classical)}**](CLASSICAL.md) · [**📚 Paper Library**](ALL_PAPERS.md) · [**🧩 JSON**](../data/papers.json)",
        "",
        "</div>",
        "",
        "## Explore by direction",
        "",
        "| # | Research direction | Canonical | Latest 30d tracked |",
        "|---:|---|---:|---:|",
    ]
    for idx, slug, name, canonical_n, latest_n in nav_rows:
        readme.append(f"| {idx:02d} | [**{name}**]({slug}.md) | **{canonical_n}** | **{latest_n}** |")
    readme += [
        "",
        "> Counts are multi-label and therefore do not sum to the unique-paper total. A canonical paper can intentionally appear in several directions.",
        "",
        "## Reading tiers",
        "",
        "- ⭐⭐⭐⭐⭐ **Must Read** — field-defining or indispensable canonical work",
        "- ⭐⭐⭐⭐ **Important** — major route node with strong systems/architecture impact",
        "- ⭐⭐⭐ **Valuable** — meaningful contribution or important branch",
        "- 🧭 **P1 Watch** — directly relevant and promising, still awaiting stronger evidence/adoption",
        "- 📎 **P2 Relevant** — directly in scope but currently lower-priority; retained for recent recall and future upgrade review",
        "",
        "The next enrichment pass adds verified official repositories, open-source status, GitHub-star snapshots, and explicit technical lineage annotations paper by paper.",
        "",
    ]
    (ROOT / "papers" / "README.md").write_text("\n".join(readme))

    stats = {
        "unique_papers": len(records),
        "latest_30d_tracked_total": len(latest_tracking),
        "latest_30d_quality_gated": len(latest30),
        "latest_30d_watchlist": len(watch),
        "latest_30d_relevant_low_priority": len(low_priority),
        "classical_papers": len(classical),
        "latest_strong": sum(r.get("formal_class") == "STRONG_CURRENT" for r in latest30),
        "papers_with_primary_link": sum(bool(r["paper_url"]) for r in records),
        "papers_with_verified_code_link": sum(bool(r["code_url"]) for r in records),
        "venues": len(set(r.get("venue") or "Fresh / Preprint" for r in records)),
        "direction_counts": {name: len(bydir[slug]) for slug, name, _ in DIRECTIONS},
        "source_date_beijing": d.get("date_beijing", ""),
        "updated_at_beijing": d.get("updated_at_beijing", ""),
    }
    (ROOT / "data" / "stats.json").write_text(json.dumps(stats, ensure_ascii=False, indent=2) + "\n")
    refresh_landing_counts(ROOT / "README.md", stats)
    refresh_landing_counts(ROOT / "README.zh-CN.md", stats)
    print(json.dumps(stats, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
