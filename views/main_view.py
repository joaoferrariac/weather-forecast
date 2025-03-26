import tkinter as tk
from views.components.current_weather import CurrentWeatherView
from views.components.forecast import ForecastView

class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Previsão do Tempo")
        self.root.geometry("600x500")
        
        self.create_header()
        self.current_weather = CurrentWeatherView(self.root)
        self.forecast = ForecastView(self.root)
    
    def create_header(self):
        header_frame = tk.Frame(self.root, padx=10, pady=10)
        header_frame.pack(fill=tk.X)
        
        self.city_label = tk.Label(header_frame, text="", font=("Arial", 16, "bold"))
        self.city_label.pack(side=tk.LEFT)
        
        self.change_city_btn = tk.Button(header_frame, text="Trocar Cidade")
        self.change_city_btn.pack(side=tk.RIGHT)
    
    def update_city_label(self, city, country):
        self.city_label.config(text=f"{city}, {country}")