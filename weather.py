import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_weather(city):
    """
    Fetch weather data for a given city using OpenWeatherMap API.
    """
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")  # Get API key from .env
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    if response.get("cod") != 200:
        return None
    weather = response["weather"][0]["description"]
    temperature = response["main"]["temp"]
    humidity = response["main"]["humidity"]
    return {
        "weather": weather,
        "temperature": temperature,
        "humidity": humidity
    }

def speak_weather(city, speak_function):
    """
    Fetch and speak the weather for a given city.
    """
    weather_data = get_weather(city)
    if weather_data:
        weather_info = f"The weather in {city} is {weather_data['weather']} with a temperature of {weather_data['temperature']}°C and humidity of {weather_data['humidity']}%."
    else:
        weather_info = "Sorry, I couldn't fetch the weather."
    speak_function(weather_info)