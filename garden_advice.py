# Function to determine advice based on the season
def get_season_advice(season):
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


# Function to determine advice based on plant type
def get_plant_advice(plant_type):
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


# Allow users to enter their own choices
season = input("Enter the season: ").lower()
plant_type = input("Enter the plant type: ").lower()


# Generate gardening advice
advice = ""
advice += get_season_advice(season)
advice += get_plant_advice(plant_type)


# Display the generated advice
print(advice)

