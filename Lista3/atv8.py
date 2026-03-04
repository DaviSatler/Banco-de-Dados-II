#8 - Dado a lista: nomes = ['Maria', 'joão', 'Pedro', 'José', 'Ricardo', 'Moisés', 'Antônio'], faça uma iteração que mostre todos os nomes até o nome Ricardo.


nomes = ['Maria', 'joão', 'Pedro', 'José', 'Ricardo', 'Moisés', 'Antônio']



for nome in nomes:
 if nome == "Ricardo":
      print(nome)
      print(f"O nome {nome} acabou corrompendo a lista, não consigo prosseguir, adeus... \n")
      break
 else:
      print (nome)
      
      