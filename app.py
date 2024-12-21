from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_cors import CORS
import nltk
from nltk.corpus import wordnet
import re

# Download WordNet if not already installed
nltk.download('wordnet')
nltk.download('words')
from nltk.corpus import words

app = Flask(__name__)
CORS(app)  # Allow requests from the frontend (React app)

def normalize_feedback(feedback):
    """Normalize feedback by converting synonyms to basic sentiments."""
    sentiment_words = {
        "good": "positive",
        "great": "positive",
        "excellent": "positive",
        "bad": "negative",
        "poor": "negative",
        "terrible": "negative",
        "okay": "neutral",
        "fine": "neutral",
        "neutral": "neutral",
        "amazing": "positive",
        "horrible": "negative",
        "awful": "negative",
        "satisfactory": "neutral"
    }

    words = feedback.lower().split()
    normalized_feedback = []

    for word in words:
        # Use WordNet to get synonyms of the word
        synsets = wordnet.synsets(word)
        # Check if any synonym of the word matches sentiment-related terms
        for synset in synsets:
            for lemma in synset.lemmas():
                if lemma.name().lower() in sentiment_words:
                    normalized_feedback.append(sentiment_words[lemma.name().lower()])
                    break
            else:
                continue
            break
        else:
            # If no synonym found, keep the original word
            normalized_feedback.append(word)

    return " ".join(normalized_feedback)

def is_valid_feedback(feedback):
    """Check if feedback contains meaningful content for sentiment analysis."""
    # Reject single names, empty strings, or feedback too short (less than 2 meaningful words)
    if not feedback.strip():
        return False

    # Check if feedback contains only a name (capitalized single word or short phrases)
    if re.match(r'^[A-Z][a-z]+$', feedback.strip()):
        return False  # Invalid feedback (a single name)

    # Check if feedback contains too few recognizable words (this will reject gibberish)
    words_in_feedback = feedback.split()
    valid_words = set(words.words())  # List of valid English words from nltk
    recognizable_words = [word for word in words_in_feedback if word.lower() in valid_words]
    
    # If there are very few recognizable words (less than 2 valid words), treat it as gibberish
    if len(recognizable_words) < 2:
        return False

    return True

@app.route('/analyze-feedback', methods=['POST'])
def analyze_feedback():
    data = request.json
    feedback = data.get("feedback", "")

    if not feedback:
        return jsonify({"error": "Feedback is required"}), 400

    # If feedback is invalid (only contains names, gibberish, or too few recognizable words)
    if not is_valid_feedback(feedback):
        return jsonify({"error": "The feedback provided is invalid or not meaningful for sentiment analysis."}), 400

    # Normalize feedback by replacing synonyms with standardized sentiment words
    normalized_feedback = normalize_feedback(feedback)

    # Analyze sentiment using TextBlob
    blob = TextBlob(normalized_feedback)
    sentiment = "Positive" if blob.sentiment.polarity > 0.1 else \
            "Negative" if blob.sentiment.polarity < -0.1 else \
            "Neutral"
    
    # Return the analyzed result in JSON format
    return jsonify({"feedback": feedback, "normalized_feedback": normalized_feedback, "sentiment": sentiment})

if __name__ == '__main__':
    app.run(debug=True)
