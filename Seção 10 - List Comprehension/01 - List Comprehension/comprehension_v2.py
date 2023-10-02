#!python
'''
SUSTENIDO!/usr/local/bin/python3
'''

# Sem comprehension
list = []
for i in range(1, 11):
    if i % 2 == 0:
        list.append(i * 2)

print(list)

# com comprehension

doubros = [i * 2 for i in range(11) if i % 2 == 0]
print(doubros)
