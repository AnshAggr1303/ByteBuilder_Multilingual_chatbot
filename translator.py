from langdetect import detect
from deep_translator import GoogleTranslator

def detect_language(text):
    try:
        return detect(text)
    except:
        return "en"

def translate_to_english(text):
    lang = detect_language(text)
    if lang != "en":
        return GoogleTranslator(source=lang, target='en').translate(text)
    return text

def translate_to_hindi(text, lang):
    if lang == "hi":
        return GoogleTranslator(source='en', target='hi').translate(text)
    return text
