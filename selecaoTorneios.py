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
combo['values'] = ('Alemanha Supertaça', 'Amistoso de Elite', 'Brasileiro Série A', 'Brasileiro Série B', 'Bundesliga Alemã',
                    'CONMEBOL Libertadores', 'Campeonato Brasileiro', 'Capa do Mundo da FIFA Feminino', 'Copa Do Brasil',
                    'Copa da Alemanha', 'Copa da Itália', 'Copa do Nordeste', 'Escócia - Premiership', 'Espanha La Liga',
                    'França ligue 1', 'Holanda - Eredivisie', 'Inglaterra Community Shield', 'Inglaterra Premier League',
                    'Itália - Série A', 'Itália Serie A', 'Liga Conferência Europa', 'Liga Profissional da Arábia Saudita',
                    'Portugal Supertaça', 'Portugal- Primeira Liga', 'Sul Americana', 'UEFA Champions League', 'UEFA Champions League',
                    'UEFA Euro Eliminatórias', 'UEFA Europa Conference League', 'UEFA Liga Das Nações', 'UEFA Liga Europa', 'UEFA Liga Europa',
                    'UEFA Liga dos Campeões Eliminatórias', 'UEFA Supertaça')
combo.pack()


# Envio das Escolhas
button2 = ttk.Button(root, text="Enviar", command=mercado())
button2.pack()

root.mainloop()