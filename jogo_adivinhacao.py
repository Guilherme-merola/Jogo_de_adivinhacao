from random import randrange as rr


#jogo de adivinhação
def adivinhacao():
    """Função que gerará um número pseudoaleatório que será o alvo da adivinhação e com um input do usuário será verificado se ele digitou um número 
maior ou menor"""
    numero = rr(1, 101)

    while True:

        palpite = input('Adivinhe o número\n')

        try:
            palpite = int(palpite)

            if palpite > numero:
                print('Tente um número menor\n')

            elif palpite < numero:
                print('Tente um número maior\n')

            else:

                print('Parabéns! você acertou o número\n')
                break

        except ValueError:
            print('O valor deve ser um número\n')            


#looping infinito para rodar o jogo
while True:
    resposta = input('Digite "1" para jogar ou "0" para sair\n')

    if resposta == '1':
        adivinhacao()
    elif resposta == '0':
        print('Obrigado por jogar\n')
        break
    else:
        print('resposta invalida\n')
