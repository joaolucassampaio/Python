"""
Listas em Python - Parte 3 (Inserindo itens em qualquer índice da lista com insert e limpando com clear):
Métodos:
    insert - Adiciona um item no índice escolhido
    clear - limpa a lista
    extend - estende a lista
    +     - concatena listas
"""

# insert
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.insert(0, 'João')      # insert é um method que precisa de 2 argumentos (o índice e o valor)
print(lista)

# clear
#          0    1    2    3    4
lista2 = ['a', 'b', 'c', 'd', 'e']
lista2.clear()
print(lista2)

# +
lista3 = [0, 1, 2, 3]
lista4 = [4, 5, 6, 7]
lista5 = lista3 + lista4        # concatenação
print(lista5)

# extend
lista6 = lista3.extend(lista4)
lista3.extend(lista4)          # "adicionou" a variável lista4 na lista3
print(lista6)                  # None
print(lista3)

# o extend muda permanentemente o valor da variável anunciada, sem retornar nada.
# Por isso, ao printar lista 6, o valor retornado é None, porque a variável mudada através do method extend foi a lista 3 e não 6.