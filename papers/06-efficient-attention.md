# 06 · Efficient Attention

> **53 papers** currently mapped to this direction. Cross-direction duplication is intentional when a paper has multiple technical roles.

[← Research Map](README.md) · [Complete Paper List](ALL_PAPERS.md)

| Paper | Venue | Topic | Paper | Code |
|---|---|---|---|---|
| **MHA2MLA-VLM: Enabling DeepSeek’s Economical Multi-Head Latent Attention Across Vision-Language Models** | AAAI 2026 | VLM inference / MLA / KV cache compression | [Link](https://doi.org/10.1609/aaai.v40i36.40319) | — |
| **Q Cache: Visual Attention Is Valuable in Less than Half of Decode Layers for Multimodal Large Language Model** | AAAI 2026 | MLLM inference / cross-layer attention reuse / KV cache | [Link](https://doi.org/10.1609/aaai.v40i16.38414) | — |
| **Self-Indexing KVCache: Predicting Sparse Attention from Compressed Keys** | AAAI 2026 | KV cache compression / sparse attention / CUDA kernel | [Link](https://doi.org/10.1609/aaai.v40i33.39988) | — |
| **Sparse Attention Across Multiple-Context KV Cache** | AAAI 2026 | RAG / sparse attention / multi-context KV cache | [Link](https://doi.org/10.1609/aaai.v40i36.40266) | — |
| **Evolving Sparsity: Leveraging Token Importance Dynamics for Efficient LLM Decoding with Sparse Attention** | ACL 2026 | sparse attention / long-context decoding | [Link](https://doi.org/10.18653/v1/2026.acl-long.530) | — |
| **VecInfer: Efficient LLM Inference with Low-Bit KV Cache via Outlier-Suppressed Vector Quantization** | ACL 2026 | KV-cache quantization / low-bit LLM inference / CUDA kernel | [Link](https://doi.org/10.18653/v1/2026.acl-long.1454) | — |
| **BAT: Efficient Generative Recommender Serving with Bipartite Attention** | ASPLOS 2026 | generative recommender serving / KV prefix cache | [Link](https://doi.org/10.1145/3779212.3790131) | — |
| **I/O Analysis is All You Need: An I/O Analysis for Long-Sequence Attention** | ASPLOS 2026 | attention accelerator / I/O analysis | [Link](https://doi.org/10.1145/3779212.3790174) | — |
| **PAT: Accelerating LLM Decoding via Prefix-Aware Attention with Resource Efficient Multi-Tile Kernel** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | [Link](https://arxiv.org/abs/2511.22333) | — |
| **STARC: Selective Token Access with Remapping and Clustering for Efficient LLM Decoding on PIM Systems** | ASPLOS 2026 | sparse attention / PIM / KV cache | [Link](https://doi.org/10.1145/3779212.3790226) | — |
| **TPLA: Tensor Parallel Latent Attention for Efficient Disaggregated Prefill & Decode Inference** | ASPLOS 2026 | MLA / tensor parallelism / KV cache / disaggregated inference | [Link](https://arxiv.org/abs/2508.15881) | — |
| **X-EcoMLA: Upcycling Pre-Trained Attention into MLA for Efficient and Extreme KV Compression** | COLM 2025 | KV cache compression / efficient attention architecture | [Link](https://arxiv.org/abs/2503.11132) | — |
| **HiDiffusion: Unlocking Higher-Resolution Creativity and Efficiency in Pretrained Diffusion Models** | ECCV 2024 | diffusion inference acceleration | — | — |
| **Inf-DiT: Upsampling any-resolution image with memory-efficient diffusion transformer.** | ECCV 2024 | diffusion memory efficiency | — | — |
| **Cost-Optimal Grouped-Query Attention for Long-Context Modeling** | EMNLP 2025 | efficient attention / GQA / long-context modeling | [Link](https://doi.org/10.18653/v1/2025.emnlp-main.272) | — |
| **Speculative Streaming: Efficient and Scalable Speculative Decoding with Multi-Stream Attention** | EMNLP 2025 | speculative decoding / multi-stream attention | [Link](https://doi.org/10.18653/v1/2025.emnlp-main.986) | — |
| **TokenSelect: Efficient Long-Context Inference and Length Extrapolation for LLMs via Dynamic Token-Level KV Cache Selection** | EMNLP 2025 | long-context inference / KV selection / sparse attention | [Link](https://doi.org/10.18653/v1/2025.emnlp-main.1079) | — |
| **SAS: Sparse Attention Synthesizer for Efficient Language Model Inference** | EuroSys 2026 | efficient attention / kernel synthesis / KV cache | [Link](https://arxiv.org/abs/2602.09051) | — |
| **Enabling Efficient SpMM for Sparse Attention on GEMM-Optimized Hardware with Block Aggregation** | FPGA 2026 | sparse attention / FPGA / SpMM-GEMM transformation | [Link](https://doi.org/10.1145/3748173.3779187) | — |
| **FARE: A Fine-grained Pipelined Reconfigurable FlashAttention Kernel** | FPGA 2026 | FlashAttention accelerator / FPGA | [Link](https://doi.org/10.1145/3748173.3779572) | — |
| **PADE: A Predictor-Free Sparse Attention Accelerator via Unified Execution and Stage Fusion** | HPCA 2026 | sparse attention accelerator / algorithm-hardware co-design | [Link](https://arxiv.org/abs/2512.14322) | — |
| **Multi-Head Low-Rank Attention** | ICLR 2026 | KV-efficient attention / tensor-parallel decoding | — | — |
| **ProxyAttn: Guided Sparse Attention via Representative Heads** | ICLR 2026 | sparse attention / long-context prefill | — | — |
| **Star Attention: Efficient LLM Inference over Long Sequences** | ICML 2025 | long-context / KV cache / efficient LLM inference | — | — |
| **A Unified Sparse Attention via Multi-Granularity Compression** | ICML 2026 | efficient attention / long-context inference | [Link](https://arxiv.org/abs/2512.14082) | — |
| **SALE : Low-bit Estimation for Efficient Sparse Attention in Long-context LLM Prefilling** | ICML 2026 | efficient attention / low-bit estimation / long-context prefill | [Link](https://arxiv.org/abs/2505.24179) | — |
| **Scout Before You Attend: Sketch-and-Walk Sparse Attention for Efficient LLM Inference** | ICML 2026 | efficient attention / long-context inference | [Link](https://arxiv.org/abs/2602.07397) | — |
| **Token Sparse Attention: Efficient Long-Context Inference with Interleaved Token Selection** | ICML 2026 | sparse attention / long-context inference | [Link](https://arxiv.org/abs/2602.03216) | — |
| **CHIME: A Case for Efficient Long-Context Attention-FC Disaggregated Inference with DIMM-PIM** | ISCA 2026 | long-context LLM / disaggregated inference / PIM | — | — |
| **LongSight: Compute-Enabled Memory to Accelerate Large-Context LLMs via Sparse Attention** | MICRO 2025 | long-context LLM / sparse attention / CXL memory | [Link](https://doi.org/10.1145/3725843.3756062) | — |
| **BLASST: Dynamic BLocked Attention Sparsity via Softmax Thresholding** | MLSys 2026 | sparse attention / long-context inference | — | — |
| **IntAttention: A Fully Integer Attention Pipeline for Efficient Edge Inference** | MLSys 2026 | edge inference / integer attention | — | — |
| **Efficient Large Language Model Inference with Neural Block Linearization** | NeurIPS 2025 | LLM inference acceleration / attention approximation | [Link](https://doi.org/10.52202/085713-0196) | — |
| **SageAttention3: Microscaling FP4 Attention for Inference and An Exploration of 8-Bit Training** | NeurIPS 2025 | low-bit attention kernel / FP4 | [Link](https://doi.org/10.52202/085713-1799) | — |
| **Spotlight Attention: Towards Efficient LLM Generation via Non-linear Hashing-based KV Cache Retrieval** | NeurIPS 2025 | sparse attention / KV retrieval / CUDA kernel | [Link](https://doi.org/10.52202/085713-2883) | — |
| **ECHO: Efficient KV Cache Offloading with Lossless Prefetching for Serving Native Sparse Attention LLMs** | OSDI 2026 | sparse-attention KV-cache serving | — | — |
| **Neptune: Advanced ML Operator Fusion for Locality and Parallelism on GPUs** | PLDI 2026 | ML compiler / attention operator fusion | — | — |
| **FlashAttention-T: Towards Fully Tensorized Attention by Exploiting Tensor-Vector Parallelism** | PPoPP 2026 | attention kernel / tensor core / GPU | [Link](https://doi.org/10.1145/3774934.3786425) | — |
| **HelixPipe: Efficient Distributed Training of Long Sequence Transformers with Attention Parallel Pipeline Parallelism** | PPoPP 2026 | distributed training / long-context transformer | — | — |
| **JanusQuant: Accurate and Efficient 2-bit KV Cache Quantization for Long-Context Inference** | PPoPP 2026 | KV cache quantization / long-context inference | [Link](https://doi.org/10.1145/3774934.3786428) | — |
| **MetaAttention: A Unified and Performant Attention Framework across Hardware Backends** | PPoPP 2026 | attention runtime / cross-backend kernel optimization | [Link](https://doi.org/10.1145/3774934.3786444) | — |
| **HydraCache: LLM Inference Prefill Parallelization Through Distributed Cache Blending** | SC 2025 | LLM serving / distributed prefill / KV cache blending | — | — |
| **MegaScale-Infer: Efficient Mixture-of-Experts Model Serving with Disaggregated Expert Parallelism** | SIGCOMM 2025 | MoE serving / disaggregated expert parallelism / networking | [Link](https://arxiv.org/abs/2504.02263) | — |
| **DepCache: A KV Cache Management Framework for GraphRAG with Dependency Attention** | SIGMOD 2026 | GraphRAG dependency attention / KV-cache management | — | — |
| **Serving Hybrid LLM Loads with SLO Guarantees Using CPU-GPU Attention Piggybacking** | SIGMOD 2026 | LLM serving / heterogeneous CPU-GPU / SLO scheduling | [Link](https://arxiv.org/abs/2603.12831) | — |
| **Weaver: Efficient Multi-LLM Serving with Attention Offloading** | USENIX ATC 2025 | multi-LLM serving / attention offloading | — | — |
| **Silicon-Oracle (Soracle): A Multi-Modal Autoregressive Model Accelerator for Context-Aware Assistance on Mobile Platform** | VLSI Symposium 2026 | multimodal autoregressive accelerator / mobile inference | [Link](https://doi.org/10.1109/VLSITechnologyandCir65830.2026.11577228) | — |
| **DeaMoE: Efficient MoE Structure for Fast Small-Batch Decoding** | Fresh / preprint | MoE architecture / small-batch decoding | [Link](https://arxiv.org/abs/2608.14385) | — |
| **Every Expert Counts: ExactMoE for Memory-Efficient W4A16 Inference** | Fresh / preprint | MoE memory-efficient W4A16 inference / GPU slot cache | [Link](https://arxiv.org/abs/2608.15383) | — |
| **GraniKV: Asymmetric Granularity KV-Cache Paging for Multi-Agent Systems with Long Shared Prefix** | Fresh / preprint | KV-cache paging / multi-agent serving | [Link](https://arxiv.org/abs/2608.15584) | — |
| **SCOPE: Subspace Clustering with Online Per-Head Top-K Estimation for Sparse Video Attention** | Fresh / preprint | sparse video attention / DiT inference | [Link](https://arxiv.org/abs/2608.12780) | — |
| **SQuad: Sub-Quadratic Attention Distillation for Efficient Video Generation** | Fresh / preprint | video generation acceleration / efficient attention | [Link](https://arxiv.org/abs/2608.16585) | — |
| **TileMix: Tile-Centric Mixed-Precision Attention for LLM Inference Acceleration** | Fresh / preprint | mixed-precision attention kernel / long-context inference | [Link](https://arxiv.org/abs/2608.17336) | — |
