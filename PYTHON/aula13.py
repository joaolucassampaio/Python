# Formatação de strings com o método format
a = 'AAA'
b = 'BBB'
c = 2.20

formato1 = 'a={} b={} c={:.2f}'.format(a, b, c)
print(formato1)

string = 'a={} b={} c={}' # Os parênteses indicam a ordem do format. Sendo o primeiro = a...
formato2 = string.format(a, b, c)
print(formato2)

string = 'c={2} b={1} a={0}' # Caso queira reescrever sem seguir a ordem dos parênteses
formato3 = string.format(a, b, c) # Considere o primeiro = 0...
print(formato3)

string = 'a={nome1} b={nome2} c={nome3}' # Caso queira reescrever sem seguir a ordem dos parênteses
formato4 = string.format(nome1 = a, nome2 = b, nome3 = c) # Dê nomes
print(formato4)

# Usando format você pega uma variável qualquer e formata para string