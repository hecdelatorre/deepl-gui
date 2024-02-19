import tkinter as tk

def create_text_fields(root):
    text_frame = tk.Frame(root)
    text_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

    input_label = tk.Label(text_frame, text="Input Text")
    input_label.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

    output_label = tk.Label(text_frame, text="Translated Text")
    output_label.grid(row=0, column=2, columnspan=2, sticky="nsew", padx=10, pady=10)

    input_box = tk.Text(text_frame, height=10, width=40, wrap="word")
    input_box.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

    output_box = tk.Text(text_frame, height=10, width=40, wrap="word", state="disabled")
    output_box.grid(row=1, column=2, columnspan=2, sticky="nsew", padx=10, pady=10)

    input_box.focus()

    return input_box, output_box
