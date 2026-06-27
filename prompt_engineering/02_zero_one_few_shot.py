"""
==========================================================================
 MODULE 02 — ZERO-SHOT, ONE-SHOT & FEW-SHOT PROMPTING
==========================================================================

The word "shot" just means "EXAMPLE". How many examples do you show the
model *inside the prompt* before asking it to do the real task?

▶ ZERO-SHOT  (0 examples)
   You give only an instruction — no examples.
   "Classify this review as Positive or Negative: 'I loved it!'"
   ✅ Fast and simple. Great when the task is common/obvious.

▶ ONE-SHOT  (1 example)
   You show ONE example of input -> output, then ask for a new one.
   Helps the model copy your exact STYLE or FORMAT.

▶ FEW-SHOT  (2+ examples)
   You show SEVERAL examples. The model learns the pattern from them.
   ✅ Best for custom formats, tricky edge cases, or unusual tasks.
   This is "learning from examples" WITHOUT retraining the model —
   it's often called "in-context learning".

▶ HOW TO CHOOSE
   Start zero-shot. If the output is wrong or badly formatted, add
   examples (one-shot, then few-shot) until it behaves. More examples =
   more guidance, but also a longer (more expensive) prompt.

▶ GOLDEN RULES FOR EXAMPLES
   - Keep the format of every example IDENTICAL.
   - Cover different cases (e.g., include a Positive AND a Negative).
   - Put the real question in the SAME format as your examples.

--------------------------------------------------------------------------
 HOW TO RUN
   cd prompt_engineering
   python 02_zero_one_few_shot.py
--------------------------------------------------------------------------
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from common.llm_client import LLMClient, banner


# We use temperature=0 because classification should be consistent.
llm = LLMClient(temperature=0)

REVIEW_TO_CLASSIFY = "The screen is gorgeous but the battery dies in 2 hours."


def zero_shot() -> None:
    banner("ZERO-SHOT — just an instruction, no examples")

    prompt = (
        "Classify the sentiment of this product review as "
        "Positive, Negative, or Mixed.\n\n"
        f"Review: {REVIEW_TO_CLASSIFY}\n"
        "Sentiment:"
    )

    print(prompt)
    print("\nMODEL ->", llm.ask(prompt))


def one_shot() -> None:
    banner("ONE-SHOT — show ONE example first")

    prompt = (
        "Classify the sentiment as Positive, Negative, or Mixed.\n\n"
        # --- the single example (teaches the format) ---
        "Review: The food was cold and the waiter was rude.\n"
        "Sentiment: Negative\n\n"
        # --- the real task (same format) ---
        f"Review: {REVIEW_TO_CLASSIFY}\n"
        "Sentiment:"
    )

    print(prompt)
    print("\nMODEL ->", llm.ask(prompt))


def few_shot() -> None:
    banner("FEW-SHOT — show SEVERAL labelled examples")

    prompt = (
        "Classify the sentiment as Positive, Negative, or Mixed.\n\n"
        "Review: Absolutely love it, works perfectly!\n"
        "Sentiment: Positive\n\n"
        "Review: Total waste of money, broke on day one.\n"
        "Sentiment: Negative\n\n"
        "Review: Great camera, but it's way too expensive.\n"
        "Sentiment: Mixed\n\n"
        f"Review: {REVIEW_TO_CLASSIFY}\n"
        "Sentiment:"
    )

    print(prompt)
    print("\nMODEL ->", llm.ask(prompt))


def few_shot_custom_format() -> None:
    """Few-shot shines when you need a SPECIFIC output format (e.g., JSON)."""
    banner("FEW-SHOT for a custom format — extract data as JSON")

    prompt = (
        "Extract the product and the problem from each review as JSON.\n\n"
        'Review: My new Dell laptop keeps overheating.\n'
        '{"product": "Dell laptop", "problem": "overheating"}\n\n'
        'Review: The Sony headphones have terrible bluetooth lag.\n'
        '{"product": "Sony headphones", "problem": "bluetooth lag"}\n\n'
        f"Review: {REVIEW_TO_CLASSIFY}\n"
    )

    print(prompt)
    print("\nMODEL ->", llm.ask(prompt))


if __name__ == "__main__":
    if llm.is_demo:
        print(
            "\nℹ️  DEMO MODE: answers are simulated. Add your OPENAI_API_KEY "
            "in a .env file for real results.\n"
        )

    zero_shot()
    one_shot()
    few_shot()
    few_shot_custom_format()

    banner("TAKEAWAYS")
    print(
        "• 'Shot' = example shown inside the prompt.\n"
        "• Zero-shot: instruction only — try this first.\n"
        "• One-shot: one example — locks in the style/format.\n"
        "• Few-shot: many examples — best for tricky/custom tasks.\n"
        "• Keep every example in the SAME format and cover different cases."
    )

