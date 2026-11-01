# AI Engineer Notebooks

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Notebook quality checks](https://github.com/harpreetsingh171190-cmyk/ai-engineer-notebooks/actions/workflows/notebook-ci.yml/badge.svg)](https://github.com/harpreetsingh171190-cmyk/ai-engineer-notebooks/actions/workflows/notebook-ci.yml)

Hands-on Colab notebooks for the **AI Engineer / Forward Deployed Engineer (FDE)** skill set. You build working systems on top of foundation models (model APIs, RAG, evals, agents, adaptation, security, serving) using raw APIs rather than frameworks.

Start here: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/harpreetsingh171190-cmyk/ai-engineer-notebooks/blob/main/00-setup/00-environment.ipynb)

## Highlights

- **Framework-free.** You write the agent loop, RAG pipeline, and evals from raw API calls first, so you understand what libraries such as LangChain or LlamaIndex do before you use them.
- **Evaluation first.** "Measure before you tune" appears early and returns in every later section.
- **Free to run.** The notebooks use the free [Groq](https://console.groq.com/) API, which needs no credit card. Topics that need a GPU (LoRA fine-tuning and self-hosted serving) have optional, clearly marked Colab GPU appendices.
- **Case studies.** Four end-to-end case studies combine the skills under realistic constraints, from a support assistant to a red-team robustness benchmark.
- **OpenAI-compatible.** The patterns carry over to OpenAI and, with small changes, to Anthropic.

## Who this is for

Backend and full-stack engineers moving into AI Engineer, FDE, Applied AI, or AI Solutions Engineer roles.

## Curriculum

Work from top to bottom. Each notebook installs its own dependencies, reads its API key from Colab secrets, and ends with exercises.

| Section | Topic | Notebooks |
|---|---|---|
| 00 | Setup | [Environment and cost hygiene](00-setup/00-environment.ipynb) |
| 01 | Model APIs | [Prompting](01-model-apis/00-prompting-basics.ipynb), [structured output](01-model-apis/01-structured-output.ipynb), [tool calling](01-model-apis/02-tool-calling.ipynb), [streaming](01-model-apis/03-streaming.ipynb), [context and caching](01-model-apis/04-context-and-caching.ipynb) |
| 02 | Evals I | [Measuring outputs](02-evals-basics/01-measuring-outputs.ipynb) |
| 03 | RAG | [What is RAG](03-rag/00-what-is-rag.ipynb), [embeddings and retrieval](03-rag/01-embeddings-retrieval.ipynb), [hybrid search and reranking](03-rag/02-hybrid-and-reranking.ipynb), [chunking](03-rag/03-chunking.ipynb), [why RAG fails](03-rag/04-why-rag-fails.ipynb) |
| 04 | Evals II | [Golden sets](04-evals/01-golden-sets.ipynb), [LLM as judge](04-evals/02-llm-as-judge.ipynb), [regression evals](04-evals/03-regression-evals.ipynb) |
| 05 | Agents | [Agent loop from scratch](05-agents/01-agent-loop-from-scratch.ipynb), [tool design](05-agents/02-tool-design.ipynb), [guardrails and budgets](05-agents/03-guardrails-and-budgets.ipynb), [MCP and the tool ecosystem](05-agents/04-mcp-and-the-tool-ecosystem.ipynb), [skills and progressive disclosure](05-agents/05-skills-and-progressive-disclosure.ipynb), [harness engineering](05-agents/06-harness-engineering.ipynb) |
| 06 | Adaptation | [Fine-tune vs RAG vs prompt](06-adaptation/01-fine-tune-vs-rag-vs-prompt.ipynb) |
| 07 | Security | [Prompt injection and trust](07-security/01-prompt-injection-and-trust.ipynb) |
| 08 | Operations | [Observability and LLMOps](08-operations/01-observability-and-llmops.ipynb), [reliability and fallbacks](08-operations/02-reliability-and-fallbacks.ipynb), [experiment tracking and registry](08-operations/03-experiment-tracking-and-registry.ipynb) |
| 09 | Serving and inference | [Serving frameworks](09-serving-inference/01-serving-frameworks.ipynb), [inference performance](09-serving-inference/02-inference-performance.ipynb) |
| 10 | ML system design | [Designing an inference service](10-ml-system-design/01-designing-an-inference-service.ipynb) |
| 11 | Customer craft | [Scoping and discovery](11-customer-craft/01-scoping-and-discovery.ipynb) |
| 12 | Case studies and capstone | [Customer-support assistant](12-case-studies-and-capstone/01-customer-support-assistant.ipynb), [contract extraction: pipeline vs agent](12-case-studies-and-capstone/02-contract-extraction-pipeline-vs-agent.ipynb), [red-team robustness benchmark](12-case-studies-and-capstone/03-red-team-robustness-benchmark.ipynb), [deepfake detection](12-case-studies-and-capstone/04-deepfake-image-detection.ipynb) |

The [section 12 overview](12-case-studies-and-capstone/README.md) explains how the case studies lead to the [capstone project](12-case-studies-and-capstone/CAPSTONE.md).

## Setup

1. Get a free API key at [console.groq.com](https://console.groq.com/).
2. In Colab, open the key icon in the left sidebar, add a secret named `GROQ_API_KEY`, and turn on notebook access.
3. Open any notebook from the table above and run it from top to bottom.

To run locally instead:

```bash
pip install -r requirements.txt
pip install -e .
export GROQ_API_KEY=your-key-here
jupyter notebook
```

## Quality checks

Run the offline checks, which need no API key:

```bash
python scripts/check_notebooks.py
python -m compileall -q aien
```

The first command checks the structure of all 34 notebooks and runs three standalone examples. CI runs the same commands on every push. The limits of these checks are described in [QUALITY_REPORT.md](QUALITY_REPORT.md).

## Credits

This project is based on [calmrocks/ai-engineer-notebooks](https://github.com/calmrocks/ai-engineer-notebooks), released under the MIT License. The original copyright notice is kept in [LICENSE](LICENSE). The modifications in this edition are maintained by [Harpreet Singh](https://github.com/harpreetsingh171190-cmyk).

## License

MIT. See [LICENSE](LICENSE).
