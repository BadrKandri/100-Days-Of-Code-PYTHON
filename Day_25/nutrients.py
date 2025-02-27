from googletrans import Translator
import asyncio
import requests

def nutrution_info(url,headers):
    # Traduction du nom de l'aliment en anglais
    translator = Translator()
    async def translate_food_item(food_item):
        translated = await translator.translate(food_item, src='fr', dest='en')
        return translated.text       
    text = input("Enter a food item (e.g., '1 orange'): ")
    # Traduction du nom de l'aliment en anglais
    translated_food_item = asyncio.run(translate_food_item(text))
    data = {"query": translated_food_item}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        result = response.json()
        food_info = result["foods"][0]
        name = food_info["food_name"].capitalize()
        calories = food_info["nf_calories"]
        protein = food_info["nf_protein"]
        carbs = food_info["nf_total_carbohydrate"]
        fat = food_info["nf_total_fat"]
        fiber = food_info.get("nf_dietary_fiber", "N/A")  # Certains aliments n'ont pas de fibres

        # Extraire les vitamines et minéraux
        full_nutrients = {item["attr_id"]: item["value"] for item in food_info["full_nutrients"]}
        vitamin_c = full_nutrients.get(401, "N/A")  # 401 = Vitamine C
        potassium = full_nutrients.get(306, "N/A")  # 306 = Potassium

        # Vérifier les restrictions alimentaires (exemple simple)
        gluten_free = "✅" if "wheat" not in food_info["food_name"].lower() else "❌"
        lactose_free = "✅" if "milk" not in food_info["food_name"].lower() else "❌"
        vegan = "✅" if food_info["food_name"].lower() not in ["chicken", "beef", "fish", "milk", "egg"] else "❌"

        # Affichage des résultats
        print(f"""
        📜 {name} (100g)
        🔹 Calories : {calories} kcal
        🔹 Protéines : {protein}g
        🔹 Glucides : {carbs}g
        🔹 Lipides : {fat}g
        🔹 Fibres : {fiber}g
        🔹 Vitamine C : {vitamin_c} mg (immunité, peau)
        🔹 Potassium : {potassium} mg (électrolytes, muscles)
        🔹 Sans gluten : {gluten_free}
        🔹 Sans lactose : {lactose_free}
        🔹 Végétalien : {vegan}
        """)
    else:
        print(f"Erreur: {response.status_code}")
