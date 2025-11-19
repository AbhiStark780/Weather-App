# 🌦️ CLI Weather App

A simple, robust Command Line Interface (CLI) application that fetches real-time weather data for any city using the OpenWeatherMap API.

## 🚀 Features
* **Real-time Data:** Fetches current temperature, humidity, wind speed, and weather conditions.
* **Visual Feedback:** Uses dynamic emojis (☀️, 🌧️, ❄️) based on weather conditions.
* **User Friendly:** Handles typos and errors gracefully without crashing.
* **Interactive:** Runs in a loop until you decide to quit.

## 🛠️ Tech Stack
* **Language:** Python 3.11.5
* **Libraries:** `requests`
* **API:** OpenWeatherMap

## ⚙️ Setup & Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/AbhiStark780/Weather-App.git](https://github.com/AbhiStark780/Weather-App.git)
    ```

2.  **Install dependencies**
    ```bash
    pip install requests
    ```

3.  **API Key Configuration**
    * Sign up at [OpenWeatherMap](https://openweathermap.org/) to get a free API Key.
    * Create a file named `config.py` in the project folder.
    * Add your key inside it like this:
        ```python
        apiKey = "YOUR_SECRET_KEY_HERE"
        ```

4.  **Run the App**
    ```bash
    python weather.py
    ```

## 📸 Usage Example

```text
Enter a city name: London

----------------------------------------
Weather Report for London
----------------------------------------
🌧️   light rain
🌡️   Temperature: 15.32°C
💧   Humidity: 82%
💨   Wind: 4.12 m/s
----------------------------------------