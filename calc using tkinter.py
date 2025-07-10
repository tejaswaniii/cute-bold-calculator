import tkinter as tk

# 🌈 Theme Setup
LIGHT = {
    "bg": "#fff5f8", "entry": "#fff", "button": "#ff80ab",
    "hover": "#ff4081", "result": "#ffe0f0", "text": "#000"
}

DARK = {
    "bg": "#2c2c2c", "entry": "#3b3b3b", "button": "#e91e63",
    "hover": "#ad1457", "result": "#4a4a4a", "text": "#fff"
}

theme = LIGHT

# 🧠 Smart Type Conversion
def convert_result(res):
    return int(res) if res == int(res) else round(res, 4)

# 🧮 Operation Logic
def calculate(op):
    try:
        a_raw = entry_a.get()
        b_raw = entry_b.get()
        a = float(a_raw)
        b = float(b_raw)

        if op == "add": r = a + b
        elif op == "sub": r = a - b
        elif op == "mul": r = a * b
        elif op == "div":
            if b == 0:
                result_var.set("❌ Can't divide by 0")
                return
            r = a / b

        smart = convert_result(r)
        result_var.set(smart)
        with open("result.txt", "w") as f:
            f.write(f"Result: {smart}")

    except ValueError:
        result_var.set("❌ Invalid Input")

# 🧹 Clear all
def clear_all():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    result_var.set("")

# 🌓 Theme toggle
def toggle_theme():
    global theme
    theme = DARK if theme == LIGHT else LIGHT
    apply_theme()

# 🎨 Apply styles
def apply_theme():
    window.configure(bg=theme["bg"])
    for widget in widgets:
        widget.configure(bg=theme["bg"], fg=theme["text"])
    for btn in buttons:
        btn.configure(bg=theme["button"], activebackground=theme["hover"], fg="#fff")
    for entry in [entry_a, entry_b, result_entry]:
        entry.configure(bg=theme["entry"], fg=theme["text"])
    result_entry.configure(bg=theme["result"], fg="#0277bd")

# 🌟 UI Setup
window = tk.Tk()
window.title("💗 Tejaswani's Cute + Bold Calculator")
window.geometry("400x430")
window.resizable(False, False)

font = ("Comic Sans MS", 12, "bold")
widgets, buttons = [], []

# Input Labels + Entries
lbl_a = tk.Label(window, text="Column A:", font=font)
lbl_b = tk.Label(window, text="Column B:", font=font)
widgets.extend([lbl_a, lbl_b])

entry_a = tk.Entry(window, font=font, justify="center")
entry_b = tk.Entry(window, font=font, justify="center")

lbl_a.grid(row=0, column=0, padx=10, pady=15, sticky="e")
entry_a.grid(row=0, column=1, padx=10, pady=15)
lbl_b.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_b.grid(row=1, column=1, padx=10, pady=5)

# Operation Buttons
ops = [("➕ Add", "add"), ("➖ Sub", "sub"), ("✖ Mul", "mul"), ("➗ Div", "div")]
for i, (txt, op) in enumerate(ops):
    btn = tk.Button(window, text=txt, font=font, width=14, command=lambda o=op: calculate(o))
    btn.grid(row=2+i//2, column=i%2, padx=10, pady=8)
    buttons.append(btn)

# Result Box
lbl_res = tk.Label(window, text="Result:", font=font)
widgets.append(lbl_res)
result_var = tk.StringVar()
result_entry = tk.Entry(window, textvariable=result_var, font=font, justify="center", state="readonly")
lbl_res.grid(row=4, column=0, padx=10, pady=20, sticky="e")
result_entry.grid(row=4, column=1, padx=10, pady=20)

# Bottom Buttons
btn_clear = tk.Button(window, text="🧹 Clear", font=font, width=14, command=clear_all)
btn_theme = tk.Button(window, text="🌓 Toggle Theme", font=font, width=14, command=toggle_theme)
btn_clear.grid(row=5, column=0, pady=10)
btn_theme.grid(row=5, column=1, pady=10)
buttons.extend([btn_clear, btn_theme])

# Footer
footer = tk.Label(window, text="Made with 💖 by Tejaswani", font=("Comic Sans MS", 10, "italic"))
footer.grid(row=6, column=0, columnspan=2, pady=8)
widgets.append(footer)

# Start
apply_theme()
window.mainloop()
