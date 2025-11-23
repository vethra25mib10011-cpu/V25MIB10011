from weather import get_weather
from soil import analyze_soil
from crop import recommend_crop
from water import irrigation_advice
from fertilizer import fertilizer_recommendation
from market import get_market_price
from report import generate_report

def main():
    print("\n===== AGRICULTURE ASSISTANT SYSTEM =====\n")

    location = input("Enter your location/state: ")
    soil_type = input("Enter soil type (Clay/Sandy/Loam): ")
    rainfall = float(input("Enter expected rainfall (mm): "))
    farm_area = float(input("Enter farm size (in acres): "))

    print("\nProcessing your data...\n")

    weather_data = get_weather(location)
    soil_score = analyze_soil(soil_type)
    crop = recommend_crop(soil_type, rainfall)
    irrigation = irrigation_advice(rainfall, farm_area)
    fertilizer = fertilizer_recommendation(crop, soil_type)
    price = get_market_price(crop)

    print("\n📌 Recommendations Ready!\n")
    generate_report(location, soil_type, rainfall, crop, irrigation, fertilizer, price)

if _name_ == "_main_":
    main()
