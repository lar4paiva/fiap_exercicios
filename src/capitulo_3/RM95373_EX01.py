plano = -1
bonus = 0
faturamento = 0
faturamento = float(input("Informe o faturamento do cliente: "))

print("Planos disponiveis:")
print("1 - Platinum")
print("2 - Gold")
print("3 - Silver")
print("4 - Basic")

while plano > 4 or plano < 1:
    plano = int(input("Selecione o plano do cliente: "))
    if plano > 4 or plano < 1:
        print("Por favor, selecione uma opção válida")
if plano == 1:
    bonus = 5
elif plano == 2:
    bonus = 10
elif plano == 3:
    bonus = 20
elif plano == 4:
    bonus = 30

print("O valor do bonus no plano é de: {} %".format(bonus))
print("O valor do bonus a ser pago é de: R$ {:.2f}".format(faturamento * (bonus / 100)))
