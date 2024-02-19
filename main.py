import tkinter as tk
from tkinter.messagebox import showerror
import pyperclip
from language_selector import create_language_selector
from text_fields import create_text_fields
from buttons import create_buttons
from translator import translator
from config import get_auth_key


root = tk.Tk()
root.title("GUI Translator")
root.geometry("715x470")

auth_key = get_auth_key() # replace with your actual auth key

source_var, target_var = create_language_selector(root)
input_box, output_box = create_text_fields(root)

def swap_languages():
    # Get the current values of the source and target languages
    source_lang = source_var.get()
    target_lang = target_var.get()
    # Set the source language to the previous target language
    source_var.set(target_lang)
    # Set the target language to the previous source language
    target_var.set(source_lang)

def clear_text():
    # Clear the input text box
    input_box.delete("1.0", "end")
    input_box.focus()
    # Clear the output text box
    output_box.config(state="normal")
    output_box.delete("1.0", "end")
    output_box.config(state="disabled")

def copy_to_clipboard():
    # Get the translated text from the output text box
    output_text = output_box.get("1.0", "end-1c")
    # Check if the output text is not empty
    if len(output_text.strip()) > 0:  # check if output text is not empty
        # Copy the output text to the clipboard using pyperclip
        pyperclip.copy(output_text)

def paste_from_clipboard():
    # Clear the input text box
    clear_text()
    # Get the clipboard content
    clipboard_content = pyperclip.paste()
    # Paste the clipboard content into the input text box
    input_box.insert("end", clipboard_content)

def translate_text():
    input_text = input_box.get("1.0", "end-1c")
    if input_text.strip():  # check if input text is not empty
        translated_text = translator(auth_key, source_var.get(), target_var.get(), input_text)
        output_box.config(state="normal")
        output_box.delete("1.0", "end")
        output_box.insert("end", translated_text)
        output_box.config(state="disabled")

create_buttons(root, swap_languages, paste_from_clipboard, copy_to_clipboard, clear_text, translate_text)

root.mainloop()
