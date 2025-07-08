"""
This module provides a simple interface to interact with various local and remote
Large Language Models (LLMs) using the langchain library.

It defines available models and a function to send a message to a specified model.
"""

import os
import time
from pathlib import Path
from typing import TypedDict

from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_ollama import OllamaLLM
from langchain_openai import ChatOpenAI

# Load .env from project root
root_dir = Path(__file__).resolve().parents[3]
load_dotenv(root_dir / ".env")

# Configure API clients
CHAT_OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CHAT_MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

LOCAL_MODELS = {
    "mistral": {"model": OllamaLLM(model="mistral"), "available": True},
    "deepseek-r1": {"model": OllamaLLM(model="deepseek-r1"), "available": False},
}

REMOTE_MODELS = {
    "gpt-4o-mini": {
        "model": ChatOpenAI(model="gpt-4o-mini", api_key=CHAT_OPENAI_API_KEY),
        "available": bool(CHAT_OPENAI_API_KEY),
    },
    "mistral": {
        "model": ChatMistralAI(
            model="mistral-small-latest", api_key=CHAT_MISTRAL_API_KEY
        ),
        "available": bool(CHAT_MISTRAL_API_KEY),
    },
}


class LLMResponse(TypedDict):
    """Type definition for LLM response.

    Attributes:
        message: The response text from the LLM.
        model_name: The name of the model that generated the response.
        remote: Whether the response came from a remote or local model.
        inference_time: Time taken to execute the request in seconds.
    """

    message: str
    model_name: str
    remote: bool
    inference_time: float


def ask_llm(model_name: str, message: str, remote: bool = False) -> LLMResponse:
    """Sends a message to a specified LLM and returns the response.

    Args:
        model_name: The name of the model to use (e.g., "mistral", "gpt-4o-mini").
        message: The message/prompt to send to the model.
        remote: A boolean flag to indicate whether to use a remote or local model.
               Defaults to False.

    Returns:
        LLMResponse containing:
            message: The response text from the LLM
            model_name: Name of the model used
            remote: Whether a remote or local model was used

    Raises:
        ValueError: If the specified model is not found or is not available.
    """
    if remote:
        model = REMOTE_MODELS.get(model_name)
    else:
        model = LOCAL_MODELS.get(model_name)

    if not model or not model["available"]:
        raise ValueError(f"Model {model_name} not found or not available")

    t0 = time.time()
    raw = model["model"].invoke(message)
    inference_time = round(time.time() - t0, 2)

    response_text = getattr(raw, "content", str(raw))

    return LLMResponse(
        message=response_text,
        model_name=model_name,
        remote=remote,
        inference_time=inference_time,
    )
