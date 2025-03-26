import requests
from datetime import datetime
from models.settings import Settings

class WeatherModel:
    def __init__(self):
        self.settings = Settings()

    def get_weather(self, city=None):
        city = city or self.settings.DEFAULT_CITY
        current = self._get_weather_data("weather", city)
        forecast = self._get_weather_data("forecast", city)
        return current, forecast

    def _get_weather_data(self, endpoint, city):
        url = (f"{self.settings.BASE_URL}{endpoint}?"
               f"q={city}&units={self.settings.UNITS}&"
               f"lang={self.settings.LANG}&appid={self.settings.API_KEY}")
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def process_forecast_data(forecast_data):
        daily_forecasts = {}
        for forecast in forecast_data['list']:
            date = datetime.fromtimestamp(forecast['dt']).strftime('%Y-%m-%d')
            if date not in daily_forecasts:
                daily_forecasts[date] = []
            daily_forecasts[date].append(forecast)
        
        return sorted(daily_forecasts.items())[1:5]  # Próximos 4 dias