import requests

def burned_calories(url,headers):
    gender = input("enter your gender(male/female): ")
    weight_kg = int(input("enter your weight in KG: "))
    height_cm = int(input("enter your height in CM: "))
    age = int(input("enter your age: "))
    text=input('What did you do today? ')
    
    body = {
        "query": text,
        "gender": gender,
        "weight_kg": weight_kg,
        "height_cm": height_cm,
        "age": age}
    response = requests.post(url, json=body, headers=headers)
    if response.status_code == 200:
        result = response.json()['exercises'][0]['nf_calories']
        print(f'you burned {result} Calories')
    else:
        print("Can you explain more so I can give you exact answers?")
