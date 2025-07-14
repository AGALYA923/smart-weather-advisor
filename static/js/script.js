function fetchWeather() {
  const city = document.getElementById("cityInput").value;
  const country = document.getElementById("countryInput").value;
  const fullCity = country ? `${city},${country}` : city;

  fetch("/get-weather", {
    method: "POST",
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ city: fullCity })
  })
  .then(res => res.json())
  .then(data => {
    if (data.error) return alert(data.error);

    document.getElementById("weatherResult").style.display = "block";
    document.getElementById("resultCity").textContent = data.city;
    document.getElementById("temp").textContent = data.temp;
    document.getElementById("humidity").textContent = data.humidity;
    document.getElementById("wind").textContent = data.wind;
    document.getElementById("feels").textContent = data.feels;
    document.getElementById("pressure").textContent = data.pressure;
    document.getElementById("suggestionText").textContent = data.advice;
    document.getElementById("mapLink").href = `https://www.google.com/maps/search/${data.city}`;
    document.getElementById("weatherIcon").src = `https://openweathermap.org/img/wn/${data.icon}@2x.png`;

    document.getElementById("todayDate").textContent = new Date().toDateString();
    document.getElementById("localTime").textContent = new Date().toLocaleTimeString();

    const tips = [
      "Check humidity before hiking!",
      "Windy day? Secure loose items!",
      "Use sunscreen when UV is high!",
      "Avoid traveling during fog!",
      "Stay hydrated on hot days!"
    ];
    document.getElementById("tip").textContent = tips[Math.floor(Math.random() * tips.length)];
  });
}

function toggleTheme() {
  document.body.classList.toggle("dark-mode");
}

function speakWeather() {
  const text = document.getElementById("suggestionText").textContent;
  const speech = new SpeechSynthesisUtterance(text);
  window.speechSynthesis.speak(speech);
}
