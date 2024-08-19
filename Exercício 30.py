notasAlunos = [0,0,0,0,0]
cont = 0
soma =0
for x  in range(len(notasAlunos)):
    notasAlunos[x] = float(input("Digite a nota: "))

for y in range(len(notasAlunos)):
    soma = soma + notasAlunos[y]
media = soma/len(notasAlunos)

for z in range(len(notasAlunos)):
    if notasAlunos[z]>=media:
        cont = cont + 1
print("A média da sala foi:", media, "e", cont, "Alunos foram aprovados")
