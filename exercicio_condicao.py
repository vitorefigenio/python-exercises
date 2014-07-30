#Problema:
    #Pergunte a velocidade de um carro,
    #supondo um valor inteiro.
    #Caso ultrapsse 110 km/h, exiba uma mensagem dizendo
    #que o usuário foi multado.
    #Neste casso, exiba o valor da multa, cobrando
    #R$5,00, por km acima de 110.

# minha resolução do Problema
velocidade = int(input('Velocidade em Km: '))
if velocidade <= 110:
    print('Você está dentro da velocidade')
if velocidade > 110:
    valor = (velocidade - 110)*5
    print('Você foi multado em R$', valor,' e se ferrou!')

#resolução do Massa: youtube nome: TWP110 Else
v = int(input("Velocidade: "))
if v > 110:
    print('Você foi multado!')
    multa = (v-110)*5
    print ('Valor da multa: R$ %5.2f' %multa)
