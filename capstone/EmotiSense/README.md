# EmotiSense

EmotiSense is a Streamlit application for sentiment and emotion analysis. It
uses Python preprocessing and TF-IDF for local text features and Google's
Gemini API for sentiment, emotion scores, and an explanation.

## Features

- Classifies input as Positive, Negative, Neutral, or Mixed using Gemini.
- Displays sentiment confidence, emotion scores, the dominant emotion, and an
  explanation.
- Cleans and tokenizes text, removes English stopwords, and extracts TF-IDF
  keywords locally.
- Shows preprocessing details in the Streamlit interface.

The model's output is generated and may be inaccurate. Do not use the results
as professional advice or as the sole basis for consequential decisions. Text
submitted for analysis is sent to the configured Gemini service; do not submit
sensitive or identifying information.

## Requirements

- Python 3.10 or newer
- A Google Gemini API key
- Internet access for initial NLTK resource downloads and Gemini analysis
- Gemini model: `gemini-3.5-flash-lite` (configured in `config/config.json`)

## Installation

Run these commands from this directory (`capstone/EmotiSense`):

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Edit `.env` and replace `YOUR_GEMINI_API_KEY` with your own key:

```text
GEMINI_API_KEY=your_actual_key
```

Keep `.env` private. It is ignored by Git; never commit or share it. The
`.env.example` file is safe to commit because it contains only a placeholder.

## Run

With the virtual environment activated and `.env` configured:

```powershell
streamlit run app.py
```

Open the local URL printed by Streamlit, enter text, and select **Analyze
Text**. The first NLP import downloads the required NLTK tokenizer and English
stopword data if they are not already installed. Gemini analysis requires a
valid API key and available model/API quota.

## Project layout

```text
EmotiSense/
├── app.py                 # Streamlit user interface
├── llm_analyzer.py        # Gemini API request and response parsing
├── nlp_processor.py       # Cleaning, tokenization, stopwords, and TF-IDF
├── config/config.json     # Model and generation settings
├── prompts/prompts.txt    # Sentiment/emotion analysis instructions
├── requirements.txt       # Python dependencies
└── .env.example           # Environment variable template (no real key)
```

## Analysis flow

```text
Text input
  ├── Local processing: cleaning -> tokenization -> stopword filtering -> TF-IDF keywords
  └── Gemini API: sentiment -> confidence -> emotion scores -> explanation
                                     ↓
                              Streamlit results
```

## Deliverables and verification

The source and setup guide are included in this repository. Add actual
application screenshots and measured test/evaluation results under the
repository's `resources/` directory before final submission. Do not report
illustrative model outputs as measured results. The presentation draft is in
the repository's `presentations/` directory and still needs real screenshots,
evaluation evidence, and any final team details.

Run the local preprocessing unit tests from this directory:

```powershell
python -m unittest discover -s tests -v
```

These tests cover text normalization and keyword extraction. They do not call
Gemini or evaluate model accuracy. Captured screenshots and measured model
evaluation results are not included at this time.
