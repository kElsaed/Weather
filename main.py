from fastapi import FastAPI 
import requests
import uvicorn 
from pydantic import BaseModel

app = FastAPI()

# The url Of The APi
url = "https://api.openweathermap.org/data/2.5/weather?"
# My API Key
API_KEY = "78998ec441450b1904ee4741a94b522b"


@app.get("/weather")
async def post_weather(city_name:str):
    '''A Function That Get The Temperature in kelvin and Celsius 
     from OpenWeather Open Source API 
     It takes
     The city name : Str 
     return json format  '''
    
    # Store the requests with json format  
    req = requests.get(url + "q=" + city_name +"&appid=" + API_KEY).json()
    
    # get the Temperature in kelvin
    kelvin = req["main"]["temp"]
    # convert Temperature to Celsius
    cels =  kelvin - 273.15
    
    # return json format 
    return { "Temperature In kelvin " : kelvin , 
            "Temperature In Celsius " : cels 
             } 

# run the app 
if __name__ == "__main__" :
    uvicorn.run(app=app,host="127.0.0.1",port=8000)
