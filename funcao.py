# Criação de MYSQL:

def scriptInputJogoRedGreen(valor):
    string_float=float(valor)
    if string_float < 0:
        res = "Red"
        return res
    else:
        res ="Green"
        return res


def criacaoScriptMysql(data, torneio, mandante, visitante, operacao, oddsentrada, minentrada, oddssaida, minsaida, golscasa,golsvisitante,golscasa2tempo,golsvisitante2tempo,valoroperacao,retornooperacao ):

    script = ["insert into input values(default",
              data,
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
              valoroperacao,
              scriptInputJogoRedGreen(retornooperacao),
              retornooperacao,
              'default);']

    return script