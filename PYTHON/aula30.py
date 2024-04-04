"""
REPETIÇÕES:
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira

Loop Infinito:
condicao = True

while condicao
    print(1)
    print(2)
    print(3)

Existem 2 formas de quebrar o looping do while. A primeira é usando break e a segunda é colocando
uma condição que torne o while False. Por exemplo:
"""
condicao = True
while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break #quebra o while

print('Acabou')


contador = 0
while contador <= 10: #quebra o while
    print(contador)
    contador = contador + 1

print('Acabou')