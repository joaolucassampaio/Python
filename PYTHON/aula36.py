# Calculadora com While
# O while é usado para não deixar o programa "parado".

print('Calculadora em While')
while True: # O ciclo sempre acontecerá, a menos que aconteca um break ou uma situação que gere False.
    num1 = input('Digite um número: ') # Pega o número do usuário.
    num2 = input('Digite outro número: ') # Pega outro número do usuário.
    num1_float = 0 # Sempre que criar uma variável no meio do programa, indique ela no início.
    num2_float = 0 # Sempre que criar uma variável no meio do programa, indique ela no início.
    flag_num_valido = None # Isso é uma bandeira.

    try:
        num1_float = float(num1) # Converte o primeiro número em float.
        num2_float = float(num2) # Converte o segundo número em float.
        flag_num_valido = True # Caso os números conseguirem ser convertidos em float, a bandeira vira True.

    except:
        flag_num_valido = None # Caso digite algo que não possa ser convertido em float, a bandeira permanece None.

    if flag_num_valido == None: # Caso a bandeira for None, printará o que está escrito abaixo.
        print('Um ou ambos números digitados são inválidos, digite novamente.')
        continue # Retorna ao while caso as exigências do programa não forem atendidas.

    operador = input('Digite um operador (+-*/): ') # Pega o operador do usuário.
    operador_valido = '+-*/' # Indica quais operadores são válidos.
    

    if operador not in operador_valido: # Checa se o operador está dentro da literal do operador_valido.
        print('Operador inválido, digite novamente.')
        continue # Retorna ao while caso as exigências do programa não forem atendidas.

    if len(operador) > 1: # Checa se o usuário não digitou mais de um operador.
        print('Digite apenas um operador.')
        continue # Retorna ao while caso as exigências do programa não forem atendidas.

    print('Realizando a sua conta, confira o resultado abaixo:')

    if operador == '+': # Caso o usuário tenha digitado +, printará o que está escrito abaixo:
        print(f'{num1_float} + {num2_float} =', num1_float + num2_float) 
    # f-strings usadas para poder printar a variável como uma str.
    elif operador == '-': # Caso o usuário tenha digitado -, printará o que está escrito abaixo:
        print(f'{num1_float} - {num2_float} =', num1_float - num2_float)
    # , usada para separar a str da operação realizada.
    elif operador == '*': # Caso o usuário tenha digitado *, printará o que está escrito abaixo:
        print(f'{num1_float} * {num2_float} =', num1_float * num2_float)

    elif operador == '/': # Caso o usuário tenha digitado /, printará o que está escrito abaixo:
        print(f'{num1_float} / {num2_float} =', num1_float / num2_float)

    sair = input('Deseja sair? [S]im: ').lower().startswith('s') # .lower() coloca o que foi digitado em minúsculo.
    # .startwith('s') chega que o que foi digitado começa com s, responde em boolean.
    if sair is True: # Usa a resposta acima, em boolean, para checar a condição do if.
        break # Encerra o programa.


