# Criação dos diretórios

import os
import os.path
import dadosData



pastaAno = dadosData.anoAtual
pastaMes = dadosData.nomeDoMes
pastaDia = dadosData.dataHoje

# Pasta PAI:

def pastaPrincipal():
  if os.path.exists('Entradas'):
    print("\n")
    print('Diretório ENTRADA encontrado.....OK ')
    return True
  else:
    try:
      os.mkdir('Entradas')
      print('Diretório ENTRADA criado com sucesso.....OK')
      return True

    except:
      # print("Falha ao criar o diretório: 'Entradas' ")
      print("Falha ao encontrar ou criar o diretório 'Entradas'.....FALHOU ")
      return False


# Chamando a função para criar o diretório PAI - Principal:
pastaPrincipal()

# Verificação do diretório PAI "ENTRADAS":
os.chdir("Entradas") #diretorio da pasta PAI

# Criando  a pasta ANO dentro de Entradas:
if os.path.exists(f'{pastaAno}'):
  # print('Já existe a pasta - Entradas/Ano')
  print(f'Diretório ENTRADAS/{pastaAno}.....OK')
else:
  os.mkdir(f'{pastaAno}')
  # print('Precisei criar - Entradas/Ano')
  print(f'Diretório ENTRADAS/{pastaAno}.....Criado')

# Criando  a pasta MES dentro de Entradas/anoAtual:

if os.path.exists(f'{pastaAno}/{pastaMes}'):
  # print('Já existe a pasta - Entradas/Ano/Mês')
  print(f'Diretório ENTRADAS/{pastaAno}/{pastaMes}.....OK')
else:
  os.mkdir(f'{pastaAno}/{pastaMes}')
  # print('Precisei criar - Entradas/Ano/Mês')
  print(f'Diretório ENTRADAS/{pastaAno}/{pastaMes}.....Criada')

# Criando a pasta DATA do dia dentro de Entradas/anoAtual/mesAtual:

if os.path.exists(f'{pastaAno}/{pastaMes}/{pastaDia}'):
  # print('Já existe a pasta - Entradas/Ano/Mês/Dia')
  print(f'Diretório ENTRADAS/{pastaAno}/{pastaMes}/{pastaDia}.....OK')
else:
  os.mkdir(f'{pastaAno}/{pastaMes}/{pastaDia}')
  # print('Precisei criar - Entradas/Ano/Mês/Dia')
  print(f'Diretório ENTRADAS/{pastaAno}/{pastaMes}/{pastaDia}.....Criada')

# Relatorio das pastas
if os.path.exists(f'{pastaAno}/{pastaMes}/{pastaDia}'):
  print('Todos os diretórios criados com Sucesso.....OK')
  print("\n\n")
  statusDiretororio = True
else:
  print('Falha na criação de um ou mais diretórios.....Falha')
  print("\n\n")
  statusDiretororio = False
