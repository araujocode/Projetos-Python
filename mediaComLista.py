notas = []

i = 0
while i < 4:    
    entradas = float(input("Digite as suas notas: "))
    i += 1
    notas.append(entradas)    

print("As notas digitadas foram: ", notas)
media = sum(notas) / len(notas)
print("Média das notas:", media)







"""" 
notas = []


while len(notas) < 4:
    
    entradas = input("Digite as quatro notas separadas por espaços: ")
    
    notasDigitadas = entradas.split()

    
    if len(notas) + len(notasDigitadas) > 4:
        print("Você digitou mais de quatro notas")
    else:        
        i = 0
        while i < len(notasDigitadas):
            notas.append(float(notasDigitadas[i]))
            i += 1

print("Notas digitadas:", notas)

media = sum(notas) / len(notas)
print("Média das notas:", media)
"""

