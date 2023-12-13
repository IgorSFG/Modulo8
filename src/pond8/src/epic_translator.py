from stt import STT
from supertranslator import SuperTranslator
from tts import TTS
import sys
import os

class EpicTranslator:
    def __init__(self):
        print("\nInitializing EpicTranslator...\n")
        self.audio_path = sys.argv[1]
        self.stt = STT()
        self.super_translator = SuperTranslator()
        self.tts = TTS()
        
        if len(sys.argv) != 2:
            print("Usage: python epic_translator.py <audio_path>")
            sys.exit(1)

        if not os.path.exists(self.audio_path):
            print("Audio path does not exist.")
            sys.exit(1)

        if not self.audio_path.endswith(".wav"):
            print("Converting audio to a compatible format...")
            self.audio_path = self.stt.process_audio(self.audio_path)

    def start(self):
        text = self.stt.speech_to_text(self.audio_path)
        text = self.super_translator.translate(text)
        audio = self.tts.text_to_speech(text)
        self.tts.play_audio(audio)

def main():
    epic_translator = EpicTranslator()
    epic_translator.start()

if __name__ == "__main__":
    main()