"""
This module provides a simple interface to interact with various local and remote
Large Language Models (LLMs) using the langchain library.

It defines available models and a function to send a message to a specified model.
"""

import time
from typing import TypedDict

from langchain_mistralai import ChatMistralAI
from langchain_ollama import OllamaLLM
from langchain_openai import ChatOpenAI

LOCAL_MODELS = {
    "mistral": {"model": OllamaLLM(model="mistral"), "available": True},
    "deepseek-r1": {"model": OllamaLLM(model="deepseek-r1"), "available": False},
}

REMOTE_MODELS = {
    "gpt-4o-mini": {"model": ChatOpenAI(model="gpt-4o-mini"), "available": True},
    "mistral": {
        "model": ChatMistralAI(model="mistral-small-latest"),
        "available": True,
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

    start_time = time.time()
    raw_response = model["model"].invoke(message)
    inference_time = time.time() - start_time

    if isinstance(raw_response, str):
        response = raw_response
    else:
        try:
            response = raw_response.content
        except AttributeError as err:
            raise ValueError("Response content not found") from err

    return LLMResponse(
        message=str(response),
        model_name=model_name,
        remote=remote,
        inference_time=round(inference_time, 2),
    )
