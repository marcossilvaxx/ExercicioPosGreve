base = eval(input("Informe a base:\n"))
expoente = eval(input("Informe um expoente:\n"))

frase = ""

resultado = 1

for i in range(1, expoente + 1):
  resultado = resultado * base
  if i != expoente:
    frase = frase + str(base) + "x"
  else:
    frase = frase + str(base)
print(frase, "=", resultado)