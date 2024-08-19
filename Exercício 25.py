somamedia = 0
alunos = int(input("Digite a quantidade de alunos que você quer cadastrar: "))
for x in range(1,alunos+1):
        n1 = float(input("Digite o primeiro valor:"))
        while n1 < 0 or n1 > 10:
          n1 = int(input("Número inválido, digite novamnete um valor: "))

        n2 = float(input("Digite o segundo valor: "))
        while n2 < 0 or n2 > 10:
            n2 = float(input("Número inválido, digite novamente um valor:"))

            media = (n1 + n2)/2
            print(media)
            somamedia = somamedia + media
media = somamedia/alunos
print("Média total da sala ", media)