# 1) Uma editora de uma revista e deseja comparar
#dois artigos para identificar quais palavras aparecem em ambos. Sua tarefa é
#criar um programa que receba os dois textos e exiba um conjunto com as
#palavras comuns entre eles.
 
texto1 = """
O desenvolvimento de software moderno exige domínio absoluto sobre algoritmos
e estruturas de dados complexas. Python se destaca como uma ferramenta poderosa,
permitindo que desenvolvedores criem soluções eficientes para problemas reais
com código limpo.
"""
 
texto2 = """
Grandes desenvolvedores utilizam Python para resolver problemas complexos com
eficiência e elegância. O domínio sobre a linguagem permite a criação de software
de alto nível, transformando algoritmos em soluções reais que impactam o mundo moderno.
"""
 
def extrair_palavras(texto):
    import string
    palavras = texto.lower().split()
    palavras_limpas = set()
    
    for palavra in palavras:
        palavra_limpa = palavra.strip(string.punctuation)
        if palavra_limpa:
            palavras_limpas.add(palavra_limpa)
    return palavras_limpas
 
palavras_texto1 = extrair_palavras(texto1)
palavras_texto2 = extrair_palavras(texto2)
 
palavras_comuns = palavras_texto1 & palavras_texto2
 
print("=" * 50)
print("  EXERCÍCIO 1 — Palavras comuns entre os artigos")
print("=" * 50)
print(f"\nTotal de palavras únicas no Texto 1 : {len(palavras_texto1)}")
print(f"Total de palavras únicas no Texto 2 : {len(palavras_texto2)}")
print(f"\nPalavras em comum ({len(palavras_comuns)}):")
for palavra in sorted(palavras_comuns):
    print(f"  • {palavra}")
 
 
# Laura e Ana
# resolveram fazer compras juntas, mas criaram duas listas diferentes. Elas
# querem um programa que mostre:
#a)     
#Quais itens
#apareceram nas duas listas

#b)    
#Quais foram
#exclusivos de Laura

#c)     
#Quais foram
#exclusivos da Ana
 
lista_laura = {
    "Picanha", "Carvão", "Cerveja", "Refrigerante", "Pão de alho",
    "Queijo coalho", "Linguiça", "Asinha de frango", "Farofa", "Gelo",
    "Cebola", "Tomate", "Vinagre", "Sal", "Papel toalha"
}
 
lista_ana = {
    "Arroz", "Feijão", "Azeite", "Alface", "Banana", "Maçã",
    "Batata", "Ovos", "Leite", "Detergente",
    "Cebola", "Tomate", "Vinagre", "Sal", "Papel toalha"
}
 
itens_comuns        = lista_laura & lista_ana       
exclusivos_laura    = lista_laura - lista_ana       
exclusivos_ana      = lista_ana   - lista_laura     
 
print("\n" + "=" * 55)
print("  EXERCÍCIO 2 — Listas de compras")
print("=" * 55)
 
print(f"\na) Itens em comum ({len(itens_comuns)}):")
for item in sorted(itens_comuns):
    print(f"  • {item}")
 
print(f"\nb) Exclusivos da Laura ({len(exclusivos_laura)}):")
for item in sorted(exclusivos_laura):
    print(f"  • {item}")
 
print(f"\nc) Exclusivos da Ana ({len(exclusivos_ana)}):")
for item in sorted(exclusivos_ana):
    print(f"  • {item}")
 
