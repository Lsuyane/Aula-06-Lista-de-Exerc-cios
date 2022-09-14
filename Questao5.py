from typing import List

P1 = []
P2 = []
n = int(input("Digite o tamanho da turma: "))

i = 0
while i < n:
    Notas = float(input("Digite as notas da Prova 1: "))
    P1.append(Notas)
    i = i+1

j = 0
while j < n:
    Nota_s = float(input("Digite as notas da Prova 2: "))
    P2.append(Nota_s)
    j = j+1

print("Tamanho da turma: ", n)
print("P1: ", P1)
print("P2: ", P2)

media1 = sum(P1) / n
media2 = sum(P2) / n

print("Média da turma na prova 1:", media1)
print("Média da turma na prova 2:", media2)

if media1 > media2:
    print("A turma obteve a melhor média na prova 1.")
else:
    print("A turma obteve a melhor média na prova 2.")