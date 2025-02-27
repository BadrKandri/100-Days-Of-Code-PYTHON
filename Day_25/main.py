from nutrients import nutrution_info
from exercise import burned_calories
from bmr import bmr_need
from gained_calories import gained_calories
import os
from dotenv import load_dotenv

load_dotenv()
#get yours from this website: https://developer.nutritionix.com/admin/access_details
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

print("\nhello,💪 This is your full gym guide made by Badr Kandri\n")
question=int(input("1-Get nutrition info\n2-Get calories burned from an exercise\n3-Get calories gained from food\n4-Calculate Basal Metabolic Rate (BMR)\n----->"))
data_mapping = {
    1: 'nutrients',
    2: 'exercise',
    3: 'nutrients'
}
mydata = data_mapping.get(question, 'error 404')
url = f'https://trackapi.nutritionix.com/v2/natural/{mydata}'
headers = {
    'x-app-id': APP_ID,
    'x-app-key' : API_KEY}


repeat = True
while(repeat):
    if question == 1:
        nutrution_info(url,headers)
    if question == 2:
        burned_calories(url,headers)
    if question == 3:    
        gained_calories(url,headers)
    if question == 4:
        bmr_need()
    yes_no = int(input("do you wanna try again?(0/1) --->"))
    if yes_no != 1:
        print("have a nice Day 💪")
        repeat = False
