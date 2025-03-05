from dotenv import load_dotenv
import os

load_dotenv
mail=os.getenv("mail")
mdp=os.getenv("mdp")
phone_number=os.getenv("phone_number")

def get_per_info():
    return mail,mdp,phone_number
