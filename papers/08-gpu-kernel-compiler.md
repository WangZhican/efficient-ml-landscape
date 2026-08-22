# 08 · GPU Kernel / DSL / Compiler

> **215 papers** currently mapped to this direction. Cross-direction duplication is intentional when a paper has multiple technical roles.

[← Research Map](README.md) · [Complete Paper List](ALL_PAPERS.md)

| Paper | Venue | Topic | Paper | Code |
|---|---|---|---|---|
| **Accelerating LLM Inference Throughput via Asynchronous KV Cache Prefetching** | AAAI 2026 | LLM inference / KV cache prefetch / GPU memory hierarchy | [Link](https://doi.org/10.1609/aaai.v40i25.39224) | — |
| **FlashSVD: Memory-Efficient Inference with Streaming for Low-Rank Models** | AAAI 2026 | sparsity/pruning / GPU kernels | [Link](https://doi.org/10.1609/aaai.v40i30.39720) | — |
| **Self-Indexing KVCache: Predicting Sparse Attention from Compressed Keys** | AAAI 2026 | KV cache compression / sparse attention / CUDA kernel | [Link](https://doi.org/10.1609/aaai.v40i33.39988) | — |
| **ContrastKV: Robust KV Cache Eviction via Contrastive Signal Fusion for Multi-Query Generalization** | ACL 2026 | KV-cache eviction / long-context multi-query inference | [Link](https://doi.org/10.18653/v1/2026.acl-long.417) | — |
| **Focus-dLLM: Accelerating Long-Context Diffusion LLM Inference via Confidence-Guided Context Focusing** | ACL 2026 | diffusion LLM / sparse attention | [Link](https://doi.org/10.18653/v1/2026.acl-long.556) | — |
| **VecInfer: Efficient LLM Inference with Low-Bit KV Cache via Outlier-Suppressed Vector Quantization** | ACL 2026 | KV-cache quantization / low-bit LLM inference / CUDA kernel | [Link](https://doi.org/10.18653/v1/2026.acl-long.1454) | — |
| **AB-Cache: Training-Free Acceleration of Diffusion Models via Adams-Bashforth Cached Feature Reuse** | ACM Multimedia 2025 | diffusion caching / generative inference acceleration | [Link](https://arxiv.org/abs/2504.10540) | — |
| **Accelerating Diffusion Transformer via Error-Optimized Cache** | ACM Multimedia 2025 | diffusion transformer inference / feature caching | [Link](https://arxiv.org/abs/2501.19243) | — |
| **Compute Only 16 Tokens in One Timestep: Accelerating Diffusion Transformers with Cluster-Driven Feature Caching** | ACM Multimedia 2025 | diffusion token/feature caching | [Link](https://arxiv.org/abs/2509.10312) | — |
| **DilateQuant: Accurate and Efficient Quantization-Aware Training for Diffusion Models via Weight Dilation** | ACM Multimedia 2025 | diffusion quantization / efficient inference | [Link](https://arxiv.org/abs/2409.14307) | — |
| **Single Trajectory Distillation for Accelerating Image and Video Style Transfer** | ACM Multimedia 2025 | diffusion/style-transfer acceleration / trajectory distillation | [Link](https://arxiv.org/abs/2412.18945) | — |
| **SpeCa: Accelerating Diffusion Transformers with Speculative Feature Caching** | ACM Multimedia 2025 | diffusion speculative caching | [Link](https://arxiv.org/abs/2509.11628) | — |
| **UltraVSR: Achieving Ultra-Realistic Video Super-Resolution with Efficient One-Step Diffusion Space** | ACM Multimedia 2025 | one-step diffusion / efficient video super-resolution | [Link](https://arxiv.org/abs/2505.19958) | [Repo](https://github.com/yongliuy/UltraVSR) |
| **Bullet: Boosting GPU Utilization for LLM Serving via Dynamic Spatial-Temporal Orchestration** | ASPLOS 2026 | LLM serving / GPU utilization / scheduling | [Link](https://arxiv.org/abs/2504.19516) | — |
| **Linear Layouts: Robust Code Generation of Efficient Tensor Computation Using F_2** | ASPLOS 2026 | GPU kernel / tensor compiler / Triton / tensor layouts | [Link](https://arxiv.org/abs/2505.23819) | — |
| **Mugi: Value Level Parallelism For Efficient LLMs** | ASPLOS 2026 | LLM accelerator / value-level parallelism / low precision | [Link](https://arxiv.org/abs/2601.10823) | — |
| **PAT: Accelerating LLM Decoding via Prefix-Aware Attention with Resource Efficient Multi-Tile Kernel** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | [Link](https://arxiv.org/abs/2511.22333) | — |
| **SwiftSpec: Ultra-Low Latency LLM Decoding by Scaling Asynchronous Speculative Decoding** | ASPLOS 2026 | speculative decoding / low-latency LLM serving | [Link](https://arxiv.org/abs/2506.11309) | — |
| **TetriServe: Efficiently Serving Mixed DiT Workloads** | ASPLOS 2026 | diffusion/DiT serving / scheduling | [Link](https://arxiv.org/abs/2510.01565) | — |
| **Towards High-Goodput LLM Serving with Prefill-decode Multiplexing** | ASPLOS 2026 | LLM serving / prefill-decode multiplexing | [Link](https://arxiv.org/abs/2504.14489) | — |
| **Hardware-Efficient Attention for Fast Decoding** | COLM 2025 | efficient attention / KV-cache bandwidth / serving | [Link](https://arxiv.org/abs/2505.21487) | — |
| **FLOWER: Democratizing Generalist Robot Policies with Efficient Vision-Language-Flow Models** | CoRL 2025 | Physical AI / efficient VLA / model compression / flow policy | [Link](https://arxiv.org/abs/2509.04996) | [Repo](https://github.com/intuitive-robots/flower_vla_pret) |
| **Accelerating Autoregressive Video Diffusion via History-Guided Cache and Residual Correction** | CVPR 2026 | autoregressive video diffusion / caching | — | — |
| **Accelerating Diffusion-based Video Editing via Heterogeneous Caching: Beyond Full Computing at Sampled Denoising Timestep** | CVPR 2026 | video diffusion editing / heterogeneous caching | — | — |
| **Adaptive Spectral Feature Forecasting for Diffusion Sampling Acceleration** | CVPR 2026 | diffusion/video generation acceleration / spectral feature forecasting / long-range reuse | [Link](https://arxiv.org/abs/2603.01623) | [Repo](https://github.com/hanjq17/Spectrum) |
| **Attention Surgery: An Efficient Recipe to Linearize Your Video Diffusion Transformer** | CVPR 2026 | video diffusion / linear attention / mobile inference | — | — |
| **D2Cache: Second-Order Delta Caching for Higher Video Diffusion Acceleration** | CVPR 2026 | video diffusion / second-order caching | — | — |
| **DeltaQuant: 4-bit Video Diffusion Models with Spatiotemporal Delta Smoothing** | CVPR 2026 | video diffusion / W4A4 quantization / efficient kernels | — | — |
| **Denoising as Path Planning: Training-Free Acceleration of Diffusion Models with DPCache** | CVPR 2026 | diffusion / cache scheduling | — | — |
| **Forecast the Principal, Stabilize the Residual: Subspace-Aware Feature Caching for Diffusion Transformers** | CVPR 2026 | diffusion / subspace-aware feature caching | — | — |
| **Otil: Accelerating Diffusion Model Inference via Communication-Efficient Multi-GPU Parallelism** | CVPR 2026 | diffusion inference / multi-GPU / communication reduction | — | — |
| **QuantVLA: Scale-Calibrated Post-Training Quantization for Vision-Language-Action Models** | CVPR 2026 | VLA / PTQ / Physical AI / diffusion action head | — | — |
| **ResCa: Residual Caching for Diffusion Transformers Acceleration** | CVPR 2026 | diffusion transformer / residual caching | — | — |
| **SeaCache: Spectral-Evolution-Aware Cache for Accelerating Diffusion Models** | CVPR 2026 | diffusion / spectral caching | — | — |
| **SenCache: Accelerating Diffusion Model Inference via Sensitivity-Aware Caching** | CVPR 2026 | diffusion inference / sensitivity-aware caching | — | — |
| **HybriMoE: Hybrid CPU-GPU Scheduling and Cache Management for Efficient MoE Inference** | DAC 2025 | MoE inference / hybrid CPU-GPU scheduling / expert prefetch and cache management | [Link](https://arxiv.org/abs/2504.05897) | [Repo](https://github.com/PKU-SEC-Lab/HybriMoE) |
| **SQ-DM: Accelerating Diffusion Models with Aggressive Quantization and Temporal Sparsity** | DAC 2025 | diffusion acceleration / low-bit quantization / temporal activation sparsity / accelerator co-design | [Link](https://arxiv.org/abs/2501.15448) | — |
| **AdaDiff: Accelerating Diffusion Models through Step-Wise Adaptive Computation** | ECCV 2024 | diffusion acceleration / adaptive computation / early exit | [Link](https://arxiv.org/abs/2309.17074) | [Repo](https://github.com/Tangshengku/AdaDiff) |
| **BK-SDM: A Lightweight, Fast, and Cheap Version of Stable Diffusion** | ECCV 2024 | diffusion pruning / compact model | — | — |
| **Efficient Diffusion Transformer with Step-wise Dynamic Attention Mediators** | ECCV 2024 | diffusion/flow acceleration / efficient attention | — | — |
| **HiDiffusion: Unlocking Higher-Resolution Creativity and Efficiency in Pretrained Diffusion Models** | ECCV 2024 | diffusion inference acceleration | — | — |
| **Inf-DiT: Upsampling any-resolution image with memory-efficient diffusion transformer.** | ECCV 2024 | diffusion memory efficiency | — | — |
| **MixDQ: Memory-Efficient Few-Step Text-to-Image Diffusion Models with Metric-Decoupled Mixed Precision Quantization** | ECCV 2024 | diffusion quantization | — | — |
| **Mixture of Efficient Diffusion Experts Through Automatic Interval and Sub-Network Selection** | ECCV 2024 | diffusion/flow acceleration / pruning | — | — |
| **Post-training Quantization with Progressive Calibration and Activation Relaxing for Text-to-Image Diffusion Models** | ECCV 2024 | diffusion quantization | — | — |
| **SlimFlow: Training Smaller One-Step Diffusion Models with Rectified Flow** | ECCV 2024 | compact one-step diffusion | — | — |
| **Timestep-Aware Correction for Quantized Diffusion Models** | ECCV 2024 | diffusion quantization | — | — |
| **Dovetail: A CPU/GPU Heterogeneous Speculative Decoding for LLM inference** | EMNLP 2025 | heterogeneous CPU/GPU inference / speculative decoding | [Link](https://doi.org/10.18653/v1/2025.emnlp-main.879) | — |
| **FlashPS: Efficient Generative Image Editing with Mask-aware Caching and Scheduling** | EuroSys 2026 | diffusion serving / image editing / activation caching / continuous batching | [Link](https://arxiv.org/abs/2505.20600) | — |
| **FlexiQ: Adaptive Mixed-Precision Quantization for Latency/Accuracy Trade-Offs in Deep Neural Networks** | EuroSys 2026 | adaptive mixed-precision quantization / runtime accuracy-latency tradeoff / NPU-GPU inference | [Link](https://arxiv.org/abs/2510.02822) | — |
| **FlexPipe: Adapting Dynamic LLM Serving Through Inflight Pipeline Refactoring in Fragmented Serverless Clusters** | EuroSys 2026 | LLM serving / serverless / pipeline parallelism | [Link](https://arxiv.org/abs/2510.11938) | — |
| **MegaScale-MoE: Large-Scale Communication-Efficient Training of Mixture-of-Experts Models in Production** | EuroSys 2026 | MoE training systems / communication optimization | [Link](https://arxiv.org/abs/2505.11432) | — |
| **MFS: An Efficient Model Family Serving System for LLMs** | EuroSys 2026 | LLM model-family serving / multi-tier batching / cross-model KV sharing | [Link](https://doi.org/10.1145/3767295.3769355) | — |
| **Reducing the GPU Memory Bottleneck with Lossless Compression for ML** | EuroSys 2026 | GPU memory / tensor compression / ML systems | [Link](https://doi.org/10.1145/3767295.3803595) | — |
| **SAS: Sparse Attention Synthesizer for Efficient Language Model Inference** | EuroSys 2026 | efficient attention / kernel synthesis / KV cache | [Link](https://arxiv.org/abs/2602.09051) | — |
| **Scaling LLM Test-Time Compute with Mobile NPU on Smartphones** | EuroSys 2026 | on-device LLM reasoning / mobile NPU / hardware-aware quantization | [Link](https://arxiv.org/abs/2509.23324) | — |
| **Enabling Efficient SpMM for Sparse Attention on GEMM-Optimized Hardware with Block Aggregation** | FPGA 2026 | sparse attention / FPGA / SpMM-GEMM transformation | [Link](https://doi.org/10.1145/3748173.3779187) | — |
| **FARE: A Fine-grained Pipelined Reconfigurable FlashAttention Kernel** | FPGA 2026 | FlashAttention accelerator / FPGA | [Link](https://doi.org/10.1145/3748173.3779572) | — |
| **BitDecoding: Unlocking Tensor Cores for Long-Context LLMs with Low-Bit KV Cache** | HPCA 2026 | low-bit KV cache / Tensor Core decoding | [Link](https://doi.org/10.1109/HPCA68181.2026.11408481) | — |
| **PADE: A Predictor-Free Sparse Attention Accelerator via Unified Execution and Stage Fusion** | HPCA 2026 | sparse attention accelerator / algorithm-hardware co-design | [Link](https://arxiv.org/abs/2512.14322) | — |
| **SCALE: Tackling Communication Bottlenecks in Confidential Distributed Machine Learning** | HPCA 2026 | confidential multi-GPU ML / communication acceleration | [Link](https://doi.org/10.1109/HPCA68181.2026.11408582) | — |
| **Towards Compute-Aware In-Switch Computing for LLMs Tensor-Parallelism on Multi-GPU Systems** | HPCA 2026 | tensor parallelism / in-switch collective-compute co-design | [Link](https://arxiv.org/abs/2605.05628) | — |
| **Towards Resource-Efficient Serverless LLM Inference with SLINFER** | HPCA 2026 | serverless LLM serving / heterogeneous CPU-GPU sharing | [Link](https://arxiv.org/abs/2507.00507) | — |
| **eGPU: Production-Scale Elastic Sharing over 10,000 GPUs** | HPCA 2026 Industry Track | production GPU sharing / elastic multi-tenant ML | [Link](https://doi.org/10.1109/HPCA68181.2026.11408556) | — |
| **Accelerating Diffusion Transformer via Gradient-Optimized Cache** | ICCV 2025 | diffusion transformer feature caching | — | — |
| **Adaptive Caching for Faster Video Generation with Diffusion Transformers** | ICCV 2025 | video diffusion acceleration / adaptive feature caching | [Link](https://arxiv.org/abs/2411.02397) | — |
| **CHORDS: Diffusion Sampling Accelerator with Multi-core Hierarchical ODE Solvers** | ICCV 2025 | diffusion sampling acceleration / multi-core parallel ODE solvers | [Link](https://arxiv.org/abs/2507.15260) | [Repo](https://github.com/hanjq17/CHORDS) |
| **Fewer Denoising Steps or Cheaper Per-Step Inference: Towards Compute-Optimal Diffusion Model Deployment** | ICCV 2025 | diffusion deployment / compute-optimal inference | — | — |
| **From Reusing to Forecasting: Accelerating Diffusion Models with TaylorSeers** | ICCV 2025 | diffusion acceleration / feature forecasting | [Link](https://arxiv.org/abs/2503.06923) | [Repo](https://github.com/Shenyi-Z/TaylorSeer) |
| **Model Reveals What to Cache: Profiling-Based Feature Reuse for Video Diffusion Models** | ICCV 2025 | video diffusion acceleration / profiling-guided feature reuse | [Link](https://arxiv.org/abs/2504.03140) | — |
| **QuantCache: Adaptive Importance-Guided Quantization with Hierarchical Latent and Layer Caching for Video Generation** | ICCV 2025 | video diffusion acceleration / quantization + caching | — | — |
| **QuEST: Low-bit Diffusion Model Quantization via Efficient Selective Finetuning** | ICCV 2025 | diffusion low-bit quantization | — | — |
| **Text Embedding Knows How to Quantize Text-Guided Diffusion Models** | ICCV 2025 | diffusion quantization / dynamic precision | — | — |
| **Towards Stabilized and Efficient Diffusion Transformers through Long-Skip-Connections with Spectral Constraints** | ICCV 2025 | diffusion transformer training/inference acceleration | — | — |
| **Fast-dLLM v2: Efficient Block-Diffusion LLM** | ICLR 2026 | diffusion LLM inference / block diffusion / hierarchical caching | [Link](https://arxiv.org/abs/2509.26328) | [Repo](https://github.com/NVlabs/Fast-dLLM) |
| **Fast-dLLM: Training-free Acceleration of Diffusion LLM by Enabling KV Cache and Parallel Decoding** | ICLR 2026 | diffusion LLM inference / KV cache / parallel decoding | [Link](https://arxiv.org/abs/2505.22618) | [Repo](https://github.com/NVlabs/Fast-dLLM) |
| **FreeKV: Boosting KV Cache Retrieval for Efficient LLM Inference** | ICLR 2026 | KV cache retrieval / CPU-GPU hybrid memory / long-context inference | [Link](https://arxiv.org/abs/2505.13109) | — |
| **Inference-Cost-Aware Dynamic Tree Construction for Efficient Inference in Large Language Models** | ICLR 2026 | speculative decoding / hardware-aware tree construction | — | — |
| **QuoKA: Query-Oriented KV Selection for Efficient LLM Prefill** | ICLR 2026 | efficient attention / long-context prefill | — | — |
| **ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models** | ICLR 2026 | KV cache compression / efficient reasoning | — | — |
| **AsymRnR: Video Diffusion Transformers Acceleration with Asymmetric Reduction and Restoration** | ICML 2025 | video diffusion transformer token reduction / training-free acceleration | — | [Repo](https://github.com/wenhao728/AsymRnR) |
| **Ca2-VDM: Efficient Autoregressive Video Diffusion Model with Causal Generation and Cache Sharing** | ICML 2025 | video diffusion acceleration | — | — |
| **Diffusion Adversarial Post-Training for One-Step Video Generation** | ICML 2025 | one-step video/image diffusion generation | — | — |
| **Modulated Diffusion: Accelerating Generative Modeling with Modulated Quantization** | ICML 2025 | diffusion acceleration / quantization | — | — |
| **Morse: Dual-Sampling for Lossless Acceleration of Diffusion Models** | ICML 2025 | diffusion sampling acceleration | — | [Repo](https://github.com/deep-optimization/Morse) |
| **Q-VDiT: Towards Accurate Quantization and Distillation of Video-Generation Diffusion Transformers** | ICML 2025 | video diffusion quantization / distillation | — | [Repo](https://github.com/wlfeng0509/Q-VDiT) |
| **Attn-QAT: 4-Bit Attention With Quantization-Aware Training** | ICML 2026 | FP4 attention / quantization-aware training / fused attention kernels | [Link](https://arxiv.org/abs/2603.00040) | — |
| **SALE : Low-bit Estimation for Efficient Sparse Attention in Long-context LLM Prefilling** | ICML 2026 | efficient attention / low-bit estimation / long-context prefill | [Link](https://arxiv.org/abs/2505.24179) | — |
| **Scout Before You Attend: Sketch-and-Walk Sparse Attention for Efficient LLM Inference** | ICML 2026 | efficient attention / long-context inference | [Link](https://arxiv.org/abs/2602.07397) | — |
| **Sparse ActionGen: Accelerating Diffusion Policy with Real-time Pruning** | ICML 2026 | Physical AI / diffusion-policy acceleration / pruning+reuse | [Link](https://arxiv.org/abs/2601.12894) | — |
| **Understand and Accelerate Memory Processing Pipeline for Large Language Model Inference** | ICML 2026 | LLM memory processing / GPU-FPGA heterogeneous acceleration | [Link](https://arxiv.org/abs/2603.29002) | — |
| **Rethinking the Practicality of Vision-language-action Model: A Comprehensive Benchmark and An Improved Baseline** | ICRA 2026 | Physical AI / lightweight VLA / consumer-GPU deployment / action chunking / cross-embodiment | [Link](https://arxiv.org/abs/2602.22663) | [Repo](https://github.com/OpenHelix-Team/LLaVA-VLA) |
| **FBQuant: FeedBack Quantization for Large Language Models** | IJCAI 2025 | LLM weight quantization / CUDA kernel | [Link](https://arxiv.org/abs/2501.16385) | — |
| **Accelerating MoE with Dynamic In-Switch Computing on Multi-GPUs** | ISCA 2026 | MoE / multi-GPU / in-switch computing | — | — |
| **DisDP: Disaggregating Compute, Network, and Storage for Model-Sharded Data-Parallel Training** | ISCA 2026 | distributed LLM training / disaggregation / SmartNIC-SmartSwitch | — | — |
| **MoE-Hub: Taming Software Complexity for Seamless MoE Overlap with Hardware-Accelerated Communication on Multi-GPU Systems** | ISCA 2026 | MoE systems / multi-GPU communication overlap | — | — |
| **OASIS: Outlier-Aware LUT-Based GEMM with Dual-Side Quantization for LLM Inference Acceleration** | ISCA 2026 | edge speculative reasoning + quantization + memory-system + generative inference accelerators | — | — |
| **PowerWeave: Unlocking Energy-Efficient ML on GPUs with OS-Level Spatial Power Management** | ISCA 2026 | GPU power management / LLM serving / agentic workloads | — | — |
| **QiMeng-Tensify: Scaling up Tensor Computation Optimization via Architecture-Aware LLM-Guided MCTS** | ISCA 2026 | tensor compiler / architecture-aware optimization / LLM-guided search | — | — |
| **Symbiotic MLLM Serving: Dynamically Balancing Parallelism Across GPUs and Resources Within GPUs** | ISCA 2026 | multimodal LLM serving / GPU resource balancing | — | — |
| **UniCore: A Bit-Width Scalable GEMM Unit for Unified LLM Inference** | ISCA 2026 | LLM accelerator / variable bit-width GEMM | — | — |
| **Spyre: An inference-optimized scalable AI accelerator for enterprise workloads** | ISSCC 2026 | AI accelerator / enterprise inference | [Link](https://doi.org/10.1109/ISSCC49663.2026.11409090) | — |
| **Enhancing Learned Knowledge in LoRA Adapters Through Efficient Contrastive Decoding on Ascend NPUs** | KDD 2025 | LLM decoding / LoRA / Ascend NPU kernel optimization | [Link](https://arxiv.org/abs/2505.14620) | — |
| **Exploiting Student Parallelism for Low-latency GPU Inference of BERT-like Models in Online Services** | KDD 2025 | GPU online inference / BERT serving / student parallelism | [Link](https://arxiv.org/abs/2408.12526) | — |
| **AxCore: A Quantization-Aware Approximate GEMM Unit for LLM Inference** | MICRO 2025 | LLM quantization / accelerator | — | — |
| **Coruscant: Co-Designing GPU Kernel and Sparse Tensor Core to Advocate Unstructured Sparsity in Efficient LLM Inference** | MICRO 2025 | sparse LLM inference / GPU kernel co-design | — | — |
| **HLX** | MICRO 2025 | MoE + diffusion + tensor compression + hybrid LM + reasoning + edge training acceleration | — | — |
| **LLM.265** | MICRO 2025 | MoE + diffusion + tensor compression + hybrid LM + reasoning + edge training acceleration | — | — |
| **LongSight: Compute-Enabled Memory to Accelerate Large-Context LLMs via Sparse Attention** | MICRO 2025 | long-context LLM / sparse attention / CXL memory | [Link](https://doi.org/10.1145/3725843.3756062) | — |
| **ORCHES** | MICRO 2025 | MoE + diffusion + tensor compression + hybrid LM + reasoning + edge training acceleration | — | — |
| **Pimba: A Processing-in-Memory Acceleration for Post-Transformer Large Language Model Serving** | MICRO 2025 | post-transformer LLM serving / PIM / low precision | [Link](https://arxiv.org/abs/2507.10178) | — |
| **REACT3D** | MICRO 2025 | MoE + diffusion + tensor compression + hybrid LM + reasoning + edge training acceleration | — | — |
| **S-DMA** | MICRO 2025 | MoE + diffusion + tensor compression + hybrid LM + reasoning + edge training acceleration | — | — |
| **Stratum** | MICRO 2025 | MoE + diffusion + tensor compression + hybrid LM + reasoning + edge training acceleration | — | — |
| **BLASST: Dynamic BLocked Attention Sparsity via Softmax Thresholding** | MLSys 2026 | sparse attention / long-context inference | — | — |
| **Efficient, VRAM-Constrained xLM Inference on Clients** | MLSys 2026 | client LLM/VLM inference / CPU-GPU hybrid runtime / Physical AI | — | — |
| **Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost** | MLSys 2026 | KV cache quantization / low-bit inference | — | — |
| **Locality-Aware Beam Scheduling for Efficient Test-Time Compute with a Consumer-grade GPU** | MLSys 2026 | efficient reasoning / test-time compute / KV offload scheduling | — | — |
| **Modality Plug-and-Play: Runtime Modality Adaptation in LLM-Driven Autonomous Mobile Systems** | MobiCom 2025 | Physical AI / multimodal edge runtime / efficient modality adaptation | [Link](https://doi.org/10.1145/3680207.3723491) | [Repo](https://github.com/pittisl/mPnP-LLM) |
| **HiFC: High-efficiency Flash-based KV Cache Swapping for Scaling LLM Inference** | NeurIPS 2025 | KV cache swapping / SSD / GDS | [Link](https://doi.org/10.52202/085713-1587) | — |
| **MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference** | NeurIPS 2025 | KV pruning / sparse attention kernel | [Link](https://doi.org/10.52202/085713-2564) | — |
| **SageAttention3: Microscaling FP4 Attention for Inference and An Exploration of 8-Bit Training** | NeurIPS 2025 | low-bit attention kernel / FP4 | [Link](https://doi.org/10.52202/085713-1799) | — |
| **Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion** | NeurIPS 2025 | autoregressive video diffusion / streaming generation | [Link](https://doi.org/10.52202/085713-5576) | — |
| **Speculate Deep and Accurate: Lossless and Training-Free Acceleration for Offloaded LLMs via Substitute Speculative Decoding** | NeurIPS 2025 | offloaded LLM inference / speculative decoding | — | — |
| **Spotlight Attention: Towards Efficient LLM Generation via Non-linear Hashing-based KV Cache Retrieval** | NeurIPS 2025 | sparse attention / KV retrieval / CUDA kernel | [Link](https://doi.org/10.52202/085713-2883) | — |
| **FastServe: Iteration-Level Preemptive Scheduling for Large Language Model Inference** | NSDI 2026 | LLM serving / preemptive scheduling / GPU memory management | — | — |
| **SwiftEP: Accelerating MoE Inference with Buffer Fusion and TMA Offloading** | NSDI 2026 | MoE communication / inference runtime | — | — |
| **Efficient LLM Serving on Commodity GPU Clusters with Data-Reduced Cross-Instance Orchestration** | OSDI 2026 | commodity-GPU LLM serving | — | — |
| **Kairox: Adaptive GPU-CPU Hybrid LLM Inference via Online Neuron Balancing** | OSDI 2026 | LLM inference / GPU-CPU hybrid execution / activation sparsity / edge inference | — | — |
| **No Buffer, No Bottleneck: Efficient Zero-Copy KV Cache Offloading for Long-Context LLMs** | OSDI 2026 | LLM serving / KV cache offloading / heterogeneous CPU-GPU memory | — | — |
| **Prism: Cost-Efficient Multi-LLM Serving via GPU Memory Ballooning** | OSDI 2026 | LLM serving / multi-model serving / GPU memory ballooning / production deployment | — | [Repo](https://github.com/ovg-project/kvcached) |
| **Revisiting Pipeline Parallelism for LLM Serving** | OSDI 2026 | LLM serving / pipeline parallelism / scheduling / SGLang | — | [Repo](https://github.com/Sys-KU/FastPP) |
| **Compiling Strassen-like Matrix Multiplication Algorithms to Fast CUDA Kernels** | PLDI 2026 | GPU compiler / matrix multiplication / LLM inference kernel | [Link](https://doi.org/10.1145/3808267) | [Repo](https://github.com/microsoft/subcuber) |
| **Neptune: Advanced ML Operator Fusion for Locality and Parallelism on GPUs** | PLDI 2026 | ML compiler / attention operator fusion | — | — |
| **Accelerating Sparse Transformer Inference on GPU** | PPoPP 2026 | sparse transformer inference + mixed-precision quantization | — | — |
| **BEEMS: Boosting Machine Vision Efficiency via Computation Graph-Based Memory Smoothing** | PPoPP 2026 | vision foundation model inference / memory-aware compiler | [Link](https://doi.org/10.1145/3774934.3786430) | — |
| **CCL-D: A High-Precision Diagnostic System for Slow and Hang Anomalies in Large-Scale Model Training** | PPoPP 2026 | distributed training infrastructure / diagnosis | [Link](https://doi.org/10.1145/3774934.3786429) | — |
| **ChituDiffusion: A Data-Characteristic-Aware Serving System for Diffusion Models** | PPoPP 2026 | diffusion serving / compile-runtime co-optimization | [Link](https://doi.org/10.1145/3774934.3786424) | — |
| **Elastor: Elastic and Efficient Model Partitioning and Checkpointing for Fault-Tolerant Distributed Training** | PPoPP 2026 | distributed training / elastic checkpointing | [Link](https://doi.org/10.1145/3774934.3786445) | — |
| **FlashAttention-T: Towards Fully Tensorized Attention by Exploiting Tensor-Vector Parallelism** | PPoPP 2026 | attention kernel / tensor core / GPU | [Link](https://doi.org/10.1145/3774934.3786425) | — |
| **High-Throughput Non-uniformly Quantized 3-bit LLM Inference** | PPoPP 2026 | 3-bit LLM quantization / GPU kernels | [Link](https://doi.org/10.1145/3774934.3786423) | — |
| **JanusQuant: Accurate and Efficient 2-bit KV Cache Quantization for Long-Context Inference** | PPoPP 2026 | KV cache quantization / long-context inference | [Link](https://doi.org/10.1145/3774934.3786428) | — |
| **MetaAttention: A Unified and Performant Attention Framework across Hardware Backends** | PPoPP 2026 | attention runtime / cross-backend kernel optimization | [Link](https://doi.org/10.1145/3774934.3786444) | — |
| **MixFusion: A Patch-Level Parallel Serving System for Mixed-Resolution Diffusion Models** | PPoPP 2026 | diffusion serving / patch-level parallelism | [Link](https://doi.org/10.1145/3774934.3786420) | — |
| **FAST: Efficient Action Tokenization for Vision-Language-Action Models** | RSS 2025 | Physical AI / VLA action tokenization / efficient training and inference | [Link](https://arxiv.org/abs/2501.09747) | — |
| **Unified Video Action Model** | RSS 2025 | Physical AI / efficient world-action model inference | [Link](https://doi.org/10.15607/RSS.2025.XXI.074) | — |
| **Muninn: Your Trajectory Diffusion Model But Faster** | RSS 2026 | Physical AI / trajectory diffusion acceleration / training-free cache reuse | [Link](https://arxiv.org/abs/2605.09999) | [Repo](https://github.com/gokulp01/Muninn) |
| **RLux-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models** | RSS 2026 | Physical AI / VLA RL systems / scalable training | [Link](https://arxiv.org/abs/2510.06710) | — |
| **Compile-Time QoS Scheme for Deep Learning Inferences** | SC 2025 | multi-tenant inference / QoS / compiler scheduling | [Link](https://doi.org/10.1145/3712285.3759846) | — |
| **Engine-Agnostic Model Hot-Swapping for Cost-Effective LLM Inference** | SC 2025 | LLM serving / GPU model hot-swapping | [Link](https://doi.org/10.1145/3731599.3767354) | — |
| **Hetis: Serving LLMs in Heterogeneous GPU Clusters with Fine-grained and Dynamic Parallelism** | SC 2025 | LLM serving / heterogeneous GPU / dynamic parallelism | [Link](https://arxiv.org/abs/2509.08309) | — |
| **Alibaba Stellar: A New Generation RDMA Network for Cloud AI** | SIGCOMM 2025 | cloud AI networking / RDMA virtualization / distributed training and inference infrastructure | [Link](https://doi.org/10.1145/3718958.3750539) | — |
| **AoRA: AI-on-RAN for Backhaul-free Edge Inference** | SIGCOMM 2025 | edge AI inference / AI-on-RAN / heterogeneous GPU-NPU infrastructure | [Link](https://doi.org/10.1145/3718958.3750517) | — |
| **ByteScale: Communication-Efficient Scaling of LLM Training with a 2048K Context Length on 16384 GPUs** | SIGCOMM 2025 | KV encoding + MoE training fabric + long-context training + AI networking/inference | [Link](https://arxiv.org/abs/2502.21231) | — |
| **DistTrain: Addressing Model and Data Heterogeneity with Disaggregated Training for Multimodal Large Language Models** | SIGCOMM 2025 | multimodal training systems / disaggregated training | [Link](https://arxiv.org/abs/2408.04275) | — |
| **InfiniteHBD: Building Datacenter-Scale High-Bandwidth Domain for LLM with Optical Circuit Switching Transceivers** | SIGCOMM 2025 | AI networking / LLM training fabric / optical interconnect | [Link](https://arxiv.org/abs/2502.03885) | — |
| **MegaScale-Infer: Efficient Mixture-of-Experts Model Serving with Disaggregated Expert Parallelism** | SIGCOMM 2025 | MoE serving / disaggregated expert parallelism / networking | [Link](https://arxiv.org/abs/2504.02263) | — |
| **ResCCL: Resource-Efficient Scheduling for Collective Communication** | SIGCOMM 2025 | distributed training / collective communication / GPU resource scheduling | [Link](https://doi.org/10.1145/3718958.3750514) | — |
| **From Prefix Cache to Fusion RAG Cache: Accelerating LLM Inference in Retrieval-Augmented Generation** | SIGMOD 2026 | RAG KV-cache reuse / TTFT acceleration | [Link](https://arxiv.org/abs/2601.12904) | — |
| **Serving Hybrid LLM Loads with SLO Guarantees Using CPU-GPU Attention Piggybacking** | SIGMOD 2026 | LLM serving / heterogeneous CPU-GPU / SLO scheduling | [Link](https://arxiv.org/abs/2603.12831) | — |
| **SG-Serve: Efficient Model Serving for Subgraph-based Graph Representation Learning** | SIGMOD 2026 | graph model serving / tail-latency optimization / workload-aware GPU batching | [Link](https://doi.org/10.1145/3786697) | — |
| **Medha** | SoCC 2026 | KV virtualization + long-context serving + GPU colocation + on-device adaptation | — | — |
| **Memory-Decoupled Layer-Wise Fine-Tuning** | SoCC 2026 | KV virtualization + long-context serving + GPU colocation + on-device adaptation | — | — |
| **MosaicKV: SLO-Aware KV Cache Virtualization for Efficient LLM Serving** | SoCC 2026 | KV virtualization + long-context serving + GPU colocation + on-device adaptation | [Link](https://arxiv.org/abs/2607.00760) | — |
| **No Request Left Behind: Tackling Heterogeneity in Long-Context LLM Inference with Medha** | SoCC 2026 | KV virtualization + long-context serving + GPU colocation + on-device adaptation | [Link](https://arxiv.org/abs/2409.17264) | — |
| **PEACE: Power and Performance Aware Colocation for Efficient GPU Spatial Partitioning** | SoCC 2026 | KV virtualization + long-context serving + GPU colocation + on-device adaptation | [Link](https://doi.org/10.1145/3815789.3827949) | — |
| **Tessera: Contract-Driven Cost–SLO Optimization for Multi-tenant GPU Clouds** | SoCC 2026 | multi-tenant GPU cloud / cost-SLO optimization / AI infrastructure scheduling | — | — |
| **Aegaeon: Effective GPU Pooling for Concurrent LLM Serving on the Market** | SOSP 2025 | LLM serving / KV / GPU systems | — | — |
| **Characterizing Mobile SoC for Accelerating Heterogeneous LLM Inference** | SOSP 2025 | on-device LLM inference / heterogeneous GPU-NPU mobile SoC | [Link](https://arxiv.org/abs/2501.14794) | — |
| **DiffKV: Differentiated Memory Management for Large Language Models with Parallel KV Compaction** | SOSP 2025 | LLM serving / KV / GPU systems | — | — |
| **IC-Cache: Efficient Large Language Model Serving via In-context Caching** | SOSP 2025 | LLM serving / KV / GPU systems | — | — |
| **Jenga: Effective Memory Management for Serving LLM with Heterogeneity** | SOSP 2025 | LLM serving / KV / GPU systems | — | — |
| **KTransformers: Unleashing the Full Potential of CPU/GPU Hybrid Inference for MoE Models** | SOSP 2025 | LLM serving / KV / GPU systems | — | — |
| **Mercury: Unlocking Multi-GPU Operator Optimization for LLMs via Remote Memory Scheduling** | SOSP 2025 | LLM serving / KV / GPU systems | — | — |
| **Pie: A Programmable Serving System for Emerging LLM Applications** | SOSP 2025 | LLM serving / KV / GPU systems | [Link](https://arxiv.org/abs/2510.24051) | — |
| **PrefillOnly: An Inference Engine for Prefill-only Workloads in Large Language Model Applications** | SOSP 2025 | LLM serving / KV / GPU systems | [Link](https://arxiv.org/abs/2505.07203) | — |
| **Robust LLM Training Infrastructure at ByteDance** | SOSP 2025 | distributed LLM training / reliability / fault tolerance | [Link](https://arxiv.org/abs/2509.16293) | — |
| **Tempo: Compiled Dynamic Deep Learning with Symbolic Dependence Graphs** | SOSP 2025 | ML compiler / dynamic deep learning | [Link](https://doi.org/10.1145/3731569.3764840) | — |
| **HeteroSim: Towards High-Fidelity Heterogeneous LLM Training Simulation on GPUs** | The Web Conference 2026 | heterogeneous LLM training / systems simulation | [Link](https://doi.org/10.1145/3774904.3792254) | — |
| **Colocating ML Inference and Training with Fast GPU Memory Handover** | USENIX ATC 2025 | GPU inference-training colocation / elastic GPU memory handover | — | — |
| **GeneralSparse: Bridging the Gap in SpMM for Pruned Large Language Model Inference on GPUs** | USENIX ATC 2025 | sparse LLM inference / GPU kernels | — | — |
| **GMI-DRL: Empowering Multi-GPU DRL with Adaptive-Grained Parallelism** | USENIX ATC 2025 | distributed DRL training / multi-GPU adaptive-grained parallelism / GPU multiplexing | — | — |
| **JENGA: Enhancing LLM Long-Context Fine-tuning with Contextual Token Sparsity** | USENIX ATC 2025 | long-context LLM fine-tuning / contextual token sparsity / kernels | — | — |
| **Katz** | USENIX ATC 2025 | production KV-cache + quantized-kernel compiler + diffusion workflow serving | — | — |
| **KVCache Cache in the Wild** | USENIX ATC 2025 | production KV-cache + quantized-kernel compiler + diffusion workflow serving | — | — |
| **mTuner: Accelerating Parameter-Efficient Fine-Tuning on Multi-GPU Servers with Elastic Tensor** | USENIX ATC 2025 | LLM PEFT / multi-GPU fine-tuning / dynamic tensor memory management | — | [Repo](https://github.com/xxcclong/mTuner) |
| **Optimus: Accelerating Large-Scale Multi-Modal LLM Training by Bubble Exploitation** | USENIX ATC 2025 | multimodal LLM training / distributed training / pipeline bubble exploitation | [Link](https://arxiv.org/abs/2408.03505) | — |
| **PPipe: Efficient Video Analytics Serving on Heterogeneous GPU Clusters via Pool-Based Pipeline Parallelism** | USENIX ATC 2025 | heterogeneous GPU inference serving / pipeline parallelism | — | — |
| **QFactory** | USENIX ATC 2025 | production KV-cache + quantized-kernel compiler + diffusion workflow serving | — | — |
| **Toppings: CPU-Assisted, Rank-Aware Adapter Serving for LLM Inference** | USENIX ATC 2025 | LoRA serving / heterogeneous CPU-GPU scheduling | — | — |
| **Torpor: GPU-Enabled Serverless Computing for Low-Latency, Resource-Efficient Inference** | USENIX ATC 2025 | serverless GPU inference / model swapping / scheduling | — | — |
| **Chameleon: a Heterogeneous and Disaggregated Accelerator System for Retrieval-Augmented Language Models** | VLDB/PVLDB Volume 18 | RAG acceleration / heterogeneous disaggregated system | [Link](https://arxiv.org/abs/2310.09949) | — |
| **mLoRA: Fine-Tuning LoRA Adapters via Highly-Efficient Pipeline Parallelism in Multiple GPUs** | VLDB/PVLDB Volume 18 | LoRA fine-tuning systems / multi-GPU pipeline | [Link](https://arxiv.org/abs/2312.02515) | — |
| **Algorithm-Architecture Co-Design for Efficient VLA Inference via Speculative Inference and Verification** | Fresh / preprint | VLA speculative inference / algorithm-architecture co-design | [Link](https://arxiv.org/abs/2608.15636) | — |
| **An Empirical Study of Training Pixel-Space Text-to-Image Diffusion Models** | Fresh / preprint | image generation acceleration | [Link](https://arxiv.org/abs/2608.16887) | — |
| **AViTS: Adaptive Spatiotemporal Token Selection for Efficient Dynamic-Resolution Generation** | Fresh / preprint | diffusion/image generation acceleration / adaptive token selection | [Link](https://arxiv.org/abs/2608.17995) | — |
| **Beyond Capacity: Scalable MoE LLM Inference via High-Bandwidth Flash with Direct GPU and HBM Paths** | Fresh / preprint | MoE serving / high-bandwidth flash architecture | [Link](https://arxiv.org/abs/2608.14333) | — |
| **CoRun: Padding is Simple and Efficient for Deterministic LLM Inference** | Fresh / preprint | LLM serving / deterministic inference / fixed-shape scheduling | [Link](https://arxiv.org/abs/2608.14376) | — |
| **DriveCache: Action-Aware Caching for Driving World Model Inference** | Fresh / preprint | world-model / diffusion caching | [Link](https://arxiv.org/abs/2608.16354) | — |
| **Every Expert Counts: ExactMoE for Memory-Efficient W4A16 Inference** | Fresh / preprint | MoE memory-efficient W4A16 inference / GPU slot cache | [Link](https://arxiv.org/abs/2608.15383) | — |
| **FlashPrefill V2: Block-Sparse Prefill Attention for Long-Context LLM Serving** | Fresh / preprint | long-context LLM serving / block-sparse prefill attention / GPU kernel | [Link](https://arxiv.org/abs/2608.19758) | — |
| **FluxBin: Flexible LUT-based Ultra-low-bit LLM Inference by Algorithm-Kernel Synergy** | Fresh / preprint | LLM quantization / CUDA kernel co-design | [Link](https://arxiv.org/abs/2608.15602) | — |
| **From LLM Inference to Agentic Workloads: Characterization and Implications for Serving Systems** | Fresh / preprint | agentic serving characterization / systems benchmark | [Link](https://arxiv.org/abs/2608.15127) | — |
| **From Local Mismatch to Global Impact: Optimizing Cache Reuse Policy for Efficient Diffusion** | Fresh / preprint | diffusion cache policy / video-image generation acceleration | [Link](https://arxiv.org/abs/2608.13043) | — |
| **Global Simulation-Guided Dynamic Operator Scheduling for Efficient Multi-Tenant Model Serving** | Fresh / preprint | multi-tenant model serving / operator-level scheduling | [Link](https://arxiv.org/abs/2608.15762) | — |
| **GraniKV: Asymmetric Granularity KV-Cache Paging for Multi-Agent Systems with Long Shared Prefix** | Fresh / preprint | KV-cache paging / multi-agent serving | [Link](https://arxiv.org/abs/2608.15584) | — |
| **LinCa: Accelerating Diffusion Models via Learnable Decomposed Feature Caching** | Fresh / preprint | diffusion/video generation acceleration / feature caching | [Link](https://arxiv.org/abs/2608.17973) | — |
| **Optimize Your Sampling: Tuned Diffusion Sampling with Bayesian Optimization** | Fresh / preprint | diffusion sampling acceleration | [Link](https://arxiv.org/abs/2608.18040) | — |
| **PTXBench: Benchmark and Adapt LLMs for GPU Kernel Optimization with Architecture-specific PTX** | Fresh / preprint | GPU kernel / LLM code generation / benchmark | [Link](https://arxiv.org/abs/2608.17379) | — |
| **Reflex: Enabling Fast and Predictive Vision-Language-Action Models for Reaction-Critical Manipulation** | Fresh / preprint | fast VLA runtime / reaction-critical manipulation | [Link](https://arxiv.org/abs/2608.14379) | — |
| **rl-triton: High-Performance Triton GPU Kernels for Reinforcement Learning Credit Assignment** | Fresh / preprint | GPU kernel / Triton / RL infrastructure | [Link](https://arxiv.org/abs/2608.17641) | — |
| **Rollplex: Cross-Phase GPU Spatial Sharing for Vision Language Model Post-Training** | Fresh / preprint | VLM post-training / GPU spatial sharing / RL runtime | [Link](https://arxiv.org/abs/2608.14498) | — |
| **SCOPE: Subspace Clustering with Online Per-Head Top-K Estimation for Sparse Video Attention** | Fresh / preprint | sparse video attention / DiT inference | [Link](https://arxiv.org/abs/2608.12780) | — |
| **TEMPO: Makespan-Aware Expert-Parallel Load Balancing Across Memory- and Compute-Bound Regimes** | Fresh / preprint | MoE expert-parallel load balancing / serving | [Link](https://arxiv.org/abs/2608.13057) | — |
| **TileMix: Tile-Centric Mixed-Precision Attention for LLM Inference Acceleration** | Fresh / preprint | mixed-precision attention kernel / long-context inference | [Link](https://arxiv.org/abs/2608.17336) | — |
