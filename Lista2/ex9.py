print("Descobre Triângulos - Informe os valores abaixo...")

A = int(input("Escreva o valor de A: "))
B = int(input("Escreva o valor de B: "))
C = int(input("Escreva o valor de C: "))


if A + B > C and A + C > B and B + C > A:
    
    print("Os valores podem formar um triângulo!")
    
    if A == B and B == C:
        print("Triângulo Equilátero")
    elif A == B or A == C or B == C:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")

else:
    print("Os valores NÃO podem formar um triângulo.")