'''
	Comentários de várias linahs com 3 aspas
	Faça um programa que leia três números e mostre o maior deles
'''
a = int(input("Numero 1: "))
b = int(input("Numero 2: "))
c = int(input("Numero 3: "))

if a >= b and a >= c:
	print('O maior é %d' %a)
elif b >= c:
	print('O maior é %d' %b)
else:
	print('O maior é %d' %c)