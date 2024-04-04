texto = 'João'
iterador = iter(texto) # iter() é uma function que substituí o method __iter__()

while True:
     try:
         letra = next(iterador) # next() é uma function que substituí o method __next__()
         print(letra)
     except StopIteration: # erro que aparece quando as letras da iteração acabam, usou-se o expect para evitar o erro
         break