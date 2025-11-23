def irrigation_advice(rainfall, farm_area):
    if rainfall > 600:
        return "Less irrigation needed"
    elif rainfall > 300:
        return "Moderate drip irrigation needed"
    else:
        return "Regular irrigation required"
