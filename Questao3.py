
vingadores = ["Homem de Ferro", "Capitão América", "Thor", "Hulk", "Viúva Negra", "Gavião Arqueiro"]
print(vingadores)

vingadores.append("Homem-Aranha")
print(vingadores)

if "Thor" in vingadores:
    print("Posição do Thor: ", vingadores.index("Thor"))

if "Viúva Negra" in vingadores:
    vingadores.remove("Viúva Negra")
if "Homem de Ferro" in vingadores:
    vingadores.remove("Homem de Ferro")
print(vingadores)