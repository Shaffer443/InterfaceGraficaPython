# Objetivo: Escolher o torneio e abrir uma nova janela com os dados deste torneio selecionado
# Muitos BUGS


import tkinter as tk
from tkinter import ttk
# import premierLeague # Chamando essa importação antes de rodar o script - ATENÇÂO

premier = tk.Tk()
premier.title("Testes - Seleção de Torneio e Times| Update 1.2.2")

# fechandoTela(janela,5)
def fechandoTela(janela, tempo):
    janela.after(tempo * 1000, lambda: janela.destroy())
def mercado():
    value = combo_var.get()
    label_result.config(text=f"Torneio selecionado {value} ...")

    print("\nTorneio Selecionado: ", end=" ")
    print(value)

    if value == 'Premier League':
        premierLeague()
        fechandoTela(premier, 2)

    return fechandoTela(premier, 2)


# Rótulo para exibir o resultado
label_result = ttk.Label(premier, text="")
label_result.pack(pady=10)

# Menu suspenso (Combobox)
combo_var = tk.StringVar()
combo = ttk.Combobox(premier, textvariable=combo_var)
combo['values'] = ('Premier League', 'Bundesliga', 'Outros')
combo.pack()

# Envio das opções e Escolhas
button1 = ttk.Button(premier, text="Enviar", command=mercado)
button1.pack()

def premierLeague():
    import premierLeague
    fechandoTela(premier, 2)
    return premierLeague

premier.mainloop()