import requests
from langchain.tools import tool

@tool
def get_delivery_estimate(distance: float, items: int, weather: str):
    """
    Estimate delivery time using the local Flask API.
    """

    url = "http://127.0.0.1:5000/"

    data = {
        "distance": distance,
        "items": items,
        "weather": weather
    }

    response = requests.post(url, json=data)

    result = response.json()

    return f"Estimated delivery time is {result['delivery_time']} minutes."