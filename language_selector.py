import tkinter as tk
from tkinter import ttk

def create_language_selector(root, default_font_bold):
    lang_frame = tk.Frame(root)
    lang_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=5)

    source_var = tk.StringVar(lang_frame)
    source_var.set("ES")

    languages = [
        "BG", "CS", "DA", "DE", "EL", "EN-US", "EN-GB", "ES", "ET", "FI", "FR", "HU", "IT", "JA", "KO", "LT", "LV", "NL", "PL", "PT-PT", "PT-BR", "RO", "RU", "SK", "SL", "SV", "TR", "UK", "ZH"
    ]

    source_menu = ttk.Combobox(lang_frame, state="readonly", width=6, textvariable=source_var, values=languages, font=default_font_bold)
    source_menu.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    target_var = tk.StringVar(lang_frame)
    target_var.set("EN-US")

    target_menu = ttk.Combobox(lang_frame, state="readonly", width=6, textvariable=target_var, values=languages, font=default_font_bold)
    target_menu.grid(row=0, column=3, sticky="nsew", padx=10, pady=10)

    return source_var, target_var
