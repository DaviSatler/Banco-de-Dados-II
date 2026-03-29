# ================================================================
#   EXERCÍCIO 9
#
#   O professor de uma disciplina tem uma lista com os nomes de
#   6 alunos. Ele precisa de um programa que, para cada nome na
#   lista, solicite a digitação de duas notas (Nota A e Nota B).
#
#   1) O programa deve calcular a média aritmética simples de
#      cada aluno.
#   2) Ao final, o programa deve exibir o nome do aluno, sua
#      média e se ele está:
#      - Aprovado    (média >= 7.0)
#      - Recuperação (média entre 4.5 e 5.5 — inclusive)
#      - Reprovado   (média < 4.5)
#
#   Dica: Use um laço for para percorrer a lista de nomes e
#   realizar os cálculos dentro do laço.
# ================================================================

alunos = ["Ana", "Bruno", "Carla", "Diego", "Elisa", "Felipe"]

resultados = []   


def ler_nota(prompt):
    while True:
        entrada = input(prompt).strip().replace(",", ".")
        try:
            nota = float(entrada)
            if 0.0 <= nota <= 10.0:
                return nota
            else:
                print(" Nota deve estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print(" Valor inválido. Digite um número (ex: 7.5).")

# ── Coleta de notas ──────────────────────────────────────────────

print("=" * 50)
print(" SISTEMA DE NOTAS — TURMA")
print("=" * 50)

for nome in alunos:
    print(f"\n  Aluno: {nome}")
    print(f"  {'─' * 30}")
    nota_a = ler_nota("    Nota A: ")
    nota_b = ler_nota("    Nota B: ")

    media = (nota_a + nota_b) / 2

    if media >= 7.0:
        situacao = "Aprovado"
    elif media >= 4.5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    resultados.append((nome, nota_a, nota_b, media, situacao))


print("\n\n" + "=" * 58)
print(" RELATÓRIO FINAL DA TURMA")
print("=" * 58)
print(f"  {'Aluno':<10} {'Nota A':>7} {'Nota B':>7} {'Média':>7}  {'Situação'}")
print(f"  {'─' * 10} {'─' * 7} {'─' * 7} {'─' * 7}  {'─' * 16}")

aprovados   = 0
recuperacao = 0
reprovados  = 0

for nome, nota_a, nota_b, media, situacao in resultados:
    print(f"  {nome:<10} {nota_a:>7.1f} {nota_b:>7.1f} {media:>7.1f}  {situacao}")
    if "Aprovado" in situacao:
        aprovados += 1
    elif "Recuperação" in situacao:
        recuperacao += 1
    else:
        reprovados += 1

print("=" * 58)
print(f"\n  RESUMO DA TURMA:")
print(f"Aprovados    : {aprovados}")
print(f"Recuperação  : {recuperacao}")
print(f"Reprovados   : {reprovados}")
media_turma = sum(m for _, _, _, m, _ in resultados) / len(resultados)
print(f"Média geral  : {media_turma:.1f}")
print("=" * 58)