programacao_evento = [
	"08:30 - Credenciamento",
	"09:00 - Keynote: Economia Global e Oportunidades",
	"10:30 - Estratégias de Inovação",
	"12:00 - Almoço",
	"14:00 - Workshop: Transformação Digital",
	"16:00 - O Futuro das Startups no Brasil",
	"18:00 - Coquetel de Encerramento"
]

horarios = []
atividades = []

for event in programacao_evento:
    horarios.append(event.split(" - ")[0])
    atividades.append(event.split(" - ")[1])

atividades.reverse()

nova_programacao = []
for i in range(len(atividades)):
    nova_programacao.append(f"{horarios[i]} - {atividades[i]}")

print("Programação do evento na ordem correta:")
for atividade in nova_programacao:
    print(atividade)