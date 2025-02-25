import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from datetime import datetime


r = sr.Recognizer()


def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            vicky_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            vicky_speak('Sorry,  I did not get that !')
        except sr.RequestError:
            vicky_speak('Sorry, my speech service is down')
        return voice_data

def vicky_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en', tld='us')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    print(voice_data)
    if 'what is your name' in voice_data:
        vicky_speak('My name is Vicky')
    if 'what time is it' in voice_data:
        vicky_speak(datetime.now().time().strftime("%H:%M:%S"))
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        return webbrowser.open('https://www.google.com/search?q=' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        return webbrowser.open('https://www.google.nl/maps/place/' + location + '/&amp;')
    if 'Vicky stop' in  voice_data:
        vicky_speak('Bye bye , Andriyan!')
        exit()




time.sleep(1)
vicky_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)


# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
