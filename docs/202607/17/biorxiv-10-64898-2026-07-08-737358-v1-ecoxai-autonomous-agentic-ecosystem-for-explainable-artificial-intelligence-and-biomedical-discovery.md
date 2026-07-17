---
title: "EcoXAI: Autonomous Agentic Ecosystem for Explainable Artificial Intelligence and Biomedical Discovery"
title_zh: "EcoXAI: 用于可解释人工智能和生物医学发现的自主智能体生态系统"
authors: "Matsumoto, N., Choi, H., Freda, P. J., Hernandez, M. E., Wang, Z. P., Moore, J. H."
date: 2026-07-13
pdf: "https://www.biorxiv.org/content/10.64898/2026.07.08.737358v1.full.pdf"
tags: ["query:ma-la"]
score: 6.0
evidence: 模块化多智能体数据分析系统，含智能体通信
tldr: 生物医学数据规模庞大且异构，现有AI工具易产生幻觉，分析流程碎片化。EcoXAI提出模块化容器化多智能体框架，基于知识图谱集成与显式管线执行，增强推理透明性与可验证性。在阿尔茨海默病药物重定位中，系统评估103种候选药物，识别出79个新候选，其中CCR5拮抗剂Maraviroc的假设获得文献支持。该工作证明知识图谱驱动的AI智能体可有效加速假设驱动的生物医学发现。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-07-08-737358-v1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1770, \"height\": 773, \"label\": \"Figure\"}]"
motivation: 现有AI工具处理生物医学大数据时存在幻觉与流程碎片化，需自主可解释的智能系统来降低分析门槛。
method: 构建模块化容器化多智能体框架，整合生物信息学智能体与知识图谱推理，通过显式管线执行增强透明性。
result: 在阿尔茨海默病药物重定位中，评估103种候选药物，识别79个新候选，Maraviroc的假设获文献验证。
conclusion: 知识图谱驱动的AI智能体架构为可验证推理提供新范式，加速假设驱动的生物医学发现。
---

## 摘要
动机：随着生物医学数据集和知识图谱在规模、复杂性和异质性上的持续增长，从中导航和提取可操作见解成为研究人员的主要瓶颈。迫切需要能够利用智能体AI最新进展（如智能体协调和循环工程）且不引入幻觉或工作流碎片化的自主分析解决方案。无论技术水平如何，研究人员都需要能够简化复杂数据分析、提供基于数据和既有生物医学知识的有意义、可操作见解的工具。EcoXAI通过引入一个模块化、可定制、容器化的多智能体系统来解决这一问题，该系统将分析结构化为明确的流水线执行阶段，降低了临床和转化研究人员的计算门槛。

结果：EcoXAI用自主执行驱动的框架取代了单体AI文本界面，该框架配备专门的生物信息学智能体，能够基于已有的生物学知识提供主动、数据驱动的见解。与纯粹由大语言模型驱动或集成度较低的AI解决方案（容易产生幻觉或生物上不合理的结果）不同，EcoXAI的多智能体框架利用现代智能体管理和显式知识图谱集成，在其推理过程中提供了更高的透明度和可验证性。在我们针对阿尔茨海默病的药物重定位用例中，EcoXAI评估了103种候选药物，并识别出79种新型候选药物，其预测模型超过了随机基线，包括CCR5拮抗剂马拉维罗，其生成的假设随后得到了文献支持。这些结果证明了基于知识图谱的AI智能体在加速假设驱动的生物医学研究方面的潜力。

可用性和实现：EcoXAI可在GitHub上获取：https://github.com/EpistasisLab/EcoXAI。

联系方式：jason.moore@csmc.edu

## Abstract
MotivationAs biomedical datasets and knowledge graphs continue to grow in size, complexity, and heterogeneity, navigating and extracting actionable insights from them presents a major bottleneck for researchers. There is a clear need for autonomous analytical solutions that can utilize recent advancements in agentic AI such as agent harnessing and loop engineering without introducing hallucination or workflow fragmentation. Researchers, regardless of technical expertise, need tools that streamline complex data analysis and deliver meaningful, actionable insights grounded in both data and established biomedical knowledge. EcoXAI addresses this by introducing a modular, customizable, containerized multi-agent system that structures analysis into explicit pipeline execution stages, lowering the computational barrier for clinical and translational researchers.

ResultEcoXAI replaces monolithic AI text interfaces with an autonomous execution-driven framework with specialized bioinformatics agents for delivering proactive, data-driven insights grounded in established biological knowledge. Unlike purely LLM-driven or less integrated AI solutions prone to hallucinations or biologically implausible outcomes, EcoXAIs multi-agent framework, which leverages modern agentic management and explicit knowledge graph integration, provides greater transparency and verifiability in its reasoning. In our use case in drug repurposing for Alzheimers Disease, EcoXAI evaluated 103 drug candidates and identified 79 novel candidates whose predictive models exceeded a randomized baseline, including the CCR5 antagonist Maraviroc, whose generated hypothesis was subsequently supported by the literature. These results demonstrate the potential of knowledge graph-grounded AI agents to accelerate hypothesis-driven biomedical research.

Availability and implementationEcoXAI is available on GitHub at: https://github.com/EpistasisLab/EcoXAI.

Contactjason.moore@csmc.edu