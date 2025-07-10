import tkinter as tk

window = tk.Tk()
window.title("My First Tkinter App")
window.geometry("300x200")

label = tk.Label(window, text="Hello, Tejaswani!", font=("Arial", 16))
label.pack(pady=20)

button = tk.Button(window, text="Click Me", command=lambda: label.config(text="You clicked me!"))
button.pack()

window.mainloop()
