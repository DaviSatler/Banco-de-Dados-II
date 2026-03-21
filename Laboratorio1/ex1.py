

produtos ={
 'Produto A ': 300.0,
 'Produto B ': 80.0,
 'Produto C ': 60.0,
 'Produto D ': 200.0,
 'Produto E ': 250.0,
 'Produto F ': 30.0
}



#Soma produtos
soma_produtos = sum(produtos.values())
print(f"Soma dos produtos: {soma_produtos}")
print(f"O produto mais vendido foi: {max(produtos, key=produtos.get)}")