'''Import necessary packages and this file defines the function
emotion detector using various parameters'''
#import HTTP request
import requests
#import json to run the app smoothly
import json

#function definition for emotion_detector
def emotion_detector(text_to_analyze):

# Define the URL for the emotion analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

# Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

# Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

# Send a POST request to the API with the text and headers return response.text 
    response = requests.post(url, json = myobj, headers=header)

# Parsing the JSON response from the API 
    formatted_response = json.loads(response.text)

# Extracting emotion scores from the nested response dictionary
    emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotion_predictions['anger']
    disgust_score = emotion_predictions['disgust']
    fear_score = emotion_predictions['fear']
    joy_score = emotion_predictions['joy']
    sadness_score = emotion_predictions['sadness']

# Finding the highest scoring emotion name
    dominant_emotion = max(emotion_predictions, key=emotion_predictions.get)


# Returning a dictionary containing final emotion analysis results
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }



