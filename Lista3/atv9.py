#9 - Dado a lista: nomes = ['Maria', 'joão', 'Pedro', 'José', 'Ricardo', 'Moisés', 'Antônio'], faça uma iteração que mostre na tela todos os nomes, exceto o nome Ricardo.

nomes = ['Maria', 'joão', 'Pedro', 'José', 'Ricardo', 'Moisés', 'Antônio']


for nome in nomes:
 if nome == "Ricardo":
   continue
 else:
      print (nome)
