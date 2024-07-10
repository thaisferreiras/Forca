#Desenvolvimento de game V1
#import

import random
from os import system, name

#função para limpar a tela a cada execusão
def limpa_tela():

    #windows
    if name == 'nt':
        _=system('cls')

    #mac ou linux
    else:
        _=system('clear')

#função
def game():
    limpa_tela()
    print ("\n Bem vindo(a) ao jogo da forca!")
    print("Advinhe a palavra abaixo:\n")

#lista de palavras para o jogo
palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

#escolher uma palavra
palavra = random.choice(palavras)

#usar o list comprehension para incluir _ a cada letra da palavra escolhida
letras_descobertas = ['_' for letra in palavra]

#numero de tentativas
chances = 6

#lista para letras erradas
letras_erradas = []

#loop enquanto o numero de chances for maior do que zero
while chances > 0:
    print(" ".join(letras_descobertas))
    print("\nChances restantes:", chances)
    print("letras erradas", " ".join(letras_erradas))

    #tentativa
    tentativa = input("\nDigite uma letra: ").lower()

    #condicional
    if tentativa in palavra:
        index = 0
        for letra in palavra:
            if tentativa == letra:
                letras_descobertas[index] = letra
            index += 1
    else:
        chances -=1
        letras_erradas.append(tentativa)

    #condicional
    if "_" not in letras_descobertas:
        print("\nVocê venceu, a palavra era:", palavra)
        break

#condicional
if "_" in letras_descobertas:
    print("\nVocê perdeu, a palavra era:", palavra)

#bloco main
if __name__ == "__main__":
    game()
    print("\nParabens, você esta aprendendo programação em Python com a DSA. :)\n")



