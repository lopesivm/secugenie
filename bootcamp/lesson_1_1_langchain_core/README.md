# Lesson 1.1 — LangChain Core Quickstart 🚀

**Week 1 — LLM App Bootcamp**

---

## Goal

Wrap an OpenAI or Mistral model behind a simple chat endpoint using **LangChain 0.3** so you can query it from any Python script or CLI tool.

You’ll also set up a clean project structure under `bootcamp/lesson_1_1_langchain_core/` within a single Poetry-managed workspace rooted at `secugenie/`, so each week’s progress is easy to track and share.

---

## Exercises

| #   | Title                       | What you’ll build                                                                                                                        |
| --- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Set up your environment** | Create a Poetry-managed Python project **at the root of `secugenie/`**, and install `langchain`, `openai`, `mistralai`, `python-dotenv`. |
| 2   | **Hello, ChatOpenAI**       | Send a "Hello, world!" prompt to OpenAI using `ChatOpenAI` (via `langchain_openai`) and print the model’s response.                      |
| 3   | **Wrap in a helper**        | Write a `ask_llm(prompt: str, model: str = ...) -> str` function that returns a model reply.                                             |
| 4   | **Swap to Mistral**         | Replace OpenAI with `ChatMistralAI` (via `langchain_mistralai`)—verify modularity. Requires Mistral API key.                             |
| 5   | **Turn it into a CLI**      | Create `chat.py` script callable from terminal: `python chat.py "What is RAG in LLMs?"`.                                                 |
| 6   | **BONUS – Config via .env** | Store your API keys + model in a `.env` file. Load them using `dotenv_values` from `python-dotenv`.                                      |

---

## Step-by-Step Setup (Poetry, Root-Based)

### 1. Environment Setup

```bash
# Create main project directory
mkdir -p secugenie && cd secugenie

# Initialize poetry at the project root
poetry init --name secugenie --python "^3.10" --dependency langchain --dependency openai --dependency mistralai --dependency python-dotenv -n

# Install dependencies
poetry install

# Create lesson folder for this week
mkdir -p bootcamp/lesson_1_1_langchain_core && cd bootcamp/lesson_1_1_langchain_core
```

### 2. Create a .env file in the project root

```env
OPENAI_API_KEY=sk-...
MISTRAL_API_KEY=...
MODEL=openai/gpt-4o
```

Make sure this file is listed in `.gitignore`.

### 3. Run a model call (from lesson folder)

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o")
response = llm.invoke("Hello, world!")
print(response.content)
```

To run scripts with Poetry:

```bash
poetry run python chat.py
```

---

## Key Takeaways

- LangChain v0.3 is **modular**—import from `langchain_core`, `langchain_openai`, etc.
- Use `ChatOpenAI` and `ChatMistralAI` to access models with unified APIs.
- Store secrets in `.env`, never in code.
- Maintain a single Poetry project at the root to streamline dependency management across all lessons.

---

## Output

Push this lesson to:

```
secugenie/bootcamp/lesson_1_1_langchain_core/
```

Tag your commit:

```
git commit -m "feat: lesson 1.1 complete"
```

Let’s rock! 🚀
