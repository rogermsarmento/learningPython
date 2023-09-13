# 1º Caso: IF e ELSE executado
# for i in range(1, 11):
#     if i == 6:
#     print(i)
# else:
#     print('Fim!')

# 2º Caso: O break impede a execução do ELSE
# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)
# else:
#     print('Fim!')

# Criar uma função que joga um dado de 1 a 6.
# Crie um for com rahge 1 a 6
# Se o numero for par e for igual ao sorteado
# pela funçãodado imprimir ACERTOU e depois chamar o break.
# Se não acertar chamar o else e imprimir NÃO ACERTOU
from random import randint


def sortear_dado():
    return randint(1, 6)


for i in range(1, 7):
    if i % 2 == 1:
        continue

    if sortear_dado() == i:
        print('ACERTOU', i)
        break
else:
    print('Não acertou o número!')
