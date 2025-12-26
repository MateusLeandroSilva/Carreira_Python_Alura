#Ferramentas de controle de fluxo: if, elif e else
import os
def titulo(texto):
    os.system('cls')
    print('=' * (len(texto) + 4))
    print(f'= {texto} =')
    print('=' * (len(texto) + 4))
def skip():
    os.system('pause')
    os.system('cls')
    print('Proxima Atividade! -->') 



# Monitorando vendas no comércio

titulo('Monitorando vendas no comércio')
maca = int(input('Digite a quantidade de maçãs vendidas: '))
banana = int(input('Digite a quantidade de bananas vendidas: '))

if maca > banana:
        print('Foram vendidas mais maçãs.')
elif maca == banana:
        print('A quantidade de maçãs e bananas vendidas foi igual.')
else:
        print('Foram vendidas mais bananas.')
skip()    



# Calculando o tempo total de projeto

titulo('Calculando o tempo total de projeto')
tarefaA = int(input('Digite a quantidade de horas gastas na tarefa A: '))
tarefaB = int(input('Digite a quantidade de horas gastas na tarefa B: ' ))
tarefaC = int(input('Digite a quantidade de horas gastas na tarefa C: '))   

tempo_total = tarefaA + tarefaB + tarefaC

if tempo_total > 0:
    print(f'O tempo total gasto no projeto foi de {tempo_total} horas.')
else:
    print('ERRO: Os dias não podem ser negativos.')
skip()


# Temperatura dos servidores

titulo('Temperatura dos servidores')
temperatura = int(input('Digite a temperatura atual do servidor em °C: '))

if temperatura <= 25:
    print('Temperatura normal.')
elif temperatura > 25:
    print('Alerta! Temperatura acima do limite permitido.')
skip() 



# Calculando o IMC

titulo('Calculando o IMC')
peso = float(input('Digite seu peso em kg: '))  
altura = float(input('Digite sua altura em metros: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal.')
elif imc >= 25 and imc < 30:
    print('Você está acima do peso ideal.')
else:
    print('Você está obeso.')
skip()



# Controlando o orçamento mensal

titulo('Controlando o orçamento mensal')
despesa = float(input('Digite sua receita mensal: R$ '))

if despesa > 3000:
    print('Atenção! Você ultrapassou o limite do orçamento.')
else:
    print('Seu orçamento está dentro do limite permitido.')
skip()



# Controle de acesso ao escritório

titulo('Controle de acesso ao escritório')
hora = int(input('Digite a hora atual (Formato 24 horas): '))

if hora >= 8 and hora <= 18:
    print('Acesso permitido. Bem-vindo ao escritório!')
else:
    print('Acesso negado. O escritório está fechado.')
    skip()



# Classificando estudantes por média

titulo('Classificando estudantes por média')
nota1 = float(input('Digite a primeira nota: '))    
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print('Aluno aprovado.')
elif media >= 5 and media < 7:
    print('Aluno em recuperação.')
else:
    print('Aluno reprovado.')
skip()



# Calculando pedágio

titulo('Calculando pedágio')
distancia = float(input('Digite a distância percorrida em km: '))

if distancia <= 100:
    print(f'O valor do pedágio é R$ 10,00.')
elif distancia > 100 and distancia <= 200:
    print(f'O valor do pedágio é R$ 20,00.')
else:
    print(f'O valor do pedágio é R$ 30,00.')
skip()



# Verificando a paridade de um número

titulo('Verificando a paridade de um número')
numero = int(input('Digite um número inteiro: '))

if numero % 2 == 0:
    print('O número é par.')
else:
    print('O número é ímpar.')
skip()



# Aprovando empréstimo

titulo('Aprovando empréstimo')
salario = float(input('Digite o valor do seu salário mensal: R$ '))
emprestimo = float(input('Digite o valor do empréstimo solicitado: R$ '))

if salario >= 2000 and emprestimo <= salario * 30:  
    print('Empréstimo aprovado.')
else:
    print('Empréstimo negado.')