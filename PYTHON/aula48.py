"""
Cuidados com tipos de dados mutáveis - list e copy
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

# valores imutáveis
nome = 'João'             
noutra_variavel = nome    # Caso você não crie outra variável que aponte para 'João', esse dado seria 'apagado da memória'.
nome = 'Lucas'            # Aqui você está fazendo a variável apontar para outra lugar da memória.
print(nome)
print(noutra_variavel)
"""Esse tipo de variável é imutável porque, caso você tente mudar algo nela acontecará um erro.
 Por exmeplo: nome = 'João'
              nome[1] = 'D' (erro)

"""

# copy e valores mutáveis
lista_a = ['João', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
"""Aqui você está copiando uma lista antes de alterá-la. Sendo assim, exibirá dois textos diferentes.
"""