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

                                                                                                                                                                                                        #update1.2.3
def criacaoScriptMysql(torneio, mandante, visitante, operacao, oddsentrada, minentrada, oddssaida, minsaida, golscasa,golsvisitante,golscasa2tempo,golsvisitante2tempo,valoroperacao,retornooperacao,retornoPorcentagem):
    introTuplaMySQl = "insert into input values(default"
    finalTuplaMySQL = "default);"
    script = {'intro': introTuplaMySQl,
              'Data': organizandoData(),
              'Torneio': torneio,
              'Mandante': mandante,
              'Visitante': visitante,
              'Mercado': operacao,
              'Odds Entradas':oddsentrada,
              'Minuto da Entradas': minentrada,
              'Odds da Saida': oddssaida,
              'Minuto da Saida': minsaida,
              'Gols Casa no Primeiro Tempo': golscasa,
              'Gols Visitante no Primeiro Tempo': golsvisitante,
              'Gols Casa no Segundo Tempo ': golscasa2tempo,
              'Gols Visitante no Segundo Tempo': golsvisitante2tempo,
              'Valor em Dinheiro na Operação':padraoValorEntrada(valoroperacao),
              'Green ou Red':scriptInputJogoRedGreen(retornooperacao),
              'Lucro ou Prejuízo em dinheiro':retornooperacao,
              'Retorno da operação sobre a Stake':retornoPorcentagem,#update1.2.3
              'final': finalTuplaMySQL}

    scriptChaves = script.keys()
    scriptValores = script.values()

    # print(novoScript)
    # print(scriptChaves)


    textoScript = (f"{script['intro']}, "
                   f"'{script['Data']}', "
                   f"'{script['Torneio']}',"
                   f"'{script['Mandante']}',"
                   f"'{script['Visitante']}',"
                   f"'{script['Mercado']}',"
                   f"{script['Odds Entradas']},"
                   f"{script['Minuto da Entradas']},"
                   f"{script['Odds da Saida']},"
                   f"{script['Minuto da Saida']},"
                   f"{script['Gols Casa no Primeiro Tempo']},"
                   f"{script['Gols Visitante no Primeiro Tempo']},"
                   f"{script['Gols Casa no Segundo Tempo ']},"
                   f"{script['Gols Visitante no Segundo Tempo']},"
                   f"{script['Valor em Dinheiro na Operação']},"
                   f"'{script['Green ou Red']}',"
                   f"{script['Lucro ou Prejuízo em dinheiro']},"
                   f"{script['Retorno da operação sobre a Stake']},"
                   f"{script['final']}"
                   )

    print(scriptChaves) #informações no terminal
    print("\n")
    print(textoScript) #informações no terminal

    return textoScript

print("\n")

# def fechandoTela(janela, tempo):
#         janela.after(tempo * 1000, lambda: janela.destroy())



# chamada para testes

# padraoValorEntrada()

# organizandoData()

# criacaoScriptMysql('Brasileiro Série A', 'teste', 'teste', 'Over 1.5', 1.00, 31, 1.50, 50, 0,0,0,0,1.00, -0.01, -0.52 )

# porcentagemLucroPrejuizo(1.80,0.32)