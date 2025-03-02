"""Module to interact with IPMA API"""
from datetime import datetime
import logging
import requests
from services.settings import CITY_ID
from services.settings import IPMA_API_URL


logging.basicConfig(level=logging.INFO)

def get_weather_forecast():
    """ Forecasts from IPMA """
    url = f"{IPMA_API_URL}{CITY_ID}.json"
    try:
        response = requests.get(url,timeout=30)
        response.raise_for_status()
        data = response.json()
        today_forecast = data['data'][0]
        data_weather = {
            "min_temp": today_forecast["tMin"],
            "max_temp": today_forecast["tMax"],
            "precipitation": today_forecast["precipitaProb"],
            "date": datetime.now().strftime("%Y-%m-%d"),
            "execution_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        }
        return data_weather
    except Exception as e:
        logging.error(f"Error: {e}")
        return None
