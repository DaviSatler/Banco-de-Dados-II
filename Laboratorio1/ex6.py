notas_alunos = {"Ana": 8.5, 
                "Bruno": 7.0, 
                "Carla": 9.0}

#Novo aluno
notas_alunos["Diego"] = 6.5

print("------------NOTAS DOS ALUNOS------------")
for aluno, nota in notas_alunos.items():
    print(f"{aluno}: {nota}")
    
print("------------MÉDIA DAS NOTAS DOS ALUNOS------------")
media = sum(notas_alunos.values()) / len(notas_alunos)
print(f"A média das notas dos alunos é: {media:.2f}")        