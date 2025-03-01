"""Settings..."""
import os 
from dotenv import load_dotenv

# Load vars from .env
load_dotenv()

IPMA_API_URL = os.getenv("IPMA_API_URL")
IPMA_API_KEY = os.getenv("IPMA_API_KEY")
CITY_ID = "1110600" #Lisbon

#Twilio
TWILIO_ACCOUNT_SID=os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN=os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER=os.getenv("TWILIO_PHONE_NUMBER")
USER_PHONE_NUMBER=os.getenv("USER_PHONE_NUMBER")