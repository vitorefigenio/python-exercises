'''
	Faça um programa para uma loja de tintas. O programa
	deverá pedir o tamanho em metros quadrados da área a
	ser pintada. Considere que a cobertura de tinta é de
	1 litro para cada 3 metros quadrados e que a tinta
	é vendida em latas de 18 litros, que custam R$80,00.
	Informe ao usuário a quantidade de latas de tinta a
	a serem compradas e o preço total.

	Obs.: somente são vendidos um númeor inteiro de latas.
'''

metros = int(input('Quantidade de m² a ser pintados: '))
if metros % 54 != 0:
	latas = int(metros / 54) + 1
else:
	latas = metros / 54

valor = latas * 80

print('%d lata(s) a um custo de %.2f' %(latas, valor))