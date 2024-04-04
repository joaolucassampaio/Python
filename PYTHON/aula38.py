# Esse código do professor ficou bem confuso, para entender melhor use o debugger.

frase = 'aaaooo'
i = 0 # variável índice
letra_atual = ''
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase): # quando o índice for menor que a qtd de caracteres da variável frase, entrar no while
    letra_atual = frase[i] # está iterando (partindo) a frase conforme o índice. Ou seja, escolhendo as letras.
 
    if letra_atual == ' ': # se a variável letra_atual for um espaço, faço o que estiver escrito abaixo.
        i += 1
        continue

    qtd_atual = frase.count(letra_atual) # conta quantas vezes a letra atual (do índice) apareceu.

    if qtd_apareceu_mais_vezes < qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)