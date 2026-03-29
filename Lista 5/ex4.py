# ================================================================
#   EXERCÍCIO 4
#
#   Ana é responsável pelo controle de estoque de uma loja de
#   artigos para papelaria. Ela precisa de um programa que permita
#   cadastrar os produtos em um dicionário, onde cada produto será
#   uma (chave) e a quantidade correspondente será o (valor).
#   Crie um menu com as opções:
#
#   1 - Cadastrar : realiza o cadastro do nome do produto e da
#                   quantidade;
#   2 - Exibir   : exibe todos os produtos e quantidades;
#   3 - Atualizar: solicita o nome do produto e atualiza a
#                  quantidade do produto;
#   0 - Sair     : exibe uma mensagem de encerramento e finaliza
#                  o programa.
#
#   Faça a validação das entradas para não aceitar caracteres
#   inválidos e dados inconsistentes e informe se o produto não
#   existir.
# ================================================================

estoque = {}   


def ler_nome_produto(prompt):

    while True:
        nome = input(prompt).strip()
        if not nome:
            print("  Nome não pode ser vazio. Tente novamente.")
        elif not all(c.isalpha() or c in (" ", "-") for c in nome):
            print("  Nome inválido. Use apenas letras, espaços ou hífens.")
        else:
            return nome.title()  


def ler_quantidade(prompt):
    while True:
        entrada = input(prompt).strip()
        if not entrada.lstrip("-").isdigit():
            print(" Quantidade inválida. Digite um número inteiro.")
        elif int(entrada) <= 0:
            print(" A quantidade deve ser maior que zero.")
        else:
            return int(entrada)


def cadastrar():
    print("\n CADASTRAR PRODUTO")
    nome = ler_nome_produto("  Nome do produto : ")

    if nome in estoque:
        print(f"'{nome}' já está cadastrado (qtd: {estoque[nome]}).")
        print("       Use a opção 3 para atualizar a quantidade.")
        return

    qtd = ler_quantidade("  Quantidade      : ")
    estoque[nome] = qtd
    print(f" '{nome}' cadastrado com sucesso! Quantidade: {qtd}")


def exibir():
    print("\nESTOQUE ATUAL")
    if not estoque:
        print(" Nenhum produto cadastrado.")
        return

    largura_nome = max(len(n) for n in estoque) + 2
    print(f"  {'PRODUTO':<{largura_nome}} {'QTD':>6}")
    print(f"  {'─' * largura_nome} {'─' * 6}")
    for nome, qtd in sorted(estoque.items()):
        print(f"  {nome:<{largura_nome}} {qtd:>6}")
    print(f"  {'─' * (largura_nome + 7)}")
    print(f"  Total de itens cadastrados: {len(estoque)}")


def atualizar():
    print("\n ATUALIZAR QUANTIDADE ")
    if not estoque:
        print(" Nenhum produto cadastrado para atualizar.")
        return

    nome = ler_nome_produto("  Nome do produto : ")

    if nome not in estoque:
        print(f" Produto '{nome}' não encontrado no estoque.")
        print("       Verifique o nome ou cadastre-o na opção 1.")
        return

    print(f" Quantidade atual de '{nome}': {estoque[nome]}")
    nova_qtd = ler_quantidade("  Nova quantidade  : ")
    estoque[nome] = nova_qtd
    print(f" '{nome}' atualizado com sucesso! Nova quantidade: {nova_qtd}")


def sair():
    print("   Encerrando o sistema de estoque.")
    print("   Obrigado, Ana! Até logo.  ")


def exibir_menu():
    print("           CONTROLE DE ESTOQUE — PAPELARIA      ")
    print("     1 - Cadastrar produto                       ")
    print("     2 - Exibir estoque                          ")
    print("     3 - Atualizar quantidade                    ")
    print("     0 - Sair                                    ")



def main():
    opcoes = {"1": cadastrar, "2": exibir, "3": atualizar}

    while True:
        exibir_menu()
        escolha = input("  Escolha uma opção: ").strip()

        if escolha == "0":
            sair()
            break
        elif escolha in opcoes:
            opcoes[escolha]()
        else:
            print("Opção inválida. Digite 1, 2, 3 ou 0.")
            
if __name__ == "__main__":
    main()