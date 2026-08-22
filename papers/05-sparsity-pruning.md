# 05 · Sparsity / Pruning

> **92 papers** currently mapped to this direction. Cross-direction duplication is intentional when a paper has multiple technical roles.

[← Research Map](README.md) · [Complete Paper List](ALL_PAPERS.md)

| Paper | Venue | Topic | Paper | Code |
|---|---|---|---|---|
| **FlashSVD: Memory-Efficient Inference with Streaming for Low-Rank Models** | AAAI 2026 | sparsity/pruning / GPU kernels | [Link](https://doi.org/10.1609/aaai.v40i30.39720) | — |
| **Self-Indexing KVCache: Predicting Sparse Attention from Compressed Keys** | AAAI 2026 | KV cache compression / sparse attention / CUDA kernel | [Link](https://doi.org/10.1609/aaai.v40i33.39988) | — |
| **SlimInfer: Accelerating Long-Context LLM Inference via Dynamic Token Pruning** | AAAI 2026 | long-context LLM inference / token pruning / asynchronous KV manager | [Link](https://arxiv.org/abs/2508.06447) | [Repo](https://github.com/Longxmas/SlimInfer) |
| **Sparse Attention Across Multiple-Context KV Cache** | AAAI 2026 | RAG / sparse attention / multi-context KV cache | [Link](https://doi.org/10.1609/aaai.v40i36.40266) | — |
| **EfficientLLM: Unified Pruning-Aware Pretraining for Auto-Designed Compact Language Models** | ACL 2026 | pruning / compact edge LLM | [Link](https://doi.org/10.18653/v1/2026.acl-long.355) | — |
| **Evolving Sparsity: Leveraging Token Importance Dynamics for Efficient LLM Decoding with Sparse Attention** | ACL 2026 | sparse attention / long-context decoding | [Link](https://doi.org/10.18653/v1/2026.acl-long.530) | — |
| **Focus-dLLM: Accelerating Long-Context Diffusion LLM Inference via Confidence-Guided Context Focusing** | ACL 2026 | diffusion LLM / sparse attention | [Link](https://doi.org/10.18653/v1/2026.acl-long.556) | — |
| **Maximum Redundancy Pruning: A Principle-Driven Layerwise Sparsity Allocation for LLMs** | ACM Multimedia 2025 | LLM pruning / sparsity allocation | [Link](https://arxiv.org/abs/2503.18377) | — |
| **VISA: Group-wise Visual Token Selection and Aggregation via Graph Summarization for Efficient MLLMs Inference** | ACM Multimedia 2025 | MLLM inference / visual token pruning and aggregation | [Link](https://arxiv.org/abs/2508.17857) | — |
| **SpeContext: Enabling Efficient Long-context Reasoning with Speculative Context Sparsity in LLMs** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | [Link](https://arxiv.org/abs/2512.00722) | — |
| **STARC: Selective Token Access with Remapping and Clustering for Efficient LLM Decoding on PIM Systems** | ASPLOS 2026 | sparse attention / PIM / KV cache | [Link](https://doi.org/10.1145/3779212.3790226) | — |
| **Adaptive Computation Pruning for the Forgetting Transformer** | COLM 2025 | efficient attention / sparsity / training efficiency | [Link](https://arxiv.org/abs/2504.06949) | [Repo](https://github.com/zhixuan-lin/forgetting-transformer) |
| **Mixture of Attention Spans: Optimizing LLM Inference Efficiency with Heterogeneous Sliding-Window Lengths** | COLM 2025 | sparse attention / long-context inference / KV cache compression | [Link](https://arxiv.org/abs/2406.14909) | [Repo](https://github.com/thu-nics/MoA) |
| **FLOWER: Democratizing Generalist Robot Policies with Efficient Vision-Language-Flow Models** | CoRL 2025 | Physical AI / efficient VLA / model compression / flow policy | [Link](https://arxiv.org/abs/2509.04996) | [Repo](https://github.com/intuitive-robots/flower_vla_pret) |
| **IF-Prune: Information-Flow Guided Token Pruning for Efficient Vision-Language Models** | CVPR 2026 | VLM inference / token pruning | — | — |
| **ParallelVLM: Lossless Video-LLM Acceleration with Visual Alignment Aware Parallel Speculative Decoding** | CVPR 2026 | video-LLM / speculative decoding / visual token pruning | — | — |
| **Prune2Drive: A Plug-and-Play Framework for Accelerating Vision-Language Models in Autonomous Driving** | CVPR 2026 | autonomous driving / VLM token pruning / Physical AI | — | — |
| **TransPrune: Token Transition Pruning for Efficient Large Vision-Language Model** | CVPR 2026 | VLM inference / token pruning | — | — |
| **VLM-Pruner: Buffering for Spatial Sparsity in an Efficient VLM Centrifugal Token Pruning Paradigm** | CVPR 2026 | VLM inference / visual token pruning | — | — |
| **ZOO-Prune: Training-Free Token Pruning via Zeroth-Order Gradient Estimation in Vision-Language Models** | CVPR 2026 | VLM inference / training-free visual-token pruning / zeroth-order sensitivity | — | [Repo](https://github.com/AIM-SKKU/ZOO-Prune) |
| **SpecASR: Accelerating LLM-based Automatic Speech Recognition via Speculative Decoding** | DAC 2025 | speculative decoding / audio-language inference / real-time ASR | [Link](https://arxiv.org/abs/2507.18181) | — |
| **SQ-DM: Accelerating Diffusion Models with Aggressive Quantization and Temporal Sparsity** | DAC 2025 | diffusion acceleration / low-bit quantization / temporal activation sparsity / accelerator co-design | [Link](https://arxiv.org/abs/2501.15448) | — |
| **An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models** | ECCV 2024 | VLM visual-token pruning | — | — |
| **BK-SDM: A Lightweight, Fast, and Cheap Version of Stable Diffusion** | ECCV 2024 | diffusion pruning / compact model | — | — |
| **IVTP: Instruction-guided Visual Token Pruning for Large Vision-Language Models** | ECCV 2024 | VLM visual-token pruning | — | — |
| **Mixture of Efficient Diffusion Experts Through Automatic Interval and Sub-Network Selection** | ECCV 2024 | diffusion/flow acceleration / pruning | — | — |
| **Turbo: Informativity-Driven Acceleration Plug-In for Vision-Language Large Models** | ECCV 2024 | VLM inference acceleration / token redundancy pruning | [Link](https://arxiv.org/abs/2407.11717) | [Repo](https://github.com/anakin-skywalker-Joseph/Folder) |
| **LeanK: Learnable K Cache Channel Pruning for Efficient Decoding** | EMNLP 2025 | KV cache pruning / decoding acceleration | [Link](https://doi.org/10.18653/v1/2025.emnlp-main.1584) | — |
| **TokenSelect: Efficient Long-Context Inference and Length Extrapolation for LLMs via Dynamic Token-Level KV Cache Selection** | EMNLP 2025 | long-context inference / KV selection / sparse attention | [Link](https://doi.org/10.18653/v1/2025.emnlp-main.1079) | — |
| **More Tokens, Lower Precision: Towards the Optimal Token-Precision Trade-off in KV Cache Compression** | EMNLP 2025 Findings | KV cache compression / token-precision co-optimization | [Link](https://doi.org/10.18653/v1/2025.findings-emnlp.429) | — |
| **SAS: Sparse Attention Synthesizer for Efficient Language Model Inference** | EuroSys 2026 | efficient attention / kernel synthesis / KV cache | [Link](https://arxiv.org/abs/2602.09051) | — |
| **SolidAttention: Low-Latency SSD-based Serving on Memory-Constrained PCs** | FAST 2026 | LLM serving / sparse attention / SSD KV-cache offload | — | — |
| **Enabling Efficient SpMM for Sparse Attention on GEMM-Optimized Hardware with Block Aggregation** | FPGA 2026 | sparse attention / FPGA / SpMM-GEMM transformation | [Link](https://doi.org/10.1145/3748173.3779187) | — |
| **KANELÉ: Kolmogorov-Arnold Networks for Efficient LUT-based Evaluation** | FPGA 2026 | efficient FPGA ML inference / LUT neural networks | [Link](https://arxiv.org/abs/2512.12850) | — |
| **PADE: A Predictor-Free Sparse Attention Accelerator via Unified Execution and Stage Fusion** | HPCA 2026 | sparse attention accelerator / algorithm-hardware co-design | [Link](https://arxiv.org/abs/2512.14322) | — |
| **AIM: Adaptive Inference of Multi-Modal LLMs via Token Merging and Pruning** | ICCV 2025 | multimodal token merging/pruning | — | — |
| **FastVAR: Linear Visual Autoregressive Modeling via Cached Token Pruning** | ICCV 2025 | autoregressive image generation acceleration / cached token pruning | [Link](https://arxiv.org/abs/2503.23367) | [Repo](https://github.com/csguoh/FastVAR) |
| **Keyframe-oriented Vision Token Pruning: Enhancing Efficiency of Large Vision Language Models on Long-Form Video Processing** | ICCV 2025 | video VLM token pruning / long-form video efficiency | — | — |
| **Pruning All-Rounder: Rethinking and Improving Inference Efficiency for Large Vision Language Models** | ICCV 2025 | multimodal/VLM token-layer pruning | — | — |
| **QuantCache: Adaptive Importance-Guided Quantization with Hierarchical Latent and Layer Caching for Video Generation** | ICCV 2025 | video diffusion acceleration / quantization + caching | — | — |
| **SparseMM: Head Sparsity Emerges from Visual Concept Responses in MLLMs** | ICCV 2025 | multimodal KV-cache / head sparsity | — | [Repo](https://github.com/CR400AF-A/SparseMM) |
| **SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference** | ICCV 2025 | multimodal/VLM sparse prefill+decode inference | — | — |
| **VFlowOpt: A Token Pruning Framework for LMMs with Visual Information Flow-Guided Optimization** | ICCV 2025 | multimodal/VLM token pruning / KV efficiency | — | — |
| **ZipVL: Accelerating Vision-Language Models through Dynamic Token Sparsity** | ICCV 2025 | VLM dynamic token sparsity / KV efficiency | — | — |
| **Draft-based Approximate Inference for LLMs** | ICLR 2026 | KV cache compression / sparse attention / prompt compression | — | [Repo](https://github.com/furiosa-ai/draft-based-approx-llm) |
| **ProxyAttn: Guided Sparse Attention via Representative Heads** | ICLR 2026 | sparse attention / long-context prefill | — | — |
| **RESA: Bringing Back What Sparse Attention Ignores with Residual Estimation** | ICLR 2026 | sparse attention / KV efficiency | — | — |
| **Retrospective Sparse Attention for Efficient Long-Context Generation** | ICLR 2026 | KV cache compression / long-generation inference | — | [Repo](https://github.com/csh3695/RetroAttention) |
| **Tactic: Adaptive Sparse Attention with Clustering and Distribution Fitting for Long-Context LLMs** | ICLR 2026 | sparse attention / long-context inference | — | — |
| **WINA: Weight Informed Neuron Activation for Accelerating Large Language Model Inference** | ICLR 2026 | training-free sparse activation / LLM inference | — | — |
| **CoreMatching: A Co-adaptive Sparse Inference Framework with Token and Neuron Pruning for Comprehensive Acceleration of Vision-Language Models** | ICML 2025 | VLM sparsity / pruning | — | — |
| **DLP: Dynamic Layerwise Pruning in Large Language Models** | ICML 2025 | LLM pruning | — | — |
| **Sparse Video-Gen: Accelerating Video Diffusion Transformers with Spatial-Temporal Sparsity** | ICML 2025 | video/image generation acceleration / efficient attention | — | — |
| **A Unified Sparse Attention via Multi-Granularity Compression** | ICML 2026 | efficient attention / long-context inference | [Link](https://arxiv.org/abs/2512.14082) | — |
| **Elastic Attention: Test-time Adaptive Sparsity Ratios for Efficient Transformers** | ICML 2026 | adaptive sparse attention / long-context inference | [Link](https://arxiv.org/abs/2601.17367) | [Repo](https://github.com/LCM-Lab/Elastic-Attention) |
| **PuzzleMoE: Efficient Compression of Large Mixture-of-Experts Models via Sparse Expert Merging and Bit-packed inference** | ICML 2026 | MoE compression / sparse expert merging / bit-packed inference | [Link](https://arxiv.org/abs/2511.04805) | — |
| **SALE : Low-bit Estimation for Efficient Sparse Attention in Long-context LLM Prefilling** | ICML 2026 | efficient attention / low-bit estimation / long-context prefill | [Link](https://arxiv.org/abs/2505.24179) | — |
| **Scout Before You Attend: Sketch-and-Walk Sparse Attention for Efficient LLM Inference** | ICML 2026 | efficient attention / long-context inference | [Link](https://arxiv.org/abs/2602.07397) | — |
| **Sparse ActionGen: Accelerating Diffusion Policy with Real-time Pruning** | ICML 2026 | Physical AI / diffusion-policy acceleration / pruning+reuse | [Link](https://arxiv.org/abs/2601.12894) | — |
| **SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference** | ICML 2026 | LLM inference / activation sparsity | [Link](https://arxiv.org/abs/2411.12692) | — |
| **Stochastic Sparse Attention for Memory-Bound Inference** | ICML 2026 | sparse attention / memory-bound decoding / stochastic KV access | [Link](https://arxiv.org/abs/2605.01910) | [Repo](https://github.com/OPUSLab/SANTA) |
| **Token Sparse Attention: Efficient Long-Context Inference with Interleaved Token Selection** | ICML 2026 | sparse attention / long-context inference | [Link](https://arxiv.org/abs/2602.03216) | — |
| **The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning** | ICRA 2026 | Physical AI / VLA / adaptive visual-token pruning / inference acceleration | [Link](https://arxiv.org/abs/2509.12594) | [Repo](https://github.com/LiAutoAD/LightVLA) |
| **Accurate Sublayer Pruning for Large Language Models by Exploiting Latency and Tunability Information** | IJCAI 2025 | LLM sublayer pruning / latency-aware inference acceleration | [Link](https://arxiv.org/abs/2506.03510) | [Repo](https://github.com/snudm-starlab/SPRINT) |
| **Not All Layers of LLMs Are Necessary During Inference** | IJCAI 2025 | adaptive early-exit / dynamic-depth LLM inference | [Link](https://arxiv.org/abs/2403.02181) | — |
| **AdaToken-3D: Dynamic Spatial Gating for Efficient 3D Large Multimodal-Models Reasoning** | IROS 2025 | 3D multimodal inference / token pruning / Physical AI | [Link](https://arxiv.org/abs/2505.12782) | — |
| **Task-Oriented Token Pruning for Efficient Object Detection and Segmentation** | IROS 2025 | robot perception / task-aware token pruning / Physical AI | — | — |
| **BitL: A Hybrid Bit-Serial and Parallel Deep Learning Accelerator for Critical Path Reduction** | MICRO 2025 | bit-level sparsity / hybrid bit-serial-bit-parallel DNN accelerator / efficient inference | [Link](https://doi.org/10.1145/3725843.3756044) | — |
| **Coruscant: Co-Designing GPU Kernel and Sparse Tensor Core to Advocate Unstructured Sparsity in Efficient LLM Inference** | MICRO 2025 | sparse LLM inference / GPU kernel co-design | — | — |
| **LongSight: Compute-Enabled Memory to Accelerate Large-Context LLMs via Sparse Attention** | MICRO 2025 | long-context LLM / sparse attention / CXL memory | [Link](https://doi.org/10.1145/3725843.3756062) | — |
| **MCBP: A Memory-Compute Efficient LLM Inference Accelerator Leveraging Bit-Slice-enabled Sparsity and Repetitiveness** | MICRO 2025 | LLM accelerator / bit-slice sparsity | — | — |
| **BLASST: Dynamic BLocked Attention Sparsity via Softmax Thresholding** | MLSys 2026 | sparse attention / long-context inference | — | — |
| **Delta Attention: Fast and Accurate Sparse Attention Inference by Delta Correction** | NeurIPS 2025 | sparse attention / long-context inference | [Link](https://doi.org/10.52202/085713-0403) | — |
| **MoESD: Unveil Speculative Decoding's Potential for Accelerating Sparse MoE** | NeurIPS 2025 | MoE inference / speculative decoding | [Link](https://doi.org/10.52202/085713-4176) | — |
| **MUSTAFAR: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference** | NeurIPS 2025 | KV pruning / sparse attention kernel | [Link](https://doi.org/10.52202/085713-2564) | — |
| **SALS: Sparse Attention in Latent Space for KV Cache Compression** | NeurIPS 2025 | KV cache compression / sparse attention | [Link](https://doi.org/10.52202/085713-0013) | — |
| **Spotlight Attention: Towards Efficient LLM Generation via Non-linear Hashing-based KV Cache Retrieval** | NeurIPS 2025 | sparse attention / KV retrieval / CUDA kernel | [Link](https://doi.org/10.52202/085713-2883) | — |
| **ECHO: Efficient KV Cache Offloading with Lossless Prefetching for Serving Native Sparse Attention LLMs** | OSDI 2026 | sparse-attention KV-cache serving | — | — |
| **Kairox: Adaptive GPU-CPU Hybrid LLM Inference via Online Neuron Balancing** | OSDI 2026 | LLM inference / GPU-CPU hybrid execution / activation sparsity / edge inference | — | — |
| **Accelerating Sparse Transformer Inference on GPU** | PPoPP 2026 | sparse transformer inference + mixed-precision quantization | — | — |
| **RoMeo** | PPoPP 2026 | sparse transformer inference + mixed-precision quantization | — | — |
| **DCP: Addressing Input Dynamism In Long-Context Training via Dynamic Context Parallelism** | SOSP 2025 | long-context LLM training / dynamic context parallelism | [Link](https://arxiv.org/abs/2510.10620) | [Repo](https://github.com/chenyu-jiang/dcp) |
| **Probe-and-Fetch: Dynamic KV Cache Pruning for Accelerated Long-Context Inference in Web-Scale AI Search** | The Web Conference 2026 | KV cache pruning / long-context inference | [Link](https://doi.org/10.1145/3774904.3792794) | — |
| **GeneralSparse: Bridging the Gap in SpMM for Pruned Large Language Model Inference on GPUs** | USENIX ATC 2025 | sparse LLM inference / GPU kernels | — | — |
| **JENGA: Enhancing LLM Long-Context Fine-tuning with Contextual Token Sparsity** | USENIX ATC 2025 | long-context LLM fine-tuning / contextual token sparsity / kernels | — | — |
| **Universal Checkpointing: A Flexible and Efficient Distributed Checkpointing System for Large-Scale DNN Training with Reconfigurable Parallelism** | USENIX ATC 2025 | distributed LLM training / elastic checkpointing / reconfigurable parallelism | — | — |
| **Sirius: A Dual-Chiplet System for Multimodal Embodied AI with Heterogeneous RVV Cores, Dense and Sparse Accelerators** | VLSI Symposium 2026 | Physical AI / multimodal embodied edge accelerator | [Link](https://doi.org/10.1109/VLSITechnologyandCir65830.2026.11577229) | — |
| **AViTS: Adaptive Spatiotemporal Token Selection for Efficient Dynamic-Resolution Generation** | Fresh / preprint | diffusion/image generation acceleration / adaptive token selection | [Link](https://arxiv.org/abs/2608.17995) | — |
| **Every Expert Counts: ExactMoE for Memory-Efficient W4A16 Inference** | Fresh / preprint | MoE memory-efficient W4A16 inference / GPU slot cache | [Link](https://arxiv.org/abs/2608.15383) | — |
| **FlashPrefill V2: Block-Sparse Prefill Attention for Long-Context LLM Serving** | Fresh / preprint | long-context LLM serving / block-sparse prefill attention / GPU kernel | [Link](https://arxiv.org/abs/2608.19758) | — |
| **ReCache: Efficient KV Cache Reuse and Compression for Tool-Augmented LLM Agents** | Fresh / preprint | agent serving / KV cache reuse / compression | [Link](https://arxiv.org/abs/2608.19662) | [Repo](https://github.com/EIT-NLP/ReCache) |
| **SCOPE: Subspace Clustering with Online Per-Head Top-K Estimation for Sparse Video Attention** | Fresh / preprint | sparse video attention / DiT inference | [Link](https://arxiv.org/abs/2608.12780) | — |
