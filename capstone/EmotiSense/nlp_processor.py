import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer


def download_nltk_resources():
    """Download required NLTK resources."""
    resources = [
        ("tokenizers/punkt", "punkt"),
        ("tokenizers/punkt_tab", "punkt_tab"),
        ("corpora/stopwords", "stopwords")
    ]

    for resource_path, resource_name in resources:
        try:
            nltk.data.find(resource_path)
        except LookupError:
            nltk.download(resource_name, quiet=True)


download_nltk_resources()


def clean_text(text):
    """Clean input text using basic NLP preprocessing."""

    # Convert to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"https?://\S+|www\.\S+", "", text)

    # Remove special characters and numbers
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text


def tokenize_text(text):
    """Tokenize text using NLTK."""

    cleaned = clean_text(text)
    tokens = word_tokenize(cleaned)

    return tokens


def remove_stopwords(tokens):
    """Remove common English stopwords."""

    stop_words = set(stopwords.words("english"))

    filtered_tokens = [
        token for token in tokens
        if token not in stop_words
    ]

    return filtered_tokens


def extract_keywords(text, top_n=10):
    """Extract important keywords using TF-IDF."""

    cleaned = clean_text(text)

    if not cleaned.strip():
        return []

    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=top_n
    )

    try:
        matrix = vectorizer.fit_transform([cleaned])
        feature_names = vectorizer.get_feature_names_out()
        scores = matrix.toarray()[0]

        keywords = sorted(
            zip(feature_names, scores),
            key=lambda x: x[1],
            reverse=True
        )

        return [
            {
                "word": word,
                "score": round(float(score), 3)
            }
            for word, score in keywords
        ]

    except ValueError:
        return []


def analyze_text(text):
    """Perform basic NLP analysis."""

    tokens = tokenize_text(text)
    filtered_tokens = remove_stopwords(tokens)
    keywords = extract_keywords(text)

    return {
        "original_text": text,
        "cleaned_text": clean_text(text),
        "token_count": len(tokens),
        "tokens": tokens,
        "filtered_tokens": filtered_tokens,
        "keywords": keywords
    }