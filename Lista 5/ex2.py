#2)     Você está desenvolvendo um sistema de acesso
#que possui três níveis de CRUD:

#(n1 -
#somente leitura), (n2 - leitura e atualização) e (n3 - Criação, leitura,
#atualização e exclusão)

#Faça um
#programa que realize o processo de login de três usuários e mostre as
#funcionalidades de acordo com nível de acesso. Cada um destes usuários deverá
#ter um tipo de acesso diferente. O login deverá ser composto por CPF e senha.
#Faça a validação se o usuário pode entrar ou não entrar no sistema e se
#entrar, qual é o nível de acesso deste usuário.
 
usuarios = {
    "111.111.111-11": {
        "nome":  "Ana Luiza",
        "senha": "ana123",
        "nivel": 1
    },
    "222.222.222-22": {
        "nome":  "Davi Satler",
        "senha": "davi123",
        "nivel": 2
    },
    "333.333.333-33": {
        "nome":  "Leandro Satler",
        "senha": "leandro123",
        "nivel": 3
    },
}
 
permissoes = {
    1: {
        "descricao": "N1 — Somente Leitura",
        "acoes": [" Ler / Consultar registros"]
    },
    2: {
        "descricao": "N2 — Leitura e Atualização",
        "acoes": ["Ler / Consultar registros",
                  "Atualizar registros existentes"]
    },
    3: {
        "descricao": "N3 — Acesso Total (CRUD completo)",
        "acoes": ["Criar novos registros",
                  "Ler / Consultar registros",
                  "Atualizar registros existentes",
                  "Excluir registros"]
    },
}
 
 
 
 
def exibir_menu_acesso(usuario):
    nivel = usuario["nivel"]
    info  = permissoes[nivel]
    print("\n" + "=" * 50)
    print(f"  Bem-vindo, {usuario['nome']}!")
    print(f"  Nível de acesso: {info['descricao']}")
    print("=" * 50)
    print("  Funcionalidades disponíveis:")
    for acao in info["acoes"]:
        print(f"    {acao}")
    print("=" * 50)
 
 
 
 
 
def login():
    MAX_TENTATIVAS = 3
    print("\n" + "=" * 50)
    print("       SISTEMA DE CONTROLE DE ACESSO")
    print("=" * 50)
 
 
    tentativas = 0
    while tentativas < MAX_TENTATIVAS:
        print(f"\n[ Tentativa {tentativas + 1} de {MAX_TENTATIVAS} ]")
        cpf   = input("  CPF   (ex: 111.111.111-11): ").strip()
        senha = input("  Senha: ").strip()
 
        if cpf not in usuarios:
            print("\n  CPF não cadastrado no sistema.")
        else:
            usuario = usuarios[cpf]
            if usuario["senha"] == senha:
                print("\nLogin realizado com sucesso!")
                exibir_menu_acesso(usuario)
                return  
            else:
                print("\n Senha incorreta.")
 
 
 
        tentativas += 1
        restantes = MAX_TENTATIVAS - tentativas
        if restantes > 0:
            print(f" Tentativas restantes: {restantes}")
 
    print("\n" + "=" * 50)
    print(" Acesso bloqueado após 3 tentativas inválidas.")
    print("     Entre em contato com o administrador.")
    print("=" * 50)
 
 
if __name__ == "__main__":
    login()