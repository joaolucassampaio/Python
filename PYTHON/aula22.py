"""Fatiamento de strings e a função len:
 012345678 (índices +)
 Olá mundo (string)
-987654321 (índices -)"""

# Fatiamento [i:f:p] [::]
# Sendo que, i= ínicio; f= fim; p= passo(checagem/contagem de caracteres. Padrão =1. Ou seja,
# conta de 1 em 1).
variavel = 'Olá mundo'
print(variavel[0]) #Pega a variável no índice 0;
print(variavel[0:3]) #Fatia de 0 à 3;
print(variavel[:3])  #Obs: o 0 poder ser omitido;
print(variavel[4:9]) #Fatia de 4 à 9;
print(variavel[4:8]) #Obs: o interpretador nunca considera o valor final;
print(variavel[0:]) #Obs: pode-se omitir o final da string inteira.

# Função len
print(len(variavel)) #Indicade a quantidade de carácteres na str.
# Obs: o total de caracteres de "variavel" é 9 mas o índice vai até 8. Isso ocorre porque começamos o
# o índice no 0

print(variavel[0:9:2]) # Contando os carácteres de 2 em 2.
print(variavel[::-1]) # Conta ao contrário.


