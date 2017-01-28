listaA = list(input("Informe uma lista de nomes:\n").split(", "))
listaB = []


for nome in listaA:
    nomeSeparado = nome.split(" ")
    nomeSeparado.reverse()
    nomeFormatado = " ".join(nomeSeparado)
    listaB.append(nomeFormatado)

print("Lista Formatada:", listaB)