
# Address to Coordinates Bot using Twilio and FastAPI

This project provides a FastAPI-based service that integrates with Twilio WhatsApp to allow users to send their address to the bot and receive the corresponding latitude and longitude as a response.

## Features

- **Twilio WhatsApp Integration**: Receive messages from users via WhatsApp.
- **Location IQ Geocoding**: Converts user-provided address into geographic coordinates.
- **Error Handling**: Ensures robust error handling for both API calls and user input.
- **Logging**: Provides detailed logging for debugging and monitoring.

## Prerequisites

1. **Python 3.7 or higher**: Ensure you have Python installed on your system.
2. **Twilio Account**: Set up a Twilio account and obtain your Account SID and Auth Token.
3. **Location IQ API Key**: Sign up at [Location IQ](https://locationiq.com/) and obtain an API key.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure environment variables in a `config.py` file:
    ```python
    # config.py
    twilio = {
        "account_sid": "your_account_sid",
        "auth_token": "your_auth_token"
    }
    api_key = "your_location_iq_api_key"
    url = "https://us1.locationiq.com/v1/search.php?key="
    ```

5. Run the application:
    ```bash
    uvicorn main:app --reload
    ```

## Usage

1. **Set up Twilio WhatsApp**:
    - Configure a Twilio WhatsApp-enabled number.
    - Set the webhook URL to `http://<your-domain>/api/v1/whatsapp/`.

2. **Send a message**:
    - Send an address (e.g., `1600 Amphitheatre Parkway, Mountain View, CA`) to the Twilio WhatsApp number.

3. **Receive the response**:
    - The bot will reply with the latitude and longitude of the provided address.

## Example Interaction

1. User sends: `1600 Amphitheatre Parkway, Mountain View, CA`
2. Bot replies: `Coordinates for "1600 Amphitheatre Parkway, Mountain View, CA": Latitude 37.422, Longitude -122.084`

## Logging

Logs are generated for each step of the process and are helpful for debugging. Configure logging in the `utils/logger.py` file.

## Error Handling

- If the address is invalid or the geocoding API fails, the bot responds with an appropriate error message.

## Dependencies

- `FastAPI`: For creating the API.
- `Twilio`: For WhatsApp integration.
- `requests`: For making HTTP requests to the geocoding API.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
