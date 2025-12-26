# 1 -  Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
dados = [
         {'nome': 'Mateus', 'idade': 23, 'cidade': 'Fortaleza'},
         {'nome': 'Ana', 'idade': 17, 'cidade': 'Casa Branca'},
         {'nome': 'Livia', 'idade': 6, 'cidade': 'Vargem Grande Do Sul'}, 
        ]


# 2 - Utilizando o dicionário criado no item 1:. 

# Atualizando a idade de Livia
dados[0]['idade'] = 24
print(f'\n{dados}')

# Adicionando o campo profissão para Ana
dados[1]['profissao'] = 'Estudante'
print(f'\n{dados}')

# Removendo o campo cidade de Livia
del dados[2]['cidade']

# 3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(f'\n{numeros_quadrados}')

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
dados1 = {'nome': 'Carlos', 'idade': 30, 'cidade': 'São Paulo'}
if 'idade' in dados1:
    print(f"\nA chave 'idade' existe no dicionário com o valor: {dados1['idade']}")
else:
    print("\nA chave 'idade' não existe no dicionário.")

#5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
frase = "O rato roeu a roupa do rei de Roma"
palavras = frase.lower().split()   
frequencia_palavras = {}
for palavra in palavras:
    if palavra in frequencia_palavras:
        frequencia_palavras[palavra] += 1
    else:
        frequencia_palavras[palavra] = 1
print(f'\n{frequencia_palavras}')