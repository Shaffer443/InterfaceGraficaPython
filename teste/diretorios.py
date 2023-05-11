#Teste de criação de diretórios

import os
import os.path
from datetime import date
import datetime

today = date.today()

os.chdir("pastasParaTestes")

#os.chdir("b")


print(os.getcwd())

for a in os.listdir("."):
    if os.path.isdir(a):
        print(f"{a}/")
    elif os.path.isfile(a):
        print(a)

#criando pastas

if os.path.exists(f"{today}"):
    print("\n\nDiretórios já existente. Não foi criado")
    os.chdir(f"{today}")
    arquivo = open(f"{today}.txt", "a+")
    arquivo.write("Teste do arquivo diretorio.py")
    arquivo.close()
else:
    os.mkdir(f"{today}")
    print("\n\nDiretórios foi criado")
    os.chdir(f"{today}")
    arquivo = open(f"{today}.txt", "a+")
    arquivo.write("Teste do arquivo diretorio.py")
    arquivo.close()