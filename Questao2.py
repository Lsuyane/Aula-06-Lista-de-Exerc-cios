print(" Digite números positivos:")
L = []
while True:
    p = int(input())
    if p <= 0:
        break
    L.append(p)
x = int(input("Qual o número a procurar? "))
if x in L:
    print(x, "pertence à lista")
else:
    print(x, "não pertence à lista")