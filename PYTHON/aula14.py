# Usando a função input para coletar dados do usuário
nome = input('Qual é o seu nome? ') # Pegou o dado do usuário e colocou na variável nome
print(f'O seu nome é {nome}') # f inseriu a variável na str
# O programa ficará parado até o usuário responder a pergunta
idade = input('Qual é a sua idade? ') # É bom sempre dar um espaço após a pergunta
print(f'A sua idade é {idade}')
# O valor adquirido pelo input sempre será uma str, por isso é importante saber as conversões através das
# técnicas de formatação. Por exemplo:
numero_1 = input('Digite um número: ') # Número será armazenado na varíavel numero_1 como uma str
numero_2 = input('Digite outro número: ') # Número será armazenado na varíavel numero_2 como uma str

int_numero_1 = int(numero_1) # A str numero_1 será convertida em int
int_numero_2 = int(numero_2) # A str numero_2 será convertida em int

print(f'A soma dos dois números é: {int_numero_1 + int_numero_2}')