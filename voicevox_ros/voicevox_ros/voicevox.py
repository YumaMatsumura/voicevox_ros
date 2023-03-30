import requests
import json
import pyaudio
import wave
import io
from time import sleep

class Voicevox:
    def __init__(self, speaker=0):
        self.speaker = speaker
        
    def post_audio_query(self, text):
        params = {'text': text, 'speaker': self.speaker}
        
        try:
            res = requests.post('http://localhost:50021/audio_query', params=params)
            return res.json()
            
        except Exception as e:
            raise
        
    def post_synthesis(self, audio_query_response):
        params = {'speaker': self.speaker}
        headers = {'content-type': 'application/json'}
        
        try:
            audio_query_response_json = json.dumps(audio_query_response)
            res = requests.post(
                'http://localhost:50021/synthesis',
                data=audio_query_response_json,
                params=params,
                headers=headers)
            return res.content
            
        except Exception as e:
            raise
        
    def play(self, voice_file):
        try:
            wave_read = wave.open(io.BytesIO(voice_file))
            p = pyaudio.PyAudio()
            stream = p.open(
                format=p.get_format_from_width(wave_read.getsampwidth()),
                channels=wave_read.getnchannels(),
                rate=wave_read.getframerate(),
                output=True)
            chunk = 1024
            data = wave_read.readframes(chunk)
            
            while data:
                stream.write(data)
                data = wave_read.readframes(chunk)
                
            sleep(0.5)
            stream.close()
            p.terminate()
            
        except Exception as e:
            raise
        
    def speak(self, text):
        try:
            res = self.post_audio_query(text)
            wav = self.post_synthesis(res)
            self.play(wav)
            
        except Exception as e:
            raise
