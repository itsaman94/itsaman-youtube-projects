"""
common/llm_client.py
====================

A tiny, friendly wrapper around an LLM so EVERY module in this course can talk
to a model with a single line of code:

    from common.llm_client import LLMClient

    llm = LLMClient()
    print(llm.ask("Say hello in one short sentence."))

Why this file exists
--------------------
Beginners shouldn't have to wrestle with SDK boilerplate in every example.
This wrapper hides the messy parts and gives us two simple methods:

    llm.ask("...")          -> send one prompt, get one string back
    llm.chat([...messages]) -> send a full conversation, get one string back

Two modes, zero setup headaches
-------------------------------
1. REAL MODE  : If an OPENAI_API_KEY is found (in your .env file), we call the
                real OpenAI API.
2. DEMO MODE  : If NO key is found, we fall back to a built-in simulator so the
                scripts still RUN on any machine. Perfect for following along
                in the video before you add billing/keys.

You can tell which mode you're in with:  llm.is_demo  (True/False)
"""

from __future__ import annotations

import os
import random
import sys
import textwrap

# Make sure emoji and special characters print correctly on Windows consoles
# (which default to the cp1252 code page and would otherwise crash or show
# garbled "mojibake" text). We switch both Python AND the console to UTF-8.
try:
    if sys.platform == "win32":
        import ctypes

        # Tell the Windows console itself to interpret output as UTF-8 (65001).
        ctypes.windll.kernel32.SetConsoleOutputCP(65001)
        ctypes.windll.kernel32.SetConsoleCP(65001)
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    sys.stderr.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except Exception:  # pragma: no cover - older Pythons / non-standard streams
    pass

# Load variables from a .env file if python-dotenv is installed.
try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception:  # pragma: no cover - dotenv is optional
    pass


# The default model. Cheap + fast + smart enough for everything in this course.
DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


class LLMClient:
    """A minimal, beginner-friendly LLM client.

    Parameters
    ----------
    model : str
        Which model to call (defaults to gpt-4o-mini or the OPENAI_MODEL env var).
    temperature : float
        Creativity / randomness. 0.0 = focused & repeatable, 1.0 = creative.
    system : str
        An optional default system prompt applied to every ``ask`` call.
    demo_responses : list[str] | None
        Only used in DEMO MODE. If a script provides a list of sample answers,
        the simulator will return them (randomly when temperature > 0). This
        lets demos look realistic even without an API key — for example, the
        Self-Consistency module can hand us several different reasoning paths.
    """

    def __init__(
        self,
        model: str | None = None,
        temperature: float = 0.7,
        system: str | None = None,
        demo_responses: list[str] | None = None,
        provider: str | None = None,
    ) -> None:
        self.model = model or DEFAULT_MODEL
        self.temperature = temperature
        self.system = system
        self.demo_responses = demo_responses
        self.provider = provider or self._detect_provider()
        self._openai_client = None

        if self.provider == "openai":
            self._init_openai()

    # ------------------------------------------------------------------ #
    # Setup helpers
    # ------------------------------------------------------------------ #
    def _detect_provider(self) -> str:
        """Use OpenAI if a key exists, otherwise the offline simulator."""
        if os.getenv("OPENAI_API_KEY"):
            return "openai"
        return "mock"

    def _init_openai(self) -> None:
        try:
            from openai import OpenAI

            self._openai_client = OpenAI()
        except Exception as exc:  # noqa: BLE001
            print(
                f"[LLMClient] Could not start the OpenAI client ({exc}).\n"
                f"            Falling back to DEMO MODE."
            )
            self.provider = "mock"

    @property
    def is_demo(self) -> bool:
        """True when we're returning simulated answers (no API key)."""
        return self.provider == "mock"

    # ------------------------------------------------------------------ #
    # The two methods you'll actually call
    # ------------------------------------------------------------------ #
    def ask(
        self,
        prompt: str,
        system: str | None = None,
        temperature: float | None = None,
    ) -> str:
        """Send a single prompt and get the model's reply as a string."""
        messages: list[dict] = []
        system_message = system or self.system
        if system_message:
            messages.append({"role": "system", "content": system_message})
        messages.append({"role": "user", "content": prompt})
        return self.chat(messages, temperature=temperature)

    def chat(
        self,
        messages: list[dict],
        temperature: float | None = None,
    ) -> str:
        """Send a list of {"role", "content"} messages and get one reply."""
        temp = self.temperature if temperature is None else temperature
        if self.provider == "openai":
            return self._chat_openai(messages, temp)
        return self._chat_mock(messages, temp)

    # ------------------------------------------------------------------ #
    # Provider implementations
    # ------------------------------------------------------------------ #
    def _chat_openai(self, messages: list[dict], temperature: float) -> str:
        response = self._openai_client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
        )
        return (response.choices[0].message.content or "").strip()

    def _chat_mock(self, messages: list[dict], temperature: float) -> str:
        """A fake model used when no API key is available.

        It can't *think*, but it keeps every script runnable and demonstrates
        the SHAPE of each technique. When a script supplies ``demo_responses``,
        we sample from those so the output looks realistic.
        """
        if self.demo_responses:
            if temperature and temperature > 0:
                return random.choice(self.demo_responses)
            return self.demo_responses[0]

        last_user = next(
            (m["content"] for m in reversed(messages) if m["role"] == "user"),
            "",
        )
        preview = textwrap.shorten(last_user.replace("\n", " "), width=180)
        return (
            "[DEMO MODE — no OPENAI_API_KEY found, so this is a simulated reply]\n"
            f'You asked: "{preview}"\n'
            "Set your API key in a .env file to see a real model response."
        )


def banner(title: str) -> None:
    """Pretty section header used by the example scripts."""
    line = "=" * 70
    print(f"\n{line}\n{title}\n{line}")


if __name__ == "__main__":
    # Quick self-test:  python common/llm_client.py
    client = LLMClient()
    banner("LLMClient self-test")
    print("Demo mode?", client.is_demo)
    print(client.ask("Give me a one-line definition of prompt engineering."))



