# 10 · Multimodal / MLLM Serving

> **52 papers** currently mapped to this direction. Cross-direction duplication is intentional when a paper has multiple technical roles.

[← Research Map](README.md) · [Complete Paper List](ALL_PAPERS.md)

| Paper | Venue | Topic | Paper | Code |
|---|---|---|---|---|
| **AccKV: Towards Efficient Audio-Video LLMs Inference via Adaptive-Focusing and Cross-Calibration KV Cache Optimization** | AAAI 2026 | audio-video LLM / multimodal KV cache optimization | [Link](https://doi.org/10.1609/aaai.v40i7.37467) | — |
| **Efficient Multimodal Large Language Model via Dynamic KV Cache Quantization** | AAAI 2026 | MLLM inference / KV cache quantization | [Link](https://doi.org/10.1609/aaai.v40i25.39241) | — |
| **MHA2MLA-VLM: Enabling DeepSeek’s Economical Multi-Head Latent Attention Across Vision-Language Models** | AAAI 2026 | VLM inference / MLA / KV cache compression | [Link](https://doi.org/10.1609/aaai.v40i36.40319) | — |
| **Q Cache: Visual Attention Is Valuable in Less than Half of Decode Layers for Multimodal Large Language Model** | AAAI 2026 | MLLM inference / cross-layer attention reuse / KV cache | [Link](https://doi.org/10.1609/aaai.v40i16.38414) | — |
| **HybridKV: Hybrid KV Cache Compression for Efficient Multimodal Large Language Model Inference** | ACL 2026 | multimodal KV-cache compression / efficient MLLM inference | [Link](https://doi.org/10.18653/v1/2026.acl-long.594) | — |
| **VISA: Group-wise Visual Token Selection and Aggregation via Graph Summarization for Efficient MLLMs Inference** | ACM Multimedia 2025 | MLLM inference / visual token pruning and aggregation | [Link](https://arxiv.org/abs/2508.17857) | — |
| **DUET-VLM: Dual stage Unified Efficient Token reduction for VLM Training and Inference** | CVPR 2026 | VLM training+inference / token reduction | — | — |
| **IF-Prune: Information-Flow Guided Token Pruning for Efficient Vision-Language Models** | CVPR 2026 | VLM inference / token pruning | — | — |
| **Prune2Drive: A Plug-and-Play Framework for Accelerating Vision-Language Models in Autonomous Driving** | CVPR 2026 | autonomous driving / VLM token pruning / Physical AI | — | — |
| **TransPrune: Token Transition Pruning for Efficient Large Vision-Language Model** | CVPR 2026 | VLM inference / token pruning | — | — |
| **VLM-Pruner: Buffering for Spatial Sparsity in an Efficient VLM Centrifugal Token Pruning Paradigm** | CVPR 2026 | VLM inference / visual token pruning | — | — |
| **ZOO-Prune: Training-Free Token Pruning via Zeroth-Order Gradient Estimation in Vision-Language Models** | CVPR 2026 | VLM inference / training-free visual-token pruning / zeroth-order sensitivity | — | [Repo](https://github.com/AIM-SKKU/ZOO-Prune) |
| **An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models** | ECCV 2024 | VLM visual-token pruning | — | — |
| **Efficient Inference of Vision Instruction-Following Models with Elastic Cache** | ECCV 2024 | KV cache / multimodal inference | — | — |
| **IVTP: Instruction-guided Visual Token Pruning for Large Vision-Language Models** | ECCV 2024 | VLM visual-token pruning | — | — |
| **LLaMA-VID: An Image is Worth 2 Tokens in Large Language Models** | ECCV 2024 | video VLM token compression | — | — |
| **Turbo: Informativity-Driven Acceleration Plug-In for Vision-Language Large Models** | ECCV 2024 | VLM inference acceleration / token redundancy pruning | [Link](https://arxiv.org/abs/2407.11717) | [Repo](https://github.com/anakin-skywalker-Joseph/Folder) |
| **Efficient Multimodal Serving via Module Multiplexing** | EuroSys 2026 | multimodal/MLLM serving / module multiplexing | — | — |
| **Adaptive Draft Sequence Length** | HPCA 2026 | efficient VLM + PIM inference + reasoning accelerator + speculative decoding | — | — |
| **Focus** | HPCA 2026 | efficient VLM + PIM inference + reasoning accelerator + speculative decoding | — | — |
| **LoCaLUT** | HPCA 2026 | efficient VLM + PIM inference + reasoning accelerator + speculative decoding | — | — |
| **PIMphony** | HPCA 2026 | efficient VLM + PIM inference + reasoning accelerator + speculative decoding | — | — |
| **RPU** | HPCA 2026 | efficient VLM + PIM inference + reasoning accelerator + speculative decoding | — | — |
| **AIM: Adaptive Inference of Multi-Modal LLMs via Token Merging and Pruning** | ICCV 2025 | multimodal token merging/pruning | — | — |
| **AirCache: Activating Inter-modal Relevancy KV Cache Compression for Efficient Large Vision-Language Model Inference** | ICCV 2025 | multimodal KV-cache compression | — | — |
| **Pruning All-Rounder: Rethinking and Improving Inference Efficiency for Large Vision Language Models** | ICCV 2025 | multimodal/VLM token-layer pruning | — | — |
| **ShortV: Efficient Multimodal Large Language Models by Freezing Visual Tokens in Ineffective Layers** | ICCV 2025 | training-free VLM layer/token efficiency | — | — |
| **Skip-Vision: Efficient and Scalable Acceleration of Vision-Language Models via Adaptive Token Skipping** | ICCV 2025 | VLM training/inference acceleration | — | — |
| **Token-Efficient VLM: High-Resolution Image Understanding via Dynamic Region Proposal** | ICCV 2025 | VLM efficiency / dynamic region proposal / token-efficient high-resolution vision | — | — |
| **ZipVL: Accelerating Vision-Language Models through Dynamic Token Sparsity** | ICCV 2025 | VLM dynamic token sparsity / KV efficiency | — | — |
| **CoreMatching: A Co-adaptive Sparse Inference Framework with Token and Neuron Pruning for Comprehensive Acceleration of Vision-Language Models** | ICML 2025 | VLM sparsity / pruning | — | — |
| **EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation** | ICRA 2026 | Physical AI / VLA / real-time adaptive-horizon replanning / low-cost deployment | [Link](https://arxiv.org/abs/2511.05397) | [Repo](https://github.com/everydayvla/EveryDayVLA) |
| **The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning** | ICRA 2026 | Physical AI / VLA / adaptive visual-token pruning / inference acceleration | [Link](https://arxiv.org/abs/2509.12594) | [Repo](https://github.com/LiAutoAD/LightVLA) |
| **AdaToken-3D: Dynamic Spatial Gating for Efficient 3D Large Multimodal-Models Reasoning** | IROS 2025 | 3D multimodal inference / token pruning / Physical AI | [Link](https://arxiv.org/abs/2505.12782) | — |
| **AQuant: Repurposing CODEC for VLM Acceleration via Adaptive Quantization** | ISCA 2026 | VLM acceleration / adaptive quantization / hardware co-design | — | — |
| **DiTPA: A DiT-based Action Planner Accelerator Exploiting Action-Denoising-Multimodality Redundancy for Embodied Artificial Intelligence** | ISCA 2026 | Physical AI / embodied action planner / DiT accelerator | — | — |
| **Omni-LUT: Energy-Efficient LUT-based Accelerator with Hardware-Aware KV Cache Quantization** | ISCA 2026 | LLM inference accelerator / LUT / KV-cache quantization | — | — |
| **Symbiotic MLLM Serving: Dynamically Balancing Parallelism Across GPUs and Resources Within GPUs** | ISCA 2026 | multimodal LLM serving / GPU resource balancing | — | — |
| **Efficient, VRAM-Constrained xLM Inference on Clients** | MLSys 2026 | client LLM/VLM inference / CPU-GPU hybrid runtime / Physical AI | — | — |
| **RLux-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models** | RSS 2026 | Physical AI / VLA RL systems / scalable training | [Link](https://arxiv.org/abs/2510.06710) | — |
| **DistTrain: Addressing Model and Data Heterogeneity with Disaggregated Training for Multimodal Large Language Models** | SIGCOMM 2025 | multimodal training systems / disaggregated training | [Link](https://arxiv.org/abs/2408.04275) | — |
| **Task-Aware Cloud-End Offloading for Vision-Language Model Serving via Dynamic Modality-Specific Adapter Scheduling** | The Web Conference 2026 | multimodal/VLM serving / cloud-edge offloading | [Link](https://doi.org/10.1145/3774904.3792127) | — |
| **Déjà Vu: Efficient Video-Language Query Engine with Learning-based Inter-Frame Computation Reuse** | VLDB/PVLDB Volume 18 | VideoLM inference / inter-frame computation reuse | [Link](https://arxiv.org/abs/2506.14107) | — |
| **Silicon-Oracle (Soracle): A Multi-Modal Autoregressive Model Accelerator for Context-Aware Assistance on Mobile Platform** | VLSI Symposium 2026 | multimodal autoregressive accelerator / mobile inference | [Link](https://doi.org/10.1109/VLSITechnologyandCir65830.2026.11577228) | — |
| **Sirius: A Dual-Chiplet System for Multimodal Embodied AI with Heterogeneous RVV Cores, Dense and Sparse Accelerators** | VLSI Symposium 2026 | Physical AI / multimodal embodied edge accelerator | [Link](https://doi.org/10.1109/VLSITechnologyandCir65830.2026.11577229) | — |
| **SR-VLNA: A 5.0–23.9 mJ/meter Spatial Reasoning-based Vision Language Navigation Accelerator for Embodied Agents** | VLSI Symposium 2026 | Physical AI / vision-language navigation accelerator | [Link](https://doi.org/10.1109/VLSITechnologyandCir65830.2026.11577427) | — |
| **Algorithm-Architecture Co-Design for Efficient VLA Inference via Speculative Inference and Verification** | Fresh / preprint | VLA speculative inference / algorithm-architecture co-design | [Link](https://arxiv.org/abs/2608.15636) | — |
| **EcoVLA: Energy-Efficient Device-Edge Co-Inference for Vision-Language-Action Models under Real-Time Constraints** | Fresh / preprint | VLA device-edge co-inference / energy-aware runtime | [Link](https://arxiv.org/abs/2608.15502) | — |
| **FlashDrive: Flash Vision-Language-Action Inference for Autonomous Driving** | Fresh / preprint | full-stack VLA inference acceleration | [Link](https://arxiv.org/abs/2608.12932) | — |
| **NebulaVLA: A Dual-Frequency Vision-Language-Action Model With Guide Action for Robotic Manipulation** | Fresh / preprint | VLA efficient inference | [Link](https://arxiv.org/abs/2608.16503) | — |
| **Reflex: Enabling Fast and Predictive Vision-Language-Action Models for Reaction-Critical Manipulation** | Fresh / preprint | fast VLA runtime / reaction-critical manipulation | [Link](https://arxiv.org/abs/2608.14379) | — |
| **Role-Conditioned Sub-Token Routing for Efficient Vision-Language-Action Policies** | Fresh / preprint | VLA efficiency / KV compression / sub-token routing | [Link](https://arxiv.org/abs/2608.18410) | — |
