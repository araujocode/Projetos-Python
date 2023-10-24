peso = float(input("Digite o seu peso, em kg: "))
altura = float(input("Digite sua altura, em metros: "))

imc = peso / (altura**2)

print("O seu IMC é de:", "{:.2f}".format(imc))