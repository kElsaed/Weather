# Weather API Documentation 

### EndPoint Url 
```
http://127.0.0.1:8000/weather
```

### Parameter 

- `city_name` The City Name For Location 

### Response 

- Json Format with city , lon , lat , weather_descriptions and temperature


### Examole Usage 

#### Request 
```http
 city_name : Cairo
```

#### Responce 

```json 
{
    "temperature": 28,
    "weather_descriptions": [
        "Partly cloudy"
    ],
    "City": "Cairo, Egypt",
    "lat": "30.050",
    "lon": "31.250"
}
```
