from tkinter import simpledialog, messagebox
from models.weather_model import WeatherModel
from views.main_view import MainView

class WeatherController:
    def __init__(self, root):
        self.model = WeatherModel()
        self.view = MainView(root)
        
        self.view.change_city_btn.config(command=self.change_city)
        self.update_weather()
    
    def change_city(self):
        new_city = simpledialog.askstring("Trocar Cidade", "Digite o nome da cidade:")
        if new_city:
            try:
                current, _ = self.model.get_weather(new_city)
                self.view.update_city_label(current['name'], current['sys']['country'])
                self.update_weather(new_city)
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível obter dados:\n{str(e)}")
    
    def update_weather(self, city=None):
        try:
            current, forecast = self.model.get_weather(city)
            processed_forecast = self.model.process_forecast_data(forecast)
            
            self.view.update_city_label(current['name'], current['sys']['country'])
            self.view.current_weather.update(current)
            self.view.forecast.update(processed_forecast)
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível atualizar dados:\n{str(e)}")