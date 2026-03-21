carrinho ={
'Item1': 50.0,
'Item2': 100.0,
'Item3': 20.0,
}


print("------------CARRINHO DE COMPRAS------------")
print("Itens no carrinho:")
for item, valor in carrinho.items():
    print(f"{item}: R${valor:.2f}")

    
print("De repente, o cliente decidiu remover o Item2 do carrinho.")
poped_item = carrinho.pop('Item2', None)

print(f"O item de valor R${poped_item:.2f} foi removido do carrinho.")

print("E, de repente, o cliente decidiu remover um item 4! Mas ele não existe no carrinho...")
poped_item = carrinho.pop('Item4', None)
if poped_item is None:
    print("O item solicitado não existe no carrinho.")
