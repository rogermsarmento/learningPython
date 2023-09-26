#! python
# SUSTENIDO!/usr/local/bin/python3
from math import pi

raio = input('Informe o raio: ')
print('Área do círculo', pi * float(raio) ** 2)

# Pertence ao modulo main, ou seja, modulo main (Princial).
print('Nome do módulo', __name__)
print('Nome do pacote', __package__)  # Não pertece a nenhum pacote: None
