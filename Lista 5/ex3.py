# ============================================================
#   EXERCÍCIO 3
#
#   O gerente de projetos do seu departamento precisa
#   consolidar as listas de tarefas de duas equipes distintas
#   equipe A e equipe B. Após unir as listas, você precisa
#   remover uma tarefa específica que foi informada pelo
#   usuário. Sua tarefa é criar um programa que realize estas
#   operações. Valide as entradas e informe caso a tarefa não
#   seja encontrada.
# ============================================================
#   CONSOLIDADOR DE TAREFAS — Equipe A + Equipe B
# ============================================================


tarefas_equipe_a = [
    "Levantar requisitos do cliente",
    "Criar protótipo da interface",
    "Desenvolver módulo de login",
    "Revisar documentação técnica",
    "Configurar ambiente de homologação",
]

tarefas_equipe_b = [
    "Elaborar plano de testes",
    "Executar testes de integração",
    "Corrigir bugs reportados",
    "Atualizar manual do usuário",
    "Apresentar relatório ao gerente",
]


def exibir_tarefas(lista, titulo):
    print(f"\n  {'─' * 44}")
    print(f"  {titulo}")
    print(f"  {'─' * 44}")
    if not lista:
        print(" Nenhuma tarefa na lista.")
    else:
        for i, tarefa in enumerate(lista, start=1):
            print(f"  {i:>2}. {tarefa}")


def consolidar_tarefas(lista_a, lista_b):
    consolidada = lista_a.copy()
    for tarefa in lista_b:
        if tarefa not in consolidada:
            consolidada.append(tarefa)
    return consolidada


def remover_tarefa(lista, nome_tarefa):
    termo = nome_tarefa.strip().lower()
    for tarefa in lista:
        if tarefa.strip().lower() == termo:
            lista.remove(tarefa)
            return lista, tarefa
    return lista, None


def main():
    print("\n" + "=" * 50)
    print("   GERENCIADOR DE TAREFAS — Consolidação de Equipes")
    print("=" * 50)



    exibir_tarefas(tarefas_equipe_a, "Tarefas — Equipe A")
    exibir_tarefas(tarefas_equipe_b, "Tarefas — Equipe B")



    lista_consolidada = consolidar_tarefas(tarefas_equipe_a, tarefas_equipe_b)

    print("\n" + "=" * 50)
    print("Listas consolidadas com sucesso!")
    exibir_tarefas(lista_consolidada, f"Lista Consolidada ({len(lista_consolidada)} tarefas)")


    print("\n" + "=" * 50)
    print("REMOÇÃO DE TAREFA")
    print("=" * 50)

    while True:
        print()
        entrada = input("  Digite o nome da tarefa a remover (ou 'sair' para encerrar):\n  > ").strip()

   
   
        if not entrada:
            print("Entrada vazia. Por favor, digite o nome da tarefa.")
            continue

        if entrada.lower() == "sair":
            print("\n Encerrando o sistema. Até logo!")
            break

        lista_consolidada, removida = remover_tarefa(lista_consolidada, entrada)

        if removida:
            print(f"\nTarefa removida com sucesso: \"{removida}\"")
            exibir_tarefas(lista_consolidada,
                           f"Lista Atualizada ({len(lista_consolidada)} tarefa(s) restante(s))")
        else:
            print(f"\n Tarefa \"{entrada}\" não encontrada na lista consolidada.")
            print(" Verifique o nome e tente novamente!")


        if not lista_consolidada:
            print("\n Todas as tarefas foram removidas. Encerrando.")
            break


if __name__ == "__main__":
    main()