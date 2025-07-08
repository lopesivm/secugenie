# Lesson 1.1 — LangChain Core Quickstart 🚀

**Week 1 — LangChain Bootcamp**

---

## 🎯 Goal

Set up LangChain 0.3 using OpenAI and/or Mistral/Ollama, and build a reusable LLM interface (`ask_llm()`) that can be wired into a CLI (`chat.py`).
This is the foundation for every future component in SecuGenie: RAG, agents, fine-tuning, and triage.

---

## ✅ Milestones

| Step | Title                         | Description                                                                                                                     |
| ---- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| 1    | **Environment Setup**         | Initialize a Poetry project at the `secugenie/` root. Install LangChain + OpenAI + Mistral + dotenv + community. Create `.env`. |
| 2    | **Test LangChain Call**       | Create a test script to call `ChatOpenAI` using a prompt. Print the output. Verify key loads.                                   |
| 3    | **`ask_llm()` Helper**        | Build a function to abstract model usage: OpenAI or Mistral, based on name. Return plain string output.                         |
| 4    | **Ollama Support (optional)** | Add `local=True` mode using `langchain_community.llms.Ollama`. Run local LLMs like `mistral`, `llama3`.                         |
| 5    | **CLI Interface**             | Create `chat.py`, which reads a prompt from CLI and prints model output. Uses `ask_llm()` internally.                           |
| 6    | **Refactor & Commit**         | Structure into `ask_llm.py`, `chat.py`. Test. Clean code. Commit with tag.                                                      |

---

## 🧱 Folder Structure

```bash
bootcamp/lesson_1_1_langchain_core/
├── README.md                # ← This file
├── ask_llm.py              # ← Your helper function
├── chat.py                 # ← CLI entrypoint
├── 01_setup_env.ipynb      # ← Optional notebook for tests
└── .env                    # ← API keys (in root)
```

---

## 💡 `ask_llm()` Design Tip

```python
# ask_llm.py
from dotenv import dotenv_values

config = dotenv_values()


def ask_llm(prompt: str, model: str = "gpt-4o", local: bool = False) -> str:
    if local:
        from langchain_community.llms import Ollama
        llm = Ollama(model=model)
        return llm.invoke(prompt)
    else:
        from langchain_openai import ChatOpenAI
        llm = ChatOpenAI(model=model)
        return llm.invoke(prompt).content
```

Then in `chat.py`:

```python
import sys
from ask_llm import ask_llm

if __name__ == "__main__":
    prompt = sys.argv[1]
    print(ask_llm(prompt))
```

---

## 🏁 Final Output

By the end of Lesson 1.1, you should be able to:

- Run `poetry run python chat.py "What is a CVE?"`
- Get an answer from OpenAI, Mistral, or Ollama
- Swap models easily with `MODEL=` in your `.env`
- Reuse `ask_llm()` in future lessons

---

## 🚀 Commit Message

```bash
git add bootcamp/lesson_1_1_langchain_core/
git commit -m "feat: complete LangChain lesson 1.1 with ask_llm and CLI"
```

Let’s roll! 💪
