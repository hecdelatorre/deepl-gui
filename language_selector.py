import tkinter as tk

def create_language_selector(root):
    lang_frame = tk.Frame(root)
    lang_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

    source_label = tk.Label(lang_frame, text="Source Language")
    source_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    source_var = tk.StringVar(root)
    source_var.set("ES")

    languages = [
        ("BG", "Bulgarian"),
        ("CS", "Czech"),
        ("DA", "Danish"),
        ("DE", "German"),
        ("EL", "Greek"),
        ("EN-US", "English"),
        ("EN-GB", "English"),
        ("ES", "Spanish"),
        ("ET", "Estonian"),
        ("FI", "Finnish"),
        ("FR", "French"),
        ("HU", "Hungarian"),
        ("IT", "Italian"),
        ("JA", "Japanese"),
        ("LT", "Lithuanian"),
        ("LV", "Latvian"),
        ("NL", "Dutch"),
        ("PL", "Polish"),
        ("PT", "Portuguese"),
        ("RO", "Romanian"),
        ("RU", "Russian"),
        ("SK", "Slovak"),
        ("SL", "Slovenian"),
        ("SV", "Swedish"),
        ("ZH", "Chinese")
    ]

    source_menu = tk.OptionMenu(lang_frame, source_var, *[code for code, name in languages])
    source_menu.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    target_label = tk.Label(lang_frame, text="Target Language")
    target_label.grid(row=0, column=3, sticky="nsew", padx=10, pady=10)

    target_var = tk.StringVar(root)
    target_var.set("EN-US")

    target_menu = tk.OptionMenu(lang_frame, target_var, *[code for code, name in languages])
    target_menu.grid(row=1, column=3, sticky="nsew", padx=10, pady=10)

    return source_var, target_var
