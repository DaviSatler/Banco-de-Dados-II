nota_alunos = []

for i in range(10):
    nota = float(input(f'Digite a nota {i + 1}: '))
    nota_alunos.append(nota)

nota_alunos.sort(reverse=True)
print("Notas dos alunos em ordem decrescente:")
for nota in nota_alunos:
    print(nota)