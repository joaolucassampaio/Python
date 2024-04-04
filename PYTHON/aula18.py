"""
Na dúvida, copie e cole o código fora do comentário.
OPERADORES LÓGICOS: AND, OR E NOT.



OPERADOR LÓGICO 'AND':



1. Todas as condições PRECISAM ser VERDADEIRAS:

entrada = input('[E]ntrar ou [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Você entrou') 

else:
    print('Você saiu')

2. Se qualquer valor for avaliado como falso, a expressão inteira será falsa. Além de que, retornará o
valor falso em questão. Tipos de valores falsos (falsy):
0; 0.0; ''; False.

print(True and True and True) #True
print(True and False and True) #Falsy - False
print(True and 0 and True) #Falsy - 0

if 0 and 1: #0 Falsy, o interpretador não lerá o código e não printará nada.
    print(True and 1)

if 1 and 1: #1 Truelym, o interpretador lerá o código e printará False.
    print(True and 1 and False)


    
OPERADOR LÓGICO 'OR':



entrada = input('[E]ntrar ou [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Você entrou') 

else:
    print('Você saiu')

variavel_a = 1 or 0
variavel_b = 0 or 1
print(variavel_a, variavel_a) #Printará 1 1



OPERADOR LÓGICO 'NOT':



Usado para inverter expressões
not True = False
not False = True

print(not True)  # False
print(not False)  # True
"""