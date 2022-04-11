minuto = int(input('Insira o valor dos minutos no relógio: '))

fatorial_dos_minutos = 1
for i in range(minuto):
    fatorial_dos_minutos = fatorial_dos_minutos * (i+1)

print('A senha para desbloqueio é: {}'.format('LIBERDADE' + str(fatorial_dos_minutos)))

