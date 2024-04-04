"""
Como o for funciona por baixo dos panos? (next, iter, iterável e iterador):
Iterável -> é o elemento que pode ser entregue um de cada vez. Por exemplo: str, range, etc
Iterador -> quem sabe entregar um valor por vez 
next -> chame o próximo valor
iter -> chame o seu iterador
"""

# __inter__() ou iter() => chama o iterator; aquele que mostra um valor por vez do iterável
# __next__() ou next() => pula pra o próximo valor do iterável

texto = 'Joao'  # iterável
iterador = iter(texto)  # iterator
# iter() é uma function que substituí o method __iter__()

print(iterador.__next__()) 
print(iterador.__next__())
print(iterador.__next__())
print(iterador.__next__())
# A quantidade de caracteres que deseja exibir terá que ser a mesma do method __next__()

# for letra in texto: *faz tudo que o while está fazendo acima com apenas essa linha de código
#     print(letra)
