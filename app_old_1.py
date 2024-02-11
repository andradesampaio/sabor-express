import os
from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_praca.receber_avaliacao('Kayo', 4)
restaurante_praca.receber_avaliacao('Diego', 3)
restaurante_praca.receber_avaliacao('Sol', 1)

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Superma', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]


def exibir_banner():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('clear')
    print('Encerrando programa!\n')

def voltar_menu_principal():
    input('\nDigite uma tecla para voltar para menu principal ')  
    main()

def exibir_subtitulo(texto):
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()



def cadastrar_restaurante():

    '''Essa função é responsável por cadastrar um novo restaurante
    - Nome do restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante à lista de restaurantes

    '''

    exibir_subtitulo('Cadastro de novos restaurantes')
    nome = input('Digite o nome do restaurante que deseja casdatrar: ')

    categoria = input(f'Digite o nome da categoria do restaurante {nome}: ')
    dados_restaurante = {'nome': nome, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'Restaurante {nome} cadastrado com sucesso!\n')
    voltar_menu_principal()


def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    
    print('Nome do restaurante    |  Categoria           | Status\n')
      
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        status = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome.ljust(20)} | {categoria.ljust(20)} | {status}')

    voltar_menu_principal()  

def alternar_status_restaurante():
    exibir_subtitulo('Alterando status do Restaurante')
    nome_restaurante = input('Digite o nome de restaurante que deseja alterar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(f'{mensagem}')

    if not restaurante_encontrado:
        print('Restaurante nao encontrado')            

    voltar_menu_principal() 

def check_opcao_selecionada():
    try:
        opcao_escolhida = int(input('Escolha uma opcao: '))
        print(f'Você escolheu a opção: {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
            Restaurante.listar_restaurantes()
        elif opcao_escolhida == 3:
           alternar_status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()    
        
    except:
        opcao_invalida()

def opcao_invalida():
    print('Opcao invalida\n')
    voltar_menu_principal()


def main():
    os.system('clear')
    Restaurante.listar_restaurantes()
    exibir_banner()
    exibir_opcoes()
    check_opcao_selecionada()

if __name__ == '__main__':
    main()