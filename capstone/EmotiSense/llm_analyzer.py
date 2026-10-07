import os
import json
from pathlib import Path

from google import genai
from google.genai import errors
from google.genai import types
from dotenv import load_dotenv
import httpx


# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Please add it to your .env file."
    )


# Bound the network wait and disable SDK retries so the app reports an API
# failure promptly instead of remaining in the Streamlit spinner.
client = genai.Client(
    api_key=API_KEY,
    http_options=types.HttpOptions(
        timeout=15_000,
        retry_options=types.HttpRetryOptions(attempts=1),
    ),
)


# Project paths
BASE_DIR = Path(__file__).resolve().parent
PROMPT_FILE = BASE_DIR / "prompts" / "prompts.txt"
CONFIG_FILE = BASE_DIR / "config" / "config.json"


def load_prompt():
    """Load the system prompt from prompts.txt."""

    with open(PROMPT_FILE, "r", encoding="utf-8") as file:
        return file.read()


def load_config():
    """Load project configuration."""

    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def analyze_with_llm(text):
    """Analyze sentiment and emotions using the configured Gemini model."""

    config = load_config()
    system_prompt = load_prompt()
    model = config["model"]

    user_prompt = f"""
Analyze the following text according to the system instructions.

TEXT:
{text}

Return ONLY the JSON object specified in the system instructions.
"""

    try:
        response = client.models.generate_content(
            model=model,
            contents=user_prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=config["temperature"],
                max_output_tokens=config["max_tokens"],
                response_mime_type="application/json"
            )
        )

        if not response.text:
            raise ValueError("Gemini returned an empty response.")

        result = json.loads(response.text)
        result["_model_used"] = model
        return result

    except (errors.APIError, httpx.HTTPError, ValueError) as error:
        return {
            "error": "Gemini analysis failed or timed out. Please try again.",
            "details": [f"{type(error).__name__}: {error}"]
        }