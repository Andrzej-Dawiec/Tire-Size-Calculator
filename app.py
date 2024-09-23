import tkinter as tk
from tkinter import messagebox

def calculate_tire_size():
    try:
        width = float(entry_width.get())
        aspect_ratio = float(entry_aspect_ratio.get())
        wheel_diameter = float(entry_wheel_diameter.get())

        sidewall_height = (aspect_ratio / 100) * width
        tire_diameter = (2 * sidewall_height / 25.4) + wheel_diameter  # Convert mm to inches

        label_result.config(text=f"Tire Diameter: {tire_diameter:.2f} inches\n"
                                 f"Sidewall Height: {sidewall_height:.2f} mm")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create the main window
window = tk.Tk()
window.title("Tire Size Calculator")

# Create and place input fields
label_width = tk.Label(window, text="Tire Width (mm):")
label_width.pack()
entry_width = tk.Entry(window)
entry_width.pack()

label_aspect_ratio = tk.Label(window, text="Aspect Ratio (%):")
label_aspect_ratio.pack()
entry_aspect_ratio = tk.Entry(window)
entry_aspect_ratio.pack()

label_wheel_diameter = tk.Label(window, text="Wheel Diameter (inches):")
label_wheel_diameter.pack()
entry_wheel_diameter = tk.Entry(window)
entry_wheel_diameter.pack()

# Create and place a button
button_calculate = tk.Button(window, text="Calculate", command=calculate_tire_size)
button_calculate.pack()

# Create and place result label
label_result = tk.Label(window, text="")
label_result.pack()

# Run the main loop
window.mainloop()
