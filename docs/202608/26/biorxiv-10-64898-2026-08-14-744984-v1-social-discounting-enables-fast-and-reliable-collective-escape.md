---
title: Social Discounting Enables Fast and Reliable Collective Escape
title_zh: 社会折现实现快速可靠的集体逃脱
authors: "Kilpatrick, Z. P."
date: 2026-08-19
pdf: "https://www.biorxiv.org/content/10.64898/2026.08.14.744984v1.full.pdf"
tags: ["query:ma-la"]
score: 6.0
evidence: 将集体逃跑建模为多智能体证据累积，同伴的飞逃与静止影响群体决策，属于交互动态研究
tldr: 独居动物检测威胁时，快速反应必然伴随更多误报。本研究表明，群体可以通过把未受惊扰的邻居当作安全的证据，从而在保持低误报的同时实现更快更准的逃逸。将个体建模为噪声证据累积器，飞逃由信念阈值触发，提出单一社会折扣率近似贝叶斯反应，以权衡邻居逃跑与静止。该模型给出群体表现的闭式解，包括安全时保持亚临界、威胁时变为超临界的级联分支比，且可从行为数据推断折扣率。应用于硫磺茉莉鱼群时，推断出的折扣率远高于个体贝叶斯更新，且能预测误报率随群体增大而保持恒定。
source: biorxiv
selection_source: fresh_fetch
motivation: 独居动物检测威胁时面临速度与准确性的权衡，群体可能通过社会信息同时改善两者，本文探究其机制。
method: 将个体建模为噪声证据累积器，用社会折扣率近似贝叶斯反应，并推导群体级联的闭式解。
result: 获得群体误报级联的分支比闭式解，安全时亚临界、威胁时超临界；从鱼类行为推断出高折扣率，并预测误报率不随群体规模变化。
conclusion: 社会折扣机制让群体逃逸又快又准，且可由行为推断，为理解集体行为中的信息整合提供了新框架。
---

## 摘要
独居动物在检测威胁时面临权衡：更快的检测意味着接受更多的误报。我们表明，群体可以通过将未受干扰的邻居视为不利于威胁的证据来更好地管理这种权衡，从而比独居个体更快更准确。将每个动物建模为嘈杂的证据累积器，当其信念超过阈值时逃跑，我们发现邻居的逃跑标志着危险，而它的静止标志着安全。天真的反应者只对逃跑做出反应，随着群体增大而增加误报；贝叶斯反应者权衡两者，通过单一的社会折现率近似，该折现率在这些极限之间插值。这产生了群体性能的闭式表达式，包括级联分支比，在安全时保持强烈亚临界，在威胁下变为超临界，因此动物在邻居保持静止时对威胁折现的速率可以仅从行为推断出来，并且它设定了动物在单独折现无法再维持其误报率之前可以关注的邻居数量上限。鸟类攻击下的野生硫磺鳉鱼群最好用折现率来描述，该折现率远高于个体贝叶斯更新在其可能关注的任何邻域内提供的折现率，并且同一模型在推断值下预测误报率随着鱼群增大而保持恒定。

## Abstract
Solitary animals face a tradeoff when detecting threats: faster detection means accepting more false alarms. We show that groups can manage this tradeoff better by treating an undisturbed neighbor as evidence against a threat, becoming both faster and more accurate than lone individuals. Modeling each animal as a noisy evidence-accumulator that flees when its belief crosses a threshold, we find that a neighbor's flight signals danger while its stillness signals safety. A naive responder reacts only to flights and inflates false alarms as the group grows; a Bayesian responder weighs both, approximated by a single social discounting rate that interpolates between these limits. This yields closed-form expressions for group performance, including cascade branching ratios that stay strongly subcritical in safety and turn supercritical under threat, so the rate at which an animal discounts a threat while its neighbors stay still can be inferred from behavior alone, and it sets a ceiling on how many neighbors an animal can attend before discounting alone can no longer hold its false-alarm rate. Wild sulphur molly shoals under bird attack are best described by discounting rates well above what individually Bayesian updating supplies over any neighborhood they could plausibly attend, and the same model, at the inferred value, predicts a false-alarm rate that stays constant as shoals grow.