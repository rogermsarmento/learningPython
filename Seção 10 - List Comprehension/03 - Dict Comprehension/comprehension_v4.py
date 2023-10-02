#!python
'''
SUSTENIDO!/usr/local/bin/python3
'''


dic = {i: i * 2 for i in range(10) if i % 2 == 0}
print(dic)

dic = {f'Item {i}': i * 2 for i in range(10) if i % 2 == 0}
print(dic)


for num, dobro in dic.items():
    print(f'{num} x 2 = {dobro}')
