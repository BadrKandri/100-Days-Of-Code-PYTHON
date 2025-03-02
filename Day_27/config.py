from dotenv import load_dotenv
import os

load_dotenv()

# Retrieve the environment variables for email details
Client_ID = os.getenv("Client_ID")
Client_secret = os.getenv("Client_secret")


def get_spotipy_info():
    return Client_ID, Client_secret
