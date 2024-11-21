# config.py

import configparser
from utils.logger import setup_logger

logger = setup_logger(__name__)

def load_config(config_file='config.ini'):
    """
    Loads configuration from the given config file.

    Args:
        config_file (str): Path to the configuration file. Defaults to 'config.ini'.

    Returns:
        dict: A dictionary containing loaded configuration values.
    """
    config = configparser.ConfigParser()
    config.read(config_file)

    try:
        # Load Twilio Configuration
        twilio = {
            'account_sid': config.get('twilio', 'account_sid'),
            'auth_token': config.get('twilio', 'auth_token'),
        }
        logger.info("Twilio configuration loaded.")

        # Load LocationIQ Configuration
        locationiq = {
            'api_key': config.get('locationiq', 'api_key'),
            'url': config.get('locationiq', 'url'),
        }
        logger.info("LocationIQ configuration loaded.")

        # Return all configurations in a dictionary
        return {'twilio': twilio, 'locationiq': locationiq}

    except (configparser.NoSectionError, configparser.NoOptionError) as e:
        logger.error(f"Configuration error: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error loading configuration: {e}")
        raise
