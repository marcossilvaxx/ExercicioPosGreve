def valorPagamento(valor_prestação, dias_atraso):
    if dias_atraso == 0:
        return valor_prestação
    else:
        multa = 3 / 100 * valor_prestação
        juros = 0.1 / 100 * valor_prestação
        valortotal = valor_prestação + multa + (juros * dias_atraso)
        return valortotal

qtdPrest = 0
valorPrestDia = 0
valor_prestação = eval(input("Informe o valor da prestação:\n"))
dias_atraso = int(input("Informe os dias de atraso:\n"))

while valor_prestação > 0:
    valorASerPago = valorPagamento(valor_prestação, dias_atraso)
    print("O valor a ser pago é: %.2f" % valorASerPago)
    qtdPrest += 1
    valorPrestDia += valorASerPago
    valor_prestação = eval(input("Informe o valor da prestação:\n"))
    dias_atraso = int(input("Informe os dias de atraso:\n"))

print('''
Exibindo relatório do dia:\n
Quantidade de prestações pagas no dia: %d
Valor total de prestações pagas no dia: %.2f
''' % (qtdPrest, valorPrestDia))

