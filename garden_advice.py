# These functions separate the advice logic from the main program.
# This makes the code easier to maintain and expand in the future.

# Function to determine advice based on the season
def get_season_advice(season):
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


# Function to determine advice based on the plant type
def get_plant_advice(plant_type):
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


# Hardcoded values for the season and plant type
season = "summer"
plant_type = "flower"

# Variable to hold gardening advice
advice = ""

# Generate advice using functions
advice += get_season_advice(season)
advice += get_plant_advice(plant_type)

# Print the generated advice
print(advice)
