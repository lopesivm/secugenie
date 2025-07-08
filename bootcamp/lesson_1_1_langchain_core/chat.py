"""CLI application for interacting with Large Language Models.

This module provides a command-line interface to interact with various LLMs
using the ask_llm module. It supports both local and remote models.

Example:
    $ python chat.py "What is the capital of France?"
    or
    $ python chat.py "What is the capital of France?" --model mistral --remote
"""

import argparse
import sys

from ask_llm import ask_llm

DEFAULT_MODEL = "mistral"


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser for the CLI.

    Returns:
        An configured argument parser instance.
    """
    parser = argparse.ArgumentParser(
        description="Ask a question to a Large Language Model.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "message",
        type=str,
        help="The message/prompt to send to the model.",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=DEFAULT_MODEL,
        help="The name of the model to use (default: %(default)s).",
    )
    parser.add_argument(
        "--remote",
        action="store_true",
        help="Use a remote model instead of a local one (default: False).",
    )
    return parser


def main() -> int:
    """Main entry point for the CLI application.

    Returns:
        int: Exit code (0 for success, 1 for error)
    """
    parser = create_parser()
    args = parser.parse_args()

    try:
        response = ask_llm(
            model_name=args.model,
            message=args.message,
            remote=args.remote,
        )
        model_type = "remote" if args.remote else "local"
        inference_time = response["inference_time"]
        print(f"[{model_type}]{response['model_name']} ({inference_time}s):\n")
        print(response["message"])
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
