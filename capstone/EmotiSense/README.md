# 🧠 EmotiSense

## NLP Sentiment & Emotion Analyzer

EmotiSense is an NLP-based sentiment and emotion analysis application that combines traditional Natural Language Processing techniques with Google's Gemini Large Language Model.

The application accepts natural language text and analyzes its overall sentiment, emotional characteristics, and important keywords.

---

## 🚀 Features

- Sentiment classification
- Sentiment confidence score
- Multi-emotion detection
- Dominant emotion identification
- AI-generated emotional explanation
- Text preprocessing
- Tokenization
- Stopword removal
- TF-IDF keyword extraction
- Google Gemini API integration
- Structured JSON responses
- Streamlit-based interactive interface
- Fallback handling for temporary Gemini API failures

---

## 🧠 NLP Pipeline

The application follows this pipeline:

```text
User Input
    ↓
Text Cleaning
    ↓
Tokenization
    ↓
Stopword Removal
    ↓
TF-IDF Keyword Extraction
    ↓
Gemini LLM Analysis
    ↓
Sentiment + Emotion Classification
    ↓
Interactive Results