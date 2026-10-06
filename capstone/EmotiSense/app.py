import streamlit as st

from nlp_processor import analyze_text
from llm_analyzer import analyze_with_llm


st.set_page_config(
    page_title="EmotiSense",
    page_icon="🧠",
    layout="centered"
)


# Custom styling
st.markdown(
    """
    <style>
        .main-title {
            text-align: center;
            font-size: 42px;
            font-weight: 700;
            margin-bottom: 0;
        }

        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #666666;
            margin-bottom: 30px;
        }

        .result-box {
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #dddddd;
            margin-bottom: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Header
# -----------------------------

st.markdown(
    '<div class="main-title">🧠 EmotiSense</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">NLP Sentiment & Emotion Analyzer</div>',
    unsafe_allow_html=True
)

st.write(
    "Analyze text using traditional Natural Language Processing "
    "and Google Gemini to identify sentiment, emotions, "
    "and important keywords."
)

st.divider()


# -----------------------------
# User Input
# -----------------------------

text = st.text_area(
    "Enter your text",
    placeholder=(
        "Example: I worked really hard for this exam, "
        "but I am disappointed with my result."
    ),
    height=150
)


# -----------------------------
# Analyze Button
# -----------------------------

if st.button("🔍 Analyze Text", use_container_width=True):

    if not text.strip():

        st.warning("Please enter some text before analyzing.")

    else:

        with st.spinner("Analyzing your text..."):

            # Traditional NLP
            nlp_result = analyze_text(text)

            # Gemini analysis
            llm_result = analyze_with_llm(text)


        # -----------------------------
        # Error Handling
        # -----------------------------

        if "error" in llm_result:

            st.error(
                "Unable to complete the Gemini analysis."
            )

            st.write(llm_result)

        else:

            # -----------------------------
            # Sentiment
            # -----------------------------

            st.subheader("📊 Sentiment")

            sentiment = llm_result.get(
                "sentiment",
                "Unknown"
            )

            confidence = llm_result.get(
                "sentiment_confidence",
                0
            )

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Overall Sentiment",
                    sentiment
                )

            with col2:
                st.metric(
                    "Confidence",
                    f"{confidence * 100:.1f}%"
                )


            st.divider()


            # -----------------------------
            # Emotions
            # -----------------------------

            st.subheader("🎭 Emotion Analysis")

            emotions = llm_result.get(
                "emotions",
                {}
            )

            if emotions:
                dominant_emotion = max(
                    emotions,
                    key=emotions.get
                )

                dominant_score = emotions[dominant_emotion]

                st.markdown(
                    f"""
                    <div class="result-box">
                        <h3>🎭 Dominant Emotion</h3>
                        <h2>{dominant_emotion.capitalize()}</h2>
                        <p>Intensity: {dominant_score * 100:.1f}%</p>
                    </div>
                   """,
                    unsafe_allow_html=True
                )

            for emotion, score in emotions.items():

                percentage = score * 100

                st.write(
                    f"**{emotion.capitalize()}** — "
                    f"{percentage:.1f}%"
                )

                st.progress(
                    min(max(float(score), 0.0), 1.0)
                )


            st.divider()


            # -----------------------------
            # AI Explanation
            # -----------------------------

            st.subheader("💡 AI Explanation")

            explanation = llm_result.get(
                "explanation",
                "No explanation available."
            )

            st.info(explanation)


            # -----------------------------
            # NLP Analysis
            # -----------------------------

            with st.expander("🔬 NLP Processing Details"):

                st.write(
                    "**Cleaned Text:**"
                )

                st.code(
                    nlp_result["cleaned_text"]
                )

                st.write(
                    "**Token Count:**"
                )

                st.write(
                    nlp_result["token_count"]
                )

                st.write(
                    "**Tokens:**"
                )

                st.write(
                    nlp_result["tokens"]
                )

                st.write(
                    "**Stopword-Filtered Tokens:**"
                )

                st.write(
                    nlp_result["filtered_tokens"]
                )

                st.write(
                    "**TF-IDF Keywords:**"
                )

                if nlp_result["keywords"]:

                    for keyword in nlp_result["keywords"]:

                        st.write(
                            f"• {keyword['word']} "
                            f"({keyword['score']:.3f})"
                        )

                else:

                    st.write(
                        "No significant keywords found."
                    )


st.divider()

st.caption(
    "EmotiSense • NLP + Google Gemini"
)