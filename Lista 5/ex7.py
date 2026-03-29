# ================================================================
#   EXERCÍCIO 7
#
#   Uma loja de eletrônicos deseja premiar os vendedores.
#   Crie um programa que armazene os nomes de 5 vendedores em uma
#   lista e seus respectivos totais de vendas em outra lista.
#
#   1) O programa deve percorrer as listas e identificar quem
#      vendeu mais de R$ 5.000,00.
#   2) Para esses vendedores, exiba o nome e calcule um bônus
#      de 10% sobre o valor das vendas.
#   3) Para os demais, exiba apenas o nome e a mensagem
#      "Meta não atingida".
# ================================================================


vendedores = ["Carlos", "Mariana", "Felipe", "Juliana", "Roberto"]

vendas     = [7200.00, 4800.00, 9500.00, 5100.00, 3200.00]

META   = 5000.00
BONUS  = 0.10

print("=" * 52)
print("  LOJA DE ELETRÔNICOS — RESULTADO DE VENDAS")
print("=" * 52)
print(f"  {'Vendedor':<12} {'Total Vendas':>14} {'Resultado'}")
print(f"  {'─' * 12} {'─' * 14} {'─' * 22}")

premiados = []

for i in range(len(vendedores)):
    nome  = vendedores[i]
    total = vendas[i]

    if total > META:
        bonus     = total * BONUS
        resultado = f"Bônus: R$ {bonus:>8.2f}"
        premiados.append((nome, total, bonus))
    else:
        resultado = "Meta não atingida"

    print(f"  {nome:<12} R$ {total:>11.2f}   {resultado}")


print("=" * 52)
print(f"\n RESUMO:")
print(f"  Meta de vendas  : R$ {META:,.2f}")
print(f"  Vendedores      : {len(vendedores)}")
print(f"  Premiados       : {len(premiados)}")
print(f"  Meta não atingida: {len(vendedores) - len(premiados)}")

if premiados:
    print(f"\n  🥇 VENDEDORES PREMIADOS:")
    print(f"  {'─' * 44}")
    for nome, total, bonus in premiados:
        print(f"  {nome:<12} → Vendas: R$ {total:>8.2f} | Bônus: R$ {bonus:.2f}")

print("=" * 52)