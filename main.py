"""
This module is used to create a GUI application for text translation.
It uses the tkinter library for the GUI and the DeepL API for translation.
"""

import tkinter as tk
from tkinter import font
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
import pyperclip
from language_selector import create_language_selector
from text_fields import create_text_fields
from buttons import create_buttons
from translator import translator
from config import get_auth_key

# Get the authentication key
AUTH_KEY = get_auth_key()  # replace with your actual auth key

ROOT = tk.Tk()
ROOT.title("GUI Translator - Deepl")

SCREEN_WIDTH = ROOT.winfo_screenwidth()
SCREEN_HEIGHT = ROOT.winfo_screenheight()
WINDOW_WIDTH = 1065
WINDOW_HEIGHT = 650

X = (SCREEN_WIDTH - WINDOW_WIDTH) // 2
Y = (SCREEN_HEIGHT - WINDOW_HEIGHT) // 2

ROOT.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{X}+{Y}')
ROOT.resizable(False, False)

# Get a list of all available font families
AVAILABLE_FONTS = font.families()

# Check if 'Open Sans' and 'Open Sans Semibold' are available, otherwise fall back to 'Arial'
DEFAULT_FONT_FAMILY = "Open Sans" if "Open Sans" in AVAILABLE_FONTS else "Arial"
DEFAULT_FONT_BOLD_FAMILY = "Open Sans" if "Open Sans" in AVAILABLE_FONTS else "Arial"

# Set the default fonts
default_font = font.Font(family=DEFAULT_FONT_FAMILY, size=12)
default_font_bold = font.Font(family=DEFAULT_FONT_BOLD_FAMILY, size=12, weight='bold')

frame_logo = tk.Frame(ROOT, padx=10, pady=15)
frame_logo.grid(row=0, column=0, columnspan=4, sticky='n')

logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(frame_logo, image=logo)
logo_label.grid(row=0, column=0)

source_var, target_var = create_language_selector(ROOT, default_font_bold)
input_box, output_box = create_text_fields(ROOT, default_font, default_font_bold)

def swap_languages():
    """
    Swap the source and target languages.
    """
    # Get the current values of the source and target languages
    source_lang = source_var.get()
    target_lang = target_var.get()
    # Set the source language to the previous target language
    source_var.set(target_lang)
    # Set the target language to the previous source language
    target_var.set(source_lang)

def clear_text():
    """
    Clear the input and output text boxes.
    """
    # Clear the input text box
    input_box.delete("1.0", "end")
    input_box.focus()
    # Clear the output text box
    output_box.config(state="normal")
    output_box.delete("1.0", "end")
    output_box.config(state="disabled")

def copy_to_clipboard():
    """
    Copy the translated text to the clipboard.
    """
    # Get the translated text from the output text box
    output_text = output_box.get("1.0", "end-1c")
    # Check if the output text is not empty
    if len(output_text.strip()) > 0:  # check if output text is not empty
        # Copy the output text to the clipboard using pyperclip
        pyperclip.copy(output_text)

def paste_from_clipboard():
    """
    Paste text from the clipboard into the input text box.
    """
    # Clear the input text box
    clear_text()
    # Get the clipboard content
    clipboard_content = pyperclip.paste()
    # Paste the clipboard content into the input text box
    input_box.insert("end", clipboard_content)

def translate_text():
    """
    Translate the text in the input box and display it in the output box.
    """
    if source_var.get() != target_var.get():
        input_text = input_box.get("1.0", "end-1c")
        if input_text.strip():  # check if input text is not empty
            translated_text = translator(AUTH_KEY, source_var.get(), target_var.get(), input_text)
            output_box.config(state="normal")
            output_box.delete("1.0", "end")
            output_box.insert("end", str(translated_text))
            output_box.config(state="disabled")
    else:
        showinfo('Attention', 'You must select different languages')

create_buttons(ROOT, default_font_bold, swap_languages, paste_from_clipboard, copy_to_clipboard, clear_text, translate_text)

ROOT.mainloop()
