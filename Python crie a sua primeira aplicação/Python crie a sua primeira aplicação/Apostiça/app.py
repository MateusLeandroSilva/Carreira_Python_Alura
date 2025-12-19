import os

restaurantes = ['Restaurante A','Restaurante B','Restaurante C']

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")


   # Funções de apoio

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal...')
    main()

def opcao_invalida():
    print('Opção inválida! Tente novamente!\n')
    voltar_ao_menu_principal()

def subtitulo(texto):
    os.system('cls')
    print(f'--- {texto} ---\n')


    #Funcões do menu
    
def cadastrar_restaurante():
    subtitulo('Cadastrar restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso!\n')
    voltar_ao_menu_principal()
    
def listar_restaurantes():
    subtitulo('Listar restaurantes')
    for restaurante in restaurantes:
        print(f'.{restaurante}')
    voltar_ao_menu_principal()

def finalizar_app():
    subtitulo('Aplicativo Finalizado')


    # Funções principais do app

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')
    
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
      
        if opcao_escolhida == 1: 
            cadastrar_restaurante()

        elif opcao_escolhida == 2: 
            listar_restaurantes()

        elif opcao_escolhida == 3: 
            print('Ativar restaurante')

        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

  
       

if __name__ == '__main__':
    main()