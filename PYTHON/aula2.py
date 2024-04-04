# A função print

'''
 É usada para exibir itens na tela através de um argumento. Existem dois tipos de argumentos, os nomeados
e os não nomeados.
 Os argumentos não nomeados serão aqueles a serem exibidos. Por exemplo:
'''
print(123) #123 É o argumento não nomeado.
print(123,456) # O uso da vírgula possibilita adicionar mais argumentos não nomeados.
'''
 Os argumentos nomeados são estruturas ativas que funcionam mesmo sem mencioná-los no código. Isso ocorre
porque são funções preexistentes, que estão apenas ocultas. Entre elas, o separador (sep) e a quebra de 
linha (/n).
'''
'''
 Você viu que ao utilizar a vírgula, os argumentos são separados. Não obstante, com o separador é possível 
mudar a simbologia da separação ao seu gosto, usando a seguinte estrutura:
'''
print(123,456, sep = "-")
print(123,456, sep = ' | ')
print(123,456,789, sep = " ? ")
print(123,456,789, sep = ' ESCOLHA UM ')
'''
 A quebra de linha é algo que acontece naturalmente com a função print, mas você pode optar por digitá-la
 manualmente. Ficaria dessa forma:
'''
print(123,456, end ='\n')