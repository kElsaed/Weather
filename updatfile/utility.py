
from dotenv import load_dotenv 
import os 
import requests


# The url Of The APi
load_dotenv(".env")
    
class weather (object):
    def __init__(self,city_name:str) -> str:
        self.url = "http://api.weatherstack.com/current?"
        self.API_KEY = os.getenv("API_KEY")
        self.city_name = city_name

    def post_weather(self):
        '''A Function That Get The Temperature 
        from weatherstack Open Source API 
        '''
    
        # Store the requests with json format  
        req = requests.get(self.url + "query=" + self.city_name +"&access_key=" + self.API_KEY).json()
        return req 

