'''
	Modifique o programa anterior para imprimir
	de 1 até o número digitado pelo usuário, mas
	dessa vez apenas os números ímpares.

	Reescreva o programa anterior para escrever
	os 10 primeiros múltiplos de 3



	Parei em
	https://www.youtube.com/watch?v=bnUiJhfgzHk&index=19&list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc
	1:19

'''
numero = int(input('(Mostra Impar) Digite um número: '))
x = 1
while x <= numero:
	while x % 2 != 0:
		print(x)
		x = x + 1	
	x = x + 1


numero = int(input('(/3) Digite um número: '))
x = 1
while x <= numero:
	while x % 3 == 0:
		print(x)
		x = x + 1	
	x = x + 1