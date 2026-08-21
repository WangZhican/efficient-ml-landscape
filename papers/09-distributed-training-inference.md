# 09 · Distributed Training / Inference

> **70 papers** currently mapped to this direction. Cross-direction duplication is intentional when a paper has multiple technical roles.

[← Research Map](README.md) · [Complete Paper List](ALL_PAPERS.md)

| Paper | Venue | Topic | Paper | Code |
|---|---|---|---|---|
| **Compute Only 16 Tokens in One Timestep: Accelerating Diffusion Transformers with Cluster-Driven Feature Caching** | ACM Multimedia 2025 | diffusion token/feature caching | [Link](https://arxiv.org/abs/2509.10312) | — |
| **Mugi: Value Level Parallelism For Efficient LLMs** | ASPLOS 2026 | LLM accelerator / value-level parallelism / low precision | [Link](https://arxiv.org/abs/2601.10823) | — |
| **Ouroboros: Wafer-Scale SRAM CIM with Token-Grained Pipelining for Large Language Model Inference** | ASPLOS 2026 | LLM accelerator / wafer-scale CIM | [Link](https://arxiv.org/abs/2603.02737) | — |
| **Shift Parallelism** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | — | — |
| **Shift Parallelism: Low-Latency, High-Throughput LLM Inference for Dynamic Workloads** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | [Link](https://arxiv.org/abs/2509.16495) | — |
| **STARC: Selective Token Access with Remapping and Clustering for Efficient LLM Decoding on PIM Systems** | ASPLOS 2026 | sparse attention / PIM / KV cache | [Link](https://doi.org/10.1145/3779212.3790226) | — |
| **TetriServe: Efficiently Serving Mixed DiT Workloads** | ASPLOS 2026 | diffusion/DiT serving / scheduling | [Link](https://arxiv.org/abs/2510.01565) | — |
| **TPLA: Tensor Parallel Latent Attention for Efficient Disaggregated Prefill & Decode Inference** | ASPLOS 2026 | MLA / tensor parallelism / KV cache / disaggregated inference | [Link](https://arxiv.org/abs/2508.15881) | — |
| **FlexPipe: Adapting Dynamic LLM Serving Through Inflight Pipeline Refactoring in Fragmented Serverless Clusters** | EuroSys 2026 | LLM serving / serverless / pipeline parallelism | [Link](https://arxiv.org/abs/2510.11938) | — |
| **MegaScale-MoE: Large-Scale Communication-Efficient Training of Mixture-of-Experts Models in Production** | EuroSys 2026 | MoE training systems / communication optimization | [Link](https://arxiv.org/abs/2505.11432) | — |
| **Enabling Efficient SpMM for Sparse Attention on GEMM-Optimized Hardware with Block Aggregation** | FPGA 2026 | sparse attention / FPGA / SpMM-GEMM transformation | [Link](https://doi.org/10.1145/3748173.3779187) | — |
| **AutoHAAP: Automated Heterogeneity-Aware Asymmetric Partitioning for LLM Training** | HPCA 2026 | heterogeneous distributed LLM training / partition search | [Link](https://doi.org/10.1109/HPCA68181.2026.11408533) | — |
| **Compression-Aware Gradient Splitting for Collective Communications in Distributed Training** | HPCA 2026 | distributed training / compressed collective communication | [Link](https://doi.org/10.1109/HPCA68181.2026.11408444) | — |
| **SCALE: Tackling Communication Bottlenecks in Confidential Distributed Machine Learning** | HPCA 2026 | confidential multi-GPU ML / communication acceleration | [Link](https://doi.org/10.1109/HPCA68181.2026.11408582) | — |
| **Towards Compute-Aware In-Switch Computing for LLMs Tensor-Parallelism on Multi-GPU Systems** | HPCA 2026 | tensor parallelism / in-switch collective-compute co-design | [Link](https://arxiv.org/abs/2605.05628) | — |
| **eGPU: Production-Scale Elastic Sharing over 10,000 GPUs** | HPCA 2026 Industry Track | production GPU sharing / elastic multi-tenant ML | [Link](https://doi.org/10.1109/HPCA68181.2026.11408556) | — |
| **Accelerating MoE with Dynamic In-Switch Computing on Multi-GPUs** | ISCA 2026 | MoE / multi-GPU / in-switch computing | — | — |
| **DisDP: Disaggregating Compute, Network, and Storage for Model-Sharded Data-Parallel Training** | ISCA 2026 | distributed LLM training / disaggregation / SmartNIC-SmartSwitch | — | — |
| **MoE-Hub: Taming Software Complexity for Seamless MoE Overlap with Hardware-Accelerated Communication on Multi-GPU Systems** | ISCA 2026 | MoE systems / multi-GPU communication overlap | — | — |
| **Symbiotic MLLM Serving: Dynamically Balancing Parallelism Across GPUs and Resources Within GPUs** | ISCA 2026 | multimodal LLM serving / GPU resource balancing | — | — |
| **Tetris: Efficient Long-context LLM Serving with Chunkwise Dynamic Sequence Parallelism** | ISCA 2026 | long-context LLM serving / sequence parallelism | — | — |
| **Exploiting Student Parallelism for Low-latency GPU Inference of BERT-like Models in Online Services** | KDD 2025 | GPU online inference / BERT serving / student parallelism | [Link](https://arxiv.org/abs/2408.12526) | — |
| **Optimizing Deployment Configurations for LLM Inference** | MLSys 2026 | LLM serving / deployment configuration / hardware heterogeneity / production systems | — | — |
| **Block-Diagonal LoRA for Eliminating Communication Overhead in Tensor Parallel LoRA Serving** | NeurIPS 2025 | LoRA serving / tensor parallel communication elimination | [Link](https://doi.org/10.52202/085713-0010) | — |
| **FastServe: Iteration-Level Preemptive Scheduling for Large Language Model Inference** | NSDI 2026 | LLM serving / preemptive scheduling / GPU memory management | — | — |
| **SwiftEP: Accelerating MoE Inference with Buffer Fusion and TMA Offloading** | NSDI 2026 | MoE communication / inference runtime | — | — |
| **SYMI: Efficient Mixture-of-Experts Training via Model and Optimizer State Decoupling** | NSDI 2026 | MoE training systems | — | — |
| **Efficient LLM Serving on Commodity GPU Clusters with Data-Reduced Cross-Instance Orchestration** | OSDI 2026 | commodity-GPU LLM serving | — | — |
| **OpenTela: Unifying Decentralized Computing Resources for Heterogeneous LLM Serving (Operational Systems)** | OSDI 2026 | LLM serving / heterogeneous clusters / decentralized orchestration / operational systems | — | [Repo](https://github.com/eth-easl/opentela) |
| **Revisiting Pipeline Parallelism for LLM Serving** | OSDI 2026 | LLM serving / pipeline parallelism / scheduling / SGLang | — | [Repo](https://github.com/Sys-KU/FastPP) |
| **Neptune: Advanced ML Operator Fusion for Locality and Parallelism on GPUs** | PLDI 2026 | ML compiler / attention operator fusion | — | — |
| **CCL-D: A High-Precision Diagnostic System for Slow and Hang Anomalies in Large-Scale Model Training** | PPoPP 2026 | distributed training infrastructure / diagnosis | [Link](https://doi.org/10.1145/3774934.3786429) | — |
| **COCCL: A Collective Communication Library Supporting Easy Integration and Configuration of Customized Compression for Scalable LLM Training** | PPoPP 2026 | distributed LLM training / compressed collectives | — | — |
| **Elastor: Elastic and Efficient Model Partitioning and Checkpointing for Fault-Tolerant Distributed Training** | PPoPP 2026 | distributed training / elastic checkpointing | [Link](https://doi.org/10.1145/3774934.3786445) | — |
| **FlashAttention-T: Towards Fully Tensorized Attention by Exploiting Tensor-Vector Parallelism** | PPoPP 2026 | attention kernel / tensor core / GPU | [Link](https://doi.org/10.1145/3774934.3786425) | — |
| **HelixPipe: Efficient Distributed Training of Long Sequence Transformers with Attention Parallel Pipeline Parallelism** | PPoPP 2026 | distributed training / long-context transformer | — | — |
| **MixFusion: A Patch-Level Parallel Serving System for Mixed-Resolution Diffusion Models** | PPoPP 2026 | diffusion serving / patch-level parallelism | [Link](https://doi.org/10.1145/3774934.3786420) | — |
| **RLinf-USER: A Unified and Extensible System for Real-World Online Policy Learning in Embodied AI** | RSS 2026 | Physical AI systems / multi-robot online learning / edge-cloud scheduling | [Link](https://arxiv.org/abs/2602.07837) | [Repo](https://github.com/RLinf/RLinf) |
| **FIRST: Federated Inference Resource Scheduling Toolkit for Scientific AI Model Access** | SC 2025 | federated inference-as-a-service / HPC AI serving | [Link](https://arxiv.org/abs/2510.13724) | — |
| **gLLM: Global Balanced Pipeline Parallelism Systems for Distributed LLMs Serving with Token Throttling** | SC 2025 | LLM serving / pipeline parallelism / token throttling | [Link](https://arxiv.org/abs/2504.14775) | [Repo](https://github.com/gty111/gLLM) |
| **Hetis: Serving LLMs in Heterogeneous GPU Clusters with Fine-grained and Dynamic Parallelism** | SC 2025 | LLM serving / heterogeneous GPU / dynamic parallelism | [Link](https://arxiv.org/abs/2509.08309) | — |
| **HydraCache: LLM Inference Prefill Parallelization Through Distributed Cache Blending** | SC 2025 | LLM serving / distributed prefill / KV cache blending | — | — |
| **Understanding Communication Bottlenecks in Multi-Node LLM Inference** | SC 2025 | distributed LLM inference / communication characterization | — | — |
| **ByteScale: Communication-Efficient Scaling of LLM Training with a 2048K Context Length on 16384 GPUs** | SIGCOMM 2025 | KV encoding + MoE training fabric + long-context training + AI networking/inference | [Link](https://arxiv.org/abs/2502.21231) | — |
| **DistTrain: Addressing Model and Data Heterogeneity with Disaggregated Training for Multimodal Large Language Models** | SIGCOMM 2025 | multimodal training systems / disaggregated training | [Link](https://arxiv.org/abs/2408.04275) | — |
| **MegaScale-Infer: Efficient Mixture-of-Experts Model Serving with Disaggregated Expert Parallelism** | SIGCOMM 2025 | MoE serving / disaggregated expert parallelism / networking | [Link](https://arxiv.org/abs/2504.02263) | — |
| **MixNet: A Runtime Reconfigurable Optical-Electrical Fabric for Distributed Mixture-of-Experts Training** | SIGCOMM 2025 | KV encoding + MoE training fabric + long-context training + AI networking/inference | [Link](https://arxiv.org/abs/2501.03905) | — |
| **ResCCL: Resource-Efficient Scheduling for Collective Communication** | SIGCOMM 2025 | distributed training / collective communication / GPU resource scheduling | [Link](https://doi.org/10.1145/3718958.3750514) | — |
| **SGLB: Scalable and Robust Global Load Balancing in Commodity AI Clusters** | SIGCOMM 2025 | KV encoding + MoE training fabric + long-context training + AI networking/inference | [Link](https://doi.org/10.1145/3718958.3750527) | — |
| **SyCCL: Exploiting Symmetry for Efficient Collective Communication Scheduling** | SIGCOMM 2025 | distributed ML training / collective communication schedule synthesis | [Link](https://doi.org/10.1145/3718958.3750499) | [Repo](https://github.com/aliyun/syccl) |
| **Characterizing Mobile SoC for Accelerating Heterogeneous LLM Inference** | SOSP 2025 | on-device LLM inference / heterogeneous GPU-NPU mobile SoC | [Link](https://arxiv.org/abs/2501.14794) | — |
| **DCP: Addressing Input Dynamism In Long-Context Training via Dynamic Context Parallelism** | SOSP 2025 | long-context LLM training / dynamic context parallelism | [Link](https://arxiv.org/abs/2510.10620) | [Repo](https://github.com/chenyu-jiang/dcp) |
| **HedraRAG: Co-Optimizing Generation and Retrieval for Heterogeneous RAG Workflows** | SOSP 2025 | RAG serving / generation-retrieval co-optimization | [Link](https://doi.org/10.1145/3731569.3764806) | — |
| **Mercury: Unlocking Multi-GPU Operator Optimization for LLMs via Remote Memory Scheduling** | SOSP 2025 | LLM serving / KV / GPU systems | — | — |
| **Mycroft: Tracing Dependencies in Collective Communication Towards Reliable LLM Training** | SOSP 2025 | distributed LLM training / collective communication / reliability | [Link](https://arxiv.org/abs/2509.03018) | — |
| **Robust LLM Training Infrastructure at ByteDance** | SOSP 2025 | distributed LLM training / reliability / fault tolerance | [Link](https://arxiv.org/abs/2509.16293) | — |
| **Sailor: Automating Distributed Training over Dynamic, Heterogeneous, and Geo-distributed Clusters** | SOSP 2025 | distributed training / heterogeneous clusters / geo-distributed systems | [Link](https://arxiv.org/abs/2504.17096) | [Repo](https://github.com/eth-easl/sailor) |
| **TrainVerify: Equivalence-Based Verification for Distributed LLM Training** | SOSP 2025 | distributed LLM training / verification / reliability | [Link](https://arxiv.org/abs/2506.15961) | [Repo](https://github.com/microsoft/TrainVerify) |
| **PPipe: Efficient Video Analytics Serving on Heterogeneous GPU Clusters via Pool-Based Pipeline Parallelism** | USENIX ATC 2025 | heterogeneous GPU inference serving / pipeline parallelism | — | — |
| **Universal Checkpointing: A Flexible and Efficient Distributed Checkpointing System for Large-Scale DNN Training with Reconfigurable Parallelism** | USENIX ATC 2025 | distributed LLM training / elastic checkpointing / reconfigurable parallelism | — | — |
| **mLoRA: Fine-Tuning LoRA Adapters via Highly-Efficient Pipeline Parallelism in Multiple GPUs** | VLDB/PVLDB Volume 18 | LoRA fine-tuning systems / multi-GPU pipeline | [Link](https://arxiv.org/abs/2312.02515) | — |
| **ClawGym II: Exploring Black-Box RL on Agent Harness** | Fresh / preprint | agent training systems | [Link](https://arxiv.org/abs/2608.16798) | — |
| **DeaMoE: Efficient MoE Structure for Fast Small-Batch Decoding** | Fresh / preprint | MoE architecture / small-batch decoding | [Link](https://arxiv.org/abs/2608.14385) | — |
| **EcoVLA: Energy-Efficient Device-Edge Co-Inference for Vision-Language-Action Models under Real-Time Constraints** | Fresh / preprint | VLA device-edge co-inference / energy-aware runtime | [Link](https://arxiv.org/abs/2608.15502) | — |
| **From LLM Inference to Agentic Workloads: Characterization and Implications for Serving Systems** | Fresh / preprint | agentic serving characterization / systems benchmark | [Link](https://arxiv.org/abs/2608.15127) | — |
| **Global Simulation-Guided Dynamic Operator Scheduling for Efficient Multi-Tenant Model Serving** | Fresh / preprint | multi-tenant model serving / operator-level scheduling | [Link](https://arxiv.org/abs/2608.15762) | — |
| **GraniKV: Asymmetric Granularity KV-Cache Paging for Multi-Agent Systems with Long Shared Prefix** | Fresh / preprint | KV-cache paging / multi-agent serving | [Link](https://arxiv.org/abs/2608.15584) | — |
| **Pre-Compiled Pipeline Shards for Distributed LLM Inference on Intel AI PC Fleets** | Fresh / preprint | distributed LLM inference / edge AI PC fleet / speculative decoding | [Link](https://arxiv.org/abs/2608.19147) | [Repo](https://github.com/labscommunity/pipeline-sharded-inference-paper) |
| **SCOPE: Subspace Clustering with Online Per-Head Top-K Estimation for Sparse Video Attention** | Fresh / preprint | sparse video attention / DiT inference | [Link](https://arxiv.org/abs/2608.12780) | — |
| **TEMPO: Makespan-Aware Expert-Parallel Load Balancing Across Memory- and Compute-Bound Regimes** | Fresh / preprint | MoE expert-parallel load balancing / serving | [Link](https://arxiv.org/abs/2608.13057) | — |
