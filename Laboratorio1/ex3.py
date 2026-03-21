estoque = {

}

#Adicionar produto ao dicionário
estoque['Teclado'] = 150.0
estoque['Mouse'] = 80.0
estoque['Monitor'] = 900.0


print("------------LISTA DE ESTOQUE------------")
for produto, valor in estoque.items():
    print(f"{produto}: R${valor:.2f}")
    