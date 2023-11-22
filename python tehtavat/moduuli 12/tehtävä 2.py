import requests

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Retrieves temperature in Celsius
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        weather_desc = weather_data['weather'][0]['description']
        temp_celsius = weather_data['main']['temp']
        return weather_desc, temp_celsius
    else:
        return None, None

def main():
    api_key = "YOUR_API_KEY"  # Replace with your actual API key from OpenWeather
    city = input("Enter the name of a city: ")

    weather_desc, temp_celsius = get_weather(api_key, city)

    if weather_desc and temp_celsius:
        print(f"Weather in {city}: {weather_desc}")
        print(f"Temperature: {temp_celsius:.2f}°C")
    else:
        print("Failed to retrieve weather information.")

if __name__ == "__main__":
    main()
