import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="Sentiment Analyzer", layout="centered")

st.title("🧠 Simple Sentiment Analyzer")
st.write("Enter a sentence and find out if it's Positive, Negative, or Neutral.")

text = st.text_area("✍️ Enter text here")

if st.button("Analyze"):
    if text:
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity

        if sentiment > 0:
            st.success("😊 Positive Sentiment")
        elif sentiment < 0:
            st.error("😠 Negative Sentiment")
        else:
            st.info("😐 Neutral Sentiment")
    else:
        st.warning("Please enter some text to analyze.")
