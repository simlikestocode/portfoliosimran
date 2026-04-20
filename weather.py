import requests

API_KEY = "YOUR_API_KEY_HERE"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        print("City not found or error.")
        return

    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    print(f"\nWeather in {city}")
    print(f"Temperature: {temp}°C")
    print(f"Condition: {weather}")
    print(f"Humidity: {humidity}%")

while True:
    city = input("\nEnter city (or type exit): ")

    if city.lower() == "exit":
        break

    get_weather(city)
