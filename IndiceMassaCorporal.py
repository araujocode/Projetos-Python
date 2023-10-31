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
    if imc <= 19:
        print("Abaixo do normal")
    elif 19 < imc <= 23.9:
        print("Normal")
    elif 24 < imc <= 28.9:
        print("Obesidade leve")
    elif 29 < imc <= 38.9:
        print("Obesidade Moderada")    
    else:
        print("Obesidade Mórbida")
else:
    print("Digite um sexo válido (sem preconceito,bls)")


