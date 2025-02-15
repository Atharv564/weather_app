# 🌤️ Weather App

A simple and modern weather app built using Django, Bootstrap, and a Weather API. This application provides real-time weather information and a 5-day forecast with a visually appealing UI.

## 🚀 Features

- 🌍 Search weather by city name
- 🌡️ Display current temperature and weather condition
- 📅 5-day weather forecast with icons
- 🎨 Dynamic background based on weather condition
- 📱 Responsive design using Bootstrap
- 🔔 Weather condition icons using the Weather Icons library

## 🛠️ Technologies Used

- **Backend:** Django, SQLite
- **Frontend:** Bootstrap, Weather Icons, JavaScript
- **APIs:** OpenWeatherMap / WeatherAPI

## 📷 Screenshots

![Weather App Screenshot](weather_project/weather/screenshots/weather-app.png)

## 🏗️ Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/weather-app.git
   cd weather-app
   ```
2. **Create and activate a virtual environment:**
   ```sh
    python -m venv venv 
    source venv/bin/activate  # For macOS/Linux
    venv\Scripts\activate     # For Windows
   ```
3. **Install dependencies:**
   ```sh
    pip install -r requirements.txt
   ```
4. **Run the Django server:**
   ```sh
    python manage.py runserver
   ```
5. **Open the app in your browser:**
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## ⚙️ Configuration

- To use the weather API, get an API key from [WeatherAPI](https://www.weatherapi.com/) or [OpenWeatherMap](https://openweathermap.org/)
- Add your API key to `settings.py`:

   ```python
   WEATHER_API_KEY = 'your_api_key_here'
  ```
## 📄 License

This project is open-source and available under the MIT License.  
See the [LICENSE](LICENSE) file for more details.
## 🤝 Contributing

Pull requests are welcome. Feel free to **fork** this project and submit a **Pull Request (PR)** with your changes.  
For major changes, please open an issue first to discuss what you'd like to improve.  

1. **Fork the repository**  
2. **Create a new branch** (`git checkout -b feature-branch`)  
3. **Commit your changes** (`git commit -m "Add some feature"`)  
4. **Push to the branch** (`git push origin feature-branch`)  
5. **Open a Pull Request**  

---

## ⭐ Show Some Love

If you like this project, please consider **giving it a star (⭐) on GitHub**!  
It helps others discover the project and motivates the contributors. 🚀

Developed by [Atharv..](https://github.com/Atharv564)
