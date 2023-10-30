peso = float(input("Digite o seu peso, em kg: "))
altura = float(input("Digite sua altura, em metros: "))

imc = peso / (altura**2)

print("Sua altura é: {0}, você pesa: {1} kg e seu IMC é: {2:.2f}".format(altura, peso, imc))


sexo = input("Digite o seu sexo (H/M): ").upper()

if sexo == "H":
    if imc <= 18.5:
        print("Abaixo do peso")
    if 18.5 < imc <= 24.9:
        print("Saudavel")
    if 25.0 < imc <= 29.9:
        print("Levemente acima do peso")
    if 30.0 < imc <= 30.4:
        print("Obesidade grau I") 
    if 35.0 < imc <= 39.9:
        print("Obesidade grau II (severa)")
    if imc >= 40:
        print("Obesidade III (mórbida)")

if sexo == "M":
    if imc <= 16:
        print("Magreza grave")
    if 16 < imc <= 17:
        print("Magreza moderada")
    if 17 < imc <= 18.5:
        print("Magreza leve")
    if 18.5 < imc <= 25:
        print("Saudável") 
    if 25 < imc <= 30:
        print("Sobrepeso")
    if 30 < imc <= 35:
        print("Obesidade Grau I")
    if 35 < imc <= 40:
        print("Obesidade Grau II (severa)")     
    if imc >= 40:
        print("Obesidade Grau III (mórbida)")
    
else:
    print("Sexo inexistente")