#Calculadora de economia 2.0
#MENU
print ('-+-+'*7)
print ('\033[4;32mCALCULADORA DE ECONOMIA v2.5\33[m')
print ('-+-+'*7)
#Variaveis
meta = float(input('Qual sua meta? R$'))
economizado = float(input('Já alcançado? R$'))
if economizado == 0:
    print('\33[31mInforme um valor maior que zero para calcular.\33[m')
guarda_mes = float(input('Quanto guarda por mês? R$'))
print('')
if guarda_mes == 0:
    print('\33[31mInforme um valor maior que zero para calcular o tempo.\33[m')
print('')
#Calcúlos
falta = meta - economizado
print ('Faltam:\33[1;31mR$ {:.3f}\33[m'.format(falta))
print('')
concluido = (economizado / meta) * 100
print ('Progresso:\n{:.0f}%'.format(concluido))
print('')
print ('Tempo estimado:')
if falta <=0:
    print('\33[1;35mParabéns! Você já atingiu sua meta\33[m.')
elif guarda_mes == 0:
    print('Não é possivel calcular o tempo.')
else:
    print('{:.0f} meses'.format((falta / guarda_mes)))
print('')
#condicoes
print ('Status:')
if concluido >= 100:
    print ('\33[34mParabéns você concluiu o seu objetivo!!\33[m.')
elif concluido >= 50:
    print('Falta tão pouco. \33[1;33mNão desista você já esta chegando no seu objetivo!!\33[m')
elif concluido == 0:
    print('Não é possivel calcular o tempo.')
else:
    print ('Ainda falta um pouco. \33[34mContinue\33[m!')