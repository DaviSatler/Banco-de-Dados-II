lista_voluntarios= []

op = ""

while op != "0" or op != "Sair":
    print("Selecione uma opção para verificar: ")
    print("1 - Inscrever novo voluntário")
    print("0- Sair")
    op = input("Digite a opção desejada: ")

    if op == "1":
        novo_voluntario = input("Digite o nome do novo voluntário: ")
        lista_voluntarios.append(novo_voluntario)
    elif op == "0":
        print("Encerrando o programa.")
        break 

print("Lista de voluntários inscritos:")
for voluntario in lista_voluntarios:
    print(voluntario)
