import json

with open("menu.json", "r") as file:
    menu = json.load(file)

def search_menu(user_diet, user_query):

    cuisine = ""

    cuisines = [
        "Indian",
        "Chinese",
        "Italian",
        "Japanese",
        "Fast Food"
    ]

    for c in cuisines:
        if c.lower() in user_query.lower():
            cuisine = c

    results = []

    for item in menu:

        if user_diet == "Vegetarian":
            if item["veg"] == False:
                continue

        if cuisine != "":
            if item["cuisine"] != cuisine:
                continue

        results.append(item)

    return results[:3]