# Exercício de programação - Cálculo do IMC (Índice de Massa Corpórea) + Ellipsis + f-strings

nome = 'João Lucas'
altura = 1.80
peso = 70
imc = (peso) / (altura ** 2)

#print('O paciente cujo nome é', nome, 'possui', altura, 'metros de altura, pesa' , 
    #  peso, 'quilos e o seu imc é:', imc)

if imc == 16.9:
    print('O paciente está muito abaixo do peso.')

elif 17 <= imc <= 18.4:
    print('O paciente está abaixo do peso.')

elif 18.5 <= imc <= 24.9:
    print('O paciente está no peso normal.')

elif 25 <= imc <= 29.9:
    print('O paciente está acima do peso.')

elif 30 <= imc <= 40:
    print('O paciente está obeso.')
    
# Ellipsis = ... (caso ainda não tenha pensado no valor da variável)
ellipsis = ...
print(...)

# Formatação de strings com o método f-strings (f=formatação) - Introdução breve
linha_1 = f'{nome} possui {altura:.2f} metros, {peso:.2f} quilos e'
linha_2 = f'o seu imc é {imc:.2f}'

print(linha_1)
print(linha_2)

# Para que serve as f-strings?
# Servem para o caso de escrever uma string (texto) numa variável e querer inserir valores.
# O que é :.2f? É utilizado para informar a quantidade de casas decimais (no exemplo, 2).