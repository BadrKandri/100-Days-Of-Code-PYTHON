import requests

def gained_calories(url,headers):

    total_calories=0
    again = True
    while again:
        text=input("What did you eat? ---> ")
        body = {"query": text}
        response = requests.post(url, json=body, headers=headers)    
        if response.status_code == 200:
            data = response.json()       
            food = data['foods'][0]
            calories = food.get('nf_calories', 0)
            total_calories+=calories     
            print(f"you gained {total_calories} calories today")
            y_n=int(input("do you wanna add more?(0/1) --->"))
            if y_n != 1:
                again = False
        else:
            print(f"Erreur: {response.status_code}")
