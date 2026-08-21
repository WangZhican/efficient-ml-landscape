# 15 · Edge / Cloud / Heterogeneous AI

> **127 papers** currently mapped to this direction. Cross-direction duplication is intentional when a paper has multiple technical roles.

[← Research Map](README.md) · [Complete Paper List](ALL_PAPERS.md)

| Paper | Venue | Topic | Paper | Code |
|---|---|---|---|---|
| **Accelerating LLM Inference Throughput via Asynchronous KV Cache Prefetching** | AAAI 2026 | LLM inference / KV cache prefetch / GPU memory hierarchy | [Link](https://doi.org/10.1609/aaai.v40i25.39224) | — |
| **DIAA: A Decoding-Efficient Inference Acceleration Approach for On-Device Large Language Models** | AAAI 2026 | on-device LLM / speculative decoding / edge inference | [Link](https://doi.org/10.1609/aaai.v40i31.39789) | — |
| **TimeBill: Time-Budgeted Inference for Large Language Models** | AAAI 2026 | LLM inference / time budget / adaptive KV eviction | [Link](https://doi.org/10.1609/aaai.v40i36.40317) | — |
| **EfficientLLM: Unified Pruning-Aware Pretraining for Auto-Designed Compact Language Models** | ACL 2026 | pruning / compact edge LLM | [Link](https://doi.org/10.18653/v1/2026.acl-long.355) | — |
| **MoE-APEX: An Efficient MoE Inference System with Adaptive Precision Expert Offloading** | ASPLOS 2026 | edge MoE inference / expert offloading / mixed precision | [Link](https://doi.org/10.1145/3779212.3790187) | — |
| **PF-LLM: Large Language Model Hinted Hardware Prefetching** | ASPLOS 2026 | LLM inference / hardware prefetching | — | — |
| **REPA: Reconfigurable PIM for the Joint Acceleration of KV Cache Offloading and Processing** | ASPLOS 2026 | KV cache / PIM acceleration | [Link](https://doi.org/10.1145/3779212.3790212) | — |
| **STARC: Selective Token Access with Remapping and Clustering for Efficient LLM Decoding on PIM Systems** | ASPLOS 2026 | sparse attention / PIM / KV cache | [Link](https://doi.org/10.1145/3779212.3790226) | — |
| **TetriServe: Efficiently Serving Mixed DiT Workloads** | ASPLOS 2026 | diffusion/DiT serving / scheduling | [Link](https://arxiv.org/abs/2510.01565) | — |
| **Mixture of Attention Spans: Optimizing LLM Inference Efficiency with Heterogeneous Sliding-Window Lengths** | COLM 2025 | sparse attention / long-context inference / KV cache compression | [Link](https://arxiv.org/abs/2406.14909) | [Repo](https://github.com/thu-nics/MoA) |
| **OverFill: Two-Stage Models for Efficient Language Model Decoding** | COLM 2025 | efficient LLM decoding / stage-specialized model | [Link](https://arxiv.org/abs/2508.08446) | — |
| **PredGen: Accelerated Inference of Large Language Models through Input-Time Speculation for Real-Time Speech Interaction** | COLM 2025 | speculative decoding / real-time speech interaction / input-time speculation | [Link](https://arxiv.org/abs/2506.15556) | — |
| **Resource-efficient Inference with Foundation Model Programs** | COLM 2025 | agentic inference / multimodal serving / dynamic model routing | [Link](https://arxiv.org/abs/2504.07247) | [Repo](https://github.com/Flitternie/FMProgramming) |
| **Accelerating Diffusion-based Video Editing via Heterogeneous Caching: Beyond Full Computing at Sampled Denoising Timestep** | CVPR 2026 | video diffusion editing / heterogeneous caching | — | — |
| **AttenPIM: Accelerating LLM Attention with Dual-mode GEMV in Processing-in-Memory** | DAC 2025 | LLM attention acceleration / processing-in-memory / dual-mode GEMV | [Link](https://doi.org/10.1109/DAC63849.2025.11133230) | — |
| **HybriMoE: Hybrid CPU-GPU Scheduling and Cache Management for Efficient MoE Inference** | DAC 2025 | MoE inference / hybrid CPU-GPU scheduling / expert prefetch and cache management | [Link](https://arxiv.org/abs/2504.05897) | [Repo](https://github.com/PKU-SEC-Lab/HybriMoE) |
| **ReaLM: Reliable and Efficient Large Language Model Inference with Statistical Algorithm-Based Fault Tolerance** | DAC 2025 | reliable and energy-efficient LLM inference / statistical ABFT / algorithm-circuit co-design | [Link](https://arxiv.org/abs/2503.24053) | [Repo](https://github.com/PKU-SEC-Lab/ReaLM_DAC25) |
| **BK-SDM: A Lightweight, Fast, and Cheap Version of Stable Diffusion** | ECCV 2024 | diffusion pruning / compact model | — | — |
| **Dovetail: A CPU/GPU Heterogeneous Speculative Decoding for LLM inference** | EMNLP 2025 | heterogeneous CPU/GPU inference / speculative decoding | [Link](https://doi.org/10.18653/v1/2025.emnlp-main.879) | — |
| **Cache Saver: A Modular Framework for Efficient, Affordable, and Reproducible LLM Inference** | EMNLP 2025 Findings | LLM inference framework / response caching / cost and carbon efficiency | [Link](https://doi.org/10.18653/v1/2025.findings-emnlp.1402) | [Repo](https://github.com/au-clan/cachesaver) |
| **Hardware-Aware Parallel Prompt Decoding for Memory-Efficient Acceleration of LLM Inference** | EMNLP 2025 Findings | speculative decoding / edge LLM / memory-efficient inference | [Link](https://doi.org/10.18653/v1/2025.findings-emnlp.120) | — |
| **AdaServe: Accelerating Multi-SLO LLM Serving with SLO-Customized Speculative Decoding** | EuroSys 2026 | LLM serving / speculative decoding / multi-SLO | — | — |
| **Scaling LLM Test-Time Compute with Mobile NPU on Smartphones** | EuroSys 2026 | on-device LLM reasoning / mobile NPU / hardware-aware quantization | [Link](https://arxiv.org/abs/2509.23324) | — |
| **TailorLLM: Collaborative End-Cloud Inference of Large and Small Language Models Based on Low-Rank Adaptation** | EuroSys 2026 | edge/cloud LLM inference / collaborative serving / LoRA | — | — |
| **CXL-SpecKV: A Disaggregated FPGA Speculative KV-Cache for Datacenter LLM Serving** | FPGA 2026 | LLM serving / CXL / FPGA / speculative KV cache | [Link](https://arxiv.org/abs/2512.11920) | [Repo](https://github.com/FastLM/CXL-SpecKV) |
| **TeLLMe: An Efficient End-to-End Ternary LLM Prefill and Decode Accelerator with Table-Lookup Matmul on Edge FPGAs** | FPGA 2026 | edge LLM inference / ternary accelerator / FPGA | [Link](https://arxiv.org/abs/2510.15926) | [Repo](https://github.com/UCI-CORSA/TeLLMe_FPGA_2026) |
| **Adaptive Draft Sequence Length** | HPCA 2026 | efficient VLM + PIM inference + reasoning accelerator + speculative decoding | — | — |
| **AQPIM: Breaking the PIM Capacity Wall for LLMs with In-Memory Activation Quantization** | HPCA 2026 | PIM / activation quantization / long-context LLM | [Link](https://arxiv.org/abs/2604.18137) | — |
| **AutoHAAP: Automated Heterogeneity-Aware Asymmetric Partitioning for LLM Training** | HPCA 2026 | heterogeneous distributed LLM training / partition search | [Link](https://doi.org/10.1109/HPCA68181.2026.11408533) | — |
| **Focus** | HPCA 2026 | efficient VLM + PIM inference + reasoning accelerator + speculative decoding | — | — |
| **LILo: Harnessing the On-chip Accelerators in Intel CPUs for Compressed LLM Inference Acceleration** | HPCA 2026 | compressed CPU LLM inference / Intel IAA-AMX-AVX co-execution | [Link](https://doi.org/10.1109/HPCA68181.2026.11408577) | — |
| **LoCaLUT** | HPCA 2026 | efficient VLM + PIM inference + reasoning accelerator + speculative decoding | — | — |
| **PIMphony** | HPCA 2026 | efficient VLM + PIM inference + reasoning accelerator + speculative decoding | — | — |
| **RPU** | HPCA 2026 | efficient VLM + PIM inference + reasoning accelerator + speculative decoding | — | — |
| **Towards Resource-Efficient Serverless LLM Inference with SLINFER** | HPCA 2026 | serverless LLM serving / heterogeneous CPU-GPU sharing | [Link](https://arxiv.org/abs/2507.00507) | — |
| **FreeKV: Boosting KV Cache Retrieval for Efficient LLM Inference** | ICLR 2026 | KV cache retrieval / CPU-GPU hybrid memory / long-context inference | [Link](https://arxiv.org/abs/2505.13109) | — |
| **DLP: Dynamic Layerwise Pruning in Large Language Models** | ICML 2025 | LLM pruning | — | — |
| **QuantSpec: Self-Speculative Decoding with Hierarchical Quantized KV Cache** | ICML 2025 | speculative decoding / KV quantization | — | — |
| **OServe: Accelerating LLM Serving via Spatial-Temporal Workload Orchestration** | ICML 2026 | LLM serving / heterogeneous deployment / scheduling | [Link](https://arxiv.org/abs/2602.12151) | — |
| **Understand and Accelerate Memory Processing Pipeline for Large Language Model Inference** | ICML 2026 | LLM memory processing / GPU-FPGA heterogeneous acceleration | [Link](https://arxiv.org/abs/2603.29002) | — |
| **LightPlanner: Unleashing the Reasoning Capabilities of Lightweight Large Language Models in Task Planning** | IROS 2025 | edge-efficient embodied task planning / lightweight LLM / long-horizon memory | [Link](https://arxiv.org/abs/2503.08508) | [Repo](https://github.com/jetteezhou/LightPlanner) |
| **Bridging Efficiency and Scalability in LLM System via 3D Hybrid PIM with 2D In-Transit Computation** | ISCA 2026 | LLM inference accelerator / hybrid PIM / in-transit computation | — | — |
| **Cassandra: Enabling Reasoning LLMs at Edge via Self-Speculative Decoding** | ISCA 2026 | edge speculative reasoning + quantization + memory-system + generative inference accelerators | [Link](https://arxiv.org/abs/2605.26558) | — |
| **CHIME: A Case for Efficient Long-Context Attention-FC Disaggregated Inference with DIMM-PIM** | ISCA 2026 | long-context LLM / disaggregated inference / PIM | — | — |
| **DIAMoND: Dynamic Inference for Adaptive Edge MoE with Heterogeneous In-NAND and Near-DRAM Compute Architecture** | ISCA 2026 | edge MoE / heterogeneous memory / adaptive inference | — | — |
| **DynoPipe: Heterogeneous Edge-Cloud LLM Serving with Dynamically Orchestrated Pipeline Boundaries** | ISCA 2026 | edge-cloud LLM serving / heterogeneous pipeline | — | — |
| **Early Silicon of Raptor: The First 3D-DRAM Accelerator for Generative Inference** | ISCA 2026 | generative inference accelerator / 3D DRAM | — | — |
| **ENEC: A Lossless AI Model Compression Method Enabling Fast Inference on Ascend NPUs** | ISCA 2026 | lossless model compression / NPU inference | — | — |
| **HybridSpec: Exploiting Hybrid-bonding Memory to Accelerate LLM Serving through Heterogeneous Architecture and Speculative Decoding** | ISCA 2026 | speculative decoding / heterogeneous memory / LLM serving | — | — |
| **MLX: Multi-Layer Execution for Structured LLM Workload Acceleration on Spatial Architectures** | ISCA 2026 | LLM workload accelerator / spatial architecture / multi-layer execution | — | — |
| **OASIS: Outlier-Aware LUT-Based GEMM with Dual-Side Quantization for LLM Inference Acceleration** | ISCA 2026 | edge speculative reasoning + quantization + memory-system + generative inference accelerators | — | — |
| **P3-LLM: An Integrated NPU-PIM Accelerator for Edge LLM Inference Using Hybrid Numerical Formats** | ISCA 2026 | edge LLM / PIM / mixed precision | [Link](https://arxiv.org/abs/2511.06838) | — |
| **Raptor** | ISCA 2026 | edge speculative reasoning + quantization + memory-system + generative inference accelerators | — | — |
| **SHyLA: 3D-Stacked NVM-DRAM Hybrid LLM-Inference Architecture Exploiting Data and Memory Heterogeneity** | ISCA 2026 | edge speculative reasoning + quantization + memory-system + generative inference accelerators | — | — |
| **SMoE: An Algorithm-System Co-Design for Pushing MoE to the Edge via Expert Substitution** | ISCA 2026 | edge MoE / algorithm-system co-design | — | — |
| **SMOOTH: Hardware-Assisted Fine-Grained On-Chip Memory Management for Efficient On-Device LLM Inference** | ISCA 2026 | edge speculative reasoning + quantization + memory-system + generative inference accelerators | — | — |
| **XtraMAC: An Efficient MAC Architecture for Mixed-Precision LLM Inference on FPGA** | ISCA 2026 | mixed-precision LLM / FPGA accelerator | — | — |
| **Spyre: An inference-optimized scalable AI accelerator for enterprise workloads** | ISSCC 2026 | AI accelerator / enterprise inference | [Link](https://doi.org/10.1109/ISSCC49663.2026.11409090) | — |
| **Enhancing Learned Knowledge in LoRA Adapters Through Efficient Contrastive Decoding on Ascend NPUs** | KDD 2025 | LLM decoding / LoRA / Ascend NPU kernel optimization | [Link](https://arxiv.org/abs/2505.14620) | — |
| **DECA: A Near-Core LLM Decompression Accelerator Grounded on a 3D Roofline Model** | MICRO 2025 | LLM inference / decompression accelerator | — | — |
| **HLX** | MICRO 2025 | MoE + diffusion + tensor compression + hybrid LM + reasoning + edge training acceleration | — | — |
| **Kelle: Co-design KV Caching and eDRAM for Efficient LLM Serving in Edge Computing** | MICRO 2025 | edge LLM serving / KV cache / eDRAM co-design | [Link](https://arxiv.org/abs/2510.16040) | — |
| **LLM.265** | MICRO 2025 | MoE + diffusion + tensor compression + hybrid LM + reasoning + edge training acceleration | — | — |
| **LongSight: Compute-Enabled Memory to Accelerate Large-Context LLMs via Sparse Attention** | MICRO 2025 | long-context LLM / sparse attention / CXL memory | [Link](https://doi.org/10.1145/3725843.3756062) | — |
| **ORCHES** | MICRO 2025 | MoE + diffusion + tensor compression + hybrid LM + reasoning + edge training acceleration | — | — |
| **Pimba: A Processing-in-Memory Acceleration for Post-Transformer Large Language Model Serving** | MICRO 2025 | post-transformer LLM serving / PIM / low precision | [Link](https://arxiv.org/abs/2507.10178) | — |
| **REACT3D** | MICRO 2025 | MoE + diffusion + tensor compression + hybrid LM + reasoning + edge training acceleration | — | — |
| **S-DMA** | MICRO 2025 | MoE + diffusion + tensor compression + hybrid LM + reasoning + edge training acceleration | — | — |
| **Stratum** | MICRO 2025 | MoE + diffusion + tensor compression + hybrid LM + reasoning + edge training acceleration | — | — |
| **StreamTensor: Make Tensors Stream in Dataflow Accelerators for LLMs** | MICRO 2025 | LLM accelerator / dataflow | — | — |
| **Efficient, VRAM-Constrained xLM Inference on Clients** | MLSys 2026 | client LLM/VLM inference / CPU-GPU hybrid runtime / Physical AI | — | — |
| **IntAttention: A Fully Integer Attention Pipeline for Efficient Edge Inference** | MLSys 2026 | edge inference / integer attention | — | — |
| **ProfInfer: An eBPF-based Fine-Grained LLM Inference Profiler** | MLSys 2026 | LLM inference profiling / edge runtime observability | — | — |
| **D2MoE: Dual Routing and Dynamic Scheduling for Efficient On-Device MoE-based LLM Serving** | MobiCom 2025 | on-device MoE serving / dynamic scheduling | [Link](https://doi.org/10.1145/3680207.3723493) | — |
| **Elastic On-Device LLM Service** | MobiCom 2025 | on-device LLM service / elastic model and prompt adaptation | [Link](https://arxiv.org/abs/2409.09071) | — |
| **LLM-Explorer: Towards Efficient and Affordable LLM-based Exploration for Mobile Apps** | MobiCom 2025 | mobile agent / efficient LLM usage | [Link](https://arxiv.org/abs/2505.10593) | — |
| **Modality Plug-and-Play: Runtime Modality Adaptation in LLM-Driven Autonomous Mobile Systems** | MobiCom 2025 | Physical AI / multimodal edge runtime / efficient modality adaptation | [Link](https://doi.org/10.1145/3680207.3723491) | [Repo](https://github.com/pittisl/mPnP-LLM) |
| **Knowing When to Stop: Efficient Context Processing via Latent Sufficiency Signals** | NeurIPS 2025 | efficient context processing / adaptive cutoff | [Link](https://doi.org/10.52202/085713-1376) | — |
| **SpecEdge: Scalable Edge-Assisted Serving Framework for Interactive LLMs** | NeurIPS 2025 | edge-cloud LLM serving / speculative decoding | — | — |
| **Cortex: Achieving Low-Latency, Cost-Efficient Remote Data Access For LLM via Semantic-Aware Knowledge Caching** | NSDI 2026 | agent systems / semantic knowledge caching | — | — |
| **ZipLLM: Efficient LLM Storage via Model-Aware Synergistic Data Deduplication and Compression** | NSDI 2026 | LLM storage / model deduplication / compression | — | — |
| **No Buffer, No Bottleneck: Efficient Zero-Copy KV Cache Offloading for Long-Context LLMs** | OSDI 2026 | LLM serving / KV cache offloading / heterogeneous CPU-GPU memory | — | — |
| **Elastor: Elastic and Efficient Model Partitioning and Checkpointing for Fault-Tolerant Distributed Training** | PPoPP 2026 | distributed training / elastic checkpointing | [Link](https://doi.org/10.1145/3774934.3786445) | — |
| **Mimic Intent, Not Just Trajectories** | RSS 2026 | Physical AI / spectral action tokenization / efficient autoregressive policy | [Link](https://arxiv.org/abs/2602.08602) | — |
| **OAT: Ordered Action Tokenization** | RSS 2026 | Physical AI / action tokenization / anytime inference | [Link](https://arxiv.org/abs/2602.04215) | — |
| **Hetis: Serving LLMs in Heterogeneous GPU Clusters with Fine-grained and Dynamic Parallelism** | SC 2025 | LLM serving / heterogeneous GPU / dynamic parallelism | [Link](https://arxiv.org/abs/2509.08309) | — |
| **Machine Learning-Guided Memory Optimization for DLRM Inference on Tiered Memory** | SC 2025 | DLRM inference / tiered memory / ML-guided caching-prefetching | [Link](https://arxiv.org/abs/2511.08568) | — |
| **Astral: A Datacenter Infrastructure for Large Language Model Training at Scale** | SIGCOMM 2025 | large-scale LLM training infrastructure / datacenter network / monitoring / performance forecasting | [Link](https://doi.org/10.1145/3718958.3750521) | — |
| **Beluga: A CXL-Based Memory Architecture for Scalable and Efficient LLM KVCache Management** | SIGMOD 2026 | CXL memory / KV-cache serving | [Link](https://arxiv.org/abs/2511.20172) | — |
| **Serving Hybrid LLM Loads with SLO Guarantees Using CPU-GPU Attention Piggybacking** | SIGMOD 2026 | LLM serving / heterogeneous CPU-GPU / SLO scheduling | [Link](https://arxiv.org/abs/2603.12831) | — |
| **Medha** | SoCC 2026 | KV virtualization + long-context serving + GPU colocation + on-device adaptation | — | — |
| **Memory-Decoupled Layer-Wise Fine-Tuning** | SoCC 2026 | KV virtualization + long-context serving + GPU colocation + on-device adaptation | — | — |
| **MosaicKV: SLO-Aware KV Cache Virtualization for Efficient LLM Serving** | SoCC 2026 | KV virtualization + long-context serving + GPU colocation + on-device adaptation | [Link](https://arxiv.org/abs/2607.00760) | — |
| **No Request Left Behind: Tackling Heterogeneity in Long-Context LLM Inference with Medha** | SoCC 2026 | KV virtualization + long-context serving + GPU colocation + on-device adaptation | [Link](https://arxiv.org/abs/2409.17264) | — |
| **PEACE: Power and Performance Aware Colocation for Efficient GPU Spatial Partitioning** | SoCC 2026 | KV virtualization + long-context serving + GPU colocation + on-device adaptation | [Link](https://doi.org/10.1145/3815789.3827949) | — |
| **Characterizing Mobile SoC for Accelerating Heterogeneous LLM Inference** | SOSP 2025 | on-device LLM inference / heterogeneous GPU-NPU mobile SoC | [Link](https://arxiv.org/abs/2501.14794) | — |
| **DCP: Addressing Input Dynamism In Long-Context Training via Dynamic Context Parallelism** | SOSP 2025 | long-context LLM training / dynamic context parallelism | [Link](https://arxiv.org/abs/2510.10620) | [Repo](https://github.com/chenyu-jiang/dcp) |
| **HedraRAG: Co-Optimizing Generation and Retrieval for Heterogeneous RAG Workflows** | SOSP 2025 | RAG serving / generation-retrieval co-optimization | [Link](https://doi.org/10.1145/3731569.3764806) | — |
| **Sailor: Automating Distributed Training over Dynamic, Heterogeneous, and Geo-distributed Clusters** | SOSP 2025 | distributed training / heterogeneous clusters / geo-distributed systems | [Link](https://arxiv.org/abs/2504.17096) | [Repo](https://github.com/eth-easl/sailor) |
| **EcoTune: Edge-Cloud Collaborative Model Adaptation for Budget-Constrained On-Device SLM Personalization** | The Web Conference 2026 | edge-cloud collaborative LLM adaptation / on-device SLM personalization / resource-efficient fine-tuning | — | — |
| **Energy-Efficient and Dequantization-Free Quantization of LLMs: A Spiking Neural Network Approach to Salient Value Mitigation** | The Web Conference 2026 | LLM quantization / edge energy efficiency / SNN | [Link](https://arxiv.org/abs/2510.19498) | — |
| **Fate: Fast Edge Inference of Mixture-of-Experts Models via Cross-Layer Gate** | The Web Conference 2026 | edge MoE inference / expert prefetch | [Link](https://arxiv.org/abs/2502.12224) | — |
| **HeteroSim: Towards High-Fidelity Heterogeneous LLM Training Simulation on GPUs** | The Web Conference 2026 | heterogeneous LLM training / systems simulation | [Link](https://doi.org/10.1145/3774904.3792254) | — |
| **LaTune: Lightweight and Adaptive Configuration Tuning for LLM Inference on Edge Devices** | The Web Conference 2026 | edge LLM runtime tuning | [Link](https://doi.org/10.1145/3774904.3792382) | — |
| **MASI: Memory-Adaptive Inference Framework for Spiking Neural Networks on Edge Devices** | The Web Conference 2026 | edge AI inference / memory-adaptive runtime / SNN | [Link](https://doi.org/10.1145/3774904.3792136) | — |
| **Self-Speculative Decoding for On-device MoE Acceleration** | The Web Conference 2026 | on-device MoE / speculative decoding | [Link](https://doi.org/10.1145/3774904.3792218) | — |
| **Task-Aware Cloud-End Offloading for Vision-Language Model Serving via Dynamic Modality-Specific Adapter Scheduling** | The Web Conference 2026 | multimodal/VLM serving / cloud-edge offloading | [Link](https://doi.org/10.1145/3774904.3792127) | — |
| **CLONE: Customizing LLMs for Efficient Latency-Aware Inference at the Edge** | USENIX ATC 2025 | edge LLM / algorithm-hardware co-design | — | — |
| **DEEPSERVE: Serverless Large Language Model Serving at Scale** | USENIX ATC 2025 | LLM serving / serverless NPU cloud / disaggregated serving | — | — |
| **PPipe: Efficient Video Analytics Serving on Heterogeneous GPU Clusters via Pool-Based Pipeline Parallelism** | USENIX ATC 2025 | heterogeneous GPU inference serving / pipeline parallelism | — | — |
| **Toppings: CPU-Assisted, Rank-Aware Adapter Serving for LLM Inference** | USENIX ATC 2025 | LoRA serving / heterogeneous CPU-GPU scheduling | — | — |
| **Chameleon: a Heterogeneous and Disaggregated Accelerator System for Retrieval-Augmented Language Models** | VLDB/PVLDB Volume 18 | RAG acceleration / heterogeneous disaggregated system | [Link](https://arxiv.org/abs/2310.09949) | — |
| **GaussDB-Vector: A Large-Scale Persistent Real-Time Vector Database for LLM Applications** | VLDB/PVLDB Volume 18 | vector database / LLM applications / retrieval systems | — | — |
| **HAKES: Scalable Vector Database for Embedding Search Service** | VLDB/PVLDB Volume 18 | vector database / RAG retrieval infrastructure | [Link](https://arxiv.org/abs/2505.12524) | — |
| **Magnus: A Holistic Approach to Data Management for Large-Scale Machine Learning Workloads** | VLDB/PVLDB Volume 18 | ML data systems / large-scale training infrastructure | — | — |
| **Silicon-Oracle (Soracle): A Multi-Modal Autoregressive Model Accelerator for Context-Aware Assistance on Mobile Platform** | VLSI Symposium 2026 | multimodal autoregressive accelerator / mobile inference | [Link](https://doi.org/10.1109/VLSITechnologyandCir65830.2026.11577228) | — |
| **Sirius: A Dual-Chiplet System for Multimodal Embodied AI with Heterogeneous RVV Cores, Dense and Sparse Accelerators** | VLSI Symposium 2026 | Physical AI / multimodal embodied edge accelerator | [Link](https://doi.org/10.1109/VLSITechnologyandCir65830.2026.11577229) | — |
| **Algorithm-Architecture Co-Design for Efficient VLA Inference via Speculative Inference and Verification** | Fresh / preprint | VLA speculative inference / algorithm-architecture co-design | [Link](https://arxiv.org/abs/2608.15636) | — |
| **EcoVLA: Energy-Efficient Device-Edge Co-Inference for Vision-Language-Action Models under Real-Time Constraints** | Fresh / preprint | VLA device-edge co-inference / energy-aware runtime | [Link](https://arxiv.org/abs/2608.15502) | — |
| **ESR-HGNN: Eliminating Semantic Redundancy for Efficient Mini-batch HGNN Inference** | Fresh / preprint | HGNN inference accelerator / redundancy-aware sampling | [Link](https://arxiv.org/abs/2608.17865) | — |
| **ETHEREAL: A 25.6-μs/inf. Low-latency Event-driven Graph-neural-network Processor for High-resolution Vision at the Edge** | Fresh / preprint | edge AI accelerator / event-driven GNN | [Link](https://arxiv.org/abs/2608.17787) | — |
| **FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution** | Fresh / preprint | edge MoE serving | [Link](https://arxiv.org/abs/2608.16157) | — |
| **From LLM Inference to Agentic Workloads: Characterization and Implications for Serving Systems** | Fresh / preprint | agentic serving characterization / systems benchmark | [Link](https://arxiv.org/abs/2608.15127) | — |
| **GraniKV: Asymmetric Granularity KV-Cache Paging for Multi-Agent Systems with Long Shared Prefix** | Fresh / preprint | KV-cache paging / multi-agent serving | [Link](https://arxiv.org/abs/2608.15584) | — |
| **Pallas: A Proactive KV Cache Migration Framework for LLM Inference in AI-RAN** | Fresh / preprint | LLM serving / KV cache / edge | [Link](https://arxiv.org/abs/2608.16477) | — |
| **Pre-Compiled Pipeline Shards for Distributed LLM Inference on Intel AI PC Fleets** | Fresh / preprint | distributed LLM inference / edge AI PC fleet / speculative decoding | [Link](https://arxiv.org/abs/2608.19147) | [Repo](https://github.com/labscommunity/pipeline-sharded-inference-paper) |
| **SCOPE: Subspace Clustering with Online Per-Head Top-K Estimation for Sparse Video Attention** | Fresh / preprint | sparse video attention / DiT inference | [Link](https://arxiv.org/abs/2608.12780) | — |
