import speech_recognition as sr
from pydub import AudioSegment

class STT():
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def process_audio(self, file_path, converted_format='wav'):
        self.audio = AudioSegment.from_file(file_path)
        self.converted_path = file_path.replace(file_path.split(".")[-1], converted_format)
        self.converted_path = "".join(self.converted_path)
        self.audio.export(self.converted_path, format=converted_format)
        print(f"Conversão concluída. Arquivo salvo em: {self.converted_path}")
        return self.converted_path

    def speech_to_text(self, audio_path, language='en'):
        with sr.AudioFile(audio_path) as source:
            audio = self.recognizer.record(source)
            text = self.recognizer.recognize_google(audio, language=language)
            print(f"You said: {text}\n")
            return text

if __name__ == "__main__":
    stt = STT()
    #stt.speech_to_text()