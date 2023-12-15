from gtts import gTTS
from pygame import mixer

class TTS():
    def __init__(self):
        self.tts = None
        self.audio_file = None
    
    def text_to_speech(self, text, language='pt-br', file="speech.mp3"):
        tts = gTTS(text, lang=language)
        audio_file = file
        tts.save(audio_file)
        return audio_file
    
    def play_audio(self, audio_file="speech.mp3"):
        mixer.init()
        mixer.music.load(audio_file)
        mixer.music.play()
        while mixer.music.get_busy():
            continue
        mixer.quit()

def main():
    tts = TTS()
    question = ""
    
    print("\nTTS Ligou!\n")
    print('Faça o "L" para sair!\n')
    
    while True:
        question = input("BOT: Escreva algo para eu falar: ")
        
        if question.lower() == "l":
            tts.text_to_speech("Fazendo o L.")
            tts.play_audio()
            return
        
        tts.text_to_speech(question)
        tts.play_audio()

if __name__ == "__main__":
    main()
