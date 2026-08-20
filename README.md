# Efficient ML Landscape

A curated, continuously maintained research map for Efficient ML / AI Infrastructure, with a focus on influential work from 2024 to the present and a small number of earlier canonical papers when necessary.

> Public repository policy: **no paper PDFs are stored here**. Each paper record links to the primary paper source and, when available, the official code/project repository.

## Scope

The repository tracks 15 major research directions:

1. LLM serving
2. Speculative decoding
3. KV cache / long-context systems
4. Quantization
5. Sparsity / pruning
6. Efficient attention
7. MoE systems / accelerators
8. GPU kernels / DSLs / compilers
9. Distributed training / inference
10. Multimodal / MLLM serving
11. Video / image generation acceleration
12. Diffusion / flow acceleration
13. Efficient reasoning / agent systems
14. VLA / WAM / Physical AI serving
15. Edge / cloud / heterogeneous AI systems

## Repository Layout

- `papers/` — direction-by-direction research maps and curated paper lists
- `groups/` — major research-group and company ecosystems
- `venues/` — venue/source census and systematic coverage map
- `data/` — normalized machine-readable paper/group/venue metadata
- `docs/` — methodology, inclusion policy, audit rules, and update notes
- `scripts/` — exporters/validators used to keep Markdown and structured data synchronized

## Paper Record

Each retained paper should expose, whenever available:

- title
- authors
- year / venue
- direction and sub-direction
- technical role in the research roadmap
- concise contribution summary
- primary paper link
- official repository / project link
- open-source status
- GitHub stars when meaningful and verifiable
- influence / recommendation tier
- relationship to predecessor and follow-up work

A paper may intentionally appear in multiple directions when it plays a different technical role in each roadmap.

## Selection Principles

There is **no fixed paper-count quota**. Papers are retained based on technical contribution, influence, relevance, route value, and first-party evidence. When contributions are comparable, open-source work, official implementations, broader community adoption, and higher GitHub-star counts receive additional weight.

## Coverage and Audit

The database is maintained with explicit freshness, venue, major-group, and citation-neighborhood audits. `SEARCHED`, `COVERED`, and `SATURATED` are treated as different states. Saturation is only claimed after systematic zero-new confirmation rounds; a large paper count alone is not considered sufficient evidence of coverage.

## Physical AI

Physical AI is a protected direction rather than a small subcategory. It explicitly covers VLA/WAM serving, cache/quantization/sparsity, action-head/flow/diffusion inference, streaming agents, cloud-edge execution, and runtime/infrastructure co-design.

## Status

The repository is being bootstrapped from an actively maintained internal literature census. Public-facing records will be synchronized only after identifier deduplication and source validation.

## Citation / Contribution

Contribution and citation instructions will be added after the first public release is stabilized.
