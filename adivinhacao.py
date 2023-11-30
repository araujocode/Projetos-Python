import random

vezesTentadas = 0 

while True :
    numero = random.randint(0,100)
    print(numero)
    imparOuPar = int(input("Digite seu palpite: "))   
    vezesTentadas += 1     
    
    if imparOuPar == numero and vezesTentadas == 5:                       
        print(f"Você acertou em {vezesTentadas} tentativas")
        break

    elif imparOuPar == numero and vezesTentadas == 5:        
        print(f"Você acertou em {vezesTentadas} tentativas")
        break