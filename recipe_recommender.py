# Код программы Recipe Recommender

recipes = {
    "Spaghetti Bolognese": ["spaghetti", "beef mince", "tomatoes", "onions", "garlic"],
    "Shepherd's Pie": ["potatoes", "beef mince", "carrots", "onions", "peas"],
    "Chicken Stir-Fry": ["chicken breast", "rice", "soy sauce", "onions", "peppers", "garlic"],
    "Beef Stroganoff": ["beef steak", "pasta", "sour cream", "mushrooms", "onions"],
    "Fish and Chips": ["fish", "potatoes", "flour", "eggs", "bread crumbs"]
}

user_ingredients = input("What ingredients do you have? ").split()

for recipe, ingredients in recipes.items():
    if all(ingredient in user_ingredients for ingredient in ingredients):
        print(recipe)
