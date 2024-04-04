# Interpolação de string com %
# O que é Interpolação? É parecida com o format e f-strings. Por exemplo:
# %s - string
# %d e %i - int
# %f - float
# .<número de dígitos>f
# %x e %X - HEXADECIMAL (ABCDEF0123456789)

nome = 'João'
preco = 1000.95897643
variavel = '%s, o preço é %.2f' %(nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500)) #X em CAPS 08 quantidades de casas.