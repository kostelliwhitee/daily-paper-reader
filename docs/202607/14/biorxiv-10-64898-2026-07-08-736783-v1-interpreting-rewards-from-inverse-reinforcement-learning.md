---
title: Interpreting Rewards from Inverse Reinforcement Learning
title_zh: 从逆强化学习解释奖励函数
authors: "Chow, J., Yang, Y., Laschowski, B."
date: 2026-07-13
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.08.736783v1.full.pdf"
tags: ["query:ma-la"]
score: 7.0
evidence: 通过奖励解释推断多智能体社交交互中的潜在动机
tldr: 逆强化学习能从行为中恢复奖励函数，但奖励的解读仍是根本挑战。本文提出结合奖励函数分析、潜在模式分配和短历史行为分析的新框架。在大型多智能体社交互动数据集上，切换逆强化学习将潜在模式解读为“谨慎”和“波动”动机轮廓。该框架为逆向工程和解读智能行为背后的潜在奖励提供了有效途径。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-08-736783-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1854, \"height\": 299, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-08-736783-v1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1843, \"height\": 709, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-08-736783-v1/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1768, \"height\": 768, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-08-736783-v1/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1769, \"height\": 859, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-08-736783-v1/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1781, \"height\": 627, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-08-736783-v1/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1821, \"height\": 867, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-08-736783-v1/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1779, \"height\": 1264, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-08-736783-v1/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1780, \"height\": 622, \"label\": \"Figure\"}]"
motivation: 逆强化学习恢复的奖励函数难以解读，缺乏理解智能行为和决策的深层动机。
method: 提出结合奖励函数分析、潜在模式分配和短历史行为分析的解读框架，并用切换逆强化学习实例化。
result: 在多智能体社交互动数据上，框架将潜在模式成功解读为“谨慎”和“波动”两类动机轮廓。
conclusion: 该框架为逆向工程和解读智能行为背后的潜在奖励提供了有前景的方法。
---

## 摘要
逆强化学习可以从观察到的行为中恢复奖励函数，但解释这些奖励对于理解智能行为和决策仍然是一个根本挑战。为了应对这一挑战，我们引入了一个新颖的奖励解释框架，该框架结合了奖励函数分析、潜在模式分配和短历史行为分析来推断潜在动机和行为动态。作为概念验证，我们在一个大规模多智能体社交互动数据集上使用切换逆强化学习实例化了该框架。我们的框架将学习到的潜在模式解释为"谨慎"和"易变"的动机特征，表明恢复的奖励函数可以揭示行为动态的独特模式。更广泛地说，这些发现表明，所提出的框架为逆向工程和解释智能行为与决策背后的潜在奖励提供了一种有前景的方法。

## Abstract
Inverse reinforcement learning can recover reward functions from observed behavior, but interpreting those rewards remains a fundamental challenge for understanding intelligent behavior and decision-making. To address this challenge, we introduce a novel framework for reward interpretation that combines reward-function analysis, latent mode assignments, and short-history behavioral analysis to infer latent motivations and behavioral dynamics. As a proof-of-concept, we instantiated the framework using switching inverse reinforcement learning on a large-scale dataset of multi-agent social interactions. Our framework interpreted the learned latent modes as "cautious" and "volatile" motivational profiles, demonstrating that recovered reward functions can reveal distinct patterns of behavioral dynamics. More broadly, these findings suggest that the proposed framework provides a promising approach for reverse-engineering and interpreting latent rewards underlying intelligent behavior and decision-making.