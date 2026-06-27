"""
==========================================================================
 MODULE 01 — INTRODUCTION TO PROMPT ENGINEERING
==========================================================================

▶ WHAT IS A PROMPT?
   A "prompt" is simply the text you send to an AI model. It's your
   instruction, your question, your request — the input that the model
   turns into an output.

▶ WHAT IS PROMPT ENGINEERING?
   Prompt engineering is the skill of writing those inputs *clearly and
   strategically* so the model gives you exactly what you want.

   Think of the AI as an extremely well-read but very literal new intern:
   - It knows a LOT.
   - But it can't read your mind.
   - The clearer your instructions, the better the result.

▶ THE ANATOMY OF A GREAT PROMPT (4 building blocks)
   1. ROLE / PERSONA   -> "You are a helpful travel agent."
   2. INSTRUCTION      -> "Suggest a 3-day trip."
   3. CONTEXT / INPUT  -> "The traveler likes hiking and has a $500 budget."
   4. OUTPUT FORMAT    -> "Answer as a bullet list, max 5 bullets."

▶ KEY MODEL SETTINGS YOU SHOULD KNOW
   - temperature : randomness. 0.0 = focused/repeatable, 1.0 = creative.
   - max_tokens  : the maximum length of the answer.
   - top_p       : another way to control randomness (leave default at first).

   Rule of thumb:
   - Facts, code, classification  -> LOW temperature (0.0 - 0.3)
   - Brainstorming, stories, ideas -> HIGH temperature (0.7 - 1.0)

--------------------------------------------------------------------------
 HOW TO RUN
   cd prompt_engineering
   python 01_introduction.py
--------------------------------------------------------------------------
"""

import os
import sys

# Make the shared "common" package importable no matter where you run from.
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from common.llm_client import LLMClient, banner


def demo_first_prompt() -> None:
    """Your very first prompt — as simple as it gets."""
    banner("1) Your first prompt")
    llm = LLMClient()
    answer = llm.ask("Explain what an API is in one simple sentence.")
    print(answer)


def demo_vague_vs_clear() -> None:
    """The single most important lesson: vague in -> vague out."""
    banner("2) Vague prompt  vs  Clear prompt")

    # temperature=0 -> we want a focused, repeatable answer
    llm = LLMClient(temperature=0)

    vague = "Write about dogs."
    clear = (
        "Write a 3-sentence friendly paragraph about why Golden Retrievers "
        "make great family pets. Use simple words a 10-year-old understands."
    )

    print("🟥 VAGUE PROMPT:", vague)
    print("   ->", llm.ask(vague))
    print()
    print("🟩 CLEAR PROMPT:", clear)
    print("   ->", llm.ask(clear))


def demo_four_building_blocks() -> None:
    """Combine Role + Instruction + Context + Output format in one prompt."""
    banner("3) The 4 building blocks in action")

    prompt = (
        # 1. ROLE
        "You are an experienced travel agent.\n"
        # 2. INSTRUCTION
        "Suggest a short weekend trip.\n"
        # 3. CONTEXT
        "The traveler loves hiking and photography and has a $400 budget.\n"
        # 4. OUTPUT FORMAT
        "Reply with exactly 3 bullet points, each under 20 words."
    )

    print("PROMPT SENT TO MODEL:\n" + prompt)
    print("\nMODEL ANSWER:")
    print(LLMClient(temperature=0.7).ask(prompt))


def demo_temperature_effect() -> None:
    """Same prompt, two temperatures — see focused vs creative."""
    banner("4) How 'temperature' changes the output")

    prompt = "Give me a creative name for a coffee shop run by cats."

    print("temperature = 0.0 (focused / safe):")
    print("  ", LLMClient(temperature=0.0).ask(prompt))
    print("\ntemperature = 1.0 (creative / surprising):")
    print("  ", LLMClient(temperature=1.0).ask(prompt))


if __name__ == "__main__":
    llm = LLMClient()
    if llm.is_demo:
        print(
            "\nℹ️  Running in DEMO MODE (no OPENAI_API_KEY found).\n"
            "   You'll see simulated answers. Add a .env file with your key\n"
            "   to see real model responses — the CODE stays exactly the same.\n"
        )

    # demo_first_prompt()
    # demo_vague_vs_clear()
    # demo_four_building_blocks()
    demo_temperature_effect()

    banner("TAKEAWAYS")
    print(
        "• A prompt = the input you give an AI model.\n"
        "• Clear, specific prompts beat vague ones every time.\n"
        "• Great prompts often have: Role + Instruction + Context + Format.\n"
        "• temperature controls creativity (low = factual, high = creative).\n"
        "• Everything else in this course builds on these basics!"
    )

