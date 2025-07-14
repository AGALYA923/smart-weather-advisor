from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os, requests
from utils import generate_advice

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-weather", methods=["POST"])
def get_weather():
    data = request.get_json()
    city = data.get("city")
    api_key = os.getenv("WEATHER_API_KEY")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()

    if response.get("cod") != 200:
        return jsonify({"error": "City not found!"})

    weather = {
        "city": response["name"],
        "temp": response["main"]["temp"],
        "humidity": response["main"]["humidity"],
        "wind": response["wind"]["speed"],
        "description": response["weather"][0]["description"],
        "icon": response["weather"][0]["icon"]
    }

    advice = generate_advice(weather["description"], weather["temp"])
    return jsonify({**weather, "advice": advice})

if __name__ == "__main__":
    app.run(debug=True)
