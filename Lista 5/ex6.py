# ================================================================
#   EXERCÍCIO 6
#
#   Você está organizando um workshop sobre tecnologia e precisa
#   de um programa que permita remover participantes que desistiram
#   do evento. O sistema armazena os participantes em um dicionário,
#   onde cada chave é o (nome) e o valor é o (nº de inscrição).
#   O programa deve ter um menu com as seguintes opções:
#   - Listar participantes
#   - Remover participante: solicita o nome, informa se está ou não
#     na lista e solicita confirmação antes de remover.
# ================================================================


participantes = {
    "Ana Lima":        1001,
    "Bruno Souza":     1002,
    "Carla Matos":     1003,
    "Diego Ferreira":  1004,
    "Elisa Nunes":     1005,
    "Felipe Rocha":    1006,
    "Gabriela Costa":  1007,
    "Henrique Alves":  1008,
    "Isabela Pires":   1009,
    "João Mendes":     1010,
}



def listar_participantes():
    print("\n PARTICIPANTES INSCRITOS ")
    if not participantes:
        print(" Nenhum participante na lista.")
        return
    print(f"  {'Nº':<6} {'Nome':<25} {'Inscrição':>10}")
    print(f"  {'─' * 6} {'─' * 25} {'─' * 10}")
    for i, (nome, inscricao) in enumerate(participantes.items(), start=1):
        print(f"  {i:<6} {nome:<25} {inscricao:>10}")
    print(f"\n  Total de inscritos: {len(participantes)}")


def remover_participante():
    print("\n REMOVER PARTICIPANTE")

    if not participantes:
        print(" Não há participantes para remover.")
        return

    nome = input("  Digite o nome do participante: ").strip()

    if not nome:
        print(" Nome não pode ser vazio.")
        return

    nome_encontrado = None
    for chave in participantes:
        if chave.lower() == nome.lower():
            nome_encontrado = chave
            break

    if not nome_encontrado:
        print(f"\n Participante '{nome}' não encontrado na lista.")
        print("     Verifique o nome e tente novamente.")
        return

    inscricao = participantes[nome_encontrado]
    print(f"\n  Participante encontrado:")
    print(f"     Nome      : {nome_encontrado}")
    print(f"     Inscrição : {inscricao}")
    print()

    confirmacao = input("  Confirma a remoção? (s/n): ").strip().lower()

    if confirmacao == "s":
        del participantes[nome_encontrado]
        print(f"\n'{nome_encontrado}' removido com sucesso!")
    elif confirmacao == "n":
        print(f"\n  Remoção cancelada. '{nome_encontrado}' permanece na lista.")
    else:
        print(" Opção inválida. Remoção cancelada.")


def sair():
    print(" Sistema encerrado.")



def exibir_menu():
    print("              WORKSHOP DE TECNOLOGIA                 ")
    print("           Gerenciamento de Participantes           ")
    print("    1 - Listar participantes                        ")
    print("    2 - Remover participante                        ")
    print("    0 - Sair                                        ")


def main():
    opcoes = {
        "1": listar_participantes,
        "2": remover_participante,
    }

    while True:
        exibir_menu()
        escolha = input("  Escolha uma opção: ").strip()

        if escolha == "0":
            sair()
            break
        elif escolha in opcoes:
            opcoes[escolha]()
        else:
            print(" Opção inválida. Digite 1, 2 ou 0.")

if __name__ == "__main__":
    main()