from transformers import pipeline

# sentiment analysis pipeline load hanne
sentiment_pipeline = pipeline("sentiment-analysis")

# User bata input line
while True:
    text = input("Enter a sentence for sentiment analysis (or type 'exit' to quit): ")
    if text.lower() == "exit":
        break
    result = sentiment_pipeline(text)
    print(f"Sentiment: {result[0]['label']} | Confidence: {result[0]['score']:.2f}")
