from langdetect import detect
from deep_translator import GoogleTranslator

def detect_language(text):
    """Detects the language of the input text."""
    try:
        return detect(text)
    except Exception as e:
        print(f"Error detecting language: {e}")
        return "en"  # Default to English

def translate_to_english(text):
    """Translates text to English if it's in Hindi."""
    lang = detect_language(text)
    if lang == "hi":
        return GoogleTranslator(source='hi', target='en').translate(text)
    return text  # If already in English, return as-is

def translate_to_hindi(text, original_lang):
    """Translates text back to Hindi if the original input was in Hindi."""
    if original_lang == "hi":
        return GoogleTranslator(source='en', target='hi').translate(text)
    return text  # If already in English, return as-is

if __name__ == "__main__":
    hindi_input = "नमस्ते, आप कैसे हैं?"  # "Hello, how are you?"
    
    # Detect language
    detected_lang = detect_language(hindi_input)
    print(f"Detected Language: {detected_lang}")  # Should print "hi"
    
    # Translate to English
    english_translation = translate_to_english(hindi_input)
    print(f"Translated to English: {english_translation}")  # Should print "Hello, how are you?"
    
    # Translate back to Hindi
    translated_back_to_hindi = translate_to_hindi(english_translation, detected_lang)
    print(f"Translated back to Hindi: {translated_back_to_hindi}")  # Should print the original Hindi text
