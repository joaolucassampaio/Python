"""
Listas em Python - Parte 2 (Alterando uma lista com índices, del, append e pop):
Métodos:
    append - Adiciona um item ao final
    pop - Remove do final ou do índice escolhido
    del - apaga um índice

Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#        0   1   2   3   4   5
lista = [10, 20, 30, 40]          # create
lista[2] = 300                    # update
del lista[3]                      # delete
print(lista)

#          0    1    2    3   4   5
lista2 = ['a', 'b', 'c', 'd']
lista2.pop()                      # remove o item no final da lista
lista2.append('e')                # adiciona ao final da lista
print(lista2)



"""
Observação: em uma lista grande, por exemplo: com mais de 1000 objetos, não é recomendado retirar(del) itens do meio dela,
porque isso exige muito processamento e pode deixar o programa lento. Isso ocorre porque o Python, quando você deleta algo,
precisa realocar os itens subsequentes para os índices anteriores, para preencher o índice do objeto que foi deletado. Por isso,
recomenda-se retirar apenas itens no final da lista. Por exemplo:
lista = [10, 20, 30, 40]
del lista[1]
Apagando o objeto no índice 1, o 20 passa a estar no 1 e a mesma lógica acontece para o resto dos números da lista.
"""