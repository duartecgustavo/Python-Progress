# Desafio 07 - Aula 7 : Programa que pegue as notas de um aluno e calcule a média.

nome = input('\033[35mOlá, digite ao lado seu nome\033[m: ')

n1 = float(input('Digite a sua nota de \033[4:36mPortuguês\033[m: '))
n2 = float(input('Digite a sua nota de \033[4:32mMatematicca\033[m: ' ))
n3 = float(input('Digite a sua note de \033[4:31mGeografia\033[m: '))

m = (n1+n2+n3)/3

print('\033[35m{}\033[m, baseado em sua \033[33mnotas\033[m, a sua \033[33mmédia\033[m é: \033[34m{:.1f}\033[m!'.format(nome, m))
