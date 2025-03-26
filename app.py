import tkinter as tk
from controllers.weather_controller import WeatherController

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherController(root)
    root.mainloop()