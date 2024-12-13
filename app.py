import streamlit as st
from textblob import TextBlob

# Function to analyze sentiment
def get_sentiment_score(text):
    # Create a TextBlob object
    blob = TextBlob(text)

    # Get sentiment polarity
    sentiment_score = blob.sentiment.polarity

    # Determine sentiment category
    if sentiment_score > 0:
        sentiment = "Positive"
    elif sentiment_score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment_score, sentiment

# Streamlit app layout
def main():
    st.title("Sentiment Analysis App")
    st.write("Enter a piece of text below to analyze its sentiment.")

    # Text input from user
    user_input = st.text_area("Enter your text here", "")

    # Button to perform sentiment analysis
    if st.button("Analyze Sentiment"):
        if user_input:
            sentiment_score, sentiment = get_sentiment_score(user_input)
            st.write(f"**Sentiment Score:** {sentiment_score}")
            st.write(f"**Sentiment:** {sentiment}")
        else:
            st.warning("Please enter some text to analyze.")

# Run the app
if __name__ == "__main__":
    main()