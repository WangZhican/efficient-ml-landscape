# 07 · MoE Systems / Accelerators

> **55 canonical papers** mapped here, plus a broader **21-paper Latest-30-Day tracker** using P0/P1/P2 tiers. Cross-direction duplication is intentional when a paper has multiple technical roles.

[← Research Map](README.md) · [🆕 Latest 30 Days](LATEST_30D.md) · [🏛️ Classical](CLASSICAL.md) · [Paper Library](ALL_PAPERS.md)

## 🆕 Latest 30 Days · 21 tracked

| Priority | Paper | Venue | Topic | Paper | Code |
|---|---|---|---|---|---|
| **P1 · Watch** | **Cacheable by Design? Training Mixture-of-Experts Routers for Locality Against the Edge Memory-Bandwidth Wall: A Pre-Registered Negative Result with a Systems Measurement Study** | Fresh / preprint | edge MoE serving / expert caching / memory bandwidth | [Link](https://arxiv.org/abs/2608.18261) | — |
| **P1 · Watch** | **MoE-ViE: Mixture of Experts Vision Encoder for Efficient Image and Video Understanding** | Fresh / preprint | multimodal vision encoder / MoE / Triton kernel | [Link](https://arxiv.org/abs/2608.17402) | [Repo](https://github.com/facebookresearch/moe_vie) |
| **P1 · Watch** | **KernelArc: A Multi-Agent Framework for GPU Kernel Optimization** | Fresh / preprint | GPU kernel / agentic optimization / H100-B200 | [Link](https://arxiv.org/abs/2608.17071) | — |
| **P0 · Strong** | **FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution** | Fresh / preprint | edge MoE serving | [Link](https://arxiv.org/abs/2608.16157) | — |
| **P2 · Relevant** | **Nexus: Structured Synergy for Efficient Text-to-Image Generation using Rectified Flow Model** | Fresh / preprint | image generation / sparse architecture / low-bit / flow matching | [Link](https://arxiv.org/abs/2608.16104) | — |
| **P0 · Strong** | **Every Expert Counts: ExactMoE for Memory-Efficient W4A16 Inference** | Fresh / preprint | MoE memory-efficient W4A16 inference / GPU slot cache | [Link](https://arxiv.org/abs/2608.15383) | — |
| **P2 · Relevant** | **MAPLE: MoE Adaptive Plug-and-play Layer-wise Expert allocation** | Fresh / preprint | llm_serving / sparse / moe / edge | [Link](https://arxiv.org/abs/2608.15299) | — |
| **P1 · Watch** | **S2-MoE: Enabling Efficient Self-Speculative Decoding for Mixture-of-Experts on Edge Devices** | Fresh / preprint |  | [Link](https://arxiv.org/abs/2608.15018) | — |
| **P0 · Strong** | **DeaMoE: Efficient MoE Structure for Fast Small-Batch Decoding** | Fresh / preprint | MoE architecture / small-batch decoding | [Link](https://arxiv.org/abs/2608.14385) | — |
| **P0 · Strong** | **Beyond Capacity: Scalable MoE LLM Inference via High-Bandwidth Flash with Direct GPU and HBM Paths** | Fresh / preprint | MoE serving / high-bandwidth flash architecture | [Link](https://arxiv.org/abs/2608.14333) | — |
| **P2 · Relevant** | **MoE Expert Execution in Disaggregated LLM Serving with a High-Bandwidth ReRAM Near-Memory Architecture** | Fresh / preprint | llm_serving / moe | [Link](https://arxiv.org/abs/2608.13962) | — |
| **P0 · Strong** | **TEMPO: Makespan-Aware Expert-Parallel Load Balancing Across Memory- and Compute-Bound Regimes** | Fresh / preprint | MoE expert-parallel load balancing / serving | [Link](https://arxiv.org/abs/2608.13057) | — |
| **P2 · Relevant** | **APEX: Adaptive Expert Prefetching for Memory-Efficient Edge MoE Inference** | Fresh / preprint | llm_serving / moe / gen | [Link](https://arxiv.org/abs/2608.11688) | — |
| **P2 · Relevant** | **Tied Trit-Planes: Constraining PTQTP to a Uniform Nine-Level Quantizer, with a Persistent Folded Format for Disk-Streamed Mixture-of-Experts Serving** | Fresh / preprint | llm_serving / quant / moe / edge | [Link](https://arxiv.org/abs/2608.08910) | — |
| **P1 · Watch** | **RotaryQuant: Fitting 120B MoE Models on Consumer Hardware via Fused Compressed-Space Attention** | Fresh / preprint | kv / quant / moe | [Link](https://arxiv.org/abs/2608.08081) | — |
| **P2 · Relevant** | **EdgeXpert: An Edge Device for Memory-Efficient LLM Inference with Mixture-of-Experts and Speculative Decoding** | Fresh / preprint | LLM serving; speculative decoding; MoE systems; generation acceleration; edge / heterogeneous AI | [Link](https://arxiv.org/abs/2608.05303) | — |
| **P1 · Watch** | **AcceptMoE: Commitment-Weighted Self-Sizing Verifier Expert Sets for Efficient MoE Speculative Decoding** | Fresh / preprint | llm_serving / spec / moe / gen | [Link](https://arxiv.org/abs/2608.02989) | — |
| **P2 · Relevant** | **HetRoute Heterogeneous and Cost-aware Collaborative Routing Framework for Distributed Edge MoE Inference** | Fresh / preprint | llm_serving / quant / moe / dist / edge | [Link](https://arxiv.org/abs/2608.00577) | — |
| **P2 · Relevant** | **Characterizing LLM Kernel Access and Memory Interaction in Multi-Partition NUMA GPUs** | Fresh / preprint | llm_serving / moe | [Link](https://arxiv.org/abs/2607.28824) | — |
| **P2 · Relevant** | **DraftExpert: Expansion-Aware Self-Speculative Decoding for End-Device MoE Inference** | Fresh / preprint | llm_serving / spec / moe / edge | [Link](https://arxiv.org/abs/2607.24434) | — |
| **P2 · Relevant** | **Decoding the Skew: Distribution-Aware MoE Inference with Adaptive Kernel Dispatch** | Fresh / preprint | llm_serving / moe | [Link](https://arxiv.org/abs/2607.23099) | — |

## 🏛️ Classical / Historical · 50 canonical

| Priority | Paper | Venue | Topic | Paper | Code |
|---|---|---|---|---|---|
| **Canonical** | **SMIDT: High-Performance Inference Framework for MoE Models with Dynamic Top-K Routing** | AAAI 2026 | MoE systems/accelerators / LLM serving | [Link](https://doi.org/10.1609/aaai.v40i27.39403) | — |
| **Canonical** | **Jakiro: Boosting Speculative Decoding via Decoupled MoE** | ACL 2026 | speculative decoding / MoE draft model | [Link](https://doi.org/10.18653/v1/2026.acl-long.487) | — |
| **Canonical** | **DFVG** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | [Link](https://doi.org/10.1145/3779212.3790153) | — |
| **Canonical** | **EARTH: An Efficient MoE Accelerator with Entropy-Aware Speculative Prefetch and Result Reuse** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | [Link](https://doi.org/10.1145/3779212.3790155) | — |
| **Canonical** | **LAER-MoE: Load-Adaptive Expert Re-layout for Efficient Mixture-of-Experts Training** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | [Link](https://arxiv.org/abs/2602.11686) | — |
| **Canonical** | **MoDM: Efficient Serving for Image Generation via Mixture-of-Diffusion Models** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | [Link](https://arxiv.org/abs/2503.11972) | — |
| **Canonical** | **MoE-APEX: An Efficient MoE Inference System with Adaptive Precision Expert Offloading** | ASPLOS 2026 | edge MoE inference / expert offloading / mixed precision | [Link](https://doi.org/10.1145/3779212.3790187) | — |
| **Canonical** | **oFFN: Outlier and Neuron-aware Structured FFN for Fast yet Accurate LLM Inference** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | [Link](https://doi.org/10.1145/3779212.3790194) | — |
| **Canonical** | **PAT: Accelerating LLM Decoding via Prefix-Aware Attention with Resource Efficient Multi-Tile Kernel** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | [Link](https://arxiv.org/abs/2511.22333) | — |
| **Canonical** | **QoServe** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | [Link](https://doi.org/10.1145/3779212.3790206) | — |
| **Canonical** | **Shift Parallelism** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | — | — |
| **Canonical** | **Shift Parallelism: Low-Latency, High-Throughput LLM Inference for Dynamic Workloads** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | [Link](https://arxiv.org/abs/2509.16495) | — |
| **Canonical** | **SpeContext: Enabling Efficient Long-context Reasoning with Speculative Context Sparsity in LLMs** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | [Link](https://arxiv.org/abs/2512.00722) | — |
| **Canonical** | **XY-Serve** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | — | — |
| **Canonical** | **XY-Serve: End-to-End Versatile Production Serving for Dynamic LLM Workloads** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | [Link](https://arxiv.org/abs/2412.18106) | — |
| **Canonical** | **ZipServ** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | — | — |
| **Canonical** | **ZipServ: Fast and Memory-Efficient LLM Inference with Hardware-Aware Lossless Compression** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | [Link](https://arxiv.org/abs/2603.17435) | — |
| **Canonical** | **HybriMoE: Hybrid CPU-GPU Scheduling and Cache Management for Efficient MoE Inference** | DAC 2025 | MoE inference / hybrid CPU-GPU scheduling / expert prefetch and cache management | [Link](https://arxiv.org/abs/2504.05897) | [Repo](https://github.com/PKU-SEC-Lab/HybriMoE) |
| **Canonical** | **MegaScale-MoE: Large-Scale Communication-Efficient Training of Mixture-of-Experts Models in Production** | EuroSys 2026 | MoE training systems / communication optimization | [Link](https://arxiv.org/abs/2505.11432) | — |
| **Canonical** | **MoEntwine: Unleashing the Potential of Wafer-scale Chips for Large-scale Expert Parallel Inference** | HPCA 2026 | MoE inference / expert parallelism / wafer-scale systems | [Link](https://arxiv.org/abs/2510.25258) | — |
| **Canonical** | **PuzzleMoE: Efficient Compression of Large Mixture-of-Experts Models via Sparse Expert Merging and Bit-packed inference** | ICML 2026 | MoE compression / sparse expert merging / bit-packed inference | [Link](https://arxiv.org/abs/2511.04805) | — |
| **Canonical** | **Accelerating MoE with Dynamic In-Switch Computing on Multi-GPUs** | ISCA 2026 | MoE / multi-GPU / in-switch computing | — | — |
| **Canonical** | **DIAMoND: Dynamic Inference for Adaptive Edge MoE with Heterogeneous In-NAND and Near-DRAM Compute Architecture** | ISCA 2026 | edge MoE / heterogeneous memory / adaptive inference | — | — |
| **Canonical** | **MoE-Hub: Taming Software Complexity for Seamless MoE Overlap with Hardware-Accelerated Communication on Multi-GPU Systems** | ISCA 2026 | MoE systems / multi-GPU communication overlap | — | — |
| **Canonical** | **Patterns Behind Chaos: Forecasting Data Movement for Efficient Large-Scale MoE LLM Inference** | ISCA 2026 | MoE systems / data movement forecasting / large-scale inference | [Link](https://arxiv.org/abs/2510.05497) | — |
| **Canonical** | **SMoE: An Algorithm-System Co-Design for Pushing MoE to the Edge via Expert Substitution** | ISCA 2026 | edge MoE / algorithm-system co-design | — | — |
| **Canonical** | **STEP: Adaptive Spatio-Temporal Expert Prefetching for Low-Latency and Memory-Efficient MoE Inference** | ISCA 2026 | MoE / expert prefetching / memory efficiency | — | — |
| **Canonical** | **HLX** | MICRO 2025 | MoE + diffusion + tensor compression + hybrid LM + reasoning + edge training acceleration | — | — |
| **Canonical** | **LLM.265** | MICRO 2025 | MoE + diffusion + tensor compression + hybrid LM + reasoning + edge training acceleration | — | — |
| **Canonical** | **ORCHES** | MICRO 2025 | MoE + diffusion + tensor compression + hybrid LM + reasoning + edge training acceleration | — | — |
| **Canonical** | **REACT3D** | MICRO 2025 | MoE + diffusion + tensor compression + hybrid LM + reasoning + edge training acceleration | — | — |
| **Canonical** | **S-DMA** | MICRO 2025 | MoE + diffusion + tensor compression + hybrid LM + reasoning + edge training acceleration | [Link](https://doi.org/10.1145/3725843.3756046) | — |
| **Canonical** | **Stratum** | MICRO 2025 | MoE + diffusion + tensor compression + hybrid LM + reasoning + edge training acceleration | [Link](https://doi.org/10.1145/3725843.3756043) | — |
| **Canonical** | **Stratum: System-Hardware Co-design with Tiered Monolithic 3D-DRAM for Efficient MoE Serving** | MICRO 2025 | MoE serving / memory-system co-design | — | — |
| **Canonical** | **CRAFT: Fine-Grained Cost-Aware Expert Replication For Efficient Mixture-of-Experts Serving** | MLSys 2026 | MoE serving / expert replication | — | — |
| **Canonical** | **From Tokens to Layers: Redefining Stall-Free Scheduling for MoE Serving with Layered Prefill** | MLSys 2026 | MoE serving / layered prefill / stall-free scheduling / energy efficiency | — | — |
| **Canonical** | **ProfInfer: An eBPF-based Fine-Grained LLM Inference Profiler** | MLSys 2026 | LLM inference profiling / edge runtime observability | — | — |
| **Canonical** | **D2MoE: Dual Routing and Dynamic Scheduling for Efficient On-Device MoE-based LLM Serving** | MobiCom 2025 | on-device MoE serving / dynamic scheduling | [Link](https://doi.org/10.1145/3680207.3723493) | — |
| **Canonical** | **MoESD: Unveil Speculative Decoding's Potential for Accelerating Sparse MoE** | NeurIPS 2025 | MoE inference / speculative decoding | [Link](https://doi.org/10.52202/085713-4176) | — |
| **Canonical** | **SwiftEP: Accelerating MoE Inference with Buffer Fusion and TMA Offloading** | NSDI 2026 | MoE communication / inference runtime | — | — |
| **Canonical** | **SYMI: Efficient Mixture-of-Experts Training via Model and Optimizer State Decoupling** | NSDI 2026 | MoE training systems | — | — |
| **Canonical** | **ByteScale: Communication-Efficient Scaling of LLM Training with a 2048K Context Length on 16384 GPUs** | SIGCOMM 2025 | KV encoding + MoE training fabric + long-context training + AI networking/inference | [Link](https://arxiv.org/abs/2502.21231) | — |
| **Canonical** | **MegaScale-Infer: Efficient Mixture-of-Experts Model Serving with Disaggregated Expert Parallelism** | SIGCOMM 2025 | MoE serving / disaggregated expert parallelism / networking | [Link](https://arxiv.org/abs/2504.02263) | — |
| **Canonical** | **MixNet: A Runtime Reconfigurable Optical-Electrical Fabric for Distributed Mixture-of-Experts Training** | SIGCOMM 2025 | KV encoding + MoE training fabric + long-context training + AI networking/inference | [Link](https://arxiv.org/abs/2501.03905) | — |
| **Canonical** | **Pegasus: A Universal Framework for Scalable Deep Learning Inference on the Dataplane** | SIGCOMM 2025 | KV encoding + MoE training fabric + long-context training + AI networking/inference | [Link](https://arxiv.org/abs/2506.05779) | — |
| **Canonical** | **SCX** | SIGCOMM 2025 | KV encoding + MoE training fabric + long-context training + AI networking/inference | — | — |
| **Canonical** | **SGLB: Scalable and Robust Global Load Balancing in Commodity AI Clusters** | SIGCOMM 2025 | KV encoding + MoE training fabric + long-context training + AI networking/inference | [Link](https://doi.org/10.1145/3718958.3750527) | — |
| **Canonical** | **KTransformers: Unleashing the Full Potential of CPU/GPU Hybrid Inference for MoE Models** | SOSP 2025 | LLM serving / KV / GPU systems | [Link](https://doi.org/10.1145/3731569.3764843) | — |
| **Canonical** | **Fate: Fast Edge Inference of Mixture-of-Experts Models via Cross-Layer Gate** | The Web Conference 2026 | edge MoE inference / expert prefetch | [Link](https://arxiv.org/abs/2502.12224) | — |
| **Canonical** | **Self-Speculative Decoding for On-device MoE Acceleration** | The Web Conference 2026 | on-device MoE / speculative decoding | [Link](https://doi.org/10.1145/3774904.3792218) | — |
