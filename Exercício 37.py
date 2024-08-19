nome = input("Digite o nome do aluno: ")

for x in range(2):

    nota = float(input("Digite a", x+1, "nota: "))
    while nota < 0 or nota >10:
        nota = int(input(f"Erro, Digite a {x + 1} nota: "))

media = nota/2

while media < 0 or media < 5:
    print("Você está reprovado: ")

print(media)