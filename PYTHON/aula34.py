# Iterando strings com while

#       0123456789
nome = 'João Lucas'  # Iteráveis
#      10987654321

indice = 0
novo_nome = '' # variável vazia (foi criada para ser usada posteriormente, é uma str)
while indice < len(nome): # entrará no while caso o indice for menor que qtd de caracteres do nome (9)
    letra = nome[indice] # criou outra váriavel que pegará a letra fatiada do nome conforme o indice
    novo_nome += f'*{letra}' # f-strings servem para adc uma variável à uma str. Nesse caso,
                             # ele está adc * na variável letra (que é a letra selecionada pelo indice do nome)
    indice += 1

print(novo_nome)

