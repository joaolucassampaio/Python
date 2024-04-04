# Introdução aos blocos de código + if / elif / else (condicionais)
# As condições possuem a capacidade de mudar o fluxo do código.
# Para isso, precisamos jogar o código dentro de um bloco, informando se será lido ou não.
# Essas condições são perguntas que retornam valores booleanos. Ou seja, True ou False.
# Dentre eles, alguns exemplos: if (se) / elif (se não se) / else (se não); que funcionam da seguinte maneira:
# if: caso a resposta for True, o interpretador irá ler o código abaixo;
# elif: caso o if for False, então interprador irá ler o código abaixo;
# e no caso de várias elif, o interpretador irá ler a que a resposta for True e ignorar o resto
# else: caso a resposta não seja nenhuma das duas acima, o interpretador irá ler o código abaixo;
# Além de que, eles respeitam uma hierarquia: sendo que elif e else não funcionam sem o if.

entrada = input('Você quer entrar ou sair? ')

if entrada == 'entrar':
    print('Você entrou no sistema.')

elif entrada == 'sair':
    print('Você saiu do sistema')

else: # Sempre a última opção.
    print('Você não digitou nem entrar nem sair')