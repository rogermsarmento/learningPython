# pep8 diz que constantes devem ser criadas com indentificadores em caixa alta.

# Tupla = ()
# Set = {}

# Qual a diferença?

PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    # set(texto.lower().split()) - quebra o texto em palavras minusculas.
    if intersecao:  # if precisa de uma expressão que retorna V ou F.
        # Nesse caso o python consegue converte um conjunto vazio para FALSE.
        print('Texto possui palavras proibidas:', intersecao)
    else:
        print('Texto autorizado:', texto)
