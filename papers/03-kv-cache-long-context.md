# 03 · KV Cache / Long Context

> **144 papers** currently mapped to this direction. Cross-direction duplication is intentional when a paper has multiple technical roles.

[← Research Map](README.md) · [Complete Paper List](ALL_PAPERS.md)

| Paper | Venue | Topic | Paper | Code |
|---|---|---|---|---|
| **Accelerating LLM Inference Throughput via Asynchronous KV Cache Prefetching** | AAAI 2026 | LLM inference / KV cache prefetch / GPU memory hierarchy | [Link](https://doi.org/10.1609/aaai.v40i25.39224) | — |
| **AccKV: Towards Efficient Audio-Video LLMs Inference via Adaptive-Focusing and Cross-Calibration KV Cache Optimization** | AAAI 2026 | audio-video LLM / multimodal KV cache optimization | [Link](https://doi.org/10.1609/aaai.v40i7.37467) | — |
| **Efficient Multimodal Large Language Model via Dynamic KV Cache Quantization** | AAAI 2026 | MLLM inference / KV cache quantization | [Link](https://doi.org/10.1609/aaai.v40i25.39241) | — |
| **KeepKV: Achieving Periodic Lossless KV Cache Compression for Efficient LLM Inference** | AAAI 2026 | KV cache compression / inference throughput | [Link](https://doi.org/10.1609/aaai.v40i39.40611) | — |
| **KVmix: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for KV Cache** | AAAI 2026 | KV cache quantization / mixed precision | [Link](https://doi.org/10.1609/aaai.v40i37.40422) | — |
| **MHA2MLA-VLM: Enabling DeepSeek’s Economical Multi-Head Latent Attention Across Vision-Language Models** | AAAI 2026 | VLM inference / MLA / KV cache compression | [Link](https://doi.org/10.1609/aaai.v40i36.40319) | — |
| **Q Cache: Visual Attention Is Valuable in Less than Half of Decode Layers for Multimodal Large Language Model** | AAAI 2026 | MLLM inference / cross-layer attention reuse / KV cache | [Link](https://doi.org/10.1609/aaai.v40i16.38414) | — |
| **Self-Indexing KVCache: Predicting Sparse Attention from Compressed Keys** | AAAI 2026 | KV cache compression / sparse attention / CUDA kernel | [Link](https://doi.org/10.1609/aaai.v40i33.39988) | — |
| **SlimInfer: Accelerating Long-Context LLM Inference via Dynamic Token Pruning** | AAAI 2026 | long-context LLM inference / token pruning / asynchronous KV manager | [Link](https://arxiv.org/abs/2508.06447) | [Repo](https://github.com/Longxmas/SlimInfer) |
| **Sparse Attention Across Multiple-Context KV Cache** | AAAI 2026 | RAG / sparse attention / multi-context KV cache | [Link](https://doi.org/10.1609/aaai.v40i36.40266) | — |
| **ContrastKV: Robust KV Cache Eviction via Contrastive Signal Fusion for Multi-Query Generalization** | ACL 2026 | KV-cache eviction / long-context multi-query inference | [Link](https://doi.org/10.18653/v1/2026.acl-long.417) | — |
| **Evolving Sparsity: Leveraging Token Importance Dynamics for Efficient LLM Decoding with Sparse Attention** | ACL 2026 | sparse attention / long-context decoding | [Link](https://doi.org/10.18653/v1/2026.acl-long.530) | — |
| **HybridKV: Hybrid KV Cache Compression for Efficient Multimodal Large Language Model Inference** | ACL 2026 | multimodal KV-cache compression / efficient MLLM inference | [Link](https://doi.org/10.18653/v1/2026.acl-long.594) | — |
| **LongSpec: Long-Context Lossless Speculative Decoding with Efficient Drafting and Verification** | ACL 2026 | speculative decoding / long-context inference | [Link](https://doi.org/10.18653/v1/2026.acl-long.83) | — |
| **SpecCache: Speculative KV Cache Reuse for Efficient RAG Serving** | ACL 2026 | RAG serving / KV cache reuse | [Link](https://doi.org/10.18653/v1/2026.acl-long.859) | — |
| **VecInfer: Efficient LLM Inference with Low-Bit KV Cache via Outlier-Suppressed Vector Quantization** | ACL 2026 | KV-cache quantization / low-bit LLM inference / CUDA kernel | [Link](https://doi.org/10.18653/v1/2026.acl-long.1454) | — |
| **BAT: Efficient Generative Recommender Serving with Bipartite Attention** | ASPLOS 2026 | generative recommender serving / KV prefix cache | [Link](https://doi.org/10.1145/3779212.3790131) | — |
| **MoE-APEX: An Efficient MoE Inference System with Adaptive Precision Expert Offloading** | ASPLOS 2026 | edge MoE inference / expert offloading / mixed precision | [Link](https://doi.org/10.1145/3779212.3790187) | — |
| **REPA: Reconfigurable PIM for the Joint Acceleration of KV Cache Offloading and Processing** | ASPLOS 2026 | KV cache / PIM acceleration | [Link](https://doi.org/10.1145/3779212.3790212) | — |
| **SpeContext: Enabling Efficient Long-context Reasoning with Speculative Context Sparsity in LLMs** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | [Link](https://arxiv.org/abs/2512.00722) | — |
| **STARC: Selective Token Access with Remapping and Clustering for Efficient LLM Decoding on PIM Systems** | ASPLOS 2026 | sparse attention / PIM / KV cache | [Link](https://doi.org/10.1145/3779212.3790226) | — |
| **TPLA: Tensor Parallel Latent Attention for Efficient Disaggregated Prefill & Decode Inference** | ASPLOS 2026 | MLA / tensor parallelism / KV cache / disaggregated inference | [Link](https://arxiv.org/abs/2508.15881) | — |
| **E2-RAG: Towards Editable Efficient RAG by Editing Compressed KV Caches** | COLM 2025 | RAG / compressed KV cache / editable cache | — | [Repo](https://github.com/tongxuluo/e2rag) |
| **Hardware-Efficient Attention for Fast Decoding** | COLM 2025 | efficient attention / KV-cache bandwidth / serving | [Link](https://arxiv.org/abs/2505.21487) | — |
| **KVSink: Understanding and Enhancing the Preservation of Attention Sinks in KV Cache Quantization for LLMs** | COLM 2025 | KV cache quantization / attention sinks | [Link](https://arxiv.org/abs/2508.04257) | — |
| **Mixture of Attention Spans: Optimizing LLM Inference Efficiency with Heterogeneous Sliding-Window Lengths** | COLM 2025 | sparse attention / long-context inference / KV cache compression | [Link](https://arxiv.org/abs/2406.14909) | [Repo](https://github.com/thu-nics/MoA) |
| **PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling** | COLM 2025 | KV cache compression / long-context inference | [Link](https://arxiv.org/abs/2406.02069) | — |
| **SQuat: Subspace-orthogonal KV Cache Quantization** | COLM 2025 | KV cache quantization | [Link](https://arxiv.org/abs/2503.24358) | — |
| **X-EcoMLA: Upcycling Pre-Trained Attention into MLA for Efficient and Extreme KV Compression** | COLM 2025 | KV cache compression / efficient attention architecture | [Link](https://arxiv.org/abs/2503.11132) | — |
| **Efficient Inference of Vision Instruction-Following Models with Elastic Cache** | ECCV 2024 | KV cache / multimodal inference | — | — |
| **Cost-Optimal Grouped-Query Attention for Long-Context Modeling** | EMNLP 2025 | efficient attention / GQA / long-context modeling | [Link](https://doi.org/10.18653/v1/2025.emnlp-main.272) | — |
| **Efficient Beam Search for Large Language Models Using Trie-Based Decoding** | EMNLP 2025 | beam search / shared KV cache / decoding acceleration | [Link](https://doi.org/10.18653/v1/2025.emnlp-main.748) | — |
| **FIER: Fine-Grained and Efficient KV Cache Retrieval for Long-context LLM Inference** | EMNLP 2025 | KV cache retrieval / long-context inference | [Link](https://doi.org/10.18653/v1/2025.findings-emnlp.515) | — |
| **GraphKV: Breaking the Static Selection Paradigm with Graph-Based KV Cache Eviction** | EMNLP 2025 | KV cache eviction / graph-based selection | [Link](https://doi.org/10.18653/v1/2025.emnlp-main.1112) | — |
| **LeanK: Learnable K Cache Channel Pruning for Efficient Decoding** | EMNLP 2025 | KV cache pruning / decoding acceleration | [Link](https://doi.org/10.18653/v1/2025.emnlp-main.1584) | — |
| **Lookahead Q-Cache: Achieving More Consistent KV Cache Eviction via Pseudo Query** | EMNLP 2025 | KV cache eviction / long-context inference | [Link](https://doi.org/10.18653/v1/2025.emnlp-main.1732) | — |
| **TokenSelect: Efficient Long-Context Inference and Length Extrapolation for LLMs via Dynamic Token-Level KV Cache Selection** | EMNLP 2025 | long-context inference / KV selection / sparse attention | [Link](https://doi.org/10.18653/v1/2025.emnlp-main.1079) | — |
| **XQuant: Achieving Ultra-Low Bit KV Cache Quantization with Cross-Layer Compression** | EMNLP 2025 | KV cache quantization / long-context inference | [Link](https://doi.org/10.18653/v1/2025.emnlp-main.494) | — |
| **DynamicKV: Task-Aware Adaptive KV Cache Compression for Long Context LLMs** | EMNLP 2025 Findings | KV cache compression / task-aware adaptive allocation | [Link](https://doi.org/10.18653/v1/2025.findings-emnlp.426) | — |
| **EvolKV: Evolutionary KV Cache Compression for LLM Inference** | EMNLP 2025 Findings | KV cache compression / evolutionary budget allocation | [Link](https://doi.org/10.18653/v1/2025.findings-emnlp.88) | — |
| **Hardware-Aware Parallel Prompt Decoding for Memory-Efficient Acceleration of LLM Inference** | EMNLP 2025 Findings | speculative decoding / edge LLM / memory-efficient inference | [Link](https://doi.org/10.18653/v1/2025.findings-emnlp.120) | — |
| **LAVa: Layer-wise KV Cache Eviction with Dynamic Budget Allocation** | EMNLP 2025 Findings | KV cache eviction / dynamic layer-head budgets | [Link](https://doi.org/10.18653/v1/2025.findings-emnlp.737) | — |
| **More Tokens, Lower Precision: Towards the Optimal Token-Precision Trade-off in KV Cache Compression** | EMNLP 2025 Findings | KV cache compression / token-precision co-optimization | [Link](https://doi.org/10.18653/v1/2025.findings-emnlp.429) | — |
| **High Throughput and Low Latency LLM Serving via Adaptive KV Caching** | EuroSys 2026 | LLM serving / KV cache / adaptive caching | [Link](https://doi.org/10.1145/3767295.3803570) | — |
| **MFS: An Efficient Model Family Serving System for LLMs** | EuroSys 2026 | LLM model-family serving / multi-tier batching / cross-model KV sharing | [Link](https://doi.org/10.1145/3767295.3769355) | — |
| **SAS: Sparse Attention Synthesizer for Efficient Language Model Inference** | EuroSys 2026 | efficient attention / kernel synthesis / KV cache | [Link](https://arxiv.org/abs/2602.09051) | — |
| **CXL-SpecKV: A Disaggregated FPGA Speculative KV-Cache for Datacenter LLM Serving** | FPGA 2026 | LLM serving / CXL / FPGA / speculative KV cache | [Link](https://arxiv.org/abs/2512.11920) | [Repo](https://github.com/FastLM/CXL-SpecKV) |
| **AQPIM: Breaking the PIM Capacity Wall for LLMs with In-Memory Activation Quantization** | HPCA 2026 | PIM / activation quantization / long-context LLM | [Link](https://arxiv.org/abs/2604.18137) | — |
| **BitDecoding: Unlocking Tensor Cores for Long-Context LLMs with Low-Bit KV Cache** | HPCA 2026 | low-bit KV cache / Tensor Core decoding | [Link](https://doi.org/10.1109/HPCA68181.2026.11408481) | — |
| **ELORA: Efficient LoRA and KV Cache Management for Multi-LoRA LLM Serving** | HPCA 2026 | multi-LoRA serving / KV cache management | [Link](https://doi.org/10.1109/HPCA68181.2026.11408492) | — |
| **AirCache: Activating Inter-modal Relevancy KV Cache Compression for Efficient Large Vision-Language Model Inference** | ICCV 2025 | multimodal KV-cache compression | — | — |
| **Autoregressive Image Generation with Randomized Parallel Decoding** | ICLR 2026 | autoregressive image generation / parallel decoding | — | — |
| **DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference** | ICLR 2026 | KV cache eviction / robust aggregation | [Link](https://arxiv.org/abs/2510.13334) | [Repo](https://github.com/FFY0/DefensiveKV) |
| **Fast-dLLM: Training-free Acceleration of Diffusion LLM by Enabling KV Cache and Parallel Decoding** | ICLR 2026 | diffusion LLM inference / KV cache / parallel decoding | [Link](https://arxiv.org/abs/2505.22618) | [Repo](https://github.com/NVlabs/Fast-dLLM) |
| **FreeKV: Boosting KV Cache Retrieval for Efficient LLM Inference** | ICLR 2026 | KV cache retrieval / CPU-GPU hybrid memory / long-context inference | [Link](https://arxiv.org/abs/2505.13109) | — |
| **ICaRus: Identical Cache Reuse for Efficient Multi-Model Inference** | ICLR 2026 | multi-model LLM serving / cross-model KV cache reuse | [Link](https://arxiv.org/abs/2603.13281) | — |
| **ProxyAttn: Guided Sparse Attention via Representative Heads** | ICLR 2026 | sparse attention / long-context prefill | — | — |
| **TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate** | ICLR 2026 | online vector quantization / KV cache compression | — | — |
| **Cache Me If You Must: Adaptive Key-Value Quantization for Large Language Models** | ICML 2025 | long-context / KV cache / efficient LLM inference | — | — |
| **CommVQ: Commutative Vector Quantization for KV Cache Compression** | ICML 2025 | KV cache quantization | — | — |
| **Compute or Load KV Cache? Why Not Both?** | ICML 2025 | long-context / KV cache / efficient LLM inference | — | — |
| **EPIC: Efficient Position-Independent Caching for Serving Large Language Models** | ICML 2025 | long-context / KV cache / efficient LLM inference | — | — |
| **KVTuner: Sensitivity-Aware Layer-Wise Mixed-Precision KV Cache Quantization for Efficient and Nearly Lossless LLM Inference** | ICML 2025 | long-context / KV cache / efficient LLM inference | — | — |
| **LaCache: Ladder-Shaped KV Caching for Efficient Long-Context Modeling of Large Language Models** | ICML 2025 | long-context / KV cache / efficient LLM inference | — | — |
| **QuantSpec: Self-Speculative Decoding with Hierarchical Quantized KV Cache** | ICML 2025 | speculative decoding / KV quantization | — | — |
| **RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression** | ICML 2025 | long-context / KV cache / efficient LLM inference | — | — |
| **ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference** | ICML 2025 | long-context / KV cache / efficient LLM inference | — | — |
| **SpeCache: Speculative Key-Value Caching for Efficient Generation of LLMs** | ICML 2025 | long-context / KV cache / efficient LLM inference | — | — |
| **Star Attention: Efficient LLM Inference over Long Sequences** | ICML 2025 | long-context / KV cache / efficient LLM inference | — | — |
| **A Unified Sparse Attention via Multi-Granularity Compression** | ICML 2026 | efficient attention / long-context inference | [Link](https://arxiv.org/abs/2512.14082) | — |
| **Elastic Attention: Test-time Adaptive Sparsity Ratios for Efficient Transformers** | ICML 2026 | adaptive sparse attention / long-context inference | [Link](https://arxiv.org/abs/2601.17367) | [Repo](https://github.com/LCM-Lab/Elastic-Attention) |
| **SALE : Low-bit Estimation for Efficient Sparse Attention in Long-context LLM Prefilling** | ICML 2026 | efficient attention / low-bit estimation / long-context prefill | [Link](https://arxiv.org/abs/2505.24179) | — |
| **Scout Before You Attend: Sketch-and-Walk Sparse Attention for Efficient LLM Inference** | ICML 2026 | efficient attention / long-context inference | [Link](https://arxiv.org/abs/2602.07397) | — |
| **Token Sparse Attention: Efficient Long-Context Inference with Interleaved Token Selection** | ICML 2026 | sparse attention / long-context inference | [Link](https://arxiv.org/abs/2602.03216) | — |
| **RotateKV: Accurate and Robust 2-Bit KV Cache Quantization for LLMs via Outlier-Aware Adaptive Rotations** | IJCAI 2025 | KV-cache quantization / low-bit inference | [Link](https://arxiv.org/abs/2501.16383) | — |
| **TreeKV: Smooth Key-Value Cache Compression with Tree Structures** | IJCAI 2025 | KV cache compression / long-context inference | [Link](https://arxiv.org/abs/2501.04987) | — |
| **CHIME: A Case for Efficient Long-Context Attention-FC Disaggregated Inference with DIMM-PIM** | ISCA 2026 | long-context LLM / disaggregated inference / PIM | — | — |
| **Combating the Memory Walls: Optimization Pathways for Long-Context Agentic LLM Inference** | ISCA 2026 | long-context agentic LLM / accelerator / memory wall | [Link](https://arxiv.org/abs/2509.09505) | — |
| **Omni-LUT: Energy-Efficient LUT-based Accelerator with Hardware-Aware KV Cache Quantization** | ISCA 2026 | LLM inference accelerator / LUT / KV-cache quantization | — | — |
| **Tetris: Efficient Long-context LLM Serving with Chunkwise Dynamic Sequence Parallelism** | ISCA 2026 | long-context LLM serving / sequence parallelism | — | — |
| **EARN: Efficient Inference Acceleration for LLM-based Generative Recommendation by Register Tokens** | KDD 2025 | LLM inference acceleration / KV cache / recommendation | [Link](https://arxiv.org/abs/2507.00715) | — |
| **Kelle: Co-design KV Caching and eDRAM for Efficient LLM Serving in Edge Computing** | MICRO 2025 | edge LLM serving / KV cache / eDRAM co-design | [Link](https://arxiv.org/abs/2510.16040) | — |
| **LongSight: Compute-Enabled Memory to Accelerate Large-Context LLMs via Sparse Attention** | MICRO 2025 | long-context LLM / sparse attention / CXL memory | [Link](https://doi.org/10.1145/3725843.3756062) | — |
| **BLASST: Dynamic BLocked Attention Sparsity via Softmax Thresholding** | MLSys 2026 | sparse attention / long-context inference | — | — |
| **Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost** | MLSys 2026 | KV cache quantization / low-bit inference | — | — |
| **Locality-Aware Beam Scheduling for Efficient Test-Time Compute with a Consumer-grade GPU** | MLSys 2026 | efficient reasoning / test-time compute / KV offload scheduling | — | — |
| **MorphServe: Efficient and Workload-Aware LLM Serving via Runtime Quantized Layer Swapping and KV Cache Resizing** | MLSys 2026 | LLM serving / dynamic quantization / KV resizing | — | — |
| **ProfInfer: An eBPF-based Fine-Grained LLM Inference Profiler** | MLSys 2026 | LLM inference profiling / edge runtime observability | — | — |
| **Accurate KV Cache Eviction via Anchor Direction Projection for Efficient LLM Inference** | NeurIPS 2025 | KV cache eviction | — | — |
| **Activated LoRA: Fine-tuned LLMs for Intrinsics** | NeurIPS 2025 | LoRA serving / KV cache reuse | — | — |
| **ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference** | NeurIPS 2025 | KV cache compression / long-context inference | [Link](https://doi.org/10.52202/085713-0966) | [Repo](https://github.com/NVIDIA/kvpress) |
| **Compress, Gather, and Recompute: REFORMing Long-Context Processing in Transformers** | NeurIPS 2025 | long-context inference / compressed KV / recompute | — | — |
| **HiFC: High-efficiency Flash-based KV Cache Swapping for Scaling LLM Inference** | NeurIPS 2025 | KV cache swapping / SSD / GDS | [Link](https://doi.org/10.52202/085713-1587) | — |
| **KeyDiff: Key Similarity-Based KV Cache Eviction for Long-Context LLM Inference in Resource-Constrained Environments** | NeurIPS 2025 | KV cache eviction / resource-constrained long context | — | — |
| **KVLink: Accelerating Large Language Models via Efficient KV Cache Reuse** | NeurIPS 2025 | KV cache reuse / RAG serving | — | — |
| **KVzip: Query-Agnostic KV Cache Compression with Context Reconstruction** | NeurIPS 2025 | KV cache eviction / multi-query reuse | [Link](https://doi.org/10.52202/085713-5585) | — |
| **Memory-Efficient Visual Autoregressive Modeling with Scale-Aware KV Cache Compression** | NeurIPS 2025 | visual autoregressive generation / KV cache compression | — | — |
| **Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion** | NeurIPS 2025 | autoregressive video diffusion / streaming generation | [Link](https://doi.org/10.52202/085713-5576) | — |
| **SmallKV: Small Model Assisted Compensation of KV Cache Compression for Efficient LLM Inference** | NeurIPS 2025 | KV cache compression / small-model assistance | — | — |
| **Speculate Deep and Accurate: Lossless and Training-Free Acceleration for Offloaded LLMs via Substitute Speculative Decoding** | NeurIPS 2025 | offloaded LLM inference / speculative decoding | — | — |
| **Spotlight Attention: Towards Efficient LLM Generation via Non-linear Hashing-based KV Cache Retrieval** | NeurIPS 2025 | sparse attention / KV retrieval / CUDA kernel | [Link](https://doi.org/10.52202/085713-2883) | — |
| **DroidSpeak: KV Cache Sharing Across Fine-tuned Model Variants** | NSDI 2026 | KV cache / multi-model serving | — | — |
| **SwiftEP: Accelerating MoE Inference with Buffer Fusion and TMA Offloading** | NSDI 2026 | MoE communication / inference runtime | — | — |
| **SYMPHONY: Enabling Compute-Memory Disaggregation in LLM Serving Systems** | NSDI 2026 | KV-cache / disaggregated memory serving | — | — |
| **ECHO: Efficient KV Cache Offloading with Lossless Prefetching for Serving Native Sparse Attention LLMs** | OSDI 2026 | sparse-attention KV-cache serving | — | — |
| **No Buffer, No Bottleneck: Efficient Zero-Copy KV Cache Offloading for Long-Context LLMs** | OSDI 2026 | LLM serving / KV cache offloading / heterogeneous CPU-GPU memory | — | — |
| **Strata: Hierarchical Context Caching for Long Context Language Model Serving** | OSDI 2026 | long-context KV-cache serving | — | — |
| **HelixPipe: Efficient Distributed Training of Long Sequence Transformers with Attention Parallel Pipeline Parallelism** | PPoPP 2026 | distributed training / long-context transformer | — | — |
| **JanusQuant: Accurate and Efficient 2-bit KV Cache Quantization for Long-Context Inference** | PPoPP 2026 | KV cache quantization / long-context inference | [Link](https://doi.org/10.1145/3774934.3786428) | — |
| **Muninn: Your Trajectory Diffusion Model But Faster** | RSS 2026 | Physical AI / trajectory diffusion acceleration / training-free cache reuse | [Link](https://arxiv.org/abs/2605.09999) | [Repo](https://github.com/gokulp01/Muninn) |
| **HydraCache: LLM Inference Prefill Parallelization Through Distributed Cache Blending** | SC 2025 | LLM serving / distributed prefill / KV cache blending | — | — |
| **ByteScale: Communication-Efficient Scaling of LLM Training with a 2048K Context Length on 16384 GPUs** | SIGCOMM 2025 | KV encoding + MoE training fabric + long-context training + AI networking/inference | [Link](https://arxiv.org/abs/2502.21231) | — |
| **HACK: Homomorphic Acceleration via Compression of the Key-Value Cache for Disaggregated LLM Inference** | SIGCOMM 2025 | KV cache / disaggregated LLM serving / quantization | [Link](https://arxiv.org/abs/2502.03589) | — |
| **MixNet: A Runtime Reconfigurable Optical-Electrical Fabric for Distributed Mixture-of-Experts Training** | SIGCOMM 2025 | KV encoding + MoE training fabric + long-context training + AI networking/inference | [Link](https://arxiv.org/abs/2501.03905) | — |
| **Pegasus: A Universal Framework for Scalable Deep Learning Inference on the Dataplane** | SIGCOMM 2025 | KV encoding + MoE training fabric + long-context training + AI networking/inference | [Link](https://arxiv.org/abs/2506.05779) | — |
| **SCX** | SIGCOMM 2025 | KV encoding + MoE training fabric + long-context training + AI networking/inference | — | — |
| **SGLB: Scalable and Robust Global Load Balancing in Commodity AI Clusters** | SIGCOMM 2025 | KV encoding + MoE training fabric + long-context training + AI networking/inference | [Link](https://doi.org/10.1145/3718958.3750527) | — |
| **Beluga: A CXL-Based Memory Architecture for Scalable and Efficient LLM KVCache Management** | SIGMOD 2026 | CXL memory / KV-cache serving | [Link](https://arxiv.org/abs/2511.20172) | — |
| **DepCache: A KV Cache Management Framework for GraphRAG with Dependency Attention** | SIGMOD 2026 | GraphRAG dependency attention / KV-cache management | — | — |
| **From Prefix Cache to Fusion RAG Cache: Accelerating LLM Inference in Retrieval-Augmented Generation** | SIGMOD 2026 | RAG KV-cache reuse / TTFT acceleration | [Link](https://arxiv.org/abs/2601.12904) | — |
| **HotPrefix: Hotness-Aware KV Cache Scheduling for Efficient Prefix Sharing in LLM Inference Systems** | SIGMOD 2026 | prefix KV-cache scheduling / LLM serving | [Link](https://doi.org/10.1145/3749168) | — |
| **Medha** | SoCC 2026 | KV virtualization + long-context serving + GPU colocation + on-device adaptation | — | — |
| **Memory-Decoupled Layer-Wise Fine-Tuning** | SoCC 2026 | KV virtualization + long-context serving + GPU colocation + on-device adaptation | — | — |
| **MosaicKV: SLO-Aware KV Cache Virtualization for Efficient LLM Serving** | SoCC 2026 | KV virtualization + long-context serving + GPU colocation + on-device adaptation | [Link](https://arxiv.org/abs/2607.00760) | — |
| **No Request Left Behind: Tackling Heterogeneity in Long-Context LLM Inference with Medha** | SoCC 2026 | KV virtualization + long-context serving + GPU colocation + on-device adaptation | [Link](https://arxiv.org/abs/2409.17264) | — |
| **PEACE: Power and Performance Aware Colocation for Efficient GPU Spatial Partitioning** | SoCC 2026 | KV virtualization + long-context serving + GPU colocation + on-device adaptation | [Link](https://doi.org/10.1145/3815789.3827949) | — |
| **DCP: Addressing Input Dynamism In Long-Context Training via Dynamic Context Parallelism** | SOSP 2025 | long-context LLM training / dynamic context parallelism | [Link](https://arxiv.org/abs/2510.10620) | [Repo](https://github.com/chenyu-jiang/dcp) |
| **Fate: Fast Edge Inference of Mixture-of-Experts Models via Cross-Layer Gate** | The Web Conference 2026 | edge MoE inference / expert prefetch | [Link](https://arxiv.org/abs/2502.12224) | — |
| **Probe-and-Fetch: Dynamic KV Cache Pruning for Accelerated Long-Context Inference in Web-Scale AI Search** | The Web Conference 2026 | KV cache pruning / long-context inference | [Link](https://doi.org/10.1145/3774904.3792794) | — |
| **Task-Aware Cloud-End Offloading for Vision-Language Model Serving via Dynamic Modality-Specific Adapter Scheduling** | The Web Conference 2026 | multimodal/VLM serving / cloud-edge offloading | [Link](https://doi.org/10.1145/3774904.3792127) | — |
| **JENGA: Enhancing LLM Long-Context Fine-tuning with Contextual Token Sparsity** | USENIX ATC 2025 | long-context LLM fine-tuning / contextual token sparsity / kernels | — | — |
| **Katz** | USENIX ATC 2025 | production KV-cache + quantized-kernel compiler + diffusion workflow serving | — | — |
| **KVCache Cache in the Wild** | USENIX ATC 2025 | production KV-cache + quantized-kernel compiler + diffusion workflow serving | — | — |
| **QFactory** | USENIX ATC 2025 | production KV-cache + quantized-kernel compiler + diffusion workflow serving | — | — |
| **Weaver: Efficient Multi-LLM Serving with Attention Offloading** | USENIX ATC 2025 | multi-LLM serving / attention offloading | — | — |
| **A 122.2μJ/Token Reasoning LLM Accelerator with Reinforcement Fine-Tune Featuring Two-Level KV-Cache Compression and Spike-Driven Predictive Update** | VLSI Symposium 2026 | reasoning LLM accelerator / KV compression / RL fine-tuning | [Link](https://doi.org/10.1109/VLSITechnologyandCir65830.2026.11577555) | — |
| **Beyond Capacity: Scalable MoE LLM Inference via High-Bandwidth Flash with Direct GPU and HBM Paths** | Fresh / preprint | MoE serving / high-bandwidth flash architecture | [Link](https://arxiv.org/abs/2608.14333) | — |
| **EcoVLA: Energy-Efficient Device-Edge Co-Inference for Vision-Language-Action Models under Real-Time Constraints** | Fresh / preprint | VLA device-edge co-inference / energy-aware runtime | [Link](https://arxiv.org/abs/2608.15502) | — |
| **From LLM Inference to Agentic Workloads: Characterization and Implications for Serving Systems** | Fresh / preprint | agentic serving characterization / systems benchmark | [Link](https://arxiv.org/abs/2608.15127) | — |
| **From Local Mismatch to Global Impact: Optimizing Cache Reuse Policy for Efficient Diffusion** | Fresh / preprint | diffusion cache policy / video-image generation acceleration | [Link](https://arxiv.org/abs/2608.13043) | — |
| **GraniKV: Asymmetric Granularity KV-Cache Paging for Multi-Agent Systems with Long Shared Prefix** | Fresh / preprint | KV-cache paging / multi-agent serving | [Link](https://arxiv.org/abs/2608.15584) | — |
| **MoNe: Modular Neural Memory for Efficient Long Context Inference** | Fresh / preprint | long-context inference / neural memory | [Link](https://arxiv.org/abs/2608.17616) | — |
| **Pallas: A Proactive KV Cache Migration Framework for LLM Inference in AI-RAN** | Fresh / preprint | LLM serving / KV cache / edge | [Link](https://arxiv.org/abs/2608.16477) | — |
| **TileMix: Tile-Centric Mixed-Precision Attention for LLM Inference Acceleration** | Fresh / preprint | mixed-precision attention kernel / long-context inference | [Link](https://arxiv.org/abs/2608.17336) | — |
