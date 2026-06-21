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
    status_code = response.status_code

    emotions = {}

    if status_code == 200:
        formatted_response = json.loads(response.text)
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions.items(), key=lambda x: x[1])
        emotions['dominant_emotion'] = dominant_emotion[0]
    elif status_code == 400:
        emotions['anger'] = None
        emotions['disgust'] = None
        emotions['fear'] = None
        emotions['joy'] = None
        emotions['sadness'] = None
        emotions['dominant_emotion'] = None
    return emotions