from dotenv import load_dotenv
import os

load_dotenv()

mail = os.getenv("mail")
PASSWORD = os.getenv("PASSWORD")

def get_log_info():
    return mail, PASSWORD
