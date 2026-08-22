---
title: A multi-agent molecular optimization framework leads to a rapid-recovery intravenous anesthetic candidate with an improved safety margin
title_zh: 一种多智能体分子优化框架催生具有更佳安全裕度的快速恢复静脉麻醉候选药物
authors: "Xue, Z., Liu, X."
date: 2026-08-20
pdf: "https://www.biorxiv.org/content/10.64898/2026.08.17.745149v1.full.pdf"
tags: ["query:ma-la"]
score: 7.0
evidence: 用于分子优化的角色专业化多智能体框架，多个智能体协同交互
tldr: 药物先导优化面临巨大化学空间与多目标冲突。提出MASCOT多智能体框架，通过分工协作与图编辑搜索优化分子。基准测试中性能最佳，并在麻醉药瑞马唑仑优化中筛选出RM-7，动物实验证实其恢复快、安全窗更宽。多智能体协调有效连接分子搜索与实验药理。
source: biorxiv
selection_source: fresh_fetch
motivation: 传统优化难以兼顾效价、药代与安全，需更智能的分子搜索策略。
method: 设计三个分工智能体（权衡、策略、反思）协同执行图编辑搜索。
result: MASCOT在6个基准上最优，并发现优于瑞马唑仑的候选物RM-7。
conclusion: 多智能体协调可提升药物优化效率，推动从计算到临床前验证转化。
---

## 摘要
先导化合物优化是通过迭代结构修饰系统性地改进治疗化合物的过程，在现代药物发现中面临双重挑战：在导航天文数字般庞大的分子设计空间的同时，平衡对药效、药代动力学和安全性相互冲突的需求。我们提出了MASCOT（分子优化的多智能体搜索），一个角色专化的多智能体分子优化框架。与化学约束的图编辑搜索集成，MASCOT协调三个专化智能体：一个权衡智能体，重新排序竞争性目标；一个策略智能体，调整分子编辑提出方式；一个反思智能体，从先前决策中提炼经验教训。计算实验表明，MASCOT在六个基准设置上达到了优于竞争方法的最佳性能。在SARS-CoV-2主蛋白酶任务上，其平均对接分数提升是最强基线的3.6倍。应用于临床使用的麻醉药瑞马唑仑（RM）时，MASCOT优选出了RM-1，与RM相比，其肝微粒体半衰期更短，脑暴露更高，治疗指数更大。随后的衍生物设计产生了RM-7。广泛的动物研究确立RM-7为一种快速恢复的静脉麻醉候选药物，具有更强的效力、更快的功能恢复、更宽的安全裕度，并保留了氟马西尼逆转性。这些结果表明，多智能体协调可以将自适应分子搜索与药物化学和实验药理学联系起来。

## Abstract
Lead optimization, the systematic refinement of therapeutic compounds through iterative structural modification, faces a dual challenge in modern drug discovery: navigating astronomically vast molecular design spaces while balancing conflicting demands on potency, pharmacokinetics, and safety. We present MASCOT (Multi-Agent SearCh for molecular OpTimization), a role-specialized multi-agent framework for molecular optimization. Integrated with a chemically constrained graph-editing search, MASCOT coordinates three specialized agents: a trade-off agent that reprioritizes competing objectives, a strategy agent that adapts how molecular edits are proposed, and a reflection agent that distills lessons from previous decisions. Computational experiments showed that MASCOT achieved the best performance over competing methods on six benchmark settings. On the SARS-CoV-2 main protease task, its mean docking-score improvement was 3.6 times that of the strongest baseline. Applied to the clinically used anesthetic remimazolam (RM), MASCOT prioritized RM-1, which showed a shorter liver microsomal half-life, higher brain exposure, and a larger therapeutic index than RM. Subsequent derivative design yielded RM-7. Extensive animal studies established RM-7 as a rapid-recovery intravenous anesthetic candidate with greater potency, faster functional recovery, a wider safety margin, and preserved flumazenil reversibility. These results demonstrate that multi-agent coordination can link adaptive molecular search to medicinal chemistry and experimental pharmacology.