
nomes_sujos = ["ana",
"pedro", "ANA", "marcos", "pedro",
"beatriz"]

nomes_limpos = set()
for nome in nomes_sujos:
    nomes_limpos.add(nome.capitalize())
print("Lista original (com erros):")
print(nomes_sujos)
print("\nLista final (sem duplicados e formatada):")
for nome in nomes_limpos:
    print(nome)

