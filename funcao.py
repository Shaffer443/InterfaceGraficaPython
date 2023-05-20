import sys
import time
import datetime
from datetime import date

today = date.today()
# Criação de MYSQL:

def scriptInputJogoRedGreen(valor):
    string_float=float(valor)
    if string_float < 0:
        res = "Red"
        return res
    else:
        res ="Green"
        return res

def padraoValorEntrada(valor_entrada=''):
    if valor_entrada == '0' or valor_entrada == '' or valor_entrada == 0:
        return 1.00
    else:
        return valor_entrada

def organizandoData():
    dt = datetime.datetime.now()
    go = dt.strftime("%Y-%m-%d")
    return go


def criacaoScriptMysql(torneio, mandante, visitante, operacao, oddsentrada, minentrada, oddssaida, minsaida, golscasa,golsvisitante,golscasa2tempo,golsvisitante2tempo,valoroperacao,retornooperacao ):

    script = ["insert into input values(default",
              organizandoData(),
              torneio,
              mandante,
              visitante,
              operacao,
              oddsentrada,
              minentrada,
              oddssaida,
              minsaida,
              golscasa,
              golsvisitante,
              golscasa2tempo,
              golsvisitante2tempo,
              padraoValorEntrada(valoroperacao),
              scriptInputJogoRedGreen(retornooperacao),
              retornooperacao,
              "default);"]
    # print(script)
    return script

# def fechandoTela(janela, tempo):
#         janela.after(tempo * 1000, lambda: janela.destroy())



# chamada para testes

# padraoValorEntrada()

# organizandoData()