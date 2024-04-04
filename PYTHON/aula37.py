# while/else
# recurso exclusivo do python e pouco utilizado
# Quando o laço (while) é executado totalmente, o else é executado.

string = 'Valor qualquer'
letra = ''
i = 0 # índice

while i < len(string): # quando o índice for menor que a qtd de caractere na variável string, entrar no while.
    letra = string[i] # o i representa o índice

    if letra == ' ': # caso encontre espaço, pare o programa
        break

    print(letra) # printa a letra
    i += 1 # soma +1 no índice
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')