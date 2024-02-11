import os
from modelos.restaurante import Restaurante
from modelos.bebida import Bebida
from modelos.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')

bebida_suco = Bebida('Suco de Melancia', 5.0,'grande')
bebida_suco.aplicar_desconto()

prato_paozinho = Prato('Paozinho',2.00,'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def exibir_banner():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n""")

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


def opcao_invalida():
    print('Opcao invalida\n')
    voltar_menu_principal()

def main():
    exibir_banner()
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()