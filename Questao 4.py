
n = int(input("Digite o tamanho da lista: "))
L = []

for i in range(n):
    L.append(int(input("Digite um numero: ")))

print(L)

for i in L:
    if i % 2 == 0:
        L.remove(i)

print(L)
