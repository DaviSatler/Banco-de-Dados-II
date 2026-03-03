def main():
	try:
		v2023 = float(input("Total de vendas em 2023: ").strip().replace(',', '.'))
		v2024 = float(input("Total de vendas em 2024: ").strip().replace(',', '.'))
	except ValueError:
		print("Entrada inválida. Use um número (ex: 12345.67).")
		return

	if v2023 == 0:
		print("Não é possível calcular o percentual: total de vendas em 2023 é zero.")
		return

	percentual = ((v2024 - v2023) / v2023) * 100

	if percentual > 0:
		status = "crescimento"
	elif percentual < 0:
		status = "decrescimento"
	else:
		status = "nenhum crescimento"

	print(f"Percentual: {percentual:.2f}% — {status}.")


if __name__ == "__main__":
	main()

