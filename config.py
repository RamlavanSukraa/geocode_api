import configparser

# Initialize configparser
config = configparser.ConfigParser()
config.read('config.ini')

# Twilio Configuration
twilio = {
    'account_sid': config.get('twilio', 'account_sid'),
    'auth_token': config.get('twilio', 'auth_token'),
}

# LocationIQ Configuration
api_key = config.get('locationiq', 'api_key')
url = config.get('locationiq', 'url')
