perfil_usuario = { "nome": "Davi",
                  "email": "davisatler6@gmail.com",
                  "Status" : "Inativo"}

#Status para ativo
perfil_usuario["Status"] = "Ativo"
print(perfil_usuario)


#Adicionando Idade
perfil_usuario["Idade"] = 25
print(perfil_usuario)


print("Chaves do dicionário:")
for chave in perfil_usuario.keys():
    print(chave)    