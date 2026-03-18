
reservas = []


print("----------MENU DE OPÇÕES----------")
print("1-Adicionar reserva")
print("2-Remover reserva")
print("3-Exibir reservas")
print("0-Sair")

while True:
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        nome = input("Digite o nome do cliente: ")
        data = input("Digite a data da reserva (DD/MM/AAAA): ")
        reservas.append((nome, data))
        print("Reserva adicionada com sucesso!")
    elif opcao == "2":
        nome = input("Digite o nome do cliente para remover a reserva: ")
        data = input("Digite a data da reserva para remover (DD/MM/AAAA): ")
        if (nome, data) in reservas:
            reservas.remove((nome, data))
            print("Reserva removida com sucesso!")
        else:
            print("Reserva não encontrada.")
    elif opcao == "3":
        if reservas:
            print("Reservas atuais:")
            for reserva in reservas:
                print(f"Cliente: {reserva[0]}, Data: {reserva[1]}")
        else:
            print("Nenhuma reserva encontrada.")
    elif opcao == "0":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")

