# Código sem comentários
import os
palavra_secreta = 'camundongo'
palavra_digitada = ''
letra_digitada = '' 
letra_acertada = ''
letra_secreta = '' 
tentativas = 0

print('Vamos brincar de forca!')
while True: 
    letra_digitada = input('Digite uma letra: ') 
    tentativas += 1

    if letra_digitada.isdigit(): 
        print('Ops, você digitou um número! Por favor, digite uma letra.')
        continue

    if len(letra_digitada) > 1: 
        print('Digite apenas uma letra.')
        continue 

    if letra_digitada in palavra_secreta:
        letra_acertada += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta

        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', tentativas)
        letras_acertadas = ''
        tentativas = 0