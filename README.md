# 🌦️ CLI Weather App

A simple, robust Command Line Interface (CLI) application that fetches real-time weather data for any city using the OpenWeatherMap API.

## 🚀 Features
* **Real-time Data:** Fetches current temperature, humidity, wind speed, and weather conditions.
* **5-Day Forecast:** Displays a clean, formatted summary of the weather for the next 5 days (noon snapshots).
* **Visual Feedback:** Uses dynamic emojis (☀️, 🌧️, ❄️) based on weather conditions.
* **User Friendly:** Handles typos and errors gracefully without crashing.
* **Interactive:** Runs in a loop until you decide to quit.

## 🛠️ Tech Stack
* **Language:** Python 3.11.5
* **Libraries:** `requests`, `datetime` (Standard Library)
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
Enter a city name: Las Vegas
----------------------------------------
Weather Report for Las Vegas
----------------------------------------
☀️   clear sky
🌡️   Temperature: 13.43°C
💧   Humidity: 57%
💨   Wind: 1.54m/s
----------------------------------------
5 Day Weather Forecast
----------------------------------------
Fri, 21 Nov    🌧️      7.61°C     - light rain
Sat, 22 Nov    🌧️      10.74°C    - light rain
Sun, 23 Nov    ☁️      12.74°C    - few clouds
Mon, 24 Nov    ☀️      11.44°C    - clear sky
Tue, 25 Nov    ☀️      11.57°C    - clear sky
Check another city ? (Y/N): 