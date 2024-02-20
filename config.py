"""
This module is used to manage the authentication key for the DeepL API.
It uses the python-dotenv library to load the key from a .env file and tkinter to prompt the user to enter the key.
"""

import os
from dotenv import load_dotenv, set_key
import tkinter as tk
from tkinter.messagebox import showinfo, showwarning

# Define the name and path of the .env file
ENV_FILE = ".deepl.env"
ENV_PATH = os.path.join(os.path.expanduser("~"), ENV_FILE)

def prompt_auth_key():
    """
    Prompt the user for the AUTH_KEY using a Tkinter GUI.
    """
    def save_auth_key():
        """
        Save the entered authentication key to the .env file.
        """
        # Get the entered authentication key
        auth_key = entry.get()
        if len(auth_key) == 39:
            # Save the AUTH_KEY value to the .env file
            set_key(ENV_PATH, "AUTH_KEY", auth_key)
            showinfo('Information', 'Your key seems correct, restart the program.')
            # Close the Tkinter window
            root.destroy()
            exit(0)
        else:
            showwarning('Attention', 'auth_key must be 39 characters')

    # Create a Tkinter window
    root = tk.Tk()
    root.title("Enter AUTH_KEY")

    # Create a label and entry widget for the user to input the AUTH_KEY
    tk.Label(root, text="Please enter the AUTH_KEY value:").pack()
    entry = tk.Entry(root, width=30)
    entry.pack()

    # Create a button to save the AUTH_KEY
    tk.Button(root, text="Save", command=save_auth_key).pack()

    # Run the Tkinter event loop
    root.mainloop()

def get_auth_key():
    """
    Get the AUTH_KEY from the .env file or prompt the user to enter it.
    """
    # Check if the .env file exists in the user's home directory
    if os.path.isfile(ENV_PATH):
        # Load the environment variables from the .env file
        load_dotenv(ENV_PATH)
        # Get the value of the AUTH_KEY variable
        auth_key = os.getenv("AUTH_KEY")
        # Check if the AUTH_KEY variable is empty
        if not auth_key:
            # Prompt the user to enter the AUTH_KEY value using Tkinter
            prompt_auth_key()
        else:
            return auth_key
    else:
        # Create an empty .env file in the user's home directory
        open(ENV_PATH, "w").close()
        # Prompt the user to enter the AUTH_KEY value using Tkinter
        prompt_auth_key()
