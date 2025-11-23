def fertilizer_recommendation(crop, soil_type):
    if crop == "Rice":
        return "Apply NPK 60:40:20 with urea"
    elif crop == "Groundnut":
        return "Apply Gypsum + Low Nitrogen Fertilizer"
    elif crop == "Millets":
        return "Minimal fertilizer. Organic compost preferred."
    else:
        return "Use balanced NPK 40:20:20"
