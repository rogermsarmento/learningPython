def imprimir(max, atual):
    if atual >= max:
        # Return sem valor é um tipo de comando
        # quando vc quer entrar sem retornar nada.
        return
    print(atual)
    imprimir(max, atual + 1)


def imprimir2(max, atual):
    if atual < max:
        print(atual)
        imprimir(max, atual + 1)
    return


imprimir(1000, 1)  # Cuidado com a condição de parada!
