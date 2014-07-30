'''
	Exercício 1
	Imprima os número pares entre 0 e um
	número fornecido usando if
'''
numero = int(input('(1) Digite um número: '))
x = 0
while x <= numero:
	if x % 2 == 0:
		print(x)
	x = x + 1

'''
	Exercício 2
	Imprima os números pares entre 0 e um
	número fornecido sem utiliza o if
'''

numero = int(input('(2) Digite um número: '))
x = 0
while x <= numero:
	while x % 2 == 0:
		print(x)
		x = x + 1	
	x = x + 1

'''
	Resolução do Professor Massa 
'''
fim = int(input('Digite o último número: ')) 
x = 0
while x <= fim:
	print(x)
	x = x + 2