"""
This module is used to create text fields for a GUI application.
It uses the tkinter library for the GUI.
"""

import tkinter as tk

def create_text_fields(root, default_font, default_font_bold):
    """
    Create text fields for the GUI application.

    Parameters:
    root (tk.Tk): The root window of the application.
    default_font (tkinter.font.Font): The font to be used for the text fields.
    default_font_bold (tkinter.font.Font): The font to be used for the labels.

    Returns:
    tuple: Returns a tuple containing the input and output text fields.
    """

    text_frame = tk.Frame(root)
    text_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=5)

    input_label = tk.Label(text_frame, text="Input Text", font=default_font_bold)
    input_label.grid(row=0, column=0, columnspan=2, sticky="n", padx=10, pady=10)

    output_label = tk.Label(text_frame, text="Translated Text", font=default_font_bold)
    output_label.grid(row=0, column=2, columnspan=2, sticky="nsew", padx=10, pady=10)

    input_box = tk.Text(text_frame, height=15, width=55, wrap="word", font=default_font)
    input_box.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

    output_box = tk.Text(text_frame, height=15, width=55, wrap="word", state="disabled", font=default_font)
    output_box.grid(row=1, column=2, columnspan=2, sticky="nsew", padx=10, pady=10)

    input_box.focus()

    return input_box, output_box
