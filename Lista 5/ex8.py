# ================================================================
#   EXERCÍCIO 8
#
#   Você recebeu um dicionário chamado estoque_papelaria que
#   contém nomes de produtos como chaves e a quantidade
#   disponível como valores.
#
#   1) O programa deve solicitar ao usuário o nome de um produto.
#   2) Se o produto estiver no dicionário, verifique a quantidade:
#      a. Se for menor que 5, exiba:
#         "Produto [Nome] em nível crítico: apenas [Qtd] unidades!"
#      b. Caso contrário, exiba:
#         "Estoque em dia: [Qtd] unidades."
#      Se o produto não existir, exiba:
#      "Produto não cadastrado".
# ================================================================

estoque_papelaria = {
    "Caneta Azul":       12,
    "Caneta Vermelha":    3,
    "Lápis HB":           8,
    "Borracha":           2,
    "Régua 30cm":        15,
    "Tesoura":            4,
    "Cola Bastão":        1,
    "Caderno 100fls":     6,
    "Apontador":          9,
    "Corretivo":          0,
}

NIVEL_CRITICO = 5


print("=" * 50)
print("  CONSULTA DE ESTOQUE — PAPELARIA")
print("=" * 50)
print("\n  Produtos cadastrados:")
print(f"  {'─' * 38}")
for produto, qtd in estoque_papelaria.items():
    alerta = " " if qtd < NIVEL_CRITICO else ""
    print(f" {produto:<20} {qtd:>4} unidades{alerta}")
print(f"  {'─' * 38}")


while True:
    print()
    entrada = input("  Digite o nome do produto (ou 'sair' para encerrar):\n  > ").strip()



    if not entrada:
        print("   Entrada vazia. Digite o nome de um produto.")
        continue



    if entrada.lower() == "sair":
        print("\n  Encerrando a consulta. Até logo!")
        break



    produto_encontrado = None
    for chave in estoque_papelaria:
        if chave.lower() == entrada.lower():
            produto_encontrado = chave
            break

    print()
    if produto_encontrado:
        qtd = estoque_papelaria[produto_encontrado]
        if qtd < NIVEL_CRITICO:
            print(f" Produto {produto_encontrado} em nível crítico: apenas {qtd} unidades!")
        else:
            print(f" Estoque em dia: {qtd} unidades.")
    else:
        print(f" Produto não cadastrado.")

print("=" * 50)