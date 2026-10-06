import os
import json
import time
from pathlib import Path

from google import genai
from google.genai import types
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Please add it to your .env file."
    )


# Create Gemini client
client = genai.Client(api_key=API_KEY)


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
    """
    Analyze sentiment and emotions using Gemini.

    Multiple available Gemini models are used as fallbacks
    in case a model is temporarily unavailable.
    """

    config = load_config()
    system_prompt = load_prompt()

    # Models confirmed to be available for this API key
    models_to_try = [
        config["model"],
        "gemini-flash-latest",
        "gemini-3.6-flash",
        "gemini-3.7-flash",
        "gemini-3.8-flash"
    ]

    # Remove duplicates while preserving order
    models_to_try = list(dict.fromkeys(models_to_try))

    user_prompt = f"""
Analyze the following text according to the system instructions.

TEXT:
{text}

Return ONLY the JSON object specified in the system instructions.
"""

    errors = []

    for model in models_to_try:

        # Try each model up to 2 times
        for attempt in range(2):

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

                response_text = response.text.strip()

                result = json.loads(response_text)

                # Record which model produced the result
                result["_model_used"] = model

                return result

            except json.JSONDecodeError as error:

                errors.append(
                    f"{model}: Invalid JSON response - {error}"
                )
                break

            except Exception as error:

                error_message = str(error)

                errors.append(
                    f"{model} attempt {attempt + 1}: {error_message}"
                )

                # Give temporary 503 errors a short retry
                if "503" in error_message and attempt == 0:
                    time.sleep(2)
                    continue

                break

    return {
        "error": "Gemini was temporarily unavailable.",
        "details": errors
    }