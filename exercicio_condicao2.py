"""Problema 2:
   Considere a empresa de telefonia Tchau. Abaixo de 200 minutos, a empresa cobra R$ 0,20
   por minuto. Entre 200 e 400 minutos, o preço
   é R$0,18. Acima de 400 minutos o preço por minuto é
   R$0,15. Calcule sua conta de telefone."""

minutos = int(input('Minutos: '))
conta = 0
if minutos <= 200:
    conta = minutos * 0.20
    print('Você é um cliente Bronze')
else:
    if minutos > 200 and minutos <= 400:
        conta = minutos * 0.18
        print('Você é um cliente Prata')
    else:
        conta = minutos * 0.15
        print('Você é um cliente Ouro')

print('O valor da conta é R$%5.2f' %conta)

#resolução do professor
min_ = int(input('Minutos utilizados: '))
if min_ < 200:
    preço = 0.20
else:
    if min_ <= 400:
        preço = 0.18
    else:
        preço = 0.15
print("Conta tlefônica: R$%6.2f" % (min_ * preço))