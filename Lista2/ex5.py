refrigerante = float(input("Digite o preço do refrigerante: "))
cerveja = float(input("Digite o preço da cerveja: "))
agua = float(input("Digite o preço da água: "))

if refrigerante < cerveja and refrigerante < agua:
    print(f"O produto mais barato é o refrigerante, custando R$ {refrigerante:.2f}")
elif cerveja < refrigerante and cerveja < agua:
    print(f"O produto mais barato é a cerveja, custando R$ {cerveja:.2f}")
else:
    print(f"O produto mais barato é a água, custando R$ {agua:.2f}")