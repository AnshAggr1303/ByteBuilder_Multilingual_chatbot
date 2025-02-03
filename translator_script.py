# Step 1: Install Required Libraries
# pip install langdetect
# pip install translate
# pip install rasa

from langdetect import detect
from translate import Translator

# Step 2: Language Detection Function
def detect_language(text):
    """Detect the language of the input text."""
    try:
        language = detect(text)
        return language
    except Exception as e:
        print(f"Error detecting language: {e}")
        return None

# Step 3: Translate Text to English (if not already in English)
def translate_to_english(text, source_language):
    """Translate text to English if not already in English."""
    if source_language != 'en':  # If the detected language is not English
        translator = Translator(to_lang='en', from_lang=source_language)
        translated_text = translator.translate(text)
        return translated_text
    return text

# Step 4: Translate Response Back to the User's Language (if necessary)
def translate_back_to_original(text, original_language):
    """Translate text back to the user's language."""
    if original_language != 'en':  # If the language is not English
        translator = Translator(to_lang=original_language, from_lang='en')
        translated_text = translator.translate(text)
        return translated_text
    return text

# Step 6: Process LLM Response and Translate Back to Original Language
def process_llm_response(response_in_english, detected_language):
    """Translate LLM response back to the user's language if it's not English."""
    # Call the translate_back_to_original function to translate the response back
    final_response = translate_back_to_original(response_in_english, detected_language)
    return final_response

# Example Usage:
user_input = "Hola, ¿cómo estás?"  # Example input from the user in Spanish

# Step 2: Detect language
detected_language = detect_language(user_input)
print(f"Detected Language: {detected_language}")

# Step 3: Translate the input to English (if needed)
translated_input = translate_to_english(user_input, detected_language)
print(f"Translated Input: {translated_input}")

# Assume we get a response from the LLM in English
llm_response_in_english = "I am doing well, thank you for asking!"

# Step 6: Process LLM response and translate it back to the original language (if needed)
final_response = process_llm_response(llm_response_in_english, detected_language)
print(f"Final Response: {final_response}")
