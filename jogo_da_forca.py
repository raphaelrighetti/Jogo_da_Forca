import random
import os
import platform
from time import sleep

palavras = ('amor', 'odio', 'felicidade', 'sentimento',
            'lobo', 'macaco', 'morango', 'pote',
            'sofrimento', 'saudade', 'jesus', 'diabo')

palavra_secreta = random.choice(palavras)
palavra_formatada_arr = []
letras_acertadas = []
letras_erradas = []

tentativas = 10

for l in palavra_secreta:
    palavra_formatada_arr.append('*')

dificuldade = int(input(
    'Escolha uma dificuldade de um a 3, onde 1 é a mais baixa e 3 a mais alta: '))

if dificuldade > 3 or dificuldade < 1:
    print('O número passado não estava dentro dos padrões, seguindo na dificuldade 2.')
    tentativas = 10
elif dificuldade == 1:
    tentativas = 15
elif dificuldade == 2:
    tentativas = 10
elif dificuldade == 3:
    tentativas = 7

os.system('cls' if platform.system() == 'Windows' else 'clear')

print('Para sair, digite "sair" ou aperte CTRL + C')

while True:
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print(f'Tentativas restantes: {tentativas}')
    print(''.join(palavra_formatada_arr))

    if tentativas < 1:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print('Você perdeu!')
        sleep(5)
        break

    letra = input('Digite uma letra: ')

    if letra.lower() == 'sair':
        break
    elif len(letra) > 1:
        print('Digite apenas uma letra!')
        sleep(1.5)
        continue
    elif not letra.isalpha():
        print('O script só aceita letras!')
        sleep(1.5)
        continue
    elif letra in letras_acertadas:
        print('Você já chutou essa letra.')
        sleep(1.5)
        continue
    elif letra in letras_erradas:

        tentativas -= 1
        print('Você já chutou essa letra (e errou).')
        sleep(1.5)
        continue

    os.system('cls' if platform.system() == 'Windows' else 'clear')

    if letra in palavra_secreta:
        letras_acertadas.append(letra)
    else:
        letras_erradas.append(letra)

    acertou = letra in palavra_secreta
    index = 0

    if not acertou:
        tentativas -= 1

    while index < len(palavra_formatada_arr):
        if palavra_formatada_arr[index] != '*':
            index += 1
            continue
        elif letra == palavra_secreta[index]:
            palavra_formatada_arr[index] = letra
        index += 1

    if ''.join(palavra_formatada_arr) == palavra_secreta:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print('Você venceu!')
        sleep(5)
        break
