import speech_recognition as sr
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from Translator import Translator
import json

# Init variables

r = sr.Recognizer()
speech = sr.Microphone()
authenticator = IAMAuthenticator('_IyP3VGIvctsvN-xScYuiUQ_h-ebJAcLuFXwGwpETEG6')
speech_to_text = SpeechToTextV1(
    authenticator=authenticator

)
speech_to_text.set_service_url('https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/8f4ade4c-22b3-46fb-bc8d-ae55a03cf378')

translator = Translator()

def get_transcript(results_obj):
    # This is so f*ck* awful...
    return results_obj["results"][0]["alternatives"][0]["transcript"]

print("/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
print("APP INITIALIZED!")
print("PARA COMENZAR HABLA POR TU MICROFONO, DI HOLA")
flag = True

if __name__ == "__main__":
    while flag:
        with speech as source:
            
            audio_file = r.adjust_for_ambient_noise(source)
            audio_file = r.listen(source)
        
        speech_recognition_results = speech_to_text.recognize(audio=audio_file.get_wav_data(), content_type='audio/wav', model="es-ES_BroadbandModel").get_result()
        #print()
        if translator.output_result(get_transcript(speech_recognition_results)):
            flag = False

