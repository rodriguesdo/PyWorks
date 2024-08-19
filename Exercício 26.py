num = int(input("Digite um número: "))
for contador in range(1, num+1):
    for x in range(0, contador):
        print(contador, end = " ")
    print()