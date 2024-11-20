
##########################################################
#                                                        #
#  Auth:       ""                                        #
#  Created:    11/06/2024                                #
#  Project:    WhatsApp Geolocation Bot                  #          
#                                                        #
#  Summary:    This module handles the incoming WhatsApp #
#              messages via Twilio, queries the          #
#              LocationIQ API for geolocation data, and  #
#              responds with latitude and longitude.     #
#                                                        #
##########################################################



from fastapi import FastAPI
from routes.whatsapp_api import router as whatsapp_router

app = FastAPI()

app.include_router(whatsapp_router)