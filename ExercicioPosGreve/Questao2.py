numero = eval(input("Escreva o numero que você quer calcular:\n"))

fatorial = 1
if (numero != 0):
    for i in range(1, numero + 1):
        fatorial = fatorial * i
    print("O fatorial de", numero, "é", fatorial)
else:
    print("O fatorial de", numero, "é", fatorial)