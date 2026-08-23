# 11 · Video / Image Generation

> **23 canonical papers** mapped here, plus a broader **13-paper Latest-30-Day tracker** using P0/P1/P2 tiers. Cross-direction duplication is intentional when a paper has multiple technical roles.

[← Research Map](README.md) · [🆕 Latest 30 Days](LATEST_30D.md) · [🏛️ Classical](CLASSICAL.md) · [Paper Library](ALL_PAPERS.md)

## 🆕 Latest 30 Days · 13 tracked

| Priority | Paper | Venue | Topic | Paper | Code |
|---|---|---|---|---|---|
| **P1 · Watch** | **Swift-Image: Exploring the Performance Frontier of Compact Unified Image Generation Models** | Fresh / preprint | image generation efficiency / pruning / few-step distillation | [Link](https://arxiv.org/abs/2608.20334) | — |
| **P1 · Watch** | **Partition the Support, Reconstruct the Residual: Training-Free Sparse Attention for Video Generation and World Models** | Fresh / preprint | efficient attention / video generation / world models | [Link](https://arxiv.org/abs/2608.18484) | — |
| **P0 · Strong** | **AViTS: Adaptive Spatiotemporal Token Selection for Efficient Dynamic-Resolution Generation** | Fresh / preprint | diffusion/image generation acceleration / adaptive token selection | [Link](https://arxiv.org/abs/2608.17995) | — |
| **P0 · Strong** | **LinCa: Accelerating Diffusion Models via Learnable Decomposed Feature Caching** | Fresh / preprint | diffusion/video generation acceleration / feature caching | [Link](https://arxiv.org/abs/2608.17973) | — |
| **P0 · Strong** | **Magnitude-Direction Decoupling for Fast Video Generation with Flow Matching Models** | Fresh / preprint | video generation acceleration / flow matching | [Link](https://arxiv.org/abs/2608.17695) | — |
| **P0 · Strong** | **An Empirical Study of Training Pixel-Space Text-to-Image Diffusion Models** | Fresh / preprint | image generation acceleration | [Link](https://arxiv.org/abs/2608.16887) | — |
| **P0 · Strong** | **GenRouter: Unified Workflow Routing for Agentic Image Generation** | Fresh / preprint | agentic image generation / workflow routing / inference efficiency | [Link](https://arxiv.org/abs/2608.16721) | — |
| **P0 · Strong** | **SQuad: Sub-Quadratic Attention Distillation for Efficient Video Generation** | Fresh / preprint | video generation acceleration / efficient attention | [Link](https://arxiv.org/abs/2608.16585) | — |
| **P2 · Relevant** | **Nexus: Structured Synergy for Efficient Text-to-Image Generation using Rectified Flow Model** | Fresh / preprint | image generation / sparse architecture / low-bit / flow matching | [Link](https://arxiv.org/abs/2608.16104) | — |
| **P0 · Strong** | **From Local Mismatch to Global Impact: Optimizing Cache Reuse Policy for Efficient Diffusion** | Fresh / preprint | diffusion cache policy / video-image generation acceleration | [Link](https://arxiv.org/abs/2608.13043) | — |
| **P2 · Relevant** | **EchoCache: Energy-Guided Cross-Modal Caching for Efficient Audio-Driven Video Generation** | Fresh / preprint | LLM serving; quantization; generation acceleration | [Link](https://arxiv.org/abs/2608.02474) | — |
| **P2 · Relevant** | **Sol-Attn: Accelerating Video Generation Inference via On-the-Fly Attention Sparsification** | Fresh / preprint | llm_serving / sparse / gen | [Link](https://arxiv.org/abs/2607.24027) | — |
| **P2 · Relevant** | **SANA-Video 2.0: Hybrid Linear Attention with Attention Residuals for Efficient Video Generation** | Fresh / preprint | llm_serving / sparse / attn / kernel / gen | [Link](https://arxiv.org/abs/2607.21553) | — |

## 🏛️ Classical / Historical · 16 canonical

| Priority | Paper | Venue | Topic | Paper | Code |
|---|---|---|---|---|---|
| **Canonical** | **Head-Aware KV Cache Compression for Efficient Visual Autoregressive Modeling** | AAAI 2026 | KV cache / image generation acceleration | [Link](https://doi.org/10.1609/aaai.v40i30.39686) | [Repo](https://github.com/Zr2223/HACK) |
| **Canonical** | **MoDM: Efficient Serving for Image Generation via Mixture-of-Diffusion Models** | ASPLOS 2026 | serving + speculative decoding + MoE + generative efficiency | [Link](https://arxiv.org/abs/2503.11972) | — |
| **Canonical** | **Adaptive Spectral Feature Forecasting for Diffusion Sampling Acceleration** | CVPR 2026 | diffusion/video generation acceleration / spectral feature forecasting / long-range reuse | [Link](https://arxiv.org/abs/2603.01623) | [Repo](https://github.com/hanjq17/Spectrum) |
| **Canonical** | **Attention Surgery: An Efficient Recipe to Linearize Your Video Diffusion Transformer** | CVPR 2026 | video diffusion / linear attention / mobile inference | — | — |
| **Canonical** | **LinVideo: A Post-Training Framework towards O(n) Attention in Efficient Video Generation** | CVPR 2026 | video generation acceleration / linear attention / post-training | [Link](https://arxiv.org/abs/2510.08318) | — |
| **Canonical** | **SURF: Signature-Retained Fast Video Generation** | CVPR 2026 | video generation acceleration / low-resolution preview / efficient refinement | [Link](https://arxiv.org/abs/2603.21002) | — |
| **Canonical** | **Adaptive Caching for Faster Video Generation with Diffusion Transformers** | ICCV 2025 | video diffusion acceleration / adaptive feature caching | [Link](https://arxiv.org/abs/2411.02397) | — |
| **Canonical** | **FastVAR: Linear Visual Autoregressive Modeling via Cached Token Pruning** | ICCV 2025 | autoregressive image generation acceleration / cached token pruning | [Link](https://arxiv.org/abs/2503.23367) | [Repo](https://github.com/csguoh/FastVAR) |
| **Canonical** | **QuantCache: Adaptive Importance-Guided Quantization with Hierarchical Latent and Layer Caching for Video Generation** | ICCV 2025 | video diffusion acceleration / quantization + caching | — | — |
| **Canonical** | **Autoregressive Image Generation with Randomized Parallel Decoding** | ICLR 2026 | autoregressive image generation / parallel decoding | — | — |
| **Canonical** | **Diffusion Adversarial Post-Training for One-Step Video Generation** | ICML 2025 | one-step video/image diffusion generation | — | — |
| **Canonical** | **Sparse Video-Gen: Accelerating Video Diffusion Transformers with Spatial-Temporal Sparsity** | ICML 2025 | video/image generation acceleration / efficient attention | — | — |
| **Canonical** | **Accelerating Diffusion-based Super-Resolution with Dynamic Time-Spatial Sampling** | IJCAI 2025 | diffusion acceleration / adaptive sampling / image generation efficiency | [Link](https://doi.org/10.24963/ijcai.2025/199) | — |
| **Canonical** | **Self Forcing: Bridging the Train-Test Gap in Autoregressive Video Diffusion** | NeurIPS 2025 | autoregressive video diffusion / streaming generation | [Link](https://doi.org/10.52202/085713-5576) | — |
| **Canonical** | **Unified Video Action Model** | RSS 2025 | Physical AI / efficient world-action model inference | [Link](https://doi.org/10.15607/RSS.2025.XXI.074) | — |
| **Canonical** | **Déjà Vu: Efficient Video-Language Query Engine with Learning-based Inter-Frame Computation Reuse** | VLDB/PVLDB Volume 18 | VideoLM inference / inter-frame computation reuse | [Link](https://arxiv.org/abs/2506.14107) | — |
