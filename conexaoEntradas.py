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


        cursor.close()
        cnx.close()
def totalRegsitrosGreen():
    if cnx.is_connected():
        cursor = cnx.cursor()
        todosOsDados = "SELECT count(*) FROM input where resultado='Red'"
        cursor.execute(todosOsDados)
        # myresult = cursor.fetchall()
        myresult = cursor.fetchone()
        print(f"Total de REGISTROS(tuplas) de RED: {int(myresult[0])}")


        cursor.close()
        cnx.close()


# Chamada das funções:

while True:
    print("\n")
    escolha = int(input("""O que deseja analisar:
                            1 - Mostrar Todas as Informações da tabela INPUT
                            2 - Mostrar o total de registro na tabela INPUT
                            3 - Mostrar Quantidade de Green's
                            4 - Mostrar Quanitdades de Red's
                            Fechar Sistema - sair | 0 | exit\n
                            """))
    if escolha == 1:
        mostrarTudo()
    if escolha == 2:
        totalRegsitros()
    if escolha == 3:
        totalRegsitrosGreen()
    if escolha == 4:
        totalRegsitrosGreen()
    else:
        if escolha == 0:
            print("Saindo do Sistema...\nBye")
            break
        else:
            print("Número digitado inválido ou fora dos padrões")
            continue

# mostrarTudo()
# totalRegsitros()