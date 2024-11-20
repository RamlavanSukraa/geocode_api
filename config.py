import configparser
from utils.logger import setup_logger

logger = setup_logger('app_logger')

def load_config(section, key, config_file='config.ini'):

    logger.info("Loading configuration")

    config = configparser.ConfigParser()
    config.read(config_file)

    if section not in config:

        logger.error(f"Section '{section}' not found in the configuration file.")
        raise Exception(f"Section '{section}' not found in the configuration file.")
    
    value = config.get(section, key).strip()  # Ensure no trailing spaces
    logger.info("Successfully configuration loaded")
    return value

# Load the API key
API_KEY = load_config('google_maps', 'api_key')
