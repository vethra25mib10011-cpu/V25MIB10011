def get_market_price(crop):
    price_list = {
        "Rice": "₹40/kg",
        "Groundnut": "₹55/kg",
        "Millets": "₹60/kg",
        "Wheat": "₹35/kg"
    }
    return price_list.get(crop, "Price Unavailable")
