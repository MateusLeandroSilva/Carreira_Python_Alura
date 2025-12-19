print("Verificador de numeros pares e ímpares")

def definir_numero():
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        print(f"O número {numero} é par.") 
    else:
        print(f"O número {numero} é ímpar.")   

def main():
        definir_numero()
    
if __name__ == "__main__":
        main()


        