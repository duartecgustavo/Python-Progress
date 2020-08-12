# AULA 19 OYTHON - DICIONARIOS!

#DICIONARIOS SÃO MUITO ÚTEIS PARA ADD INDICES AS LISTAS

#EX:

lista = []
lista.append("Gustavo")
lista.append(25)

print(lista)

# Com os  DICIONARIOS eu posso coloar 'Gustavo' com o indice  de NOME e '25' com o indice de  IDADE.

# ABRINDO DICIONARIOS

#dicionario = dict()
dicionario = {'nome':'Gustavo','idade':'22','nome':'joão','idade':'25'} # o primeito parametrô incica o INDICE e o segundo seu conteúdo
# IMPORTANTE O USO DOS :

print(f'O {dicionario["nome"]} tem {dicionario["idade"]} anos.')

print(dicionario['nome'])
print(dicionario.values()) # vai me trazer os conteúdos
print(dicionario.keys()) # vai me trazer os indices
print(dicionario.items())# me trás todas as infos

# ADICIONANDO
# aqui não usamos o comando append e sim os próprios indices

dicionario['sexo'] = 'M' # automaticamente o Python irá criar um INDICE a mais no DICIONARIO e adicionara o que
# foi indicado dentro, no caso 'M'

# USANDO LAÇOS

for k, v in dicionario.items(): # funciona na mesma lógica do ENUMERATE, no entrando o primeiro parametro me trás o
                                # indice e o segundo o conteúdo
    print(f'O {k} é {v}')

for b in dicionario.values():
    print(f'{b}')

# DELETANDO ELEMENTOS

del dicionario['sexo'] # deleta o indicee e o conteúdo

estado = {}
brasil = []

for count in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Estado: '))
    brasil.append(estado.copy())
print(brasil)

for e in brasil:
    print(f'{e["sigla"]}')

#OUUUUU

for e in brasil:
    for indice, cont in estado.items():

        print(f'O campo {indice} tem {cont} como estado.')