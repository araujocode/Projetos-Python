numero = int(input("Digite um número: "))
resultado = 1

while numero > 1:
    resultado = resultado * numero
    numero -= 1

print(f"O fatorial é {resultado}")
    