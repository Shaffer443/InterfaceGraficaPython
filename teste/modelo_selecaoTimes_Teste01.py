# Objetivos:
# 1 - Selecionar Times de acordo com o Torneio. Tanto casa quanto visitante ser possiveis apenas se fizeram aprte do torneio alvo.

import tkinter as tk
from tkinter import ttk

#EXCLUIR ESTE ARQUIVO DEPOIS DE MEXER

# def submit():
#     value = torneio.get()
#     label_result.config(text=f"Valor inserido: {value}")
#     return torneioTimes(value)

times2023 = ('Arsenal', 'Aston Villa', 'Bournemouth', 'Brentford', 'Brighton & Hove Albion', 'Burley', 'Chealse',
            'Crystal Palace', 'Everton', 'Fulham', 'Liverpool', 'Luton Town', 'Manchester City', 'Manchester United',
            'Newcastle United', 'Nottingham Forest', 'Sheffield United', 'Tottenham Hotspur', 'West Ham United', 'Wolverhampton Wanderers')

def torneioTimes():
    valueTorneio = torneio.get()
    # if  dadosTorneio == 'Premier League':
    #     valueTimeCasa = timeCasaPremierLeague.get()
    #     valueTimeVisitante = timeVisitantePremierLeague.get()
    #     label_result.config(text=f"Torneio: {valueTorneio}\n Time da Casa: {valueTimeCasa} \n Time Visitante: {valueTimeVisitante}")
        # label_result.config(text=f"Torneio: {valueTorneio}")
    valueTimeCasa = timeCasaPremierLeague.get()
    valueTimeVisitante = timeVisitantePremierLeague.get()
    label_result.config(text=f"Torneio: {valueTorneio}\n Time da Casa: {valueTimeCasa} \n Time Visitante: {valueTimeVisitante}")



root = tk.Tk()
root.title("Testes - Seleçãod e Times | Update 1.2.2")

# Rótulo para exibir o resultado
label_result = ttk.Label(root, text="")
label_result.pack(pady=10)

# Menu suspenso (Combobox) - Torneio
torneio = tk.StringVar()
combo = ttk.Combobox(root, textvariable=torneio)
combo['values'] = ('Premier League', 'Bundesliga', 'Outros')
combo.pack()

# # Botão
# button = ttk.Button(root, text="Enviar", command=submit)
# button.pack()

#Time Casa:
timeCasaPremierLeague = tk.StringVar()
casaPremierLeague = ttk.Combobox(root, textvariable=timeCasaPremierLeague)
# if timeCasaPremierLeague == 'Premier League':
#     casaPremierLeague['values'] = times2023
casaPremierLeague['values'] = times2023
casaPremierLeague.pack()


#Time Visitante:
timeVisitantePremierLeague = tk.StringVar()
visitantePremierLeague = ttk.Combobox(root, textvariable=timeVisitantePremierLeague)
# if torneio.get() == 'Premier League':
#     visitantePremierLeague['values'] = times2023
visitantePremierLeague['values'] = times2023
visitantePremierLeague.pack()



# Envio das opções e Escolhas
button2 = ttk.Button(root, text="Enviar", command=torneioTimes)
button2.pack()

root.mainloop()