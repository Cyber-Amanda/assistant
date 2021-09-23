import speech_recognition as voice
import playsound
from gtts import gTTS
import requests
import json
import os
import webbrowser

def bot_ngomong(voice_data):

    if "bagaimana kabarmu" in voice_data.lower():
        audio_string = "Hai Joe, semua sistem online."
    elif "hai" in voice_data.lower():
        audio_string = "Hai, apa yang bisa saya bantu?"
    elif 'bitcoin' in voice_data.lower():
        r = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=idr')
        a = json.loads(r.text)
        audio_string = "1 bitcoin sekarang harganya " + str(a["bitcoin"]["idr"] + " Rupiah.")
    elif 'buka youtube' in voice_data.lower():
        url = "https://www.youtube.com/"
        webbrowser.get().open(url)
        audio_string = "Membuka Youtube"
    elif 'cari youtube' in voice_data.lower(): 
        keyword = voice_data.split("mulai mencari")[-1]
        url = f"https://www.youtube.com/results?search_query={keyword}"
        webbrowser.get().open(url)
        audio_string = "Mencari di Youtube sebagai " + str(keyword)
    else:
        audio_string = "Sorry, aku gak ngeh"
    tts = gTTS(text=audio_string, lang="id")

    audio_file = 'audio.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    #os.remove(audio_file)

#bot_ngomong()

rec = voice.Recognizer()

def bot_listen():
    #print(voice.Microphone.list_microphone_names())
    with voice.Microphone(device_index=2) as source:
        audio = rec.listen(source)
        voice_data = ""
        try:
            voice_data = rec.recognize_google(audio)

        except:
            print(" Saya gak ngeh.. sorry")

    print(f"Kamu ngomong: {voice_data}")
    bot_ngomong(voice_data)
    

bot = bot_listen()