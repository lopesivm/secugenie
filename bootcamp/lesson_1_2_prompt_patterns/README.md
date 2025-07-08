# Lesson 1.2 — Prompt Patterns 🧩

**Week 1 — LLM App Bootcamp**

---

## 🎯 Goal

Master the core prompt‑engineering patterns you’ll reuse throughout SecuGenie:

1. **Few‑shot** → leverage examples to steer the model.
2. **Chain‑of‑Thought (CoT)** → coax step‑by‑step reasoning.
3. **ReAct** (Reason + Act) → interleave thinking with tool calls.
4. **Self‑Consistency** → sample multiple thoughts and pick the best.

You’ll implement these in LangChain 0.3 so they plug straight into later RAG and agent pipelines.

---

## ✅ Milestones & Exercises

| Step | Pattern                     | What you’ll build                                                                                                                            |
| ---- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | **Few‑shot Q\&A**           | Use `PromptTemplate` to supply 2 sample CVE Q\&As, then ask a new question. Measure quality vs zero‑shot.                                    |
| 2    | **CoT Math**                | Prompt GPT‑4o‑mini to solve “(87 × 23) / 46” with `"Let’s think step by step"` and parse the answer.                                         |
| 3    | **ReAct + Calculator Tool** | Implement a simple `calculate(expr)` tool (Python eval) and use LangChain’s ReAct agent to answer “What’s the square root of (511² + 498²)?” |
| 4    | **Self‑Consistency Voting** | Sample 5 CoT traces for “Which year did Heartbleed (CVE‑2014‑0160) surface?” Aggregate majority answer.                                      |
| 5    | **Benchmark**               | Create `prompt_eval.py` that times each pattern on the same prompt set and prints accuracy / latency.                                        |

---

## 🗂️ Folder Layout

```bash
bootcamp/lesson_1_2_prompt_patterns/
├── README.md              # ← this file
├── few_shot.py            # Exercise 1
├── cot_math.py            # Exercise 2
├── react_calc.py          # Exercise 3
├── self_consistency.py    # Exercise 4
└── prompt_eval.py         # Exercise 5
```

> **Tip:** Reuse `ask_llm()` from Lesson 1.1; just import it with:
>
> ```python
> from bootcamp.lesson_1_1_langchain_core.ask_llm import ask_llm
> ```

---

## 🏁 Success Criteria

By the end of this lesson you can:

- Demonstrate each pattern on the command line.
- Explain when to use few‑shot vs CoT vs ReAct.
- Measure latency & token cost for each pattern.
- Commit code + a short notebook or markdown report summarising findings.

---

## 🚀 Commit Message Template

```bash
git add bootcamp/lesson_1_2_prompt_patterns/
git commit -m "feat: lesson 1.2 prompt patterns (few‑shot, CoT, ReAct)"
```

Let’s prompt like a pro! 🧙‍♂️
