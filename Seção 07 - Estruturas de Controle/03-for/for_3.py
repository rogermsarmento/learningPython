# Percorrendo um Dicionário

produto = {'nome': 'Caneta Chic', 'preco': 14.99,
           'importada': True, 'estoque': 793}

# for chave in produto.keys: # Também funciona desta forma, poré, é redundante.
for chave in produto:
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(chave, '=', valor)

print(chave, valor)  # assim teremos l último valor disponivel pelo for!
