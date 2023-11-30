escolha = 2000
num1 = 0
num2 = 1

while True:
    resultado = num1 + num2
    print(resultado)

    num1 = num2
    num2 = resultado
    
    if(resultado >= escolha):
        break

    

