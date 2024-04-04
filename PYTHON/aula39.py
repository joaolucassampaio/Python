# Exercícios
# O que o código abaixo exibiria na tela?

start = 0
end = 10
while start < end:
    print(start)
    start += 1

# O que o código abaixo exibiria na tela?

start = 0
end = 10
while start < end:
    start += 1
    print(start)

# O que o código abaixo exibiria na tela?

linhas = 2
colunas = 2
 
linha = 1
while linha <= linhas:
    coluna = 1
    while coluna <= colunas: # Se repete 2x enquanto o primeiro while 1x
        print(linha, coluna)
        coluna += 1
    linha += 1
