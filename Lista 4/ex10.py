

convidados = set()
while True:
    nome = input("Digite o nome do convidado (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    convidados.add(nome)
print("Lista de convidados sem repetições:")
for convidado in convidados:
    print(convidado)    
