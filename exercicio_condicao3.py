#Modifique o programa da empresa Tchau para uma
#promoção onde a tarifa é de R$ 0,08 quando
#você utiliza mais do que 800 minutos

minutos = int(input("Minutos utilizados: "))
if minutos <= 200:
	conta = minutos * 0.20
else:
	if minutos <= 400:
		conta = minutos * 0.18
	else:
		if minutos > 800:
			conta = minutos * 0.15
		else:
			conta = 0.08
print('O valor da conta é R$%5.2f' %conta)

'''
	Professor \/\/\/
'''

minutos = int(input("(Massa) Minutos utilizados: "))

if minutos < 200:
	preço = 0.20
elif minutos <= 400:
	preço = 0.18
elif minutos <= 800:
	preço = 0.15
else:
	preço = 0.08
print("Conta telefônica: R$%6.2f" % (minutos * preço))