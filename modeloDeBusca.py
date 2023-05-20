insert_into_values=('default','2023-05-06','Holanda - Eredivisie','Ajax','Az Alkmaar','Over 1,5',1.59,34,1.95,47,0,0,0,0,'default','Red',-0.20,'default')

elemento_buscado = []

my_list = [0, 3, 12, 8, 2]

print(type(insert_into_values[-2]))

# print('Holanda - Eredivisie' in insert_into_values)

# procurando = float(input("O que procura? "))
# print(f"{procurando}" in insert_into_values)

# print(5 not in )
# print(12 in my_list)

procurando = float(input("O que procura? "))

for busca in insert_into_values:
    # procurando = float(input("O que procura? "))
    # if procurando in insert_into_values == True:
    # if procurando == True:
    if busca == procurando:    
        print(f"Elemento {procurando} está na TUPLA ")
        elemento_buscado.append(procurando)
        break
    else:
        print("Elemento não encontrado...")
        
print(f"Lista  de intens buscados na Tupla: {elemento_buscado}", end="-")
