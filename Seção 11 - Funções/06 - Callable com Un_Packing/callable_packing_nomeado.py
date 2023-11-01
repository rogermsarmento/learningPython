#!python
'''
SUSTENIDO!/usr/local/bin/python3
'''

'''
Vamos criar uma função que tem como objetivo 
pegar o preço de um produto e calcular o preço
final com um acresimo de um determinado imposto.

Contudo, essa função não sabe como calcular o imposto.
Quam calcula o imposto é outra função que tem seus 
proprios parâmetros.
'''


def calc_preco_final(preco_bruto, calc_imposto, **param):
    if callable(calc_imposto):
        return preco_bruto + preco_bruto * calc_imposto(**param)


'''
Com 2 ** dizemos que estamos passando um argumento nomeado.
Mas na verdade estamos passado 3 argumentos posicionais:
preco_final = calc_preco_final(preco_bruto, imposto_x, True)
preco_final = calc_preco_final(preco_final, imposto_y, True, 1.5)
Solução: nomear.

Com 2 ** estamos criando um dict e em cima deste dict ele faz
um packing de dicionario e a partir deste dict gerado ele ira
fazer um unpacking passando cada um dos args nomeados.
'''


def imposto_x(importado):
    return 0.22 if importado else 0.13


def imposto_y(explosivo, fator_mult=1):
    return 0.11 * fator_mult if explosivo else 0


if __name__ == '__main__':
    preco_bruto = 134.98
    preco_final = calc_preco_final(preco_bruto, imposto_x, importado=True)
    preco_final = calc_preco_final(
        preco_final, imposto_y, explosivo=True, fator_mult=1.5)
    print(f'Preço final R$ {preco_final}')


'''
Neste exemplo usamos tanto o fato de esta passando 
um callable e usamos também a capacidade de usar
os parâmetros variaveis.

Então passamos um série de parâmetros que foi feito
packing e unpacking.

preco_final = calc_preco_final(preco_final, imposto_y, True, 1.5)
neste momento passamos 2 parâmetros para a função calc_preco_final
doi feito o packing, ou seja, ele transformpou os dois em um tupla.

return preco_bruto + preco_bruto * calc_imposto(*param) neste momento
foi feito o unpacking, ou seja, tirando da tupla os dois parâmetros
para poder chamar essa função.

Se imposto_y recebe-se um tupla não precisariamos do * em param,
mas ele não recebe, ele recebe de fato 2 parâmetros. Então preciso
chamar a tupla dos dois prâmetros. 
'''
