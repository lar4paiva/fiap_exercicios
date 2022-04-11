soma_nota_impar = 0
soma_nota_par = 0
numero_de_alunos = 50

for i in range(1, numero_de_alunos, 2):
    print('VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS IMPARES')
    nota_aluno = float(input('POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: '.format(i)))
    soma_nota_impar = soma_nota_impar + nota_aluno

for i in range(0, numero_de_alunos, 2):
    print('VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES')
    nota_aluno = float(input('POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: '.format(i + 2)))
    soma_nota_par = soma_nota_par + nota_aluno

media_impar = soma_nota_impar / (numero_de_alunos/2)
media_par = soma_nota_par / (numero_de_alunos/2)

if media_impar > media_par:
    print('O conjunto de alunos de maior média foi o de alunos ímpares com média igual a {}.'.format(media_impar))
elif media_impar < media_par:
    print('O conjunto de alunos de maior média foi o de alunos pares com média igual a {}.'.format(media_par))
else:
    print('Ambas as turmas obtiveram média igual a {}.'.format(media_par))
