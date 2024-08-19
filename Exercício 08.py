time1 = input("Digite o nome do primeiro time: ")
t1 = int(input("Digite o número de gols: "))
time2 = input("Digite o nome do segundo time: ")
t2 = int(input("Digite o número de gols: "))

if t1 > t2:
    print("O vencedor foi o", time1, "e fez", t1, "gols")
elif t1 < t2:
    print("O vencedor foi o", time2, " e fez", t2, "gols")
else:
    print("Empate")
