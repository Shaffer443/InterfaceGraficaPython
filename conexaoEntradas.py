import mysql.connector
from mysql.connector import errorcode

# Criar a conexão com BD Entradas no servidor local
try:
    cnx = mysql.connector.connect(
        host="192.168.1.1",
        user="RafaelGouveia",
        password="rafa3241",
        database="entradas"
    )
    print(">>> Conexão estabelecida com sucesso! <<<\n")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Ocorreu um erro de acesso. Verifique o nome de usuário (user) ou senha (password).\n")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("O banco de dados (database) não existe ou não foi encontrado.\n")
    else:
        print(err)

# Executar consulta
def mostrarTudo():
    if cnx.is_connected():
        cursor = cnx.cursor()
        todosOsDados = "SELECT * FROM input"
        cursor.execute(todosOsDados)
        myresult = cursor.fetchall()

        # Exibir os resultados
        cont = 0
        for tuplas in myresult:
            print(cont, tuplas, sep="-")
            cont += 1

        cursor.close()
        cnx.close()

# Consulta via funções:

def totalRegsitros():
    if cnx.is_connected():
        cursor = cnx.cursor()
        todosOsDados = "SELECT count(*) FROM input where resultado"
        cursor.execute(todosOsDados)
        # myresult = cursor.fetchall()
        myresult = cursor.fetchone()
        print(f"Total de REGISTROS(tuplas): {int(myresult[0])}")

        cursor.close()
        cnx.close()

def totalRegsitrosGreen():
    if cnx.is_connected():
        cursor = cnx.cursor()
        todosOsDados = "SELECT count(*) FROM input where resultado='Green'"
        cursor.execute(todosOsDados)
        # myresult = cursor.fetchall()
        myresult = cursor.fetchone()
        print(f"Total de REGISTROS(tuplas) de GREEN: {int(myresult[0])}")
        # return print(f"Total de REGISTROS(tuplas) de GREEN: {int(myresult[0])}")
        cursor.close()
        cnx.close()

def totalRegsitrosRed():
    if cnx.is_connected():
        cursor = cnx.cursor()
        todosOsDados = "SELECT count(*) FROM input where resultado='Red'"
        cursor.execute(todosOsDados)
        # myresult = cursor.fetchall()
        myresult = cursor.fetchone()
        print(f"Total de REGISTROS(tuplas) de RED: {int(myresult[0])}")
        cursor.close()
        cnx.close()

def mediaRetornoOperacao():
    if cnx.is_connected():
        cursor = cnx.cursor()
        todosOsDados = "SELECT avg(valorDaOperacao) FROM input"
        cursor.execute(todosOsDados)
        myresult = cursor.fetchone()
        res = myresult[0]
        # print(type(res))
        print(f"Média de Retorno Operacional R$ ", end="")
        print(float(f"{res:.2f}"))
        # return print(f"Total de REGISTROS(tuplas) de GREEN: {int(myresult[0])}")
        cursor.close()
        cnx.close()

# Funções de validação:

def validaOpcao(numeroEscolhido):
    procurando = numeroEscolhido
    opcoes = (1,2,3,4,5)
    for busca in opcoes:
        if busca == procurando:
            # print(f"Elemento {procurando} está na TUPLA ")
            numero = procurando
            return numero
            # break
        # else:
        #     return False


# Chamada das funções:

# escolha = ''


print("\n")
print("""O que deseja analisar:

    1 - Mostrar Todas as Informações da tabela INPUT
    2 - Mostrar o total de registro na tabela INPUT
    3 - Mostrar Quantidade de Green's
    4 - Mostrar Quanitdades de Red's
    5 - Média de Ganhos Operacionais
    Fechar Sistema - 0 (zero) \n    """)

escolha = int(input(">>> "))

# for busca in opcoes:

if validaOpcao(escolha) == 1:
    mostrarTudo()
if validaOpcao(escolha) == 2:
    totalRegsitros()
if validaOpcao(escolha) == 3:
    totalRegsitrosGreen()
if validaOpcao(escolha) == 4:
    totalRegsitrosRed()
if validaOpcao(escolha) == 5:
    mediaRetornoOperacao()
else:
    if validaOpcao(escolha) != escolha:
        print("Número digitado inválido ou fora dos padrões")


# mostrarTudo()
# totalRegsitros()
# totalRegsitrosGreen()
# totalRegsitrosRed()
# escolha = int(input())
# validaOpcao(escolha)