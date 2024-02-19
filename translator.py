from deepl import Translator

def translator(auth_key, source_var, target_var, text):
    if source_var == "EN-US" or source_var == "EN-GB": source_var = "EN"
    translator = Translator(auth_key)
    result = translator.translate_text(text, source_lang=source_var, target_lang=target_var)
    return result
