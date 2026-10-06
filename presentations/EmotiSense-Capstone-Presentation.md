# EmotiSense - Capstone Presentation Draft

This is a slide-content draft, not a finished presentation deck. Replace the
marked items with verified project evidence and export to the format requested
by the instructor before submission. Do not present example content or
placeholder values as measured results.

## Slide 1 - Title

**EmotiSense: NLP Sentiment & Emotion Analyzer**

- Student: Mitansh Wagde
- Registration number: 23FE10CDS00347
- Branch / batch: B.Tech Data Science / Batch F
- Team members: [Add names and registration numbers if applicable]

## Slide 2 - Problem and objective

- Objective: analyze user-provided text for overall sentiment and emotional
  characteristics.
- Intended output: sentiment label and confidence, emotion scores, dominant
  emotion, concise explanation, and locally extracted keywords.
- Scope: an interactive demonstration, not a clinical or high-stakes decision
  system.

## Slide 3 - Application capabilities

- Streamlit interface for text input and results.
- Gemini API for contextual sentiment and emotion analysis.
- Python NLP preprocessing and TF-IDF keyword extraction.
- Expandable display of cleaned text, tokens, filtered tokens, and keywords.

## Slide 4 - Architecture and workflow

```text
User text
  ├── Local NLP: clean -> tokenize -> remove stopwords -> TF-IDF keywords
  └── Gemini: sentiment -> confidence -> emotion scores -> explanation
                                      ↓
                               Streamlit results
```

## Slide 5 - Implementation

- Interface: Streamlit (`app.py`)
- Preprocessing and keywords: NLTK and scikit-learn (`nlp_processor.py`)
- LLM request and JSON parsing: Google GenAI SDK (`llm_analyzer.py`)
- Settings and analysis prompt: `config/config.json` and `prompts/prompts.txt`

## Slide 6 - Demonstration

- Add a real screenshot of the running application before submission.
- Demonstrate one non-sensitive input and show the returned sentiment, emotion
  scores, explanation, and keyword/preprocessing details.
- Confirm the API key is configured locally; never show or include the key in
  the screenshot.

## Slide 7 - Testing and results

- Automated tests: [Add test cases, commands, and actual pass/fail results]
- Evaluation method and dataset: [Describe only if actually performed]
- Measured results: [Insert actual observations/metrics; otherwise state
  evaluation is pending]
- Do not infer accuracy or performance from a single demonstration.

## Slide 8 - Limitations and responsible use

- Results depend on the Gemini API, model behavior, network access, and quota.
- The model may produce incorrect or biased interpretations.
- Submitted text is sent to the configured Gemini service; avoid sensitive
  text.
- Not suitable as the sole basis for consequential decisions.

## Slide 9 - Contributions and project links

- Individual contributions: [List verified contributions by person]
- Personal repository:
  <https://github.com/mitanshwagde-svg/MUJ-DS-23FE10CDS00347>
- Team capstone repository: [Add the confirmed team repository URL]
- Issues / pull requests: [Link actual project issues and reviewed pull requests]

## Slide 10 - Next steps and Q&A

- Add test coverage and evaluate on a documented, suitable dataset.
- Capture genuine screenshots and record actual evaluation evidence.
- Complete the team repository, contribution record, and final presentation.
- Questions
