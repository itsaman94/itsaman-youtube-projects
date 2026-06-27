# 🧠 Prompt Engineering — From Zero to Hero

A complete, **beginner-friendly** prompt engineering course with runnable Python
examples. Every module is a single, well-commented file you can run, read, and
follow along with in the video.

> 💡 **Runs with or without an API key.** If you don't add an OpenAI key, every
> script automatically switches to **Demo Mode** and prints simulated answers,
> so you can follow along on any machine. Add a key later and the *exact same
> code* talks to a real model.

> 📖 **Prefer to read the theory first?** Every topic is explained in plain
> language in the **[`docs/`](docs/README.md)** folder — start with
> [*What Is Prompt Engineering?*](docs/00_what_is_prompt_engineering.md).

---

## 📚 What you'll learn

| #  | Module | What it teaches |
|----|--------|-----------------|
| 01 | [Introduction](01_introduction.py) | What a prompt is, the 4 building blocks, and `temperature` |
| 02 | [Zero / One / Few-Shot](02_zero_one_few_shot.py) | Teaching the model with 0, 1, or many examples |
| 03 | [Chain of Thought](03_chain_of_thought.py) | "Think step by step" for better reasoning |
| 04 | [Role & Contextual](04_role_contextual.py) | Give the model a persona + the facts it needs |
| 05 | [ReAct](05_react.py) | Reasoning + **Acting** with tools (the basis of AI agents) |
| 06 | [Retrieval-Augmented (RAG)](06_retrieval_augmented.py) | Answer from *your* documents, not the model's memory |
| 07 | [Self-Consistency](07_self_consistency.py) | Sample many answers and take a majority **vote** |
| 08 | [Tree of Thought](08_tree_of_thought.py) | Explore, score, and prune a **tree** of ideas |
| 09 | [Guardrails](09_guardrails.py) | Input/output safety checks to ship AI responsibly |

---

## 🚀 Quick start

```powershell
# 1. Go into the course folder
cd prompt_engineering

# 2. Install the (tiny) dependency list
pip install -r requirements.txt

# 3. (Optional) Add your OpenAI key for REAL answers
#    Copy .env.example to .env and paste your key inside.
copy .env.example .env

# 4. Run any module!
python 01_introduction.py
```

> No API key? No problem — just run the scripts and you'll see clearly-labelled
> **Demo Mode** output that still demonstrates every technique.

### Getting an API key (optional)
1. Sign up at <https://platform.openai.com>.
2. Create a key at <https://platform.openai.com/api-keys>.
3. Put it in your `.env` file:
   ```dotenv
   OPENAI_API_KEY=sk-your-key-here
   OPENAI_MODEL=gpt-4o-mini
   ```

---

## 🗂️ Project structure

```
prompt_engineering/
├── README.md                  ← you are here
├── requirements.txt           ← dependencies
├── .env.example               ← copy to .env and add your key
├── docs/                      ← 📖 theory for every topic (start here to read)
│   ├── README.md              ← docs index
│   ├── 00_what_is_prompt_engineering.md
│   └── 01–11 … one per topic
├── common/
│   └── llm_client.py          ← shared helper (real API + demo mode)
├── 01_introduction.py
├── 02_zero_one_few_shot.py
├── 03_chain_of_thought.py
├── 04_role_contextual.py
├── 05_react.py
├── 06_retrieval_augmented.py
├── 07_self_consistency.py
├── 08_tree_of_thought.py
└── 09_guardrails.py
```

Each `.py` file is **self-contained**: a detailed explanation lives at the top
as a comment, followed by clear, runnable example functions.

---

## 🧭 The techniques at a glance

### 1. Introduction
A **prompt** is the text you send an AI. Good prompts usually combine four
building blocks: **Role + Instruction + Context + Output format**. `temperature`
controls creativity (low = factual, high = creative).

### 2. Zero-, One- & Few-Shot
"Shot" = example. Show **0**, **1**, or **many** examples inside the prompt to
teach the model your desired format. Start zero-shot; add examples if needed.

### 3. Chain of Thought (CoT)
Ask the model to **reason step by step** before answering. Hugely improves math,
logic, and multi-step tasks. The magic phrase: *"Let's think step by step."*

### 4. Role & Contextual Prompting
**Role** sets *who* the model is (tone & expertise). **Context** gives it the
*facts* it needs. Combine them for accurate, on-brand answers.

### 5. ReAct (Reasoning + Acting)
The model loops through **Thought → Action → Observation**, using **tools**
(calculator, search, databases). This is how modern **AI agents** work.

### 6. Retrieval-Augmented Generation (RAG)
**Retrieve** relevant documents, **paste** them into the prompt, then **answer**
from them. Grounds responses in *your* data and reduces hallucinations.

### 7. Self-Consistency
Run Chain of Thought **several times** with randomness, then take the **majority
vote**. Correct reasoning paths agree; wrong ones scatter.

### 8. Tree of Thought (ToT)
**Branch** into multiple ideas, **score** them, **prune** the weak ones, and go
deeper on the best — like a chess player exploring moves.

### 9. Guardrails
**Safety checks around the model.** Validate the *input* (block injections,
redact PII, filter topics) and the *output* (check format and safety) before
anything reaches your user.

---

## 🧾 Cheat sheet

| Technique | One-liner | Best for |
|-----------|-----------|----------|
| Zero-shot | Just ask | Common, simple tasks |
| Few-shot | Show examples | Custom formats / styles |
| Chain of Thought | "Think step by step" | Math, logic, reasoning |
| Role prompting | "You are a…" | Tone & expertise control |
| Contextual | Provide the facts | Accurate, grounded answers |
| ReAct | Think → act with tools | Agents, live data, exact math |
| RAG | Retrieve then answer | Q&A over your documents |
| Self-Consistency | Vote across answers | Hard reasoning, accuracy |
| Tree of Thought | Branch, score, prune | Planning & open-ended problems |
| Guardrails | Validate in & out | Safety & production readiness |

---

## ▶️ Run everything at once

```powershell
python run_all.py
```

---

## 📝 License & use
Free to use for learning, teaching, and your own projects. Happy prompting! 🎉

