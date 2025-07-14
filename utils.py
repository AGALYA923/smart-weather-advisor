def generate_advice(description, temp, wind=0, humidity=0):
    description = description.lower()
    
    if "thunder" in description:
        return "Stay indoors. Thunderstorms are dangerous ⚡"
    elif "rain" in description or "drizzle" in description:
        return "Carry an umbrella ☔ and wear waterproof shoes."
    elif "snow" in description:
        return "Wear warm clothes and be careful of slippery roads ❄️"
    elif "fog" in description or "mist" in description:
        return "Drive slow — visibility is low 🌫️"
    elif "clear" in description:
        if temp > 30:
            return "Sunny day! Stay cool and hydrated ☀️🥵"
        return "Perfect weather! Enjoy your day ☀️"

    if temp >= 38:
        return "Heat alert! Avoid going outside during peak hours 🔥"
    elif temp >= 30:
        return "It's hot! Stay hydrated and avoid direct sunlight 🥵"
    elif temp <= 10:
        return "Very cold! Bundle up and stay warm 🧣🧥"
    elif temp < 20:
        return "Slightly chilly. Carry a light jacket 🧥"

    if wind > 30:
        return "Windy conditions — secure loose items and stay safe 🌬️"
    if humidity >= 80:
        return "High humidity! It may feel hotter than it is 💦"

    if "cloud" in description:
        return "Partly cloudy. Might get sunny or rainy later ☁️"

    return "Have a great day and stay safe! 😊"
