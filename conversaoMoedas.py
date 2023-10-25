dolar = float(input("Digite quantos dolares deseja converter: "))
euro = dolar * 0.95
franco = dolar * 0.90
real = dolar * 4.99
pesoArgentino = dolar * 349.83
iene = dolar * 149.92


print(dolar, "dolares equivalem a", "{:.2f}".format(euro), "euros")
print(dolar, "dolares equivalem a", "{:.2f}".format(franco), "francos")
print(dolar, "dolares equivalem a", "{:.2f}".format(real), "reais")
print(dolar, "dolares equivalem a", "{:.2f}".format(pesoArgentino), "pesos argentinos")
print(dolar, "dolares equivalem a", "{:.2f}".format(iene), "ienes")