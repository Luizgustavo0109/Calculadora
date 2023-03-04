import tkinter as tk

window = tk.Tk()
window.title("Calculadora")

# Frame do display
display_frame = tk.Frame(window)
display_frame.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
display = tk.Entry(display_frame, width=15, font=("Arial", 16))
display.pack(fill=tk.X, padx=5, pady=5)

# Atualiza o Display
def update_display(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(value))

# Realiza os calculos
def calculate():
    result = eval(display.get())
    display.delete(0, tk.END)
    display.insert(0, result)

number_buttons = []
for i in range(1, 10):
    button = tk.Button(window, text=str(i), width=5, height=2, command=lambda i=i: update_display(i))
    button.grid(row=(3 - (i-1)//3) + 1, column=(i-1)%3, padx=1, pady=1)
    number_buttons.append(button)

# Botão do zero
tk.Button(window, text="0", width=5, height=2, command=lambda: update_display("0")).grid(row=5, column=0, padx=1, pady=1)
# Cria as teclas para as operações
operator_buttons = []
operators = ["+", "-", "*"]
for i in range(len(operators)):
    button = tk.Button(window, text=operators[i], width=5, height=2, 
                       command=lambda i=i: update_display(operators[i]))
    button.grid(row=i+2, column=3, padx=1, pady=1)
    operator_buttons.append(button)
# Cria as teclas = . AC e +/-
tk.Button(window, text="=", width=5, height=2, command=calculate).grid(row=5, column=3, padx=1, pady=1)
tk.Button(window, text=".", width=5, height=2, command=lambda: update_display(".")).grid(row=5, column=2, padx=1, pady=1)
tk.Button(window, text="AC", width=5, height=1, command=lambda: display.delete(0, tk.END)).grid(row=1, column=3, padx=1, pady=1)
#tk.Button(window, text="+/-", width=5, height=2, command=lambda: update_display("-" + display.get())).grid(row=4, column=1, padx=1, pady=1)
tk.Button(window, text="/", width=5, height=2, command=lambda: update_display("/")).grid(row=5, column=1, padx=1, pady=1)

window.mainloop()