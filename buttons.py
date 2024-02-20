"""
This module is used to create buttons for a GUI application.
It uses the tkinter library for the GUI.
"""

import tkinter as tk

def create_buttons(root, default_font_bold, swap_languages, paste_from_clipboard, copy_to_clipboard, clear_text, translate_text):
    """
    Create buttons for the GUI application.

    Parameters:
    root (tk.Tk): The root window of the application.
    default_font_bold (tkinter.font.Font): The font to be used for the buttons.
    swap_languages (function): Function to swap source and target languages.
    paste_from_clipboard (function): Function to paste text from clipboard into the input text box.
    copy_to_clipboard (function): Function to copy translated text to the clipboard.
    clear_text (function): Function to clear the input and output text boxes.
    translate_text (function): Function to translate the text in the input box and display it in the output box.
    """

    button_frame = tk.Frame(root)
    button_frame.grid(row=3, column=0, sticky='n', columnspan=4, padx=5, pady=5)

    translate_button = tk.Button(button_frame, text="Translate", font=default_font_bold, bg='#009841', fg='white', command=translate_text)
    translate_button.grid(row=0, column=0, sticky="nsew", padx=5, pady=10)

    paste_button = tk.Button(button_frame, text="Paste from clipboard", font=default_font_bold, bg='#005B98', fg='white', command=paste_from_clipboard)
    paste_button.grid(row=0, column=1, sticky="nsew", padx=5, pady=10)
    
    swap_button = tk.Button(button_frame, text="< >", font=default_font_bold, bg='#009883', fg='white', command=swap_languages)
    swap_button.grid(row=0, column=2, sticky="nsew", padx=5, pady=10)

    clipboard_button = tk.Button(button_frame, text="Copy to clipboard", font=default_font_bold, bg='#005B98', fg='white', command=copy_to_clipboard)
    clipboard_button.grid(row=0, column=3, sticky="nsew", padx=5, pady=10)

    clear_button = tk.Button(button_frame, text="Clear", font=default_font_bold, bg='#980009', fg='white', command=clear_text)
    clear_button.grid(row=0, column=4, sticky="nsew", padx=5, pady=10)
