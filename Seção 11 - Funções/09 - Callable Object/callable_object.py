#!python
'''
SUSTENIDO!/usr/local/bin/python3
'''

# Clacula uma potência especifica


class Potencia:
    # Construtor
    def __init__(self, expoente):
        self.expoente = expoente

    # Função que será chamada
    # quando usarmos o obj como uma função.
    def __call__(self, base):
        return base ** self.expoente


if __name__ == '__main__':
    # Neste momento chamamos os construtor
    # então definimos o expoente.
    quadrado = Potencia(2)
    cubo = Potencia(3)

    if callable(quadrado) and callable(cubo):
        # Na hora de chamar eu passo a base.
        print(f'3² => {quadrado(3)}')
        print(f'5³ => {cubo(5)}')
        # outra forma
        print(Potencia(4)(2))
        # (4) chama objeto - Construtor
        # (2) passa base - Call
