spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]
    # names = []
    # for food in spicy_foods:
    #     names.append(food["name"])
    # return names


def get_spiciest_foods(spicy_foods):
    return [ food for food in spicy_foods if food["heat_level"] > 5]
        


def print_spicy_foods(spicy_foods): 
    # for food in spicy_foods:
    #     name = food["name"]
    #     cuisine = food["cuisine"]
    #     heat_level = food["heat_level"]
    #     heat_level_emoji = "🌶" * heat_level
    #     print(f"{name} ({cuisine}) | Heat Level: {heat_level_emoji}")
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level = food["heat_level"]
            heat_level_emoji = "🌶" * heat_level
            print(f"{name} ({cuisine}) | Heat Level: {heat_level_emoji}")
    # spiciest_food = get_spiciest_foods(spicy_foods)
    # print_spicy_foods(spiciest_food)

def get_average_heat_level(spicy_foods):
    # total_heat_level = 0
    # num_foods = len(spicy_foods)

    # for food in spicy_foods:
    #     total_heat_level += food["heat_level"]
    
    # if num_foods > 0:
    #     return total_heat_level // num_foods
    # else:
    #     return 0

    return sum([food["heat_level"] for food in spicy_foods]) / len(spicy_foods)
    

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods