# pep8 diz que constantes devem ser criadas com indentificadores em caixa alta.

PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palavra proibida:', palavra)
            found = True
            break  # esse if not found não deixa o else ser executado.

    if not found:
        print('Texto autorizado:', texto)
