import tkinter as tk
from tkinter import ttk

root = tk.Tk()
def mercado():
    value = combo_var.get()
    # label_result.config(text=f"Valor inserido: {value}")
    # print(value)
    return value

# Rótulo para exibir o resultado
# pode não ser usado no main principal ou paroveitar o envio da escolha
# label_result = ttk.Label(root, text="")
# label_result.pack(pady=10)

# Menu suspenso (Combobox)
combo_var = tk.StringVar()
combo = ttk.Combobox(root, textvariable=combo_var)
combo['values'] = ('Back Mandante','Back Visitante','Back Empate','Lay Empate','Lay Mandante','Lay Visitante','Over 0,5 no 2º tempo','Over 1,5','Over 2,5','Over 3,5','Under 1,5','Under 2,5','Under 3,5')
combo.pack()


# Envio das Escolhas
button2 = ttk.Button(root, text="Enviar", command=mercado())
button2.pack()

root.mainloop()