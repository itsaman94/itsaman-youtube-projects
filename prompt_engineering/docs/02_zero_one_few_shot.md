# 02 — Zero-Shot, One-Shot & Few-Shot Prompting

> 📄 **Runnable file:** [`02_zero_one_few_shot.py`](../02_zero_one_few_shot.py)

The word **"shot"** just means **"example"**. The core question of this lesson:
*how many examples do you show the model inside the prompt before asking it to do
the real task?*

---

## 📑 Table of Contents

- [🎯 The three flavours](#-the-three-flavours)
- [🧠 How to choose](#-how-to-choose)
- [✨ Few-shot shines for custom formats](#-few-shot-shines-for-custom-formats)
- [🏆 Golden rules for examples](#-golden-rules-for-examples)
- [✅ Takeaways](#-takeaways)

---

## 🎯 The three flavours

| Flavour | # Examples | Best for |
|---------|-----------|----------|
| **Zero-shot** | 0 | Common, obvious tasks. Fast and simple. |
| **One-shot** | 1 | Locking in a specific **style** or **format**. |
| **Few-shot** | 2+ | Custom formats, tricky edge cases, unusual tasks. |

### ▶ Zero-shot (0 examples)
You give only an instruction — no examples.

```
Classify this review as Positive or Negative: "I loved it!"
```

✅ Fast and simple. Great when the task is common/obvious.

### ▶ One-shot (1 example)
You show **one** example of input → output, then ask for a new one. This helps
the model copy your exact **style** or **format**.

```
Classify the sentiment as Positive, Negative, or Mixed.

Review: The food was cold and the waiter was rude.
Sentiment: Negative

Review: The screen is gorgeous but the battery dies in 2 hours.
Sentiment:
```

### ▶ Few-shot (2+ examples)
You show **several** examples. The model learns the pattern from them. This is
called **in-context learning** — the model "learns" from examples *without*
being retrained.

```
Review: Absolutely love it, works perfectly!
Sentiment: Positive

Review: Total waste of money, broke on day one.
Sentiment: Negative

Review: Great camera, but it's way too expensive.
Sentiment: Mixed

Review: The screen is gorgeous but the battery dies in 2 hours.
Sentiment:
```

---

## 🧠 How to choose

```
Start zero-shot.
   |
   v
Is the output wrong or badly formatted?
   |                         |
  No                        Yes
   |                         |
 Done!            Add ONE example (one-shot)
                             |
                             v
                  Still not right? Add MORE (few-shot)
```

Start **zero-shot**. If the output is wrong or badly formatted, add examples
(one-shot, then few-shot) until it behaves. More examples = more guidance, but
also a **longer (more expensive) prompt**.

---

## ✨ Few-shot shines for custom formats

Few-shot is especially powerful when you need a **specific output shape**, like
JSON:

```
Extract the product and the problem from each review as JSON.

Review: My new Dell laptop keeps overheating.
{"product": "Dell laptop", "problem": "overheating"}

Review: The Sony headphones have terrible bluetooth lag.
{"product": "Sony headphones", "problem": "bluetooth lag"}

Review: The screen is gorgeous but the battery dies in 2 hours.
```

The examples teach the model the **exact JSON structure** to follow.

---

## 🏆 Golden rules for examples

- Keep the **format of every example IDENTICAL**.
- Cover **different cases** (e.g., include a Positive AND a Negative).
- Put the **real question in the same format** as your examples.

---

## ✅ Takeaways

- **"Shot" = example** shown inside the prompt.
- **Zero-shot:** instruction only — try this first.
- **One-shot:** one example — locks in the style/format.
- **Few-shot:** many examples — best for tricky/custom tasks.
- Keep every example in the **same format** and cover different cases.

➡️ **Next:** [03 — Chain of Thought](03_chain_of_thought.md)

