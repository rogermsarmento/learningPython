#!python
'''
SUSTENIDO!/usr/local/bin/python3
'''
# Queremos e precisamos usar uma lista como params padrão.


def fibonacci(sequencia=None):
    sequencia = sequencia or [0, 1]
    sequencia.append(sequencia[-1] + sequencia[-2])
    # nessa linha estamos alterando o valor default.
    return sequencia


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()
    print(restart, id(restart))
    assert restart == [0, 1, 1]
