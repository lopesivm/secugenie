# SecuGenie 🧠🔐

**A local-first AI security copilot, built in 12 weeks.**

---

## 🚀 Project Goal

Build and ship a real-world, production-grade AI tool that:

1. Answers CVE questions with Retrieval-Augmented Generation (RAG)
2. Flags suspicious log lines with a fine-tuned transformer classifier
3. Triages static-analysis findings using an LLM agent

Each week targets a specific skill set and produces a useful, testable artifact.

---

## 🗂️ Project Structure

This is a monorepo with a single `pyproject.toml` (managed via Poetry) in the root:

```bash
secugenie/
├── pyproject.toml          # Poetry project config
├── .env                    # API keys (not committed)
├── bootcamp/               # Week 1: LangChain + CLI MVP
├── rag_prod/               # Week 2: Vector DB, RAG QA, API
├── agents/                 # Week 3: RouterAgent, tools, memory
├── finetune/               # Week 4: QLoRA, embeddings
├── infra/                  # Week 5: Docker, CI/CD, monitoring
└── docs/                   # Week 6+: system design, backlog
```

Each subfolder contains notebooks, scripts, and a `README.md` describing that week’s deliverables.

---

## 📆 Weekly Lessons

| Week | Focus              | Output                               |
| ---- | ------------------ | ------------------------------------ |
| 1    | LangChain, CLI MVP | `chat.py`, `ask_llm()` helper        |
| 2    | Vector store + RAG | Chroma indexer, query pipeline       |
| 3    | Agents & tools     | Threat intel agent with memory       |
| 4    | Fine-tuning        | Log classifier, embedding drift test |
| 5    | Infra              | Docker-compose stack, CI, monitoring |
| 6    | Polish & portfolio | System design doc, STAR bullets      |

---

## 🛠️ Getting Started

```bash
# Clone the project
git clone git@github.com:<your-username>/secugenie.git
cd secugenie

# Install dependencies
poetry install

# Add your keys to .env
OPENAI_API_KEY=sk-...
MISTRAL_API_KEY=...
MODEL=openai/gpt-4o

# Try out a lesson
poetry run python bootcamp/lesson_1_1_langchain_core/chat.py "Explain RAG in 2 lines"
```

---

## 💬 Questions / Feedback?

DM or open an issue!

Let’s build SecuGenie. 💥
