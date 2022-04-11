maior_votacao = 0
dia_escolhido = 1

votos_seg = int(input("Digite o número de votos de segunda-feira: "))
votos_ter = int(input("Digite o número de votos de terça-feira: "))
votos_qua = int(input("Digite o número de votos de quarta-feira: "))
votos_qui = int(input("Digite o número de votos de quinta-feira: "))
votos_sex = int(input("Digite o número de votos de sexta-feira: "))

if votos_seg > maior_votacao:
    maior_votacao = votos_seg
    dia_escolhido = 'segunda-feira'

if votos_ter > maior_votacao:
    maior_votacao = votos_ter
    dia_escolhido = 'terça-feira'

if votos_qua > maior_votacao:
    maior_votacao = votos_qua
    dia_escolhido = 'quarta-feira'

if votos_qui > maior_votacao:
    maior_votacao = votos_qui
    dia_escolhido = 'quinta-feira'

if votos_sex > maior_votacao:
    maior_votacao = votos_sex
    dia_escolhido = 'sexta-feira'

print('O dia escolhido foi {}'.format(dia_escolhido))
print('Número de votos: {}'.format(maior_votacao))
