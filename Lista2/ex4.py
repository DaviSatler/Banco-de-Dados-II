valor2022 = float(input ("Qual foi o valor do carro no ano de 2022?"))
valor2023 = float(input ("Qual foi o valor do carro no ano de 2023?"))
valor2024 = float(input ("Qual foi o valor do carro no ano de 2024?"))

if valor2022 > valor2023 and valor2022 > valor2024:
    print(f"O maior valor foi o do ano de 2022, sendo: {valor2022}")
elif valor2023 > valor2022 and valor2023 > valor2024:
    print(f"O maior valor foi o do ano de 2023, sendo: {valor2023}")
else:
    print(f"O maior valor foi o do ano de 2024, sendo: {valor2024}")