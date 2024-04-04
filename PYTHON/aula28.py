# EXERCÍCIOS
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# Aqui foi feito um fast fail através de try e except.
# Na linha 11 ele tentará converter o que foi digitado para int
# e caso for uma letra ou número de ponto fluante, dará erro (jogando para o except).

num_str = input('Digite um número inteiro: ')

try:
    num_int = int(num_str)

    if (num_int % 2) == 0:
        print(f'{num_int} é um número par.')

    else:
        print(f'{num_int} é um número ímpar.')

except:
    print('Esse não é um número inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# Aqui foi feito um fast fail através de try e except.
# O programa busca saber apenas a hora do usuário, caso digite os minutos informará o erro.

horas = input('Que hora são? ')

try:
    horas_float = int(horas)

    if 0 <= horas_float <= 11:
        print('Bom dia!')

    elif 12 <= horas_float <= 17:
        print('Boa tarde!')

    elif 18 <= horas_float <= 23:
        print('Boa noite!')

except:
    print('Digite apenas a hora.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite o seu nome: ')
qtd_caracteres = len(nome)

if qtd_caracteres <= 4:
    print('O seu nome é curto.')

elif 5 <= qtd_caracteres <= 6:
    print('O seu nome é de tamanho normal.')

else:
    print('O seu nome é grande!')
