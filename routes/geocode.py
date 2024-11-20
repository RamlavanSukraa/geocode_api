import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests
from urllib.parse import quote
from config import API_KEY 
from utils.logger import setup_logger

# Set up logging

logger = setup_logger('app_logger')
router = APIRouter()

class AddressRequest(BaseModel):
    address: str

@router.post("/api/v1/get_geocode/")
async def get_location(request: AddressRequest):
    # Log the received address
    logger.info(f"Received geocode request for address: '{request.address}'")
    
    # URL-encode the address
    address = quote(request.address.strip())
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}"
    logger.debug(f"Constructed URL for API request: {url}")

    # Make the API request
    try:
        response = requests.get(url)
        logger.info(f"API response status code: {response.status_code}")
        
        # Log the full response content for debugging
        if response.status_code == 200:
            data = response.json()
            logger.debug(f"Full API response data: {data}")

            if 'results' in data and data['results']:
                location = data['results'][0]['geometry']['location']
                logger.info(f"Extracted location - Latitude: {location['lat']}, Longitude: {location['lng']}")
                return {"latitude": location['lat'], "longitude": location['lng']}
            else:
                error_message = data.get('error_message', 'Location not found.')
                logger.warning(f"API response issue: {error_message}")
                raise HTTPException(status_code=404, detail=error_message)
        else:
            # Extract and log specific error messages
            error_message = response.json().get('error_message', response.text)
            logger.error(f"API returned an error: {error_message}")
            raise HTTPException(status_code=response.status_code, detail=error_message)
    
    except requests.exceptions.RequestException as e:
        logger.exception("An error occurred during the API request.")
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
