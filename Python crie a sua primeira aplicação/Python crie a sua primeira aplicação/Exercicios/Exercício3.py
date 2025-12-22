# Exercício 3: Loops em Python

#DEFs

def titulo(msg):
   print(f"----{msg}----")

# Listas
numeros = list(range(1, 10))
nomes = ["Clara", "Grazy", "Cida", "Livia"]
data_nasc = ["08/06/2006", "02/02/1990", "03/03/1970", "04/04/2015"]

# loop para exibir os números
print("\nNúmeros loop")
for num in numeros:
    print(num)

# loop para exibir os nomes 
print("\nNomes loop")
for nome in nomes:
    print(nome)

# loop para exibir as datas de nascimento
print("\nDatas de Nascimento loop") 
for data in data_nasc:
    print(data)

# Calculando a soma dos números impares
soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i   
    print(f"Soma parcial dos números ímpares: {soma_impares}")
    

# Loop dos números decrescentes
print("\nNúmeros decrescentes")
for i in range(10, 0, -1):
    print(i)

# tabela de multiplicação ded acordo com o número fornecido pelo usuário
num = int(input("\nDigite um número para ver sua tabela de multiplicação: "))
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")