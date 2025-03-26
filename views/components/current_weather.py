import tkinter as tk
from PIL import Image, ImageTk
import io
import requests

class CurrentWeatherView:
    def __init__(self, parent):
        self.frame = tk.LabelFrame(parent, text="Clima Atual", padx=10, pady=10)
        self.frame.pack(fill=tk.X, pady=(0, 10))
        
        self.icon_label = tk.Label(self.frame)
        self.icon_label.pack(side=tk.LEFT, padx=10)
        
        self.temp_label = tk.Label(self.frame, font=("Arial", 24))
        self.temp_label.pack(side=tk.LEFT, padx=10)
        
        self.details_label = tk.Label(self.frame, justify=tk.LEFT)
        self.details_label.pack(side=tk.LEFT, padx=10)
    
    def update(self, weather_data):
        icon_url = f"http://openweathermap.org/img/wn/{weather_data['weather'][0]['icon']}@2x.png"
        self._load_image(icon_url, self.icon_label)
        
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        description = weather_data['weather'][0]['description'].capitalize()
        
        self.temp_label.config(text=f"{temp:.1f}°C")
        details_text = (
            f"Sensação: {feels_like:.1f}°C\n"
            f"Umidade: {humidity}%\n"
            f"Vento: {wind_speed} km/h\n"
            f"{description}"
        )
        self.details_label.config(text=details_text)
    
    def _load_image(self, url, label):
        try:
            response = requests.get(url, stream=True)
            image = Image.open(io.BytesIO(response.content))
            photo = ImageTk.PhotoImage(image)
            label.config(image=photo)
            label.image = photo
        except Exception:
            label.config(text="Ícone não disponível")