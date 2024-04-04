"""
range + for para usar intervalos de números:
For + Range
range -> range(start, stop, step)
"""
# start = começa
# stop = para a contagem
# step = conta pulando a quantidade do número digitado
# o step também serve para saber quais números são múltiplos de um determinado valor e também informa
# se os números são pares.
# Por exemplo, numeros = range (0, 100, 2) mostrará quais números de 0 a 100 são pares.

numeros = range(0, 100, 8) # mostrará quais números são múltiplos de 8

for numero in numeros:
    print(numero)

# Diferente do while o for já faz as iteraçãos automaticamente, sem precisar precisar somar +1.
