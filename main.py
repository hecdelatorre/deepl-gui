# Import tkinter and pyperclip modules
import tkinter as tk
import pyperclip

# Create a root window
root = tk.Tk()
# Set the window title
root.title("GUI Translator")
# Set the window size
root.geometry("800x520")

# Create 4 columns for the window
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

# Create a frame for the header
header_frame = tk.Frame(root)
# Place the frame on the window using a grid layout
header_frame.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create a label for the language selector
lang_label = tk.Label(header_frame, text="Language Selector")
# Place the label on the frame using a grid layout
lang_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create a frame for the language selectors
lang_frame = tk.Frame(root)
# Place the frame on the window using a grid layout
lang_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Create a label for the source language
source_label = tk.Label(lang_frame, text="Source Language")
# Place the label on the frame using a grid layout
source_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Create a string variable for the source language
source_var = tk.StringVar(root)
# Set the default value to "es" for Spanish
source_var.set("ES")

# Create a list of language codes and names
languages = [
    ("BG", "Bulgarian"),
    ("CS", "Czech"),
    ("DA", "Danish"),
    ("DE", "German"),
    ("EL", "Greek"),
    ("EN", "English"),
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

# Create an option menu for the source language
source_menu = tk.OptionMenu(lang_frame, source_var, *[code for code, name in languages])
# Place the option menu on the frame using a grid layout
source_menu.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

# Create a label for the target language
target_label = tk.Label(lang_frame, text="Target Language")
# Place the label on the frame using a grid layout
target_label.grid(row=0, column=3, sticky="nsew", padx=10, pady=10)

# Create a string variable for the target language
target_var = tk.StringVar(root)
# Set the default value to "en" for English
target_var.set("EN")

# Create an option menu for the target language
target_menu = tk.OptionMenu(lang_frame, target_var, *[code for code, name in languages])
# Place the option menu on the frame using a grid layout
target_menu.grid(row=1, column=3, sticky="nsew", padx=10, pady=10)

# Define a function to swap the language values
def swap_languages():
    # Get the current values of the source and target languages
    source_lang = source_var.get()
    target_lang = target_var.get()
    # Set the source language to the previous target language
    source_var.set(target_lang)
    # Set the target language to the previous source language
    target_var.set(source_lang)

# Create a frame for the text fields
text_frame = tk.Frame(root)
# Place the frame on the window using a grid layout
text_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

# Create a label for the input text
input_label = tk.Label(text_frame, text="Input Text")
# Place the label on the frame using a grid layout
input_label.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

# Create a label for the translated text
output_label = tk.Label(text_frame, text="Translated Text")
# Place the label on the frame using a grid layout
output_label.grid(row=0, column=2, columnspan=2, sticky="nsew", padx=10, pady=10)

# Create a text box for the input text
input_box = tk.Text(text_frame, height=10, width=40, wrap="word")
# Place the text box on the frame using a grid layout
input_box.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

# Create a text box for the translated text
output_box = tk.Text(text_frame, height=10, width=40, wrap="word", state="disabled")
# Place the text box on the frame using a grid layout
output_box.grid(row=1, column=2, columnspan=2, sticky="nsew", padx=10, pady=10)

# Define a function to copy the translated text to the clipboard
def copy_to_clipboard():
    # Get the translated text from the output text box
    output_text = output_box.get("1.0", "end-1c")
    # Check if the output text is empty
    if not output_text:
        # Show an error message
        tk.messagebox.showerror("Error", "There is no text to copy.")
        return
    # Copy the output text to the clipboard using pyperclip
    pyperclip.copy(output_text)

# Define a function to clear the text fields
def clear_text():
    # Clear the input text box
    input_box.delete("1.0", "end")
    # Clear the output text box
    output_box.config(state="normal")
    output_box.delete("1.0", "end")
    output_box.config(state="disabled")

# Create a frame for the buttons
button_frame = tk.Frame(root)
# Place the frame on the window using a grid layout
button_frame.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

# Create a button for the translation
translate_button = tk.Button(button_frame, text="Translate")
# Place the button on the frame using a grid layout
translate_button.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Create a button for the swap function
swap_button = tk.Button(button_frame, text="<--->", command=swap_languages)
# Place the button on the frame using a grid layout
swap_button.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

# Create a button for the clipboard
clipboard_button = tk.Button(button_frame, text="Copy to clipboard", command=copy_to_clipboard)
# Place the button on the frame using a grid layout
clipboard_button.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

# Create a button for the clear function
clear_button = tk.Button(button_frame, text="Clear", command=clear_text)
# Place the button on the frame using a grid layout
clear_button.grid(row=0, column=3, sticky="nsew", padx=10, pady=10)

# Start the main loop of the window
root.mainloop()