from dotenv import load_dotenv
import os

load_dotenv()
# variables:
my_mail=os.getenv('my_mail')
password=os.getenv('password')
receiver=os.getenv('receiver')

def get_mail_info():
    return my_mail,password,receiver
