import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url=url, json=myobj, headers=header)  # Send a POST request to the API with the text and headers
    json_response = json.loads(response.text)

    try:
        anger_score = json_response["emotionPredictions"][0]["emotion"]["anger"]
        disgust_score = json_response["emotionPredictions"][0]["emotion"]["disgust"]
        fear_score = json_response["emotionPredictions"][0]["emotion"]["fear"]
        joy_score = json_response["emotionPredictions"][0]["emotion"]["joy"]
        sadness_score = json_response["emotionPredictions"][0]["emotion"]["sadness"]
        scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
            }
        # Determine the dominant emotion
        dominant_emotion = max(scores, key=scores.get)
    
        # Add the dominant emotion to the dictionary
        scores['dominant_emotion'] = dominant_emotion
    except:
        scores = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
            }
    
    return scores
