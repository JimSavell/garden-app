# Get season and plant type from user
season = input("Enter the season: ").lower()
plant_type = input("Enter the plant type: ").lower()

def get_season_advice(season):
    """Return gardening advice based on the season."""
    if season == "summer":
        return "Water your plants regularly and provide some shade."
    elif season == "winter":
        return "Protect your plants from frost with covers."
    else:
        return "No advice for this season."


def get_plant_advice(plant_type):
    """Return gardening advice based on the plant type."""
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."

advice = get_season_advice(season) + "\n"
advice += get_plant_advice(plant_type)

print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Store advice in a dictionary for multiple plants and seasons. 
# - Recommend plants based on the entered season.
