import tkinter as tk

def button_click():
    user_input = user_number.get()
    if user_input.isdigit():
        user_float = float(user_input)
        conversion_float = user_float * 1.609344
        float_round = round(conversion_float, 7)
        conversion.config(text=float_round)
    else:
        conversion.config(text="Enter a number...")


window = tk.Tk()
window.title("Brett Sports Miles to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=25, pady=25)

miles_label = tk.Label(text="miles", font=("Arial", 12))
miles_label.grid(column=2, row=0)
miles_label.config(pady=5)

eq_label = tk.Label(text="is equal to", font=("Arial", 12))
eq_label.grid(column=0, row=1)
eq_label.config(pady=10)

km_label = tk.Label(text="Km", font=("Arial", 12))
km_label.grid(column=2, row=1)

conversion = tk.Label(font=("Arial", 12, "bold"))
conversion.grid(column=1, row=1)
conversion.config(text="0")

# Button
button = tk.Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)

# Entry
user_number = tk.Entry(width=20)
user_number.grid(column=1, row=0)



window.mainloop()