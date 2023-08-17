# Dados Sobre a Data

import datetime
from datetime import date

# dataHoraAual = datetime.now()
dadosData = date.today()




# Achando o nome do mês atual:
nomeMes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outrubro', 'Novembro', 'Dezembro']
def pegandoMes(mes):
  numeroMes = int(mes)-1
  nome = nomeMes[numeroMes]
  # print(nome)
  return nome


# Tratando Data:
dataHoje = dadosData.day
mesAtual = dadosData.month
nomeDoMes = pegandoMes(mesAtual)
anoAtual = dadosData.year


# print(dadosData)
# print(dataHoje)
# print(mesAtual)
# print(pegandoMes(mesAtual))
# print(anoAtual)
# print(type(dadosData))


