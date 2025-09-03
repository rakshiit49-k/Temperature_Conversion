import tkinter as tk
from tkinter import messagebox
window=tk.Tk()
window.title("temperature")
window.geometry("450x400")
window.configure(bg="#e6f0fa")
window.resizable(False,False)

def calculate(temp):
    faherenheit=9/5*temp+32
    return faherenheit

def calculate_gui():
    try:
        temp=float(entry1.get())
        a=calculate(temp)
        label3.config(text=f"The Temperature in Fahrenheit is :")
        label4.config(text=f"{a}")
    except ValueError:
        messagebox.showerror("Input error","please enter a valid temperature")

label1=tk.Label(window, text="Welcome to temperature conversion",
                font=("Arial",16,"bold"),
                bg="#d9dfe7",fg="#1e3a8a")
label1.pack(pady=10)

label2=tk.Label(window, text="Enter the temperature in degree Celcius :",
                font=("Arial",14,"bold"),fg="#ff5050")
label2.pack(pady=10)

entry1=tk.Entry(window, width=15,font=("Arial",14,"bold"))
entry1.pack(pady=15)

button1=tk.Button(window, text="Click here to calculate",command=calculate_gui,
                  font=("Arial",14,"bold"),bg="#2563eb",fg="#ffffff")
button1.pack(pady=10)

label3=tk.Label(window, text="",
                font=("Arial",14,"bold"),bg="#e0fc94",fg="black")
label3.pack(pady=10)

label4=tk.Label(window, text="",
                font=("Arial",14,"bold"),bg="#f3f16c",fg="black")
label4.pack(pady=10)

window.mainloop()