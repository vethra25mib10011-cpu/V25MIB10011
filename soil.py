def analyze_soil(soil_type):
    score_map = {"Clay": 6, "Loam": 9, "Sandy": 5}
    return score_map.get(soil_type, 5)
