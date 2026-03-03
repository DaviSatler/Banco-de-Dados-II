letra = input("Digite uma letra: ").lower()

if len(letra) == 1 and letra.isalpha():
    vogais = "aeiou"
    if letra in vogais:
        print(f"'{letra}' é uma vogal")
    else:
        print(f"'{letra}' é uma consoante")
else:
    print("Por favor, digite apenas uma letra válida")