# List Comprehesion

O _List Comprehesion_ oferece uma sintaxe mais curta quando você deseja criar uma nova lista com base nos valores de uma lista existente.

## Exemplo:

Com base em uma lista de frutas, deseja-se uma nova lista, contendo apenas as frutas com a letra “a” no nome.

Sem o _list comprehesion_ você terá que escrever uma fordeclaração com um teste condicional dentro:

```
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
```

Com a compreensão de listas você pode fazer tudo isso com apenas uma linha de código:

```
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
```