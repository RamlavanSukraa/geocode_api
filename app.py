
##########################################################
#                                                        #
#  Auth:       ""                                        #
#  Created:    19/11/2024                                #
#  Project:    FastAPI Geocoding Service                 #          
#                                                        #
#  Summary:    This project is a FastAPI-based service   #
#              that handles geocoding requests using     #
#              the Google maps API. It processes user    #
#              input addresses, sends requests to        #
#              Google maps, and returns the              #
#              corresponding latitude and longitude.     #
#                                                        #
##########################################################


from routes.geocode import router as geocode_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(geocode_router)