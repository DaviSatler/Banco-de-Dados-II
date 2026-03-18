
pedidos = [
    "Hambúrguer",
    "Batata Frita",
    "Refrigerante",
    "Sorvete"
]
print("Lista de pedidos antes da remoção:")
for pedido in pedidos:
    print(pedido)
    
# Removendo o último elemento da lista
pedidos.pop()
print("\nLista de pedidos após a remoção do último elemento:")
for pedido in pedidos:
    print(pedido)


