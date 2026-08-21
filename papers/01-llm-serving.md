# 01 · LLM Serving

> **225 papers** currently mapped to this direction. Cross-direction duplication is intentional when a paper has multiple technical roles.

[← Research Map](README.md) · [Complete Paper List](ALL_PAPERS.md)

| Paper | Venue | Topic | Paper | Code |
|---|---|---|---|---|
| **Accelerating LLM Inference Throughput via Asynchronous KV Cache Prefetching** | AAAI 2026 | LLM inference / KV cache prefetch / GPU memory hierarchy | [Link](https://doi.org/10.1609/aaai.v40i25.39224) | — |
| **KeepKV: Achieving Periodic Lossless KV Cache Compression for Efficient LLM Inference** | AAAI 2026 | KV cache compression / inference throughput | [Link](https://doi.org/10.1609/aaai.v40i39.40611) | — |
| **Q Cache: Visual Attention Is Valuable in Less than Half of Decode Layers for Multimodal Large Language Model** | AAAI 2026 | MLLM inference / cross-layer attention reuse / KV cache | [Link](https://doi.org/10.1609/aaai.v40i16.38414) | — |
| **SpecCache: Speculative KV Cache Reuse for Efficient RAG Serving** | ACL 2026 | RAG serving / KV cache reuse | [Link](https://doi.org/10.18653/v1/2026.acl-long.859) | — |
| **Single Trajectory Distillation for Accelerating Image and Video Style Transfer** | ACM Multimedia 2025 | diffusion/style-transfer acceleration / trajectory distillation | [Link](https://arxiv.org/abs/2412.18945) | — |
| **BAT: Efficient Generative Recommender Serving with Bipartite Attention** | ASPLOS 2026 | generative recommender serving / KV prefix cache | [Link](https://doi.org/10.1145/3779212.3790131) | — |
| **BlendServe: Optimizing Offline Inference for Auto-regressive Large Models with Resource-aware Batching** | ASPLOS 2026 | LLM serving / offline batching / prefix sharing | [Link](https://arxiv.org/abs/2411.16102) | — |
| **Bullet: Boosting GPU Utilization for LLM Serving via Dynamic Spatial-Temporal Orchestration** | ASPLOS 2026 | LLM serving / GPU utilization / scheduling | [Link](https://arxiv.org/abs/2504.19516) | — |
| **DFVG** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | — | — |
| **EARTH** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | — | — |
| **I/O Analysis is All You Need: An I/O Analysis for Long-Sequence Attention** | ASPLOS 2026 | attention accelerator / I/O analysis | [Link](https://doi.org/10.1145/3779212.3790174) | — |
| **LAER-MoE: Load-Adaptive Expert Re-layout for Efficient Mixture-of-Experts Training** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | [Link](https://arxiv.org/abs/2602.11686) | — |
| **MoDM** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | — | — |
| **MoE-APEX: An Efficient MoE Inference System with Adaptive Precision Expert Offloading** | ASPLOS 2026 | edge MoE inference / expert offloading / mixed precision | [Link](https://doi.org/10.1145/3779212.3790187) | — |
| **Mugi: Value Level Parallelism For Efficient LLMs** | ASPLOS 2026 | LLM accelerator / value-level parallelism / low precision | [Link](https://arxiv.org/abs/2601.10823) | — |
| **oFFN** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | — | — |
| **Ouroboros: Wafer-Scale SRAM CIM with Token-Grained Pipelining for Large Language Model Inference** | ASPLOS 2026 | LLM accelerator / wafer-scale CIM | [Link](https://arxiv.org/abs/2603.02737) | — |
| **PAT: Accelerating LLM Decoding via Prefix-Aware Attention with Resource Efficient Multi-Tile Kernel** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | [Link](https://arxiv.org/abs/2511.22333) | — |
| **QoServe** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | — | — |
| **Shift Parallelism** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | — | — |
| **Shift Parallelism: Low-Latency, High-Throughput LLM Inference for Dynamic Workloads** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | [Link](https://arxiv.org/abs/2509.16495) | — |
| **SpeContext: Enabling Efficient Long-context Reasoning with Speculative Context Sparsity in LLMs** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | [Link](https://arxiv.org/abs/2512.00722) | — |
| **SpecProto** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | — | — |
| **SwiftSpec: Ultra-Low Latency LLM Decoding by Scaling Asynchronous Speculative Decoding** | ASPLOS 2026 | speculative decoding / low-latency LLM serving | [Link](https://arxiv.org/abs/2506.11309) | — |
| **TetriServe: Efficiently Serving Mixed DiT Workloads** | ASPLOS 2026 | diffusion/DiT serving / scheduling | [Link](https://arxiv.org/abs/2510.01565) | — |
| **Towards High-Goodput LLM Serving with Prefill-decode Multiplexing** | ASPLOS 2026 | LLM serving / prefill-decode multiplexing | [Link](https://arxiv.org/abs/2504.14489) | — |
| **TPLA: Tensor Parallel Latent Attention for Efficient Disaggregated Prefill & Decode Inference** | ASPLOS 2026 | MLA / tensor parallelism / KV cache / disaggregated inference | [Link](https://arxiv.org/abs/2508.15881) | — |
| **XY-Serve** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | — | — |
| **XY-Serve: End-to-End Versatile Production Serving for Dynamic LLM Workloads** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | [Link](https://arxiv.org/abs/2412.18106) | — |
| **ZipServ** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | — | — |
| **ZipServ: Fast and Memory-Efficient LLM Inference with Hardware-Aware Lossless Compression** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | [Link](https://arxiv.org/abs/2603.17435) | — |
| **CITER: Collaborative Inference for Efficient Large Language Model Decoding with Token-Level Routing** | COLM 2025 | collaborative inference / token-level routing / efficient decoding | [Link](https://arxiv.org/abs/2502.01976) | [Repo](https://github.com/aiming-lab/CITER) |
| **Hardware-Efficient Attention for Fast Decoding** | COLM 2025 | efficient attention / KV-cache bandwidth / serving | [Link](https://arxiv.org/abs/2505.21487) | — |
| **Mixture of Attention Spans: Optimizing LLM Inference Efficiency with Heterogeneous Sliding-Window Lengths** | COLM 2025 | sparse attention / long-context inference / KV cache compression | [Link](https://arxiv.org/abs/2406.14909) | [Repo](https://github.com/thu-nics/MoA) |
| **Plato: Plan to Efficient Decode for Large Language Model Inference** | COLM 2025 | parallel/plan-based LLM decoding | — | — |
| **Resource-efficient Inference with Foundation Model Programs** | COLM 2025 | agentic inference / multimodal serving / dynamic model routing | [Link](https://arxiv.org/abs/2504.07247) | [Repo](https://github.com/Flitternie/FMProgramming) |
| **Denoising as Path Planning: Training-Free Acceleration of Diffusion Models with DPCache** | CVPR 2026 | diffusion / cache scheduling | — | — |
| **ZOO-Prune: Training-Free Token Pruning via Zeroth-Order Gradient Estimation in Vision-Language Models** | CVPR 2026 | VLM inference / training-free visual-token pruning / zeroth-order sensitivity | — | [Repo](https://github.com/AIM-SKKU/ZOO-Prune) |
| **HybriMoE: Hybrid CPU-GPU Scheduling and Cache Management for Efficient MoE Inference** | DAC 2025 | MoE inference / hybrid CPU-GPU scheduling / expert prefetch and cache management | [Link](https://arxiv.org/abs/2504.05897) | [Repo](https://github.com/PKU-SEC-Lab/HybriMoE) |
| **AdaDiff: Accelerating Diffusion Models through Step-Wise Adaptive Computation** | ECCV 2024 | diffusion acceleration / adaptive computation / early exit | [Link](https://arxiv.org/abs/2309.17074) | [Repo](https://github.com/Tangshengku/AdaDiff) |
| **Turbo: Informativity-Driven Acceleration Plug-In for Vision-Language Large Models** | ECCV 2024 | VLM inference acceleration / token redundancy pruning | [Link](https://arxiv.org/abs/2407.11717) | [Repo](https://github.com/anakin-skywalker-Joseph/Folder) |
| **AdaServe: Accelerating Multi-SLO LLM Serving with SLO-Customized Speculative Decoding** | EuroSys 2026 | LLM serving / speculative decoding / multi-SLO | — | — |
| **Efficient Multimodal Serving via Module Multiplexing** | EuroSys 2026 | multimodal/MLLM serving / module multiplexing | — | — |
| **FlashPS: Efficient Generative Image Editing with Mask-aware Caching and Scheduling** | EuroSys 2026 | diffusion serving / image editing / activation caching / continuous batching | [Link](https://arxiv.org/abs/2505.20600) | — |
| **FlexPipe: Adapting Dynamic LLM Serving Through Inflight Pipeline Refactoring in Fragmented Serverless Clusters** | EuroSys 2026 | LLM serving / serverless / pipeline parallelism | [Link](https://arxiv.org/abs/2510.11938) | — |
| **High Throughput and Low Latency LLM Serving via Adaptive KV Caching** | EuroSys 2026 | LLM serving / KV cache / adaptive caching | [Link](https://doi.org/10.1145/3767295.3803570) | — |
| **KUNSERVE** | EuroSys 2026 | responsive LLM streaming + memory-overload-aware serving | — | — |
| **MFS: An Efficient Model Family Serving System for LLMs** | EuroSys 2026 | LLM model-family serving / multi-tier batching / cross-model KV sharing | [Link](https://doi.org/10.1145/3767295.3769355) | — |
| **PiLLM: Resource-Efficient LLM Inference Using Workload Prediction** | EuroSys 2026 | LLM inference / workload prediction / resource efficiency | — | — |
| **Scaling LLM Test-Time Compute with Mobile NPU on Smartphones** | EuroSys 2026 | on-device LLM reasoning / mobile NPU / hardware-aware quantization | [Link](https://arxiv.org/abs/2509.23324) | — |
| **SkyWalker: A Locality-Aware Cross-Region Load Balancer for LLM Inference** | EuroSys 2026 | LLM serving / cross-region load balancing / cloud | [Link](https://arxiv.org/abs/2505.24095) | — |
| **TailorLLM: Collaborative End-Cloud Inference of Large and Small Language Models Based on Low-Rank Adaptation** | EuroSys 2026 | edge/cloud LLM inference / collaborative serving / LoRA | — | — |
| **TokenFlow** | EuroSys 2026 | responsive LLM streaming + memory-overload-aware serving | — | — |
| **Accelerating Model Loading in LLM Inference by Programmable Page Cache** | FAST 2026 | LLM inference / model loading / programmable page cache | — | — |
| **Bidaw: Enhancing Key-Value Caching for Interactive LLM Serving via Bidirectional Computation–Storage Awareness** | FAST 2026 | LLM serving / two-tier KV cache / compute-storage co-design | — | — |
| **CacheSlide: Unlocking Cross Position-Aware KV Cache Reuse for Accelerating LLM Serving** | FAST 2026 | LLM serving / KV-cache reuse / agent workloads | — | — |
| **SolidAttention: Low-Latency SSD-based Serving on Memory-Constrained PCs** | FAST 2026 | LLM serving / sparse attention / SSD KV-cache offload | — | — |
| **CXL-SpecKV: A Disaggregated FPGA Speculative KV-Cache for Datacenter LLM Serving** | FPGA 2026 | LLM serving / CXL / FPGA / speculative KV cache | [Link](https://arxiv.org/abs/2512.11920) | [Repo](https://github.com/FastLM/CXL-SpecKV) |
| **TeLLMe: An Efficient End-to-End Ternary LLM Prefill and Decode Accelerator with Table-Lookup Matmul on Edge FPGAs** | FPGA 2026 | edge LLM inference / ternary accelerator / FPGA | [Link](https://arxiv.org/abs/2510.15926) | [Repo](https://github.com/UCI-CORSA/TeLLMe_FPGA_2026) |
| **Adaptive Draft Sequence Length: Enhancing Speculative Decoding Throughput on PIM-Enabled Systems** | HPCA 2026 | efficient VLM + PIM inference + reasoning accelerator + speculative decoding | [Link](https://doi.org/10.1109/HPCA68181.2026.11408598) | — |
| **AutoHAAP: Automated Heterogeneity-Aware Asymmetric Partitioning for LLM Training** | HPCA 2026 | heterogeneous distributed LLM training / partition search | [Link](https://doi.org/10.1109/HPCA68181.2026.11408533) | — |
| **BitDecoding: Unlocking Tensor Cores for Long-Context LLMs with Low-Bit KV Cache** | HPCA 2026 | low-bit KV cache / Tensor Core decoding | [Link](https://doi.org/10.1109/HPCA68181.2026.11408481) | — |
| **ELORA: Efficient LoRA and KV Cache Management for Multi-LoRA LLM Serving** | HPCA 2026 | multi-LoRA serving / KV cache management | [Link](https://doi.org/10.1109/HPCA68181.2026.11408492) | — |
| **PASCAL: A Phase-Aware Scheduling Algorithm for Serving Reasoning-based Large Language Models** | HPCA 2026 | reasoning LLM serving / phase-aware scheduling | [Link](https://arxiv.org/abs/2602.11530) | — |
| **PIMphony: Overcoming Bandwidth and Capacity Inefficiency in PIM-Based Long-Context LLM Inference System** | HPCA 2026 | efficient VLM + PIM inference + reasoning accelerator + speculative decoding | [Link](https://doi.org/10.1109/HPCA68181.2026.11408592) | — |
| **ReThermal: Co-Design of Thermal-Aware Static and Dynamic Scheduling for LLM Training on Liquid-Cooled Wafer-Scale Chips** | HPCA 2026 | wafer-scale LLM training / thermal-aware scheduling | [Link](https://doi.org/10.1109/HPCA68181.2026.11408476) | — |
| **Towards Resource-Efficient Serverless LLM Inference with SLINFER** | HPCA 2026 | serverless LLM serving / heterogeneous CPU-GPU sharing | [Link](https://arxiv.org/abs/2507.00507) | — |
| **Adaptive Caching for Faster Video Generation with Diffusion Transformers** | ICCV 2025 | video diffusion acceleration / adaptive feature caching | [Link](https://arxiv.org/abs/2411.02397) | — |
| **Token-Efficient VLM: High-Resolution Image Understanding via Dynamic Region Proposal** | ICCV 2025 | VLM efficiency / dynamic region proposal / token-efficient high-resolution vision | — | — |
| **Fast-dLLM: Training-free Acceleration of Diffusion LLM by Enabling KV Cache and Parallel Decoding** | ICLR 2026 | diffusion LLM inference / KV cache / parallel decoding | [Link](https://arxiv.org/abs/2505.22618) | [Repo](https://github.com/NVlabs/Fast-dLLM) |
| **ICaRus: Identical Cache Reuse for Efficient Multi-Model Inference** | ICLR 2026 | multi-model LLM serving / cross-model KV cache reuse | [Link](https://arxiv.org/abs/2603.13281) | — |
| **ProxyAttn: Guided Sparse Attention via Representative Heads** | ICLR 2026 | sparse attention / long-context prefill | — | — |
| **EPIC: Efficient Position-Independent Caching for Serving Large Language Models** | ICML 2025 | long-context / KV cache / efficient LLM inference | — | — |
| **ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference** | ICML 2025 | long-context / KV cache / efficient LLM inference | — | — |
| **AugServe: Adaptive Request Scheduling for Augmented Large Language Model Inference Serving** | ICML 2026 | LLM serving / augmented-agent request scheduling | [Link](https://arxiv.org/abs/2512.04013) | — |
| **Efficient Multi-round LLM Inference over Disaggregated Serving** | ICML 2026 | LLM serving / multi-round agents / PD disaggregation | [Link](https://arxiv.org/abs/2602.14516) | — |
| **OServe: Accelerating LLM Serving via Spatial-Temporal Workload Orchestration** | ICML 2026 | LLM serving / heterogeneous deployment / scheduling | [Link](https://arxiv.org/abs/2602.12151) | — |
| **SALE : Low-bit Estimation for Efficient Sparse Attention in Long-context LLM Prefilling** | ICML 2026 | efficient attention / low-bit estimation / long-context prefill | [Link](https://arxiv.org/abs/2505.24179) | — |
| **Scout Before You Attend: Sketch-and-Walk Sparse Attention for Efficient LLM Inference** | ICML 2026 | efficient attention / long-context inference | [Link](https://arxiv.org/abs/2602.07397) | — |
| **RotateKV: Accurate and Robust 2-Bit KV Cache Quantization for LLMs via Outlier-Aware Adaptive Rotations** | IJCAI 2025 | KV-cache quantization / low-bit inference | [Link](https://arxiv.org/abs/2501.16383) | — |
| **Semi-Clairvoyant Scheduling of Speculative Decoding Requests to Minimize LLM Inference Latency** | IJCAI 2025 | speculative decoding / request scheduling / LLM serving | [Link](https://doi.org/10.24963/ijcai.2025/951) | — |
| **Approaching Shannon Bound with Lossless LLM Weight Compression** | ISCA 2026 | lossless LLM weight compression / serving throughput | [Link](https://arxiv.org/abs/2606.15789) | — |
| **ConServe: Contiguity-Preserving Memory Management for Multi-Turn LLM Serving** | ISCA 2026 | LLM serving / multi-turn / memory management | — | — |
| **DynoPipe: Heterogeneous Edge-Cloud LLM Serving with Dynamically Orchestrated Pipeline Boundaries** | ISCA 2026 | edge-cloud LLM serving / heterogeneous pipeline | — | — |
| **HybridSpec: Exploiting Hybrid-bonding Memory to Accelerate LLM Serving through Heterogeneous Architecture and Speculative Decoding** | ISCA 2026 | speculative decoding / heterogeneous memory / LLM serving | — | — |
| **Symbiotic MLLM Serving: Dynamically Balancing Parallelism Across GPUs and Resources Within GPUs** | ISCA 2026 | multimodal LLM serving / GPU resource balancing | — | — |
| **Tetris: Efficient Long-context LLM Serving with Chunkwise Dynamic Sequence Parallelism** | ISCA 2026 | long-context LLM serving / sequence parallelism | — | — |
| **Exploiting Student Parallelism for Low-latency GPU Inference of BERT-like Models in Online Services** | KDD 2025 | GPU online inference / BERT serving / student parallelism | [Link](https://arxiv.org/abs/2408.12526) | — |
| **BitL: A Hybrid Bit-Serial and Parallel Deep Learning Accelerator for Critical Path Reduction** | MICRO 2025 | bit-level sparsity / hybrid bit-serial-bit-parallel DNN accelerator / efficient inference | [Link](https://doi.org/10.1145/3725843.3756044) | — |
| **Chameleon: Adaptive Caching and Scheduling for Many-Adapter LLM Inference Environments** | MICRO 2025 | LLM serving / adapter caching and scheduling | — | — |
| **Kelle: Co-design KV Caching and eDRAM for Efficient LLM Serving in Edge Computing** | MICRO 2025 | edge LLM serving / KV cache / eDRAM co-design | [Link](https://arxiv.org/abs/2510.16040) | — |
| **MX+: Pushing the Limits of Microscaling Formats for Efficient Large Language Model Serving** | MICRO 2025 | LLM serving / low-precision microscaling | — | — |
| **Pimba: A Processing-in-Memory Acceleration for Post-Transformer Large Language Model Serving** | MICRO 2025 | post-transformer LLM serving / PIM / low precision | [Link](https://arxiv.org/abs/2507.10178) | — |
| **Stratum: System-Hardware Co-design with Tiered Monolithic 3D-DRAM for Efficient MoE Serving** | MICRO 2025 | MoE serving / memory-system co-design | — | — |
| **BEAM** | MLSys 2026 | LLM serving + KV + speculative + reasoning efficiency | — | — |
| **BLASST: Dynamic BLocked Attention Sparsity via Softmax Thresholding** | MLSys 2026 | sparse attention / long-context inference | — | — |
| **BOute** | MLSys 2026 | LLM serving + KV + speculative + reasoning efficiency | — | — |
| **CRAFT: Fine-Grained Cost-Aware Expert Replication For Efficient Mixture-of-Experts Serving** | MLSys 2026 | MoE serving / expert replication | — | — |
| **Efficient, VRAM-Constrained xLM Inference on Clients** | MLSys 2026 | client LLM/VLM inference / CPU-GPU hybrid runtime / Physical AI | — | — |
| **fabric-lib** | MLSys 2026 | LLM serving + KV + speculative + reasoning efficiency | — | — |
| **FlexiCache** | MLSys 2026 | LLM serving + KV + speculative + reasoning efficiency | — | — |
| **From Tokens to Layers: Redefining Stall-Free Scheduling for MoE Serving with Layered Prefill** | MLSys 2026 | MoE serving / layered prefill / stall-free scheduling / energy efficiency | — | — |
| **GhostServe** | MLSys 2026 | LLM serving + KV + speculative + reasoning efficiency | — | — |
| **HELIOS: Adaptive Model And Early-Exit Selection for Efficient LLM Inference Serving** | MLSys 2026 | LLM inference / early exit / adaptive model selection / serving | — | — |
| **Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost** | MLSys 2026 | KV cache quantization / low-bit inference | — | — |
| **LAPS: A Length-Aware-Prefill LLM Serving System** | MLSys 2026 | LLM serving / prefill-decode disaggregation / length-aware batching / scheduling | — | — |
| **Locality-Aware Beam Scheduling for Efficient Test-Time Compute with a Consumer-grade GPU** | MLSys 2026 | efficient reasoning / test-time compute / KV offload scheduling | — | — |
| **MorphServe: Efficient and Workload-Aware LLM Serving via Runtime Quantized Layer Swapping and KV Cache Resizing** | MLSys 2026 | LLM serving / dynamic quantization / KV resizing | — | — |
| **OPKV** | MLSys 2026 | LLM serving + KV + speculative + reasoning efficiency | — | — |
| **Optimizing Deployment Configurations for LLM Inference** | MLSys 2026 | LLM serving / deployment configuration / hardware heterogeneity / production systems | — | — |
| **RaidServe** | MLSys 2026 | LLM serving + KV + speculative + reasoning efficiency | — | — |
| **SkipKV** | MLSys 2026 | LLM serving + KV + speculative + reasoning efficiency | — | — |
| **SpecGen** | MLSys 2026 | LLM serving + KV + speculative + reasoning efficiency | — | — |
| **SuperInfer** | MLSys 2026 | LLM serving + KV + speculative + reasoning efficiency | — | — |
| **D2MoE: Dual Routing and Dynamic Scheduling for Efficient On-Device MoE-based LLM Serving** | MobiCom 2025 | on-device MoE serving / dynamic scheduling | [Link](https://doi.org/10.1145/3680207.3723493) | — |
| **Elastic On-Device LLM Service** | MobiCom 2025 | on-device LLM service / elastic model and prompt adaptation | [Link](https://arxiv.org/abs/2409.09071) | — |
| **Activated LoRA: Fine-tuned LLMs for Intrinsics** | NeurIPS 2025 | LoRA serving / KV cache reuse | — | — |
| **Block-Diagonal LoRA for Eliminating Communication Overhead in Tensor Parallel LoRA Serving** | NeurIPS 2025 | LoRA serving / tensor parallel communication elimination | [Link](https://doi.org/10.52202/085713-0010) | — |
| **ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference** | NeurIPS 2025 | KV cache compression / long-context inference | [Link](https://doi.org/10.52202/085713-0966) | [Repo](https://github.com/NVIDIA/kvpress) |
| **HiFC: High-efficiency Flash-based KV Cache Swapping for Scaling LLM Inference** | NeurIPS 2025 | KV cache swapping / SSD / GDS | [Link](https://doi.org/10.52202/085713-1587) | — |
| **HyGen: Efficient LLM Serving via Elastic Online-Offline Request Co-location** | NeurIPS 2025 | LLM serving / online-offline co-location | [Link](https://doi.org/10.52202/085713-0502) | — |
| **KVLink: Accelerating Large Language Models via Efficient KV Cache Reuse** | NeurIPS 2025 | KV cache reuse / RAG serving | — | — |
| **Memory-Efficient Visual Autoregressive Modeling with Scale-Aware KV Cache Compression** | NeurIPS 2025 | visual autoregressive generation / KV cache compression | — | — |
| **SmallKV: Small Model Assisted Compensation of KV Cache Compression for Efficient LLM Inference** | NeurIPS 2025 | KV cache compression / small-model assistance | — | — |
| **SpecEdge: Scalable Edge-Assisted Serving Framework for Interactive LLMs** | NeurIPS 2025 | edge-cloud LLM serving / speculative decoding | — | — |
| **Spotlight Attention: Towards Efficient LLM Generation via Non-linear Hashing-based KV Cache Retrieval** | NeurIPS 2025 | sparse attention / KV retrieval / CUDA kernel | [Link](https://doi.org/10.52202/085713-2883) | — |
| **Zebra-Llama: Towards Extremely Efficient Hybrid Models** | NeurIPS 2025 | efficient hybrid LLM architecture / KV reduction | — | [Repo](https://github.com/AMD-AGI/AMD-Hybrid-Models) |
| **Agentix: An Efficient Serving Engine for LLM Agents as General Programs** | NSDI 2026 | agentic LLM serving | — | — |
| **Cortex: Achieving Low-Latency, Cost-Efficient Remote Data Access For LLM via Semantic-Aware Knowledge Caching** | NSDI 2026 | agent systems / semantic knowledge caching | — | — |
| **DroidSpeak: KV Cache Sharing Across Fine-tuned Model Variants** | NSDI 2026 | KV cache / multi-model serving | — | — |
| **FastServe: Iteration-Level Preemptive Scheduling for Large Language Model Inference** | NSDI 2026 | LLM serving / preemptive scheduling / GPU memory management | — | — |
| **FlexLLM: Token-Level Co-Serving of LLM Inference and Finetuning with SLO Guarantees** | NSDI 2026 | inference + PEFT co-serving | — | — |
| **JITServe: SLO-aware LLM Serving with Imprecise Request Information** | NSDI 2026 | LLM serving / SLO scheduling | — | — |
| **Libra: Flexible Request Partitioning and Scheduling for Serving Unbalanced and Dynamic LLM Workloads** | NSDI 2026 | LLM serving / dynamic partitioning / KV transfer | — | — |
| **RLBoost: Harvesting Preemptible Cloud Resources for Cost-Efficient Reinforcement Learning on LLMs** | NSDI 2026 | efficient reasoning / RL training infrastructure | — | — |
| **ServeGen: Workload Characterization and Generation of Large Language Model Serving in Production** | NSDI 2026 | LLM serving / production workload characterization / benchmark generation | — | [Repo](https://github.com/alibaba/ServeGen) |
| **SYMPHONY: Enabling Compute-Memory Disaggregation in LLM Serving Systems** | NSDI 2026 | KV-cache / disaggregated memory serving | — | — |
| **ECHO: Efficient KV Cache Offloading with Lossless Prefetching for Serving Native Sparse Attention LLMs** | OSDI 2026 | sparse-attention KV-cache serving | — | — |
| **Efficient LLM Serving on Commodity GPU Clusters with Data-Reduced Cross-Instance Orchestration** | OSDI 2026 | commodity-GPU LLM serving | — | — |
| **Inference in the Shadows: Taming Memory Bandwidth Contention in Mobile LLM Inference with Sereno** | OSDI 2026 | mobile LLM inference / edge serving / memory bandwidth contention / speculative decoding | — | — |
| **Kairox: Adaptive GPU-CPU Hybrid LLM Inference via Online Neuron Balancing** | OSDI 2026 | LLM inference / GPU-CPU hybrid execution / activation sparsity / edge inference | — | — |
| **No Buffer, No Bottleneck: Efficient Zero-Copy KV Cache Offloading for Long-Context LLMs** | OSDI 2026 | LLM serving / KV cache offloading / heterogeneous CPU-GPU memory | — | — |
| **OpenTela: Unifying Decentralized Computing Resources for Heterogeneous LLM Serving (Operational Systems)** | OSDI 2026 | LLM serving / heterogeneous clusters / decentralized orchestration / operational systems | — | [Repo](https://github.com/eth-easl/opentela) |
| **Prism: Cost-Efficient Multi-LLM Serving via GPU Memory Ballooning** | OSDI 2026 | LLM serving / multi-model serving / GPU memory ballooning / production deployment | — | [Repo](https://github.com/ovg-project/kvcached) |
| **Revisiting Pipeline Parallelism for LLM Serving** | OSDI 2026 | LLM serving / pipeline parallelism / scheduling / SGLang | — | [Repo](https://github.com/Sys-KU/FastPP) |
| **Strata: Hierarchical Context Caching for Long Context Language Model Serving** | OSDI 2026 | long-context KV-cache serving | — | — |
| **CCL-D: A High-Precision Diagnostic System for Slow and Hang Anomalies in Large-Scale Model Training** | PPoPP 2026 | distributed training infrastructure / diagnosis | [Link](https://doi.org/10.1145/3774934.3786429) | — |
| **ChituDiffusion: A Data-Characteristic-Aware Serving System for Diffusion Models** | PPoPP 2026 | diffusion serving / compile-runtime co-optimization | [Link](https://doi.org/10.1145/3774934.3786424) | — |
| **High-Throughput Non-uniformly Quantized 3-bit LLM Inference** | PPoPP 2026 | 3-bit LLM quantization / GPU kernels | [Link](https://doi.org/10.1145/3774934.3786423) | — |
| **JanusQuant: Accurate and Efficient 2-bit KV Cache Quantization for Long-Context Inference** | PPoPP 2026 | KV cache quantization / long-context inference | [Link](https://doi.org/10.1145/3774934.3786428) | — |
| **Laser: Unlocking Layer-Level Scheduling for Efficient Multi-SLO LLM Serving** | PPoPP 2026 | LLM serving / multi-SLO scheduling | [Link](https://doi.org/10.1145/3774934.3786413) | — |
| **MixFusion: A Patch-Level Parallel Serving System for Mixed-Resolution Diffusion Models** | PPoPP 2026 | diffusion serving / patch-level parallelism | [Link](https://doi.org/10.1145/3774934.3786420) | — |
| **CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision** | RSS 2025 | Physical AI / lightweight VLA / high-throughput robot inference | [Link](https://arxiv.org/abs/2411.00508) | [Repo](https://github.com/clip-rt/clip-rt) |
| **Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success** | RSS 2025 | Physical AI / VLA efficient fine-tuning / parallel action decoding | [Link](https://arxiv.org/abs/2502.19645) | [Repo](https://github.com/moojink/openvla-oft) |
| **Muninn: Your Trajectory Diffusion Model But Faster** | RSS 2026 | Physical AI / trajectory diffusion acceleration / training-free cache reuse | [Link](https://arxiv.org/abs/2605.09999) | [Repo](https://github.com/gokulp01/Muninn) |
| **RLinf-USER: A Unified and Extensible System for Real-World Online Policy Learning in Embodied AI** | RSS 2026 | Physical AI systems / multi-robot online learning / edge-cloud scheduling | [Link](https://arxiv.org/abs/2602.07837) | [Repo](https://github.com/RLinf/RLinf) |
| **Compile-Time QoS Scheme for Deep Learning Inferences** | SC 2025 | multi-tenant inference / QoS / compiler scheduling | [Link](https://doi.org/10.1145/3712285.3759846) | — |
| **Engine-Agnostic Model Hot-Swapping for Cost-Effective LLM Inference** | SC 2025 | LLM serving / GPU model hot-swapping | [Link](https://doi.org/10.1145/3731599.3767354) | — |
| **FIRST: Federated Inference Resource Scheduling Toolkit for Scientific AI Model Access** | SC 2025 | federated inference-as-a-service / HPC AI serving | [Link](https://arxiv.org/abs/2510.13724) | — |
| **gLLM: Global Balanced Pipeline Parallelism Systems for Distributed LLMs Serving with Token Throttling** | SC 2025 | LLM serving / pipeline parallelism / token throttling | [Link](https://arxiv.org/abs/2504.14775) | [Repo](https://github.com/gty111/gLLM) |
| **Hetis: Serving LLMs in Heterogeneous GPU Clusters with Fine-grained and Dynamic Parallelism** | SC 2025 | LLM serving / heterogeneous GPU / dynamic parallelism | [Link](https://arxiv.org/abs/2509.08309) | — |
| **HydraCache: LLM Inference Prefill Parallelization Through Distributed Cache Blending** | SC 2025 | LLM serving / distributed prefill / KV cache blending | — | — |
| **MaverIQ: Fingerprint-Guided Extrapolation and Fragmentation-Aware Layering for Intent-Based LLM Serving** | SC 2025 | LLM serving / intent-aware deployment / resource fragmentation | [Link](https://doi.org/10.1145/3712285.3759867) | [Repo](https://github.com/UT-SysML/MaverIQ) |
| **DistTrain: Addressing Model and Data Heterogeneity with Disaggregated Training for Multimodal Large Language Models** | SIGCOMM 2025 | multimodal training systems / disaggregated training | [Link](https://arxiv.org/abs/2408.04275) | — |
| **HACK: Homomorphic Acceleration via Compression of the Key-Value Cache for Disaggregated LLM Inference** | SIGCOMM 2025 | KV cache / disaggregated LLM serving / quantization | [Link](https://arxiv.org/abs/2502.03589) | — |
| **MegaScale-Infer: Efficient Mixture-of-Experts Model Serving with Disaggregated Expert Parallelism** | SIGCOMM 2025 | MoE serving / disaggregated expert parallelism / networking | [Link](https://arxiv.org/abs/2504.02263) | — |
| **ResCCL: Resource-Efficient Scheduling for Collective Communication** | SIGCOMM 2025 | distributed training / collective communication / GPU resource scheduling | [Link](https://doi.org/10.1145/3718958.3750514) | — |
| **SyCCL: Exploiting Symmetry for Efficient Collective Communication Scheduling** | SIGCOMM 2025 | distributed ML training / collective communication schedule synthesis | [Link](https://doi.org/10.1145/3718958.3750499) | [Repo](https://github.com/aliyun/syccl) |
| **100x Cost & Latency Reduction: Performance Analysis of AI Query Approximation using Lightweight Proxy Models** | SIGMOD 2026 | AI query systems / LLM cost and latency reduction / proxy-model acceleration | [Link](https://arxiv.org/abs/2603.15970) | — |
| **AlignedServe: Orchestrating Prefix-aware Batching to Build a High-throughput and Computing-efficient LLM Serving System** | SIGMOD 2026 | LLM serving / prefix-aware batching / KV scheduling | [Link](https://arxiv.org/abs/2605.23389) | — |
| **Beluga: A CXL-Based Memory Architecture for Scalable and Efficient LLM KVCache Management** | SIGMOD 2026 | CXL memory / KV-cache serving | [Link](https://arxiv.org/abs/2511.20172) | — |
| **Efficient LLM Serving for Agentic Workflows: A Data Systems Perspective** | SIGMOD 2026 | agentic LLM serving / workflow-aware caching / cache-aware scheduling | [Link](https://arxiv.org/abs/2603.16104) | [Repo](https://github.com/MachineLearningSystem/26SIGMOD-helium_demo) |
| **HotPrefix: Hotness-Aware KV Cache Scheduling for Efficient Prefix Sharing in LLM Inference Systems** | SIGMOD 2026 | prefix KV-cache scheduling / LLM serving | [Link](https://doi.org/10.1145/3749168) | — |
| **Serving Hybrid LLM Loads with SLO Guarantees Using CPU-GPU Attention Piggybacking** | SIGMOD 2026 | LLM serving / heterogeneous CPU-GPU / SLO scheduling | [Link](https://arxiv.org/abs/2603.12831) | — |
| **SG-Serve: Efficient Model Serving for Subgraph-based Graph Representation Learning** | SIGMOD 2026 | graph model serving / tail-latency optimization / workload-aware GPU batching | [Link](https://doi.org/10.1145/3786697) | — |
| **Medha** | SoCC 2026 | KV virtualization + long-context serving + GPU colocation + on-device adaptation | — | — |
| **Memory-Decoupled Layer-Wise Fine-Tuning** | SoCC 2026 | KV virtualization + long-context serving + GPU colocation + on-device adaptation | — | — |
| **MosaicKV: SLO-Aware KV Cache Virtualization for Efficient LLM Serving** | SoCC 2026 | KV virtualization + long-context serving + GPU colocation + on-device adaptation | [Link](https://arxiv.org/abs/2607.00760) | — |
| **No Request Left Behind: Tackling Heterogeneity in Long-Context LLM Inference with Medha** | SoCC 2026 | KV virtualization + long-context serving + GPU colocation + on-device adaptation | [Link](https://arxiv.org/abs/2409.17264) | — |
| **On Evaluating Performance of LLM Inference Serving Systems** | SoCC 2026 | LLM serving / evaluation methodology / systems benchmarking | [Link](https://arxiv.org/abs/2507.09019) | — |
| **PEACE: Power and Performance Aware Colocation for Efficient GPU Spatial Partitioning** | SoCC 2026 | KV virtualization + long-context serving + GPU colocation + on-device adaptation | [Link](https://doi.org/10.1145/3815789.3827949) | — |
| **Aegaeon: Effective GPU Pooling for Concurrent LLM Serving on the Market** | SOSP 2025 | LLM serving / KV / GPU systems | — | — |
| **DiffKV: Differentiated Memory Management for Large Language Models with Parallel KV Compaction** | SOSP 2025 | LLM serving / KV / GPU systems | — | — |
| **HedraRAG: Co-Optimizing Generation and Retrieval for Heterogeneous RAG Workflows** | SOSP 2025 | RAG serving / generation-retrieval co-optimization | [Link](https://doi.org/10.1145/3731569.3764806) | — |
| **IC-Cache: Efficient Large Language Model Serving via In-context Caching** | SOSP 2025 | LLM serving / KV / GPU systems | — | — |
| **Jenga: Effective Memory Management for Serving LLM with Heterogeneity** | SOSP 2025 | LLM serving / KV / GPU systems | — | — |
| **KTransformers: Unleashing the Full Potential of CPU/GPU Hybrid Inference for MoE Models** | SOSP 2025 | LLM serving / KV / GPU systems | — | — |
| **Mercury: Unlocking Multi-GPU Operator Optimization for LLMs via Remote Memory Scheduling** | SOSP 2025 | LLM serving / KV / GPU systems | — | — |
| **METIS: Fast Quality-Aware RAG Systems with Configuration Adaptation** | SOSP 2025 | RAG serving / adaptive configuration / scheduling | [Link](https://arxiv.org/abs/2412.10543) | — |
| **Pie: A Programmable Serving System for Emerging LLM Applications** | SOSP 2025 | LLM serving / KV / GPU systems | [Link](https://arxiv.org/abs/2510.24051) | — |
| **PrefillOnly: An Inference Engine for Prefill-only Workloads in Large Language Model Applications** | SOSP 2025 | LLM serving / KV / GPU systems | [Link](https://arxiv.org/abs/2505.07203) | — |
| **Adaptive Model and Strategy Routing for Cost-Efficient LLM Services** | The Web Conference 2026 | LLM serving / model routing / reasoning cost efficiency | [Link](https://arxiv.org/abs/2505.19435) | — |
| **Fate: Fast Edge Inference of Mixture-of-Experts Models via Cross-Layer Gate** | The Web Conference 2026 | edge MoE inference / expert prefetch | [Link](https://arxiv.org/abs/2502.12224) | — |
| **LaTune: Lightweight and Adaptive Configuration Tuning for LLM Inference on Edge Devices** | The Web Conference 2026 | edge LLM runtime tuning | [Link](https://doi.org/10.1145/3774904.3792382) | — |
| **Task-Aware Cloud-End Offloading for Vision-Language Model Serving via Dynamic Modality-Specific Adapter Scheduling** | The Web Conference 2026 | multimodal/VLM serving / cloud-edge offloading | [Link](https://doi.org/10.1145/3774904.3792127) | — |
| **Colocating ML Inference and Training with Fast GPU Memory Handover** | USENIX ATC 2025 | GPU inference-training colocation / elastic GPU memory handover | — | — |
| **DEEPSERVE: Serverless Large Language Model Serving at Scale** | USENIX ATC 2025 | LLM serving / serverless NPU cloud / disaggregated serving | — | — |
| **GMI-DRL: Empowering Multi-GPU DRL with Adaptive-Grained Parallelism** | USENIX ATC 2025 | distributed DRL training / multi-GPU adaptive-grained parallelism / GPU multiplexing | — | — |
| **Katz** | USENIX ATC 2025 | production KV-cache + quantized-kernel compiler + diffusion workflow serving | — | — |
| **KVCache Cache in the Wild** | USENIX ATC 2025 | production KV-cache + quantized-kernel compiler + diffusion workflow serving | — | — |
| **mTuner: Accelerating Parameter-Efficient Fine-Tuning on Multi-GPU Servers with Elastic Tensor** | USENIX ATC 2025 | LLM PEFT / multi-GPU fine-tuning / dynamic tensor memory management | — | [Repo](https://github.com/xxcclong/mTuner) |
| **Optimus: Accelerating Large-Scale Multi-Modal LLM Training by Bubble Exploitation** | USENIX ATC 2025 | multimodal LLM training / distributed training / pipeline bubble exploitation | [Link](https://arxiv.org/abs/2408.03505) | — |
| **PPipe: Efficient Video Analytics Serving on Heterogeneous GPU Clusters via Pool-Based Pipeline Parallelism** | USENIX ATC 2025 | heterogeneous GPU inference serving / pipeline parallelism | — | — |
| **QFactory** | USENIX ATC 2025 | production KV-cache + quantized-kernel compiler + diffusion workflow serving | — | — |
| **Resource Multiplexing in Tuning and Serving Large Language Models** | USENIX ATC 2025 | LLM tuning+serving colocation / scheduling | — | — |
| **Toppings: CPU-Assisted, Rank-Aware Adapter Serving for LLM Inference** | USENIX ATC 2025 | LoRA serving / heterogeneous CPU-GPU scheduling | — | — |
| **Torpor: GPU-Enabled Serverless Computing for Low-Latency, Resource-Efficient Inference** | USENIX ATC 2025 | serverless GPU inference / model swapping / scheduling | — | — |
| **Weaver: Efficient Multi-LLM Serving with Attention Offloading** | USENIX ATC 2025 | multi-LLM serving / attention offloading | — | — |
| **BigVectorBench: Heterogeneous Data Embedding and Compound Queries are Essential in Evaluating Vector Databases** | VLDB/PVLDB Volume 18 | vector database benchmark / RAG infrastructure / heterogeneous embeddings | [Link](https://doi.org/10.14778/3718057.3718078) | [Repo](https://github.com/BenchCouncil/BigVectorBench) |
| **Chameleon: a Heterogeneous and Disaggregated Accelerator System for Retrieval-Augmented Language Models** | VLDB/PVLDB Volume 18 | RAG acceleration / heterogeneous disaggregated system | [Link](https://arxiv.org/abs/2310.09949) | — |
| **ContextCache: Context-Aware Semantic Cache for Multi-Turn Queries in Large Language Models** | VLDB/PVLDB Volume 18 | LLM serving / semantic cache / multi-turn inference | — | — |
| **Algorithm-Architecture Co-Design for Efficient VLA Inference via Speculative Inference and Verification** | Fresh / preprint | VLA speculative inference / algorithm-architecture co-design | [Link](https://arxiv.org/abs/2608.15636) | — |
| **Beyond Capacity: Scalable MoE LLM Inference via High-Bandwidth Flash with Direct GPU and HBM Paths** | Fresh / preprint | MoE serving / high-bandwidth flash architecture | [Link](https://arxiv.org/abs/2608.14333) | — |
| **CoRun: Padding is Simple and Efficient for Deterministic LLM Inference** | Fresh / preprint | LLM serving / deterministic inference / fixed-shape scheduling | [Link](https://arxiv.org/abs/2608.14376) | — |
| **EcoVLA: Energy-Efficient Device-Edge Co-Inference for Vision-Language-Action Models under Real-Time Constraints** | Fresh / preprint | VLA device-edge co-inference / energy-aware runtime | [Link](https://arxiv.org/abs/2608.15502) | — |
| **Every Expert Counts: ExactMoE for Memory-Efficient W4A16 Inference** | Fresh / preprint | MoE memory-efficient W4A16 inference / GPU slot cache | [Link](https://arxiv.org/abs/2608.15383) | — |
| **FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution** | Fresh / preprint | edge MoE serving | [Link](https://arxiv.org/abs/2608.16157) | — |
| **From LLM Inference to Agentic Workloads: Characterization and Implications for Serving Systems** | Fresh / preprint | agentic serving characterization / systems benchmark | [Link](https://arxiv.org/abs/2608.15127) | — |
| **Global Simulation-Guided Dynamic Operator Scheduling for Efficient Multi-Tenant Model Serving** | Fresh / preprint | multi-tenant model serving / operator-level scheduling | [Link](https://arxiv.org/abs/2608.15762) | — |
| **GraniKV: Asymmetric Granularity KV-Cache Paging for Multi-Agent Systems with Long Shared Prefix** | Fresh / preprint | KV-cache paging / multi-agent serving | [Link](https://arxiv.org/abs/2608.15584) | — |
| **Pallas: A Proactive KV Cache Migration Framework for LLM Inference in AI-RAN** | Fresh / preprint | LLM serving / KV cache / edge | [Link](https://arxiv.org/abs/2608.16477) | — |
| **Pre-Compiled Pipeline Shards for Distributed LLM Inference on Intel AI PC Fleets** | Fresh / preprint | distributed LLM inference / edge AI PC fleet / speculative decoding | [Link](https://arxiv.org/abs/2608.19147) | [Repo](https://github.com/labscommunity/pipeline-sharded-inference-paper) |
| **TEMPO: Makespan-Aware Expert-Parallel Load Balancing Across Memory- and Compute-Bound Regimes** | Fresh / preprint | MoE expert-parallel load balancing / serving | [Link](https://arxiv.org/abs/2608.13057) | — |
| **TideRL: Boosting Agentic RL Goodput with Readiness-Aware Scheduling** | Fresh / preprint | agentic RL infrastructure | [Link](https://arxiv.org/abs/2608.10402) | — |
| **TileMix: Tile-Centric Mixed-Precision Attention for LLM Inference Acceleration** | Fresh / preprint | mixed-precision attention kernel / long-context inference | [Link](https://arxiv.org/abs/2608.17336) | — |
