from gtts import gTTS
from pygame import mixer

class TTS():
    def __init__(self):
        self.tts = None
        self.audio_file = None
    
    def text_to_speech(self, text, language='pt-br', file="sample/speech.mp3"):
        tts = gTTS(text, lang=language)
        audio_file = file
        tts.save(audio_file)
        return audio_file
    
    def play_audio(self, audio_file):
        mixer.init()
        mixer.music.load(audio_file)
        mixer.music.play()
        while mixer.music.get_busy():
            continue
        mixer.quit()
        
        