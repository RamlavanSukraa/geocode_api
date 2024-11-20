from fastapi import APIRouter, HTTPException, Request, Form
from config import twilio,api_key,url
from twilio.rest import Client
import requests
from urllib.parse import quote
from utils.logger import setup_logger

# Set up logger configuration
logger =  setup_logger(__name__)
router = APIRouter()

# Twilio client initialization
client = Client(twilio['account_sid'], twilio['auth_token'])

@router.post('/api/v1/whatsapp/')
async def sms(request: Request):
    try:
        logger.info("Receiving request from Twilio...")
        form_data = await request.form()
        logger.info(f"Received form data: {form_data}")

        # Extract fields from form_data
        body = form_data.get("Body")
        from_number = form_data.get("From")
        to_number = form_data.get("To")
        latitude = form_data.get("Latitude")
        longitude = form_data.get("Longitude")

        logger.info(f"Extracted Body: {body}")
        logger.info(f"Extracted From: {from_number}")
        logger.info(f"Extracted To: {to_number}")
        logger.info(f"Extracted Latitude: {latitude}")
        logger.info(f"Extracted Longitude: {longitude}")

        # Handle location messages
        if latitude and longitude:
            logger.info("Processing location message.")
            response_message = f'Received location: Latitude {latitude}, Longitude {longitude}'
        elif body:
            logger.info("Processing text message.")
            # Encode the location for the geocoding API
            encoded_location = quote(body)
            geocode_url = f"{url}{encoded_location}&key={api_key}&format=json"
            logger.info(f"Geocoding URL: {geocode_url}")

            try:
                response = requests.get(geocode_url)
                logger.info(f"Geocoding API response status: {response.status_code}")
                response.raise_for_status()

                geocode_data = response.json()

                if not geocode_data or len(geocode_data) == 0:
                    raise ValueError("Geocoding API returned empty data.")

                lat = geocode_data[0].get('lat')
                lon = geocode_data[0].get('lon')

                if not lat or not lon:
                    raise KeyError("Missing 'lat' or 'lon' in geocoding response.")

                logger.info(f"Extracted coordinates: Latitude {lat}, Longitude {lon}")
                response_message = f'Coordinates for "{body}": Latitude {lat}, Longitude {lon}'
            except (requests.RequestException, ValueError, KeyError, IndexError) as e:
                logger.error(f"Geocoding error: {e}")
                response_message = 'Error retrieving geolocation. Please ensure the location is valid.'
        else:
            logger.warning("Message body and location are missing.")
            raise HTTPException(status_code=400, detail="No message body or location provided")

        # Send response to Twilio
        logger.info("Sending response back to Twilio...")
        message = client.messages.create(
            from_=to_number,
            to=from_number,
            body=response_message
        )
        logger.info(f"Twilio response message SID: {message.sid}")

        return {"status": "success", "message_sid": message.sid}

    except Exception as e:
        logger.error(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
