import requests

API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data.get("cod") != 200:
            print("❌ Error:", data.get("message", "City not found."))
            return

        weather = data["weather"][0]["description"].capitalize()
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        city = data["name"]
        country = data["sys"]["country"]

        print(f"\n📍 Location: {city}, {country}")
        print(f"🌤️ Weather: {weather}")
        print(f"🌡️ Temperature: {temperature}°C (Feels like {feels_like}°C)")
        print(f"💧 Humidity: {humidity}%")
        print(f"💨 Wind Speed: {wind_speed} m/s")

    except requests.exceptions.RequestException as e:
        print("❌ Network error:", e)

def main():
    print("=== Weather App 🌦️ ===")
    while True:
        city = input("\nEnter city name (or type 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("Goodbye! ☀️")
            break
        get_weather(city)

if __name__ == "__main__":
    main()
