"""
Flask app for emotion detection.

This module sets up a Flask web application that analyzes text for emotions.
It provides routes for submitting text and rendering the main page.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask(__name__)

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Receives the text from the HTML interface and runs sentiment analysis
    over it using the emotion_detector function. The output shows the label
    and its confidence score for the provided text.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "No text provided! Please enter some text."

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    anger_score = response.get("anger", 0)
    disgust_score = response.get("disgust", 0)
    fear_score = response.get("fear", 0)
    joy_score = response.get("joy", 0)
    sadness_score = response.get("sadness", 0)
    dominant_emotion = response.get("dominant_emotion", "unknown")

    formatted_text = (
        f"For the given statement, the system response is: "
        f"'anger': {anger_score:.9f}, 'disgust': {disgust_score:.10f}, "
        f"'fear': {fear_score:.9f}, 'joy': {joy_score:.7f}, "
        f"'sadness': {sadness_score:.9f}. The dominant emotion is {dominant_emotion}."
    )

    # Return a formatted string with the sentiment label and score
    return formatted_text

@app.route("/")
def render_index_page():
    """
    Renders the main application page over the Flask channel.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
