estoque_produtos1 = (
    "Arroz Agulhinh 5kg",
    "Feijão Carioca 1kg",
    "Macarrão Espaguete",
    "Azeite de Oliva Extra Virgem",
    "Café Torrado e Moído",  # está no estoque 1 e 2
    "Pão de Forma Integral",  # está no estoque 1 e 2
    "Biscoito Recheado Chocolate",
    "Maçã Gala (Unidade)",    # está no estoque 1 e 2
    "Banana Prata (Dúzia)",   # está no estoque 1 e 2
    "Suco de Laranja Integral" # está no estoque 1 e 2
)
estoque_produtos2 = (
    "Café Torrado e Moído",      # está no estoque 1 e 2
    "Pão de Forma Integral",     # está no estoque 1 e 2
    "Leite Integral UHT",
    "Iogurte Natural",
    "Peito de Frango Desossado",
    "Patinho Bovino Moído",
    "Maçã Gala (Unidade)",       # está no estoque 1 e 2
    "Banana Prata (Dúzia)",      # está no estoque 1 e 2
    "Suco de Laranja Integral",  # está no estoque 1 e 2
    "Queijo Mussarela Fatiado"
)

novo_estoque1 = set(estoque_produtos1)
novo_estoque2 = set(estoque_produtos2)

estoque_geral = novo_estoque1 & novo_estoque2


print("Produtos presentes em ambos os estoques:")
for produto in estoque_geral:
    print(produto)