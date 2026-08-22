# 12 · Diffusion / Flow Acceleration

> **96 canonical papers** mapped here, plus a broader **23-paper Latest-30-Day tracker** using P0/P1/P2 tiers. Cross-direction duplication is intentional when a paper has multiple technical roles.

[← Research Map](README.md) · [🆕 Latest 30 Days](LATEST_30D.md) · [🏛️ Classical](CLASSICAL.md) · [Paper Library](ALL_PAPERS.md)

## 🆕 Latest 30 Days · 23 tracked

| Priority | Paper | Venue | Topic | Paper | Code |
|---|---|---|---|---|---|
| **P0 · Strong** | **Role-Conditioned Sub-Token Routing for Efficient Vision-Language-Action Policies** | Fresh / preprint | VLA efficiency / KV compression / sub-token routing | [Link](https://arxiv.org/abs/2608.18410) | — |
| **P1 · Watch** | **EDITBRIDGE: Towards Faithful and Efficient Ultra-High-Resolution Image Editing** | Fresh / preprint | image editing / diffusion / block-wise sparse attention | [Link](https://arxiv.org/abs/2608.18063) | — |
| **P0 · Strong** | **Optimize Your Sampling: Tuned Diffusion Sampling with Bayesian Optimization** | Fresh / preprint | diffusion sampling acceleration | [Link](https://arxiv.org/abs/2608.18040) | — |
| **P0 · Strong** | **AViTS: Adaptive Spatiotemporal Token Selection for Efficient Dynamic-Resolution Generation** | Fresh / preprint | diffusion/image generation acceleration / adaptive token selection | [Link](https://arxiv.org/abs/2608.17995) | — |
| **P0 · Strong** | **LinCa: Accelerating Diffusion Models via Learnable Decomposed Feature Caching** | Fresh / preprint | diffusion/video generation acceleration / feature caching | [Link](https://arxiv.org/abs/2608.17973) | — |
| **P0 · Strong** | **Magnitude-Direction Decoupling for Fast Video Generation with Flow Matching Models** | Fresh / preprint | video generation acceleration / flow matching | [Link](https://arxiv.org/abs/2608.17695) | — |
| **P0 · Strong** | **rl-triton: High-Performance Triton GPU Kernels for Reinforcement Learning Credit Assignment** | Fresh / preprint | GPU kernel / Triton / RL infrastructure | [Link](https://arxiv.org/abs/2608.17641) | — |
| **P0 · Strong** | **PTXBench: Benchmark and Adapt LLMs for GPU Kernel Optimization with Architecture-specific PTX** | Fresh / preprint | GPU kernel / LLM code generation / benchmark | [Link](https://arxiv.org/abs/2608.17379) | — |
| **P0 · Strong** | **An Empirical Study of Training Pixel-Space Text-to-Image Diffusion Models** | Fresh / preprint | image generation acceleration | [Link](https://arxiv.org/abs/2608.16887) | — |
| **P0 · Strong** | **DriveCache: Action-Aware Caching for Driving World Model Inference** | Fresh / preprint | world-model / diffusion caching | [Link](https://arxiv.org/abs/2608.16354) | — |
| **P2 · Relevant** | **Nexus: Structured Synergy for Efficient Text-to-Image Generation using Rectified Flow Model** | Fresh / preprint | image generation / sparse architecture / low-bit / flow matching | [Link](https://arxiv.org/abs/2608.16104) | — |
| **P0 · Strong** | **EcoVLA: Energy-Efficient Device-Edge Co-Inference for Vision-Language-Action Models under Real-Time Constraints** | Fresh / preprint | VLA device-edge co-inference / energy-aware runtime | [Link](https://arxiv.org/abs/2608.15502) | — |
| **P0 · Strong** | **DeaMoE: Efficient MoE Structure for Fast Small-Batch Decoding** | Fresh / preprint | MoE architecture / small-batch decoding | [Link](https://arxiv.org/abs/2608.14385) | — |
| **P0 · Strong** | **Reflex: Enabling Fast and Predictive Vision-Language-Action Models for Reaction-Critical Manipulation** | Fresh / preprint | fast VLA runtime / reaction-critical manipulation | [Link](https://arxiv.org/abs/2608.14379) | — |
| **P0 · Strong** | **Beyond Capacity: Scalable MoE LLM Inference via High-Bandwidth Flash with Direct GPU and HBM Paths** | Fresh / preprint | MoE serving / high-bandwidth flash architecture | [Link](https://arxiv.org/abs/2608.14333) | — |
| **P0 · Strong** | **From Local Mismatch to Global Impact: Optimizing Cache Reuse Policy for Efficient Diffusion** | Fresh / preprint | diffusion cache policy / video-image generation acceleration | [Link](https://arxiv.org/abs/2608.13043) | — |
| **P0 · Strong** | **SCOPE: Subspace Clustering with Online Per-Head Top-K Estimation for Sparse Video Attention** | Fresh / preprint | sparse video attention / DiT inference | [Link](https://arxiv.org/abs/2608.12780) | — |
| **P2 · Relevant** | **Spec Sheets Are Not Kernels: An ISA- and Source-Level Audit of INT8 Availability on NVIDIA Blackwell Ultra** | Fresh / preprint | llm_serving / quant / kernel / gen | [Link](https://arxiv.org/abs/2608.11693) | — |
| **P2 · Relevant** | **SparseDitto: Customizing GPU Kernels for Different Sparsity Patterns with LLM-Based Agentic System** | Fresh / preprint | sparse / kernel / gen / agent / edge | [Link](https://arxiv.org/abs/2608.05033) | — |
| **P2 · Relevant** | **SPADE: An Input-Adaptive Sparse Attention Engine for Fast Video Diffusion Models Inference** | Fresh / preprint | LLM serving; sparsity / pruning; generation acceleration; edge / heterogeneous AI | [Link](https://arxiv.org/abs/2608.03335) | — |
| **P2 · Relevant** | **WAM-Diff2: Hierarchical AR-to-Diffusion Distillation for Highly Efficient Autonomous Driving VLA** | Fresh / preprint | LLM serving; multimodal / MLLM; Physical AI | [Link](https://arxiv.org/abs/2608.01035) | — |
| **P2 · Relevant** | **OnlineCache: Learning Dynamic Caching Policies with Error Correction for Efficient Diffusion Inference** | Fresh / preprint | LLM serving; generation acceleration; edge / heterogeneous AI | [Link](https://arxiv.org/abs/2607.29398) | — |
| **P1 · Watch** | **Sparse by Command: Task-Conditional Compute Skipping for Multi-Task Inference Accelerators** | Fresh / preprint | llm_serving / quant / sparse / gen / edge | [Link](https://arxiv.org/abs/2607.22038) | — |

## 🏛️ Classical / Historical · 81 canonical

| Priority | Paper | Venue | Topic | Paper | Code |
|---|---|---|---|---|---|
| **Canonical** | **Focus-dLLM: Accelerating Long-Context Diffusion LLM Inference via Confidence-Guided Context Focusing** | ACL 2026 | diffusion LLM / sparse attention | [Link](https://doi.org/10.18653/v1/2026.acl-long.556) | — |
| **Canonical** | **AB-Cache: Training-Free Acceleration of Diffusion Models via Adams-Bashforth Cached Feature Reuse** | ACM Multimedia 2025 | diffusion caching / generative inference acceleration | [Link](https://arxiv.org/abs/2504.10540) | — |
| **Canonical** | **Accelerating Diffusion Transformer via Error-Optimized Cache** | ACM Multimedia 2025 | diffusion transformer inference / feature caching | [Link](https://arxiv.org/abs/2501.19243) | — |
| **Canonical** | **Compute Only 16 Tokens in One Timestep: Accelerating Diffusion Transformers with Cluster-Driven Feature Caching** | ACM Multimedia 2025 | diffusion token/feature caching | [Link](https://arxiv.org/abs/2509.10312) | — |
| **Canonical** | **DilateQuant: Accurate and Efficient Quantization-Aware Training for Diffusion Models via Weight Dilation** | ACM Multimedia 2025 | diffusion quantization / efficient inference | [Link](https://arxiv.org/abs/2409.14307) | — |
| **Canonical** | **Single Trajectory Distillation for Accelerating Image and Video Style Transfer** | ACM Multimedia 2025 | diffusion/style-transfer acceleration / trajectory distillation | [Link](https://arxiv.org/abs/2412.18945) | — |
| **Canonical** | **SpeCa: Accelerating Diffusion Transformers with Speculative Feature Caching** | ACM Multimedia 2025 | diffusion speculative caching | [Link](https://arxiv.org/abs/2509.11628) | — |
| **Canonical** | **UltraVSR: Achieving Ultra-Realistic Video Super-Resolution with Efficient One-Step Diffusion Space** | ACM Multimedia 2025 | one-step diffusion / efficient video super-resolution | [Link](https://arxiv.org/abs/2505.19958) | [Repo](https://github.com/yongliuy/UltraVSR) |
| **Canonical** | **TetriServe: Efficiently Serving Mixed DiT Workloads** | ASPLOS 2026 | diffusion/DiT serving / scheduling | [Link](https://arxiv.org/abs/2510.01565) | — |
| **Canonical** | **E2-RAG: Towards Editable Efficient RAG by Editing Compressed KV Caches** | COLM 2025 | RAG / compressed KV cache / editable cache | — | [Repo](https://github.com/tongxuluo/e2rag) |
| **Canonical** | **Accelerating Autoregressive Video Diffusion via History-Guided Cache and Residual Correction** | CVPR 2026 | autoregressive video diffusion / caching | — | — |
| **Canonical** | **Accelerating Diffusion-based Video Editing via Heterogeneous Caching: Beyond Full Computing at Sampled Denoising Timestep** | CVPR 2026 | video diffusion editing / heterogeneous caching | — | — |
| **Canonical** | **Adaptive Spectral Feature Forecasting for Diffusion Sampling Acceleration** | CVPR 2026 | diffusion/video generation acceleration / spectral feature forecasting / long-range reuse | [Link](https://arxiv.org/abs/2603.01623) | [Repo](https://github.com/hanjq17/Spectrum) |
| **Canonical** | **Attention Surgery: An Efficient Recipe to Linearize Your Video Diffusion Transformer** | CVPR 2026 | video diffusion / linear attention / mobile inference | — | — |
| **Canonical** | **D2Cache: Second-Order Delta Caching for Higher Video Diffusion Acceleration** | CVPR 2026 | video diffusion / second-order caching | — | — |
| **Canonical** | **DeltaQuant: 4-bit Video Diffusion Models with Spatiotemporal Delta Smoothing** | CVPR 2026 | video diffusion / W4A4 quantization / efficient kernels | — | — |
| **Canonical** | **Denoising as Path Planning: Training-Free Acceleration of Diffusion Models with DPCache** | CVPR 2026 | diffusion / cache scheduling | — | — |
| **Canonical** | **Forecast the Principal, Stabilize the Residual: Subspace-Aware Feature Caching for Diffusion Transformers** | CVPR 2026 | diffusion / subspace-aware feature caching | — | — |
| **Canonical** | **Otil: Accelerating Diffusion Model Inference via Communication-Efficient Multi-GPU Parallelism** | CVPR 2026 | diffusion inference / multi-GPU / communication reduction | — | — |
| **Canonical** | **QuantVLA: Scale-Calibrated Post-Training Quantization for Vision-Language-Action Models** | CVPR 2026 | VLA / PTQ / Physical AI / diffusion action head | — | — |
| **Canonical** | **ResCa: Residual Caching for Diffusion Transformers Acceleration** | CVPR 2026 | diffusion transformer / residual caching | — | — |
| **Canonical** | **SeaCache: Spectral-Evolution-Aware Cache for Accelerating Diffusion Models** | CVPR 2026 | diffusion / spectral caching | — | — |
| **Canonical** | **SenCache: Accelerating Diffusion Model Inference via Sensitivity-Aware Caching** | CVPR 2026 | diffusion inference / sensitivity-aware caching | — | — |
| **Canonical** | **RADiT: Redundancy-Aware Diffusion Transformer Acceleration Leveraging Timestep Similarity** | DAC 2025 | diffusion / DiT acceleration / hardware-software co-design | [Link](https://doi.org/10.1109/DAC63849.2025.11133190) | — |
| **Canonical** | **SQ-DM: Accelerating Diffusion Models with Aggressive Quantization and Temporal Sparsity** | DAC 2025 | diffusion acceleration / low-bit quantization / temporal activation sparsity / accelerator co-design | [Link](https://arxiv.org/abs/2501.15448) | — |
| **Canonical** | **AdaDiff: Accelerating Diffusion Models through Step-Wise Adaptive Computation** | ECCV 2024 | diffusion acceleration / adaptive computation / early exit | [Link](https://arxiv.org/abs/2309.17074) | [Repo](https://github.com/Tangshengku/AdaDiff) |
| **Canonical** | **BK-SDM: A Lightweight, Fast, and Cheap Version of Stable Diffusion** | ECCV 2024 | diffusion pruning / compact model | — | — |
| **Canonical** | **Efficient Diffusion Transformer with Step-wise Dynamic Attention Mediators** | ECCV 2024 | diffusion/flow acceleration / efficient attention | — | — |
| **Canonical** | **HiDiffusion: Unlocking Higher-Resolution Creativity and Efficiency in Pretrained Diffusion Models** | ECCV 2024 | diffusion inference acceleration | — | — |
| **Canonical** | **Inf-DiT: Upsampling any-resolution image with memory-efficient diffusion transformer.** | ECCV 2024 | diffusion memory efficiency | — | — |
| **Canonical** | **MixDQ: Memory-Efficient Few-Step Text-to-Image Diffusion Models with Metric-Decoupled Mixed Precision Quantization** | ECCV 2024 | diffusion quantization | — | — |
| **Canonical** | **Mixture of Efficient Diffusion Experts Through Automatic Interval and Sub-Network Selection** | ECCV 2024 | diffusion/flow acceleration / pruning | — | — |
| **Canonical** | **Post-training Quantization with Progressive Calibration and Activation Relaxing for Text-to-Image Diffusion Models** | ECCV 2024 | diffusion quantization | — | — |
| **Canonical** | **SlimFlow: Training Smaller One-Step Diffusion Models with Rectified Flow** | ECCV 2024 | compact one-step diffusion | — | — |
| **Canonical** | **Timestep-Aware Correction for Quantized Diffusion Models** | ECCV 2024 | diffusion quantization | — | — |
| **Canonical** | **Alignment-Augmented Speculative Decoding with Alignment Sampling and Conditional Verification** | EMNLP 2025 | speculative decoding / conditional verification | [Link](https://doi.org/10.18653/v1/2025.emnlp-main.343) | — |
| **Canonical** | **DynamicKV: Task-Aware Adaptive KV Cache Compression for Long Context LLMs** | EMNLP 2025 Findings | KV cache compression / task-aware adaptive allocation | [Link](https://doi.org/10.18653/v1/2025.findings-emnlp.426) | — |
| **Canonical** | **FlashPS: Efficient Generative Image Editing with Mask-aware Caching and Scheduling** | EuroSys 2026 | diffusion serving / image editing / activation caching / continuous batching | [Link](https://arxiv.org/abs/2505.20600) | — |
| **Canonical** | **Accelerating Diffusion Transformer via Gradient-Optimized Cache** | ICCV 2025 | diffusion transformer feature caching | — | — |
| **Canonical** | **Adaptive Caching for Faster Video Generation with Diffusion Transformers** | ICCV 2025 | video diffusion acceleration / adaptive feature caching | [Link](https://arxiv.org/abs/2411.02397) | — |
| **Canonical** | **CHORDS: Diffusion Sampling Accelerator with Multi-core Hierarchical ODE Solvers** | ICCV 2025 | diffusion sampling acceleration / multi-core parallel ODE solvers | [Link](https://arxiv.org/abs/2507.15260) | [Repo](https://github.com/hanjq17/CHORDS) |
| **Canonical** | **Fewer Denoising Steps or Cheaper Per-Step Inference: Towards Compute-Optimal Diffusion Model Deployment** | ICCV 2025 | diffusion deployment / compute-optimal inference | — | — |
| **Canonical** | **From Reusing to Forecasting: Accelerating Diffusion Models with TaylorSeers** | ICCV 2025 | diffusion acceleration / feature forecasting | [Link](https://arxiv.org/abs/2503.06923) | [Repo](https://github.com/Shenyi-Z/TaylorSeer) |
| **Canonical** | **Model Reveals What to Cache: Profiling-Based Feature Reuse for Video Diffusion Models** | ICCV 2025 | video diffusion acceleration / profiling-guided feature reuse | [Link](https://arxiv.org/abs/2504.03140) | — |
| **Canonical** | **QuantCache: Adaptive Importance-Guided Quantization with Hierarchical Latent and Layer Caching for Video Generation** | ICCV 2025 | video diffusion acceleration / quantization + caching | — | — |
| **Canonical** | **QuEST: Low-bit Diffusion Model Quantization via Efficient Selective Finetuning** | ICCV 2025 | diffusion low-bit quantization | — | — |
| **Canonical** | **Text Embedding Knows How to Quantize Text-Guided Diffusion Models** | ICCV 2025 | diffusion quantization / dynamic precision | — | — |
| **Canonical** | **Towards Stabilized and Efficient Diffusion Transformers through Long-Skip-Connections with Spectral Constraints** | ICCV 2025 | diffusion transformer training/inference acceleration | — | — |
| **Canonical** | **Fast-dLLM v2: Efficient Block-Diffusion LLM** | ICLR 2026 | diffusion LLM inference / block diffusion / hierarchical caching | [Link](https://arxiv.org/abs/2509.26328) | [Repo](https://github.com/NVlabs/Fast-dLLM) |
| **Canonical** | **Fast-dLLM: Training-free Acceleration of Diffusion LLM by Enabling KV Cache and Parallel Decoding** | ICLR 2026 | diffusion LLM inference / KV cache / parallel decoding | [Link](https://arxiv.org/abs/2505.22618) | [Repo](https://github.com/NVlabs/Fast-dLLM) |
| **Canonical** | **AsymRnR: Video Diffusion Transformers Acceleration with Asymmetric Reduction and Restoration** | ICML 2025 | video diffusion transformer token reduction / training-free acceleration | — | [Repo](https://github.com/wenhao728/AsymRnR) |
| **Canonical** | **Ca2-VDM: Efficient Autoregressive Video Diffusion Model with Causal Generation and Cache Sharing** | ICML 2025 | video diffusion acceleration | — | — |
| **Canonical** | **Diffusion Adversarial Post-Training for One-Step Video Generation** | ICML 2025 | one-step video/image diffusion generation | — | — |
| **Canonical** | **Modulated Diffusion: Accelerating Generative Modeling with Modulated Quantization** | ICML 2025 | diffusion acceleration / quantization | — | — |
| **Canonical** | **Morse: Dual-Sampling for Lossless Acceleration of Diffusion Models** | ICML 2025 | diffusion sampling acceleration | — | [Repo](https://github.com/deep-optimization/Morse) |
| **Canonical** | **Q-VDiT: Towards Accurate Quantization and Distillation of Video-Generation Diffusion Transformers** | ICML 2025 | video diffusion quantization / distillation | — | [Repo](https://github.com/wlfeng0509/Q-VDiT) |
| **Canonical** | **Sparse Video-Gen: Accelerating Video Diffusion Transformers with Spatial-Temporal Sparsity** | ICML 2025 | video/image generation acceleration / efficient attention | — | — |
| **Canonical** | **Sparse ActionGen: Accelerating Diffusion Policy with Real-time Pruning** | ICML 2026 | Physical AI / diffusion-policy acceleration / pruning+reuse | [Link](https://arxiv.org/abs/2601.12894) | — |
| **Canonical** | **Accelerating Diffusion-based Super-Resolution with Dynamic Time-Spatial Sampling** | IJCAI 2025 | diffusion acceleration / adaptive sampling / image generation efficiency | [Link](https://doi.org/10.24963/ijcai.2025/199) | — |
| **Canonical** | **DiTPA: A DiT-based Action Planner Accelerator Exploiting Action-Denoising-Multimodality Redundancy for Embodied Artificial Intelligence** | ISCA 2026 | Physical AI / embodied action planner / DiT accelerator | — | — |
| **Canonical** | **HLX** | MICRO 2025 | MoE + diffusion + tensor compression + hybrid LM + reasoning + edge training acceleration | — | — |
| **Canonical** | **LLM.265** | MICRO 2025 | MoE + diffusion + tensor compression + hybrid LM + reasoning + edge training acceleration | — | — |
| **Canonical** | **ORCHES** | MICRO 2025 | MoE + diffusion + tensor compression + hybrid LM + reasoning + edge training acceleration | — | — |
| **Canonical** | **REACT3D** | MICRO 2025 | MoE + diffusion + tensor compression + hybrid LM + reasoning + edge training acceleration | — | — |
| **Canonical** | **S-DMA** | MICRO 2025 | MoE + diffusion + tensor compression + hybrid LM + reasoning + edge training acceleration | — | — |
| **Canonical** | **Stratum** | MICRO 2025 | MoE + diffusion + tensor compression + hybrid LM + reasoning + edge training acceleration | — | — |
| **Canonical** | **Confidant: Customizing Transformer-based LLMs via Collaborative Training on Mobile Devices** | MobiCom 2025 | edge AI / mobile LLM training / pipeline parallelism / heterogeneous scheduling | [Link](https://arxiv.org/abs/2311.13381) | — |
| **Canonical** | **Elastic On-Device LLM Service** | MobiCom 2025 | on-device LLM service / elastic model and prompt adaptation | [Link](https://arxiv.org/abs/2409.09071) | — |
| **Canonical** | **Block-Diagonal LoRA for Eliminating Communication Overhead in Tensor Parallel LoRA Serving** | NeurIPS 2025 | LoRA serving / tensor parallel communication elimination | [Link](https://doi.org/10.52202/085713-0010) | — |
| **Canonical** | **Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion** | NeurIPS 2025 | autoregressive video diffusion / streaming generation | [Link](https://doi.org/10.52202/085713-5576) | — |
| **Canonical** | **Efficient LLM Serving on Commodity GPU Clusters with Data-Reduced Cross-Instance Orchestration** | OSDI 2026 | commodity-GPU LLM serving | — | — |
| **Canonical** | **ChituDiffusion: A Data-Characteristic-Aware Serving System for Diffusion Models** | PPoPP 2026 | diffusion serving / compile-runtime co-optimization | [Link](https://doi.org/10.1145/3774934.3786424) | — |
| **Canonical** | **MixFusion: A Patch-Level Parallel Serving System for Mixed-Resolution Diffusion Models** | PPoPP 2026 | diffusion serving / patch-level parallelism | [Link](https://doi.org/10.1145/3774934.3786420) | — |
| **Canonical** | **CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision** | RSS 2025 | Physical AI / lightweight VLA / high-throughput robot inference | [Link](https://arxiv.org/abs/2411.00508) | [Repo](https://github.com/clip-rt/clip-rt) |
| **Canonical** | **FAST: Efficient Action Tokenization for Vision-Language-Action Models** | RSS 2025 | Physical AI / VLA action tokenization / efficient training and inference | [Link](https://arxiv.org/abs/2501.09747) | — |
| **Canonical** | **Unified Video Action Model** | RSS 2025 | Physical AI / efficient world-action model inference | [Link](https://doi.org/10.15607/RSS.2025.XXI.074) | — |
| **Canonical** | **Muninn: Your Trajectory Diffusion Model But Faster** | RSS 2026 | Physical AI / trajectory diffusion acceleration / training-free cache reuse | [Link](https://arxiv.org/abs/2605.09999) | [Repo](https://github.com/gokulp01/Muninn) |
| **Canonical** | **SGLB: Scalable and Robust Global Load Balancing in Commodity AI Clusters** | SIGCOMM 2025 | KV encoding + MoE training fabric + long-context training + AI networking/inference | [Link](https://doi.org/10.1145/3718958.3750527) | — |
| **Canonical** | **Katz** | USENIX ATC 2025 | production KV-cache + quantized-kernel compiler + diffusion workflow serving | — | — |
| **Canonical** | **KVCache Cache in the Wild** | USENIX ATC 2025 | production KV-cache + quantized-kernel compiler + diffusion workflow serving | — | — |
| **Canonical** | **QFactory** | USENIX ATC 2025 | production KV-cache + quantized-kernel compiler + diffusion workflow serving | — | — |
