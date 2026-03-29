# ================================================================
#   EXERCÍCIO 10
#
#   Crie um programa que peça ao usuário para digitar 10 números
#   inteiros, um por um. À medida que os números são digitados,
#   armazene os números pares em uma lista chamada (pares) e os
#   números ímpares em uma lista chamada (ímpares).
#   Após 10 digitações, o programa deve exibir:
#
#   1. A lista completa de números pares.
#   2. A lista completa de números ímpares.
#   3. A soma total de todos os números da lista de pares e a
#      soma dos números ímpares.
# ================================================================

pares   = []
impares = []

TOTAL = 10


print("=" * 48)
print(" SEPARADOR DE PARES E ÍMPARES")
print("=" * 48)
print(f"  Digite {TOTAL} números inteiros:\n")

for i in range(1, TOTAL + 1):
    while True:
        entrada = input(f"  {i:>2}º número: ").strip()
        try:
            numero = int(entrada)
            break
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

    if numero % 2 == 0:
        pares.append(numero)
        print(f"      → Par \n")
    else:
        impares.append(numero)
        print(f"      → Ímpar \n")


print("=" * 48)
print(" RESULTADOS")
print("=" * 48)

print(f"\n  1) Números pares ({len(pares)}):")
if pares:
    print(f"     {pares}")
else:
    print("     Nenhum número par digitado.")

print(f"\n  2) Números ímpares ({len(impares)}):")
if impares:
    print(f"     {impares}")
else:
    print("     Nenhum número ímpar digitado.")

print(f"\n  3) Somas:")
print(f"     Soma dos pares  : {sum(pares)}")
print(f"     Soma dos ímpares: {sum(impares)}")
print(f"     Soma total      : {sum(pares) + sum(impares)}")

print("=" * 48)