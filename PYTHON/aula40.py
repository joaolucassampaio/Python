# INTRODUÇÃO AO FOR
# While é usado para quando você quer fazer uma repetição que NÃO tenha um limite estabelecido. 
# Já a função for serve para quando você quer fazer uma repetição que você já sabe o limite dela. 

# o for é uma estrutura de repetição usada em situações onde o limite é conhecido
# além de que, diferente do while, ele já faz iterações automaticamente

# while:
# senha_salva = '123456' # senha no "banco de dados".
# senha_digitada = '' # senha que será digitada pelo usuário.
# repeticoes = 0 # número de repetições que o usuário fará até acertar a senha
# while senha_salva != senha_digitada: # entrará em while caso a senha digitada for diferente da salva.
# Como a variável senha_digitada vale nada, incialmente, entrará da mesma forma.
#    senha_digitada = input(f'Sua senha ({repeticoes}x): ')
#    repeticoes += 1
# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas')

# for:
texto = 'Python'
novo_texto = ''

for letra in texto: # Tudo que o for quer receber aqui é um iterável
    # à cada laço o for vai colocando as variáveis da variável texto na variável letra, até terminar a iteração.
    print(letra) # desmontra a iteração e quantidade de laços necessárias (no caso, 6)
    novo_texto += f'*{letra}' # vai concatenar o * à cada letra que for iterada.
print(novo_texto) # demonstra, no final do looping, a concatenação das letras + o '*'