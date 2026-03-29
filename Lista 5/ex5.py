# ================================================================
#   EXERCÍCIO 5
#
#   Você trabalha em uma empresa de realização de eventos
#   esportivos que irá realizar uma corrida na cidade. As
#   inscrições foram realizadas em locais diferentes e possuem
#   duas listas: uma com nome e idade e outra somente com o nome.
#   Você precisa padronizar as duas listas para depois juntá-las.
#
#   Primeiro, adicione uma idade aleatória entre 18 e 60 anos,
#   utilizando random.randint(18, 60), na lista
#   Participantes_lista_2, antes de adicioná-la à
#   Participantes_lista_1.
#
#   Após a inclusão, o programa deverá apresentar:
#   1) Os nomes de todos os participantes.
#   2) As idades de todos os participantes.
#   3) A média da idade dos participantes.
# ================================================================

import random

Participantes_lista_1 = {
    "Mariana": 25,
    "Carlos":  32,
    "Beatriz": 28,
    "Rafael":  35,
}

Participantes_lista_2 = [
    "Ana",     "Bruno",   "Caio",    "Daniela", "Eduardo",
    "Fernanda","Gabriel", "Helena",  "Igor",    "Julia",
    "Kevin",   "Larissa", "Miguel",  "Natália", "Otávio",
    "Paula",   "Ricardo", "Sabrina", "Tiago",   "Ursula",
    "Vitor",   "Wanessa", "Xavier",  "Yara",    "Zeca",
    "Arthur",
]


for nome in Participantes_lista_2:
    idade = random.randint(18, 60)
    Participantes_lista_1[nome] = idade


nomes  = list(Participantes_lista_1.keys())
idades = list(Participantes_lista_1.values())
media  = sum(idades) / len(idades)

print("=" * 50)
print("CORRIDA DA CIDADE — LISTA GERAL DE PARTICIPANTES")
print("=" * 50)

# 1) Nomes
print(f"\n1) NOMES DOS PARTICIPANTES ({len(nomes)} no total):")
print("   " + "─" * 45)
for i, nome in enumerate(nomes, start=1):
    print(f"   {i:>2}. {nome}")

# 2) Idades
print(f"\n2) IDADES DOS PARTICIPANTES:")
print("   " + "─" * 45)
for nome, idade in Participantes_lista_1.items():
    print(f"   {nome:<12} → {idade} anos")

# 3) Média
print(f"\n3) MÉDIA DE IDADE DOS PARTICIPANTES:")
print("   " + "─" * 45)
print(f"   Soma das idades : {sum(idades)}")
print(f"   Nº participantes: {len(idades)}")
print(f"   Média de idade  : {media:.1f} anos")
print("=" * 55)