from utility import weather
from fastapi import FastAPI 
import uvicorn 

app = FastAPI()


@app.get("/weather")
async def post_weather(city_name:str):
    '''A Function That Get The Temperature in kelvin and Celsius 
     '''
    
    weather_class = weather(city_name)
    post_weather_method = weather_class.post_weather()
    
    # return json format 
    return { 
        "temperature": post_weather_method ["current"]["temperature"],
        "weather_descriptions": post_weather_method ["current"]["weather_descriptions"],
        "City": post_weather_method ["request"]["query"],
        "lat": post_weather_method ["location"]["lat"],
        "lon": post_weather_method ["location"]["lon"]
             } 

# run the app 
if __name__ == "__main__" :
    uvicorn.run(app=app,host="127.0.0.1",port=8000)
