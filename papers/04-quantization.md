# 04 · Quantization

> **79 papers** currently mapped to this direction. Cross-direction duplication is intentional when a paper has multiple technical roles.

[← Research Map](README.md) · [Complete Paper List](ALL_PAPERS.md)

| Paper | Venue | Topic | Paper | Code |
|---|---|---|---|---|
| **Efficient Multimodal Large Language Model via Dynamic KV Cache Quantization** | AAAI 2026 | MLLM inference / KV cache quantization | [Link](https://doi.org/10.1609/aaai.v40i25.39241) | — |
| **KVmix: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for KV Cache** | AAAI 2026 | KV cache quantization / mixed precision | [Link](https://doi.org/10.1609/aaai.v40i37.40422) | — |
| **BTC-LLM: Efficient Sub-1-Bit LLM Quantization via Learnable Transformation and Binary Codebook** | ACL 2026 | quantization / efficient LLM inference | [Link](https://doi.org/10.18653/v1/2026.acl-long.1066) | — |
| **VecInfer: Efficient LLM Inference with Low-Bit KV Cache via Outlier-Suppressed Vector Quantization** | ACL 2026 | KV-cache quantization / low-bit LLM inference / CUDA kernel | [Link](https://doi.org/10.18653/v1/2026.acl-long.1454) | — |
| **DilateQuant: Accurate and Efficient Quantization-Aware Training for Diffusion Models via Weight Dilation** | ACM Multimedia 2025 | diffusion quantization / efficient inference | [Link](https://arxiv.org/abs/2409.14307) | — |
| **Quantization Meets OOD: Generalizable Quantization-aware Training from a Flatness Perspective** | ACM Multimedia 2025 | quantization-aware training / OOD generalization | [Link](https://arxiv.org/abs/2509.00859) | — |
| **Mugi: Value Level Parallelism For Efficient LLMs** | ASPLOS 2026 | LLM accelerator / value-level parallelism / low precision | [Link](https://arxiv.org/abs/2601.10823) | — |
| **KVSink: Understanding and Enhancing the Preservation of Attention Sinks in KV Cache Quantization for LLMs** | COLM 2025 | KV cache quantization / attention sinks | [Link](https://arxiv.org/abs/2508.04257) | — |
| **SQuat: Subspace-orthogonal KV Cache Quantization** | COLM 2025 | KV cache quantization | [Link](https://arxiv.org/abs/2503.24358) | — |
| **DeltaQuant: 4-bit Video Diffusion Models with Spatiotemporal Delta Smoothing** | CVPR 2026 | video diffusion / W4A4 quantization / efficient kernels | — | — |
| **QuantVLA: Scale-Calibrated Post-Training Quantization for Vision-Language-Action Models** | CVPR 2026 | VLA / PTQ / Physical AI / diffusion action head | — | — |
| **StreamingTOM: Streaming Token Compression for Efficient Video Understanding** | CVPR 2026 | streaming video / token compression / bounded KV cache | — | — |
| **VLM-PTQ: Efficient Post-Training Quantization for Large Vision-Language Models** | CVPR 2026 | multimodal quantization / VLM PTQ | — | — |
| **SQ-DM: Accelerating Diffusion Models with Aggressive Quantization and Temporal Sparsity** | DAC 2025 | diffusion acceleration / low-bit quantization / temporal activation sparsity / accelerator co-design | [Link](https://arxiv.org/abs/2501.15448) | — |
| **MixDQ: Memory-Efficient Few-Step Text-to-Image Diffusion Models with Metric-Decoupled Mixed Precision Quantization** | ECCV 2024 | diffusion quantization | — | — |
| **Post-training Quantization with Progressive Calibration and Activation Relaxing for Text-to-Image Diffusion Models** | ECCV 2024 | diffusion quantization | — | — |
| **Timestep-Aware Correction for Quantized Diffusion Models** | ECCV 2024 | diffusion quantization | — | — |
| **QSpec: Speculative Decoding with Complementary Quantization Schemes** | EMNLP 2025 | speculative decoding / quantization | [Link](https://doi.org/10.18653/v1/2025.emnlp-main.240) | — |
| **XQuant: Achieving Ultra-Low Bit KV Cache Quantization with Cross-Layer Compression** | EMNLP 2025 | KV cache quantization / long-context inference | [Link](https://doi.org/10.18653/v1/2025.emnlp-main.494) | — |
| **More Tokens, Lower Precision: Towards the Optimal Token-Precision Trade-off in KV Cache Compression** | EMNLP 2025 Findings | KV cache compression / token-precision co-optimization | [Link](https://doi.org/10.18653/v1/2025.findings-emnlp.429) | — |
| **FlexiQ: Adaptive Mixed-Precision Quantization for Latency/Accuracy Trade-Offs in Deep Neural Networks** | EuroSys 2026 | adaptive mixed-precision quantization / runtime accuracy-latency tradeoff / NPU-GPU inference | [Link](https://arxiv.org/abs/2510.02822) | — |
| **Scaling LLM Test-Time Compute with Mobile NPU on Smartphones** | EuroSys 2026 | on-device LLM reasoning / mobile NPU / hardware-aware quantization | [Link](https://arxiv.org/abs/2509.23324) | — |
| **HGQ: High Granularity Quantization for Real-time Neural Networks on FPGAs** | FPGA 2026 | quantization / FPGA / low-latency inference | [Link](https://arxiv.org/abs/2405.00645) | — |
| **Hummingbird+: Advancing FPGA-based LLM Deployment from Research Prototype to Edge Product** | FPGA 2026 | edge LLM inference / FPGA accelerator / deployment | [Link](https://doi.org/10.1145/3748173.3779189) | — |
| **KANELÉ: Kolmogorov-Arnold Networks for Efficient LUT-based Evaluation** | FPGA 2026 | efficient FPGA ML inference / LUT neural networks | [Link](https://arxiv.org/abs/2512.12850) | — |
| **AQPIM: Breaking the PIM Capacity Wall for LLMs with In-Memory Activation Quantization** | HPCA 2026 | PIM / activation quantization / long-context LLM | [Link](https://arxiv.org/abs/2604.18137) | — |
| **BitDecoding: Unlocking Tensor Cores for Long-Context LLMs with Low-Bit KV Cache** | HPCA 2026 | low-bit KV cache / Tensor Core decoding | [Link](https://doi.org/10.1109/HPCA68181.2026.11408481) | — |
| **GyRot: Leveraging Hidden Synergy between Rotation and Fine-grained Group Quantization for Low-bit LLM Inference** | HPCA 2026 | low-bit LLM quantization / accelerator co-design | [Link](https://arxiv.org/abs/2607.27694) | — |
| **QuEST: Low-bit Diffusion Model Quantization via Efficient Selective Finetuning** | ICCV 2025 | diffusion low-bit quantization | — | — |
| **Text Embedding Knows How to Quantize Text-Guided Diffusion Models** | ICCV 2025 | diffusion quantization / dynamic precision | — | — |
| **KV-Cache Transform Coding for Compact Storage in LLM Inference** | ICLR 2026 | KV cache compression / LLM serving storage | — | — |
| **ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models** | ICLR 2026 | KV cache compression / efficient reasoning | — | — |
| **TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate** | ICLR 2026 | online vector quantization / KV cache compression | — | — |
| **Cache Me If You Must: Adaptive Key-Value Quantization for Large Language Models** | ICML 2025 | long-context / KV cache / efficient LLM inference | — | — |
| **CommVQ: Commutative Vector Quantization for KV Cache Compression** | ICML 2025 | KV cache quantization | — | — |
| **KVTuner: Sensitivity-Aware Layer-Wise Mixed-Precision KV Cache Quantization for Efficient and Nearly Lossless LLM Inference** | ICML 2025 | long-context / KV cache / efficient LLM inference | — | — |
| **Modulated Diffusion: Accelerating Generative Modeling with Modulated Quantization** | ICML 2025 | diffusion acceleration / quantization | — | — |
| **Q-VDiT: Towards Accurate Quantization and Distillation of Video-Generation Diffusion Transformers** | ICML 2025 | video diffusion quantization / distillation | — | [Repo](https://github.com/wlfeng0509/Q-VDiT) |
| **QuantSpec: Self-Speculative Decoding with Hierarchical Quantized KV Cache** | ICML 2025 | speculative decoding / KV quantization | — | — |
| **Attn-QAT: 4-Bit Attention With Quantization-Aware Training** | ICML 2026 | FP4 attention / quantization-aware training / fused attention kernels | [Link](https://arxiv.org/abs/2603.00040) | — |
| **SALE : Low-bit Estimation for Efficient Sparse Attention in Long-context LLM Prefilling** | ICML 2026 | efficient attention / low-bit estimation / long-context prefill | [Link](https://arxiv.org/abs/2505.24179) | — |
| **FBQuant: FeedBack Quantization for Large Language Models** | IJCAI 2025 | LLM weight quantization / CUDA kernel | [Link](https://arxiv.org/abs/2501.16385) | — |
| **MPPQ: Enhancing Post-Training Quantization for LLMs via Mixed Supervision, Proxy Rounding, and Pre-Searching** | IJCAI 2025 | LLM post-training quantization / W4A4 | [Link](https://doi.org/10.24963/ijcai.2025/920) | — |
| **RotateKV: Accurate and Robust 2-Bit KV Cache Quantization for LLMs via Outlier-Aware Adaptive Rotations** | IJCAI 2025 | KV-cache quantization / low-bit inference | [Link](https://arxiv.org/abs/2501.16383) | — |
| **AQuant: Repurposing CODEC for VLM Acceleration via Adaptive Quantization** | ISCA 2026 | VLM acceleration / adaptive quantization / hardware co-design | — | — |
| **Cassandra: Enabling Reasoning LLMs at Edge via Self-Speculative Decoding** | ISCA 2026 | edge speculative reasoning + quantization + memory-system + generative inference accelerators | [Link](https://arxiv.org/abs/2605.26558) | — |
| **EVA: Accelerating LLM Decoding via an Efficient Vector Quantization Architecture** | ISCA 2026 | LLM decoding / vector quantization accelerator | — | — |
| **MXFFP: Microscaling Flexible Floating Point Format for Large-Scale AI Model Acceleration** | ISCA 2026 | low-precision formats / accelerator | — | — |
| **OASIS: Outlier-Aware LUT-Based GEMM with Dual-Side Quantization for LLM Inference Acceleration** | ISCA 2026 | edge speculative reasoning + quantization + memory-system + generative inference accelerators | — | — |
| **Omni-LUT: Energy-Efficient LUT-based Accelerator with Hardware-Aware KV Cache Quantization** | ISCA 2026 | LLM inference accelerator / LUT / KV-cache quantization | — | — |
| **Raptor** | ISCA 2026 | edge speculative reasoning + quantization + memory-system + generative inference accelerators | — | — |
| **SHyLA: 3D-Stacked NVM-DRAM Hybrid LLM-Inference Architecture Exploiting Data and Memory Heterogeneity** | ISCA 2026 | edge speculative reasoning + quantization + memory-system + generative inference accelerators | — | — |
| **SingularBit: Exploiting Synergy of Singular Value Decomposition and Low-Bit Quantization for Weight and KV Compression in LLM Inference** | ISCA 2026 | quantization / KV compression / SVD | — | — |
| **SMOOTH: Hardware-Assisted Fine-Grained On-Chip Memory Management for Efficient On-Device LLM Inference** | ISCA 2026 | edge speculative reasoning + quantization + memory-system + generative inference accelerators | — | — |
| **SEPTQ: A Simple and Effective Post-Training Quantization Paradigm for Large Language Models** | KDD 2025 | LLM post-training quantization / low-bit inference | [Link](https://arxiv.org/abs/2604.10091) | — |
| **Amove: Accelerating LLMs through Mitigating Outliers and Salient Points via Fine-Grained Grouped Vectorized Data Type** | MICRO 2025 | LLM quantization / vectorized datatype | — | — |
| **AxCore: A Quantization-Aware Approximate GEMM Unit for LLM Inference** | MICRO 2025 | LLM quantization / accelerator | — | — |
| **MX+: Pushing the Limits of Microscaling Formats for Efficient Large Language Model Serving** | MICRO 2025 | LLM serving / low-precision microscaling | — | — |
| **IntAttention: A Fully Integer Attention Pipeline for Efficient Edge Inference** | MLSys 2026 | edge inference / integer attention | — | — |
| **Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost** | MLSys 2026 | KV cache quantization / low-bit inference | — | — |
| **MorphServe: Efficient and Workload-Aware LLM Serving via Runtime Quantized Layer Swapping and KV Cache Resizing** | MLSys 2026 | LLM serving / dynamic quantization / KV resizing | — | — |
| **SageAttention3: Microscaling FP4 Attention for Inference and An Exploration of 8-Bit Training** | NeurIPS 2025 | low-bit attention kernel / FP4 | [Link](https://doi.org/10.52202/085713-1799) | — |
| **ADAngel: Accelerating Arbitrary-Precision Quantized LLMs with Adaptive Computing Mapping** | OSDI 2026 | arbitrary-precision quantized LLM runtime | — | — |
| **Accelerating Sparse Transformer Inference on GPU** | PPoPP 2026 | sparse transformer inference + mixed-precision quantization | — | — |
| **High-Throughput Non-uniformly Quantized 3-bit LLM Inference** | PPoPP 2026 | 3-bit LLM quantization / GPU kernels | [Link](https://doi.org/10.1145/3774934.3786423) | — |
| **JanusQuant: Accurate and Efficient 2-bit KV Cache Quantization for Long-Context Inference** | PPoPP 2026 | KV cache quantization / long-context inference | [Link](https://doi.org/10.1145/3774934.3786428) | — |
| **RoMeo** | PPoPP 2026 | sparse transformer inference + mixed-precision quantization | — | — |
| **HACK: Homomorphic Acceleration via Compression of the Key-Value Cache for Disaggregated LLM Inference** | SIGCOMM 2025 | KV cache / disaggregated LLM serving / quantization | [Link](https://arxiv.org/abs/2502.03589) | — |
| **Energy-Efficient and Dequantization-Free Quantization of LLMs: A Spiking Neural Network Approach to Salient Value Mitigation** | The Web Conference 2026 | LLM quantization / edge energy efficiency / SNN | [Link](https://arxiv.org/abs/2510.19498) | — |
| **Katz** | USENIX ATC 2025 | production KV-cache + quantized-kernel compiler + diffusion workflow serving | — | — |
| **KVCache Cache in the Wild** | USENIX ATC 2025 | production KV-cache + quantized-kernel compiler + diffusion workflow serving | — | — |
| **QFactory** | USENIX ATC 2025 | production KV-cache + quantized-kernel compiler + diffusion workflow serving | — | — |
| **Silicon-Oracle (Soracle): A Multi-Modal Autoregressive Model Accelerator for Context-Aware Assistance on Mobile Platform** | VLSI Symposium 2026 | multimodal autoregressive accelerator / mobile inference | [Link](https://doi.org/10.1109/VLSITechnologyandCir65830.2026.11577228) | — |
| **SPECTRA: An Asymmetric-Precision Speculative Decoding LLM Accelerator with Product Quantization and Reconfigurable Flip-Flop Buffers in 28nm CMOS** | VLSI Symposium 2026 | speculative decoding / LLM accelerator | [Link](https://doi.org/10.1109/VLSITechnologyandCir65830.2026.11577608) | — |
| **Algorithm-Architecture Co-Design for Efficient VLA Inference via Speculative Inference and Verification** | Fresh / preprint | VLA speculative inference / algorithm-architecture co-design | [Link](https://arxiv.org/abs/2608.15636) | — |
| **Every Expert Counts: ExactMoE for Memory-Efficient W4A16 Inference** | Fresh / preprint | MoE memory-efficient W4A16 inference / GPU slot cache | [Link](https://arxiv.org/abs/2608.15383) | — |
| **FluxBin: Flexible LUT-based Ultra-low-bit LLM Inference by Algorithm-Kernel Synergy** | Fresh / preprint | LLM quantization / CUDA kernel co-design | [Link](https://arxiv.org/abs/2608.15602) | — |
| **Pre-Compiled Pipeline Shards for Distributed LLM Inference on Intel AI PC Fleets** | Fresh / preprint | distributed LLM inference / edge AI PC fleet / speculative decoding | [Link](https://arxiv.org/abs/2608.19147) | [Repo](https://github.com/labscommunity/pipeline-sharded-inference-paper) |
| **TileMix: Tile-Centric Mixed-Precision Attention for LLM Inference Acceleration** | Fresh / preprint | mixed-precision attention kernel / long-context inference | [Link](https://arxiv.org/abs/2608.17336) | — |
