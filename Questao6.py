
L1 = []
L2 = []

n = int(input("Digite a qtde de elementos que deseja imprimir na lista 1: "))
m = int(input("Digite a qtde de elementos que deseja imprimir na lista 2: "))

i = 0
while i < n:
    List = input("Digite os valores inteiros da Lista 1: ")
    L1.append(List)
    i = i+1

j = 0
while j < m:
    Lis = input("Digite os valores inteiros da Lista 2: ")
    L2.append(Lis)
    j = j+1
print("Elementos da Lista 1: ", L1)
print("Elementos da lista 2: ", L2)

L3 = L1 + L2

L3.sort()
print("Ordem Crescente: ", L3)

L3.sort(reverse=True)
print("Ordem Decrescente: ", L3)
