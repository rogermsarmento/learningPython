'''
Como importar os mpodulo de mesmo nome?
'''
from pacote1 import modulo1
from pacote2 import modulo1 as modulo1_sub

print('Soma: ', modulo1.soma(1, 2))

print('Subtração: ', modulo1_sub.sub(3, 2))
