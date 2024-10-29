import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class TemperatureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weekly Temperature Input")
        
        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.entries = []

        # Create input fields for each day
        for day in self.days:
            label = tk.Label(root, text=f"Temperature for {day}:")
            label.pack()
            entry = tk.Entry(root)
            entry.pack()
            self.entries.append(entry)
        
        # Create a submit button
        submit_button = tk.Button(root, text="Submit", command=self.plot_temperature)
        submit_button.pack()

    def plot_temperature(self):
        temperatures = []
        for entry in self.entries:
            try:
                temp = float(entry.get())
                temperatures.append(temp)
            except ValueError:
                messagebox.showerror("Input Error", "Please enter valid numbers for temperatures.")
                return
        
        # Plotting the temperatures
        self.show_plot(temperatures)

    def show_plot(self, temperatures):
        plt.figure(figsize=(10, 5))
        plt.plot(self.days, temperatures, marker='o', color='blue', linestyle='-', linewidth=2, markersize=6)
        
        plt.title('Weekly Temperature Overview', fontsize=16)
        plt.xlabel('Days of the Week', fontsize=14)
        plt.ylabel('Temperature (°C)', fontsize=14)
        plt.xticks(rotation=45)
        plt.grid(True)
        
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureApp(root)
    root.mainloop()
