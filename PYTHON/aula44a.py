"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = 'texugo'
palavra_digitada = '' # Flag ou variável vazia, significa que algum valor será atribuído depois.
letra_digitada = '' # Flag ou variável varia, significa que algum valor será atribuído depois.
letra_acertada = '' # Flag ou variável varia, significa que algum valor será atribuído depois. Após passar pelo while recebe um valor caso o usuário tenha acertado uma letra.
letra_secreta = '' # Flag ou variável vazia, significa que algum valor será atribuído depois. No laço de repetição, receberá as variáveis da iteração.
tentativas = 0

print('Vamos brincar de forca!')
while True: # Quando usado o True como condição para o while, o looping sempre acontecerá.
    letra_digitada = input('Digite uma letra: ') # Variável vazia recebe a função input que atribuirá valores str. O input printa um texto e recebe valores do usuário.
    tentativas += 1

    if letra_digitada.isdigit(): # Method isdigit() confere se a variável é um número.
        print('Ops, você digitou um número! Por favor, digite uma letra.')
        continue # Volta ao início do looping caso o usuário tenha digitado um número, recomeçando o programa.

    if len(letra_digitada) > 1: # A função len conta a quantidade de caracteres em uma string.
        print('Digite apenas uma letra.')
        continue # Volta ao início do looping caso o usuário tenha digitado mais de uma letra.

    if letra_digitada in palavra_secreta: # in confere se uma variável tem valores dentro de outra variável. No código ao lado, confere se a letra digitada está dentro da palavra secreta.
        letra_acertada += letra_digitada # Variável vazia é concatenada à letra digitada caso a letra digitada estiver na palavra secreta.

    palavra_formada = ''
    for letra_secreta in palavra_secreta: # for fará a iteração da palavra_secreta e colocará as variáveis, uma por uma, dentro da letra_secreta.
        if letra_secreta in letra_acertada: # caso uma dessas iterações esteja dentro da letra_acertada ele printará a letra_secreta
            palavra_formada += letra_secreta

        else: # mostrará * para as letras que não sejam a que ele acertou e caso ele não acerte nenhuma, mostrará * para todas as letras
            palavra_formada += '*'

    if palavra_formada == palavra_secreta:
        print('VOCÊ GANHOU, PARABÉNS!')
        print('A palavra era ', palavra_secreta)
        print('Tentativas: ', tentativas)
        break

    """ Resumo do if letra_digitada in palavra_secreta:
 Caso a letra_digitada esteja dentro da palavra_secreta o programa irá concatenar(acrescentar) a letra_digitada à variável vazia letra_digitada.
""" 

    """ Resumo do for letra_secreta in palavra_secreta:
o for fará a iteração da palavra_secreta (batata) e colocará as variáveis, uma por uma, dentro da letra_secreta. Ou seja, a letra_secreta será:
b
a
t
a
t
a
caso a letra_secreta estiver na letra_acertada (digitada pelo usuário) o programará printará, na ordem da iteração a letra acertada. Por exemplo, caso a letra acertada for 'a' ficará assim:
a
a
a
para preencher as lacunas e indicar que antes e depois dos 'a' tem letra foi usado o else printando * nos espaçamentos
"""
    """ Resumo do for letra_secreta in palavra_secreta:
a cada laço, o for colocará, letra por letra, da palavra_secreta na variável letra_secreta e verificará, letra por letra, se é igual
a letra digitada pelo usuário. Se ela for, somará (concatenação) à variável palavra_formada. Se não for, entrará no else e colocará um *
no lugar da letra não acertada. Isso ocorrerá em looping até o sistema terminar a iteração.
"""