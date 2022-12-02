import random

palavras = ('amor', 'odio', 'felicidade', 'sentimento',
            'lobo', 'macaco', 'morango', 'pote')

palavra_secreta = random.choice(palavras)
palavra_formatada_arr = []

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

print('Para sair, digite "sair" ou aperte CTRL + C')

while True:
    if tentativas < 1:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')
    index = 0

    if letra.lower() == 'sair':
        break
    elif len(letra) > 1:
        print('Digite apenas uma letra!')
        continue
    elif not letra.isalpha():
        print('O script só aceita letras!')
        continue

    while index < len(palavra_formatada_arr):
        if palavra_formatada_arr[index] != '*':
            index += 1
            continue
        elif letra == palavra_secreta[index]:
            palavra_formatada_arr[index] = letra
        index += 1

    tentativas -= 1

    print(f'Tentativas restantes: {tentativas}')
    print(''.join(palavra_formatada_arr))

    if ''.join(palavra_formatada_arr) == palavra_secreta:
        print('Você venceu!')
        break
