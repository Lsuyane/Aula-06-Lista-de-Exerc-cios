n = int(input("Digite a qtde de numeros: "))

lista = []

for i in range(n):
    lista.append(int(input("Digite um numero: ")))

x = int(input("Num que deseja procurar: "))

if x in lista:
    print(x, "pertece a lista")
else:
    print(x, "nao pertece a lista")