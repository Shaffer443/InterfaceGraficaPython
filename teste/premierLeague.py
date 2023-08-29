# Objetivos:
# 1 - pegar os nomes dos times de acordo com o torneio selecionado

import tkinter as tk
from tkinter import ttk


#EXCLUIR ESTE ARQUIVO DEPOIS DE MEXER

root = tk.Tk()
root.title("Premier League")


times2023 = ('Arsenal', 'Aston Villa', 'Bournemouth', 'Brentford', 'Brighton & Hove Albion', 'Burley', 'Chealse',
            'Crystal Palace', 'Everton', 'Fulham', 'Liverpool', 'Luton Town', 'Manchester City', 'Manchester United',
            'Newcastle United', 'Nottingham Forest', 'Sheffield United', 'Tottenham Hotspur', 'West Ham United', 'Wolverhampton Wanderers')

def torneioTimes():
    valueTimeCasa = timeCasaPremierLeague.get()
    valueTimeVisitante = timeVisitantePremierLeague.get()
    label_result01.config(text=f"Torneio: Premier League\nTime da Casa: {valueTimeCasa}\nTime Visitante: {valueTimeVisitante}")

# Rótulo para exibir o resultado
label_result01 = ttk.Label(root, text="")
label_result01.pack(pady=10)

#Time Casa:
timeCasaPremierLeague = tk.StringVar()
casaPremierLeague = ttk.Combobox(root,textvariable=timeCasaPremierLeague)
casaPremierLeague['values'] = times2023
casaPremierLeague.pack()


#Time Visitante:
timeVisitantePremierLeague = tk.StringVar()
visitantePremierLeague = ttk.Combobox(root, textvariable=timeVisitantePremierLeague)
visitantePremierLeague['values'] = times2023
visitantePremierLeague.pack()


# Envio das opções e Escolhas
button2 = ttk.Button(root, text="OK", command=torneioTimes)
button2.pack()

root.mainloop()

