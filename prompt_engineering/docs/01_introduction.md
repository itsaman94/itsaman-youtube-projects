# 01 — Introduction to Prompts

> 📄 **Runnable file:** [`01_introduction.py`](../01_introduction.py)

This is where it all begins: understanding what a prompt is and how to write a
clear one.

---

## 📑 Table of Contents

- [▶️ What is a prompt?](#-what-is-a-prompt)
- [▶️ What is prompt engineering?](#-what-is-prompt-engineering)
- [🧱 The anatomy of a great prompt (4 building blocks)](#-the-anatomy-of-a-great-prompt-4-building-blocks)
- [🟥 Vague vs. 🟩 Clear — the most important lesson](#-vague-vs--clear--the-most-important-lesson)
- [🌡️ Key model settings you should know](#-key-model-settings-you-should-know)
- [✅ Takeaways](#-takeaways)

---

## ▶️ What is a prompt?

A **prompt** is simply the text you send to an AI model. It's your instruction,
your question, your request — the input that the model turns into an output.

## ▶️ What is prompt engineering?

Prompt engineering is the skill of writing those inputs *clearly and
strategically* so the model gives you exactly what you want.

> Think of the AI as an extremely well-read but very literal new intern:
> it knows a LOT, but it can't read your mind. **The clearer your instructions,
> the better the result.**

---

## 🧱 The anatomy of a great prompt (4 building blocks)

Most strong prompts combine four parts:

| # | Block | Example |
|---|-------|---------|
| 1 | **Role / Persona** | *"You are a helpful travel agent."* |
| 2 | **Instruction** | *"Suggest a 3-day trip."* |
| 3 | **Context / Input** | *"The traveler likes hiking and has a $500 budget."* |
| 4 | **Output format** | *"Answer as a bullet list, max 5 bullets."* |

Put together:

```
You are an experienced travel agent.          <- ROLE
Suggest a short weekend trip.                  <- INSTRUCTION
The traveler loves hiking and photography      <- CONTEXT
and has a $400 budget.
Reply with exactly 3 bullet points,            <- OUTPUT FORMAT
each under 20 words.
```

> These four blocks map directly onto the **Prompt Design Framework**
> (Role, Task, Instructions, Context, Input) from
> [Doc 00](00_what_is_prompt_engineering.md).

---

## 🟥 Vague vs. 🟩 Clear — the most important lesson

The single biggest improvement most people can make is to **be specific**.

| Vague prompt | Clear prompt |
|--------------|--------------|
| *"Write about dogs."* | *"Write a 3-sentence friendly paragraph about why Golden Retrievers make great family pets. Use simple words a 10-year-old understands."* |

**Vague in → vague out.** The clear version tells the model the *length*, the
*tone*, the *topic*, and the *audience* — so it can deliver something useful.

---

## 🌡️ Key model settings you should know

| Setting | What it controls | Tip |
|---------|------------------|-----|
| **temperature** | Randomness / creativity. `0.0` = focused & repeatable, `1.0` = creative. | Low for facts/code, high for brainstorming. |
| **max_tokens** | The maximum length of the answer. | Cap it to control cost and verbosity. |
| **top_p** | Another way to control randomness. | Leave at default at first. |

**Rule of thumb:**

- Facts, code, classification → **LOW** temperature (0.0 – 0.3)
- Brainstorming, stories, ideas → **HIGH** temperature (0.7 – 1.0)

The same prompt — *"Give me a creative name for a coffee shop run by cats"* — will
produce a safe, predictable name at `temperature=0` and a surprising, playful one
at `temperature=1.0`.

---

## ✅ Takeaways

- A prompt = the input you give an AI model.
- Clear, specific prompts beat vague ones **every time**.
- Great prompts often have: **Role + Instruction + Context + Format**.
- `temperature` controls creativity (low = factual, high = creative).
- Everything else in this course builds on these basics!

➡️ **Next:** [02 — Zero / One / Few-Shot](02_zero_one_few_shot.md)

