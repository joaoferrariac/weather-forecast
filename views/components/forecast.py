import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk
import io
import requests

class ForecastView:
    def __init__(self, parent):
        self.frame = tk.LabelFrame(parent, text="Previsão para os Próximos Dias", padx=10, pady=10)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self.days = []
        for i in range(4):
            day_frame = tk.Frame(self.frame, relief=tk.RIDGE, borderwidth=1, padx=10, pady=10)
            day_frame.grid(row=0, column=i, sticky="nsew", padx=5)
            self.frame.grid_columnconfigure(i, weight=1)
            
            self.days.append({
                "date": tk.Label(day_frame, font=("Arial", 10, "bold")),
                "icon": tk.Label(day_frame),
                "temp": tk.Label(day_frame),
                "desc": tk.Label(day_frame)
            })
            
            for widget in self.days[i].values():
                widget.pack()
    
    def update(self, forecast_data):
        for i, (date, forecasts) in enumerate(forecast_data):
            if i >= 4:
                break
                
            midday = self._get_midday_forecast(forecasts)
            weekday = datetime.strptime(date, '%Y-%m-%d').strftime('%A')
            
            self.days[i]["date"].config(text=self._translate_weekday(weekday))
            
            icon_url = f"http://openweathermap.org/img/wn/{midday['weather'][0]['icon']}@2x.png"
            self._load_image(icon_url, self.days[i]["icon"])
            
            temp_min = min(f['main']['temp_min'] for f in forecasts)
            temp_max = max(f['main']['temp_max'] for f in forecasts)
            
            self.days[i]["temp"].config(text=f"{temp_min:.1f}° / {temp_max:.1f}°")
            self.days[i]["desc"].config(text=midday['weather'][0]['description'].capitalize())
    
    def _get_midday_forecast(self, forecasts):
        for forecast in forecasts:
            time = datetime.fromtimestamp(forecast['dt']).strftime('%H:%M')
            if time == "12:00":
                return forecast
        return forecasts[len(forecasts)//2]
    
    def _translate_weekday(self, weekday):
        translation = {
            "Monday": "Segunda", "Tuesday": "Terça", "Wednesday": "Quarta",
            "Thursday": "Quinta", "Friday": "Sexta", "Saturday": "Sábado",
            "Sunday": "Domingo"
        }
        return translation.get(weekday, weekday)
    
    def _load_image(self, url, label):
        try:
            response = requests.get(url, stream=True)
            image = Image.open(io.BytesIO(response.content))
            photo = ImageTk.PhotoImage(image)
            label.config(image=photo)
            label.image = photo
        except Exception:
            label.config(text="Ícone não disponível")