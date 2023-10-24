peso = float(input("Digite o seu peso, em kg: "))
altura = float(input("Digite sua altura, em metros: "))

imc = peso / (altura**2)

print("O seu IMC da sua alt: {2} e o KG: {0},  é de: {1}".format(altura, peso, imc))
