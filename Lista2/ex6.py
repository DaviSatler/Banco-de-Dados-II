print("Do menor para o maior")

A = int(input("Digite o número A: "))
B = int(input("Digite o número B: "))
C = int(input("Digite o número C: "))

if A >= B and A >= C:
    maior = A
elif B >= A and B >= C:
    maior = B
else:
    maior = C

if A <= B and A <= C:
    menor = A
elif B <= A and B <= C:
    menor = B
else:
    menor = C

meio = A + B + C - maior - menor

print("Ordem crescente:", menor, meio, maior)