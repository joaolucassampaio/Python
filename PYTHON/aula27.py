"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None: # Caso não passar no if (condicao = False)
    print('Não passou no if')

#else:
#    print('Passou no if')

elif passou_no_if is True: # Caso passar no if (condicao = True)
    print('Passou no if')

# O que acontece nesse código é o seguinte:
# None é não valor, o que significa que a variável passou_no_if, inicialmente, não possui valor.
# O if lê dados em boolean e caso a variável declarada for False, o interpretador não lerá o código do if.
# Além de que, no caso do exemplo acima, pulará para a linha de código do else.
# Assim, podemos concluir que, se a variável condicao for True o código será lido pelo interpretador. 
# Dessa forma, considerando a condicao como True, passou_no_if recebe o valor True em if.
# Portanto, será printado 'Não passou no if' caso não passar no if e 'Passou no if' caso passar.

# Imagine o flag como fincar um bandeira no código e o None se a variável tiver ou não um valor
# a bandeira estará fincada ou não. Is e is not checam a identidade e a identidade é aquilo que está na
# memória.