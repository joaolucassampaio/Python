""" Níveis de precedência aritméticos:
1. (n + n)
2. **
3. * / // %
4. + -
Numa expressão com operadores aritméticos de mesma precedência (por exemplo, multiplicação e divisão na mesma conta), a opereção 
será realizada da esquerda para direita (formato que o interpretador lê o código). """

conta_1 = 1 + 1 ** 5 + 5 #7
print(conta_1)

conta_2 = (1 + 1) ** (5 + 5) #1024
print(conta_2)
