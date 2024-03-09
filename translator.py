from deepl import Translator, DeepLException

def translator(auth_key, source_var, target_var, text):
    """
    Translate text using the DeepL API.

    Parameters:
    auth_key (str): The authentication key for the DeepL API.
    source_var (str): The source language for translation.
    target_var (str): The target language for translation.
    text (str): The text to be translated.

    Returns:
    str: Returns the translated text or an error message.
    """

    try:
        if source_var == "EN-US" or source_var == "EN-GB": 
            source_var = "EN" 
        elif source_var == "PT-PT" or source_var == "PT-BR":
            source_var = "PT"

        translator = Translator(auth_key)
        result = translator.translate_text(text, source_lang=source_var, target_lang=target_var)
        return result
    except DeepLException as e:
        return f"An error occurred during translation: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
