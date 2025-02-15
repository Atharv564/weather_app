import requests
from django.shortcuts import render

def weather_view(request):
    api_key = "API_KEY"  # Replace with your WeatherAPI key
    city = request.GET.get('city', 'Pune')  # Default city

    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=5&aqi=no&alerts=no"
    response = requests.get(url).json()

    weather_data = {
        'city': city,
        'temperature': response.get('current', {}).get('temp_c', 'N/A'),
        'condition': response.get('current', {}).get('condition', {}).get('text', 'N/A'),
        'icon': response.get('current', {}).get('condition', {}).get('icon', ''),
        'forecast': response.get('forecast', {}).get('forecastday', [])  # 5-day forecast
    }

    return render(request, 'weather/weather.html', {'weather': weather_data})
