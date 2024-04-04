# Exercício de programação com if e comparação
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

float_primeiro_valor = float(primeiro_valor)
float_segundo_valor = float(segundo_valor)

if float_primeiro_valor >= float_segundo_valor:
    print(f'{float_primeiro_valor= } é maior ou igual ao {float_segundo_valor= }')

else:
    print(f'{float_segundo_valor= } é maior que {float_primeiro_valor= }')

"""
Observações:
Caso considerarmos o código abaixo para este exercício, teríamos alguns problemas. Por exemplo,
o terminal diria que 5 é maior que 10 e 7 maior do que 44.

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(f'{primeiro_valor= } é maior ou igual ao {segundo_valor= }')

else:
    print(f'{segundo_valor= } é maior que {primeiro_valor= }')


Por que isso acontece?
Porque estamos trabalhando com strings, em nenhum momento convertemos nada para números... Em string, 7 é maior que 44.
Isso funciona assim com strings:
Primeiro os dois primeiros caracteres são conferidos (7 e 4). Se eles forem diferentes, então a comparação é feita e o resultado é
retornado. Essa comparação usa o code point unicode do caractere para determinar qual é maior (a função built-in ord do python 
retorna esse code point). Ou seja, 7 é maior do que 4.
Agora, se os dois primeiros caracteres da string forem iguais, o próximo caractere de ambas será checado da mesma maneira.
"""