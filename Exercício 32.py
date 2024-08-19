A = [0,0,0,0,0]

for y in range(len(A)):
    A[y] = int(input("Digite um número: "))
print(A)
for x in range(len(A)-1,-1,-1):
    print(A[x], end = " ")