
import argparse
import base64
import json
import time

from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials



# [START authenticating]

# Application default credentials provided by env variable
# GOOGLE_APPLICATION_CREDENTIALS
def get_speech_service():
    credentials = GoogleCredentials.get_application_default().create_scoped(
        ['https://www.googleapis.com/auth/cloud-platform'])
    http = httplib2.Http()
    credentials.authorize(http)

    return discovery.build('speech', 'v1beta1', http=http)
# [END authenticating]



import speech_recognition as sr

from os import path


GOOGLE_SPEECH_RECOGNITION_API_KEY = 'AIzaSyCoi7xnuy-k7nrvnTLc2R_BFJ2wcC9HHFc'


def main():

    AUDIO_FILE = "/home/pete/projects/doughboys-hashtag/downloads/test/f7923c45-7527-4e86-976c-7bfd4ad761a6.wav"

    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source) # read the entire audio file

    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))    

    google_results =  
    print google_results

if __name__ == '__main__':
    main()