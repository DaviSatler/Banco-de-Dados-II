print("---VERIFICAÇÃO DE PRODUTOS---")

#Criando uma lista de produtos
produtos = ["Arroz", "Feijão", "Óleo", "Sal"]
op = ""



while op != "0":
    print("Selecione uma opção para verificar: ")
    print("1 - Verificar se um produto está na lista")
    print("0- Sair")
    op = input("Digite a opção desejada: ")

    if op == "1":
        produto =input("Digite o nome do produto para verificar: ")
        if produto in produtos:
            print(f"O produto '{produto}' está na lista.")
        else:

            print(f"O produto '{produto}' não está na lista.")
    elif op == "0":
        print("Encerrando o programa.")
        break 