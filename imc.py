peso = float(input("Digite o seu peso, em kg: "))
altura = float(input("Digite sua altura, em metros: "))

imc = peso / (altura**2)

print("Sua altura é: {0}, você pesa: {1} kg e seu IMC é: {2:.2f}".format(altura, peso, imc))


sexo = input("Digite o seu sexo (H/M): ").upper()

if sexo == "H":
    if imc <= 18.5:
        print("Abaixo do peso")
    elif 18.5 < imc <= 24.9:
        print("Saudavel")
    elif 25.0 < imc <= 29.9:
        print("Levemente acima do peso")
    elif 30.0 < imc <= 30.4:
        print("Obesidade grau I") 
    elif 35.0 < imc <= 39.9:
        print("Obesidade grau II (severa)")
    else:
        print("Obesidade III (mórbida)")

elif sexo == "M":
    if imc <= 16:
        print("Magreza grave")
    elif 16 < imc <= 17:
        print("Magreza moderada")
    elif 17 < imc <= 18.5:
        print("Magreza leve")
    elif 18.5 < imc <= 25:
        print("Saudável") 
    elif 25 < imc < 30:
        print("Sobrepeso")
    elif 30 < imc < 35:
        print("Obesidade Grau I")
    elif 35 < imc < 40:
        print("Obesidade Grau II (severa)")     
    else:
        print("Obesidade Grau III (mórbida)")
else:
    print("Digite um sexo válido (sem preconceito,bls)")


