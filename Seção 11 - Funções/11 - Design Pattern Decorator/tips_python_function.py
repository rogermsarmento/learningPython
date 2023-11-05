#!python
'''
SUSTENIDO!/usr/local/bin/python3
'''
# Uma função pode ter uma outra função interna!


def soma(a, b):
    def soma_c(c):
        return a + b + c
    return soma_c


soma_5 = soma(2, 3)
print(soma_5(50))
print(soma(1, 3)(5))
