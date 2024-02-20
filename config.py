# config.py

# Import the modules
import os
from dotenv import load_dotenv, set_key

# Define the name and path of the .env file
env_file = ".deepl.env"
env_path = os.path.join(os.path.expanduser("~"), env_file)

# Check if the .env file exists in the user's home directory
if os.path.isfile(env_path):
    # Load the environment variables from the .env file
    load_dotenv(env_path)
    # Get the value of the AUTH_KEY variable
    auth_key = os.getenv("AUTH_KEY")
    # Check if the AUTH_KEY variable is empty
    if not auth_key:
        # Ask the user to enter the AUTH_KEY value
        auth_key = input("Please enter the AUTH_KEY value: ")
        # Save the AUTH_KEY value to the .env file
        set_key(env_path, "AUTH_KEY", auth_key)
else:
    # Create an empty .env file in the user's home directory
    open(env_path, "w").close()
    # Ask the user to enter the AUTH_KEY value
    auth_key = input("Please enter the AUTH_KEY value: ")
    # Save the AUTH_KEY value to the .env file
    set_key(env_path, "AUTH_KEY", auth_key)

# Define a function that returns the auth_key value
def get_auth_key():
    return auth_key

