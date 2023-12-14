from googletrans import Translator, LANGUAGES

class SuperTranslator:
    def __init__(self):
        self.translator = Translator()

    def translate(self, text, target_language='pt'):
        self.translation = self.translator.translate(text, dest=target_language)
        self.text = self.translation.text
        print(f"Translated text: {self.text}\n")
        return self.text    

    def get_languages(self):
        return LANGUAGES
    
if __name__ == "__main__":
    supertranslator = SuperTranslator()
    print(supertranslator.get_languages())
    text = input("Enter text to translate: ")
    print(supertranslator.translate(text))