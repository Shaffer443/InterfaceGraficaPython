import tkinter as tk
from tkinter import ttk

def submit():
    value = entry.get()
    label_result.config(text=f"Valor inserido: {value}")

def mercado():
    value = combo_var.get()
    label_result.config(text=f"Valor inserido: {value}")




root = tk.Tk()
root.title("Exemplo de Input Types")

# Campo de Texto
entry = ttk.Entry(root)
entry.pack(pady=10)

# Botão
button = ttk.Button(root, text="Enviar", command=submit)
button.pack()

# Rótulo para exibir o resultado
label_result = ttk.Label(root, text="")
label_result.pack(pady=10)

# Caixa de Seleção
check_var = tk.IntVar()
check_button = ttk.Checkbutton(root, text="Opção", variable=check_var)
check_button.pack()

# Menu suspenso (Combobox)
combo_var = tk.StringVar()
combo = ttk.Combobox(root, textvariable=combo_var)
combo['values'] = ('Back Mandante', 'Back Visitante', 'Over 1,5')
combo.pack()

# Envio das opções e Escolhas
button2 = ttk.Button(root, text="Enviar", command=mercado)
button2.pack()

root.mainloop()
