def recommend_crop(soil_type, rainfall):
    if soil_type == "Loam" and rainfall > 500:
        return "Rice"
    elif soil_type == "Sandy":
        return "Groundnut"
    elif rainfall < 400:
        return "Millets"
    else:
        return "Wheat"
