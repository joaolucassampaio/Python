"""
Listas em Python - Parte 1
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
"""

# O tipo list se utiliza dos recursos índices e fatiamento:
# Entretanto, os índices são representados por variáveis e não pelos caracteres.
#        0    1      2              3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'João Lucas',  1.2, []]
print(lista[2])

# O que significa o tipo list ser mutável?
# Significa que o seu valor pode ser alterado durante o código. Diferentemente, o código string = 'ABCDE' que não pode.
lista = [123, True, 'João Lucas',  1.2, []]
lista[-3] = 'Maria'
print(lista[-3])

# O que significa suportar vários valores de qualquer tipo? Por exemplo:
# lista = [123, True, 'João Lucas',  1.2, []] - int, boolean, str, float e list

print(bool([]))  # lista vazia é considerada bool falsy
print(lista, type(lista))