from twilio.rest import Client
import logging
from services.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, USER_PHONE_NUMBER

logging.basicConfig(level=logging.INFO)

def send_whatsapp_message(message):
    """ Sent message by WhatsApp via Twilio """
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        msg = client.messages.create(
            from_=TWILIO_PHONE_NUMBER,
            body=message,
            to=USER_PHONE_NUMBER
        )
        logging.info(f"Message sent with success! ID: {msg.sid}")
    except Exception as e:
        logging.error(f"Error when tried to sent message via Twilio: {e}")