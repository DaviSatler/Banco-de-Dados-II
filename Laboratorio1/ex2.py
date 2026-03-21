Designs = {"Design 1" : 1134, 
           "Design 2" : 982, 
           "Design 3" : 1751, 
           "Design 4" : 210}


print("-------------COMPETIÇÃO DE DESIGN-------------")
print("O design vencedor com mais votos foi: " + max(Designs, key=Designs.get))


#Porcentagem de votos do design vencedor
total_votos = sum(Designs.values())
votos_vencedor = Designs[max(Designs, key=Designs.get)]
porcentagem_votos_vencedor = (votos_vencedor / total_votos) * 100
print(f"O design vencedor recebeu {porcentagem_votos_vencedor:.2f}% dos votos.")
print("---------FIM DA COMPETIÇÃO DE DESIGN----------")
