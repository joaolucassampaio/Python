"""
INTRODUÇÃO AO TRY/EXCEPT -
Tratamentos de erro:

Todo código recebido do usuário (input) deve ser tratado. Seja convertendo-o ou identificando algum erro.
Hoje, irei aprender a usar o try/expect para tratar esses dados recebidos.

Tratando o erro com Try e Except
Nesse caso o try é para que o Python tente executar aquele código e caso não consiga executar por conta de um
erro, ele vai retornar o que temos dentro do except. Dessa maneira você pode personalizar o que será mostrado
ao usuário ao invés de uma mensagem de erro grande que pode ser difícil de entender do que se trata.
"""

numero_str = input('Vou dobrar o número que vc digitar: ')

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# O "mesmo código" usando if ao invés try/except. Nesse caso, mostra uma mensagem de erro grande e de difícil 
# entendimento ao usuário.

if numero_str:
     numero_float = float(numero_str)
     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
else:
     print('Isso não é um número')