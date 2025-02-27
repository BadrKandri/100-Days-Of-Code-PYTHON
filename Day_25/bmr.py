def bmr_need():
    gender = input("enter your gender(male/female): ")
    weight_kg = int(input("enter your weight in KG: "))
    height_cm = int(input("enter your height in CM: "))
    age = int(input("enter your age: "))
    
    if gender == 'male':
        bmr = int(88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age))
    else:
        bmr = int(447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age))
        
    print(f"your body needs {bmr} calories just to stay alive")
