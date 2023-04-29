# Standard library import
import logging

# Third-party imports
from twilio.rest import Client
from decouple import config


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = config("TWILIO_ACCOUNT_SID")
auth_token = config("TWILIO_AUTH_TOKEN")
client = Client("AC0bdc71b633452fec5718dad955770fb1", "2df91535fc1d51e256e943fec01ad5cf")
twilio_number = "+14155238886"

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Sending message logic through Twilio Messaging API
def send_message(to_number, body_text):
    try:
        message = client.messages.create(
            from_=f"whatsapp:+14155238886",
            body=body_text,
            to=f"whatsapp:+919027553376"
            )
        logger.info(f"Message sent to {to_number}: {message.body}")
    except Exception as e:
        logger.error(f"Error sending message to {to_number}: {e}")
