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
    if imc <= 19:
        print("Abaixo do normal")
    if 19 < imc <= 23.9:
        print("Normal")
    if 24 < imc <= 28.9:
        print("Obesidade leve")
    if 29 < imc <= 38.9:
        print("Obesidade Moderada")    
    if imc > 38.9:
        print("Obesidade Mórbida")
    
else:
    if sexo != "M" and sexo != "H":
        print("Sexo inexistente")   
