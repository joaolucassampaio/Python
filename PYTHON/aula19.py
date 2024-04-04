# Operadores in (está entre) e not in (não está entre)
# Strings são iteráveis
#  0 1 2 3 (índices)
#  J o ã o
# -4-3-2-1
# nome = 'João'
# print(nome[2]) #ã  -pega a variável no índice 2
# print(nome[-4]) #J -pega a variável no índice -4
# print('ão' in nome) #True
# print('zero' in nome) #False
# print('ão' not in nome) #False
# print('zero' not in nome) #True

# cada str tem um índice, que serve para o interpretador se guiar nos caracteres, podendo ser
# positivos (começando do 0) ou negativos.

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')