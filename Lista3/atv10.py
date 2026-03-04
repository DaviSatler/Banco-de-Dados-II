#10) Dado a lista: projetos = ['Python', 'Java', 'PHP', ' ', 'C', None, 'Jscript', 'HTML', 'SQL', ' '], faça um programa que leia esta lista e informe a quantidade de cursos ausentes, encontrados e que estão sem nome.

projetos = ['Python', 'Java', 'PHP', ' ', 'C', None, 'Jscript', 'HTML', 'SQL', ' ']

encontrados = 0
ausentes = 0
sem_nome = 0

for projeto in projetos:
    if projeto is None:
        ausentes += 1
    elif projeto.strip() == "":
        sem_nome += 1
    else:
        encontrados += 1

print(f"Encontrados: {encontrados}")
print(f"Ausentes: {ausentes}")
print(f"Sem nome: {sem_nome}")