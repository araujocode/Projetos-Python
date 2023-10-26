dolar = float(input("Digite quantos dolares deseja converter: "))
euro = dolar * 0.95
franco = dolar * 0.90
real = dolar * 4.99
pesoArgentino = dolar * 349.83
iene = dolar * 149.92


print("{0} dolares equivalem a {1:.2f} euros".format(dolar, euro))

print("{0} dolares equivalem a {1:.2f} francos".format(dolar, franco))

print("{0} dolares equivalem a {1:.2f} dolar".format(dolar, real))

print("{0} dolares equivalem a {1:.2f} pesos argentinos".format(dolar, pesoArgentino))

print("{0} dolares equivalem a {1:.2f} ienes".format(dolar, iene))

print(f"{dolar:.2f} dolares equivalem a {euro:.2f} euros")
print(f"{dolar:.2f} dolares equivalem a {franco:.2f} francos")
print(f"{dolar:.2f} dolares equivalem a {pesoArgentino:.2f} pesos argentinos")
print(f"{dolar:.2f} dolares equivalem a {iene:.2f} ienes")


