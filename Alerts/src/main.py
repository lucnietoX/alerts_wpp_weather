from services.weather_api import get_weather_forecast
from services.twilio_service import send_whatsapp_message
import logging

logging.basicConfig(level=logging.INFO)

def main():
    """ Get the weather forecast and send via WhatsApp """
    forecast = get_weather_forecast()
    if forecast:
        message = (
            f"Weather Lisbon Forecast for Today \n"
            f"Min: {forecast['min_temp']}°C | Max: {forecast['max_temp']}°C\n"
            f"Rain: {forecast['precipitation']}%\n"
            f"Execution Time (Source IPMA): {forecast['execution_time']}"
        )
        send_whatsapp_message(message)

if __name__ == "__main__":
    main()
