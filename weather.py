def get_weather(location):
    dummy_weather = {
        "Tamil Nadu": "Hot & Moderate Rain",
        "Kerala": "Heavy Rain",
        "Punjab": "Cold & Dry",
        "UP": "Moderate Rain and Heat",
        "Default": "Moderate"
    }
    return dummy_weather.get(location, dummy_weather["Default"])
