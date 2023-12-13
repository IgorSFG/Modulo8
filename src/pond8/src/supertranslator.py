from googletrans import Translator, LANGUAGES

class SuperTranslator:
    def __init__(self):
        self.translator = Translator()

    def translate(self, text, target_language='en'):
        self.translation = self.translator.translate(text, dest=target_language)
        return self.translation.text

    def get_languages(self):
        return LANGUAGES
    
if __name__ == "__main__":
    supertranslator = SuperTranslator()
    text = input("Enter text to translate: ")
    print(supertranslator.translate(text))