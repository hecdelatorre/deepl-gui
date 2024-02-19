import tkinter as tk

def create_buttons(root, swap_languages, paste_from_clipboard, copy_to_clipboard, clear_text, translate_text):
    button_frame = tk.Frame(root)
    button_frame.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

    translate_button = tk.Button(button_frame, text="Translate", command=translate_text)
    translate_button.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    paste_button = tk.Button(button_frame, text="Paste from clipboard", command=paste_from_clipboard)
    paste_button.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
    
    swap_button = tk.Button(button_frame, text="<--->", command=swap_languages)
    swap_button.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

    clipboard_button = tk.Button(button_frame, text="Copy to clipboard", command=copy_to_clipboard)
    clipboard_button.grid(row=0, column=3, sticky="nsew", padx=10, pady=10)

    clear_button = tk.Button(button_frame, text="Clear", command=clear_text)
    clear_button.grid(row=0, column=4, sticky="nsew", padx=10, pady=10)
