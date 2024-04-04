# Exercício calculadora
# Peça dois números e um operador ao usuário e faça a conta.

print('Seja-bem vindo a Calculadora do João!')
print('Digite dois números. ')
num_1 = input('Primeiro número: ')
num_1_int = float(num_1)
num_2 = input('Segundo número: ')
num_2_int = float(num_2)
operador = input('Você quer somar, subtrair, multiplicar'
                 ' ou dividir? ')

if operador == 'somar':
    somar = num_1_int + num_2_int
    print(somar)

elif operador == 'subtrair':
    subtrair = num_1_int - num_2_int
    print(subtrair)

elif operador == 'multiplicar':
    multiplicar = num_1_int * num_2_int
    print(multiplicar)

elif operador == 'dividir':
    dividir = num_1_int / num_2_int
    print(dividir)