import time
import os
import sys
from colorama import init, Fore, Style
import datetime 
import re


delay = 0.03




init()

def Continuar(): 
    cont = input("     Pressione qualquer tecla para continuar") 


def Animacao(texto, cor=Fore.WHITE):

    for letra in texto:

        print(cor + Style.BRIGHT + letra + Style.RESET_ALL, end='', flush=True)
        time.sleep(delay)
    print(Fore.RESET)


def boas_vindas():
    # Obtém a data e hora atuais

    # Imprime as mensagens
    
    global usuario 
    usuario = input('      Por favor, digite o seu nome!\n')
    
    return usuario


def Introducao():
    with open('introduçao.txt', 'r', encoding='utf-8') as intro:
        Animacao(intro.read())


def escolher_cenario(opcoes):
    """Lê a opção escolhida pelo usuário e retorna o número do cenário selecionado"""
    Animacao(f'\n\n     {usuario}, qual dos cenários deseja escolher?\n' , cor=Fore.YELLOW)
    while True:
        
        for chave, valor in opcoes.items():
            Animacao(f"     {chave} - {valor}\n\n", cor=Fore.YELLOW)

        try:
            cenario = int(input())
            if cenario not in opcoes:
                raise ValueError()
            if cenario == 2:
                Animacao('\n\nAté logo!', cor=Fore.RED)
                time.sleep(delay)
                sys.exit()
            elif cenario == 0:
                os.system('cls')
            else:
                os.system('cls')
                print(Fore.GREEN + Style.BRIGHT +
                      '\n\nVocê escolheu o cenário executando auxilio de profissionais terceirizados' + Style.RESET_ALL)
                Introducao()
                return cenario

        except ValueError:
            print(Fore.RED + Style.BRIGHT +
                  '\nOpção inválida. Digite um número válido.\n\n' + Style.RESET_ALL)


def MenuPrincipal(opcoes):

    while True:
        escolha = input(Fore.WHITE + Style.BRIGHT +
                        "\n\n\n        Pressione qualquer tecla para continuar. [M] para retornar ao Menu Principal. " + Style.RESET_ALL).upper()

        if escolha == 'M':
            os.system('cls')
            escolher_cenario(opcoes)

        else:
            return escolha


def obter_opcoes(var):

    while True:

        if var.isdigit() and int(var) in [1, 2]:
            return int(var)

        print(Fore.RED + Style.BRIGHT +
              "Opção inválida, digite novamente!" + Style.RESET_ALL)

        var = input('Escolha uma opção, 1 ou 2: \n\n')

    return var


def executar_cenario(cenario, opcoes):
    """Executa a ação correspondente ao cenário escolhido"""

    if cenario == 1:
        opcoesX = {

            1: 'Abraçar a inovação, mudando completamente o setor de Marketing e comunicação.',
            2: 'Fortalecer os processos já existentes, levando em conta os custos.'
        }

        opcoesY = {
            1: 'Intensificação das ações nas redes sociais',
            2: 'Pesquisa de satisfação no campus'
        }

        MenuPrincipal(opcoes)

        with open('escolhe_empresa.txt', 'r', encoding='utf-8') as escolha_empresa:
            Animacao(escolha_empresa.read())
            emp = input(f'        {usuario}, com qual empresa deseja negociar?\n\n(1) X\n\n(2) Y\n')

        emp = obter_opcoes(emp)

        if int(emp) == 1:
            with open('decisao_usuarioX.txt', 'r', encoding='utf-8') as dec:
                Animacao(dec.read())
                print(f'        {usuario}, pronto para decidir? ^^\n\n')


            for chave, valor in opcoesX.items():
                print(Fore.YELLOW + Style.BRIGHT +
                      f" {chave} - {valor}\n\n" + Style.RESET_ALL)

            decidir = input('Escolha a opção 1 ou 2:\n')

            decidido = obter_opcoes(decidir)

            if int(decidido) == 1:
                with open('decisao1x.txt', 'r', encoding='utf-8') as dec1:
                    Animacao(dec1.read())

                Continuar()
                PontinhosSuspense()

                with open('fim_decisao1x.txt', 'r', encoding='utf-8') as fim_decisaoX:
                    print(f'\n\n        {usuario},')
                    Animacao(fim_decisaoX.read(), Fore.RED)


            elif int(decidido) == 2:
                with open('decisao2x.txt', 'r', encoding='utf-8') as dec2:
                    Animacao(dec2.read())

                Continuar()
                
                with open('fim_decisao2x.txt', 'r', encoding='utf-8') as fim_decisao2x:
                    print(f'{usuario},')
                    Animacao(fim_decisao2x, cor=Fore.GREEN)

        elif int(emp) == 2:

            with open('empresaY.txt', 'r', encoding='utf-8') as escolhas_empresaY:
                Animacao(escolhas_empresaY)

            for k, v in opcoesY.items():
                print(Fore.YELLOW + Style.BRIGHT +
                      f'{k} - {v}\n\n' + Style.RESET_ALL)

            decidir = input(
                f'      {usuario}, decida a opção mais adequada, considerando tanto o contexto da instituição como o da empresa\ncontratada.')

            decidido = obter_opcoes(decidir)

            if int(decidir) == 1:
                with open('decisao1y.txt', 'r', encoding='utf-8') as decy1:
                    Animacao(decy1.read())

                  

            elif int(decidir) == 2:
                with open('decisao2y.txt', 'r', encoding='utf-8') as decy2:
                    Animacao(decy2.read())
                Continuar()
                with open('continuacao2y.txt', 'r', encoding='utf-8') as contin:
                    Animacao(contin.read())

            Continuar()
            print(f'{usuario},')    
            with open('final_decisaoY.txt','r', encoding='utf-8') as fim_decisaoY:
                    Animacao(fim_decisaoY.read(), cor=Fore.GREEN)

def PontinhosSuspense():
    for i in range(25):
        print('.', end=' ', flush=True)
        time.sleep(delay)


def cenarios():
    opcoes = {
        1: 'Terceirização no Cesurg',
        2: 'Para encerrar o programa'
    }

    cenario = escolher_cenario(opcoes)
    encerrar = executar_cenario(cenario, opcoes)

def final():
    
    while True:
        recomecar = input('Deseja recomecar?\n(1) Sim\n(2) Não\n')

        if recomecar == '1':
            os.system('cls')
            cena = cenarios()

        elif recomecar == '2':
            Animacao('Até logo!', cor=Fore.RED)
            break

        else:
            print(Fore.RED + Style.BRIGHT +
                'Opção inválida, digite novamente!' + Style.RESET_ALL)

if __name__ == '__main__':
    
    now = datetime.datetime.now()
    data = now.strftime('%d-%m-%Y')
    horas = now.strftime('%H:%M:%S')
    
    # Formata as mensagens
    print('\n\n')
    Animacao(f"         {'*' * 45}", cor=Fore.BLUE)
    Animacao(f'                         BEM VINDO !!', cor=Fore.GREEN) 
    Animacao(f"         {'*' * 45}", cor=Fore.YELLOW)
    with open ('boas_vindas.txt', 'r', encoding='utf-8') as bvv:
        Animacao(bvv.read())
    print(f'\n      Hoje é {data} e agora são {horas}'.center(80))
    boas_vindas()
    cenarios()
    final() 