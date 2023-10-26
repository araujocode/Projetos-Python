def somar(a, b):
    resultado = a + b
    return resultado

def subtrair(a, b):
    resultado = a - b
    return resultado

def multiplicar(a,b):
    resultado = a * b
    return resultado

def dividir(a,b):
    resultado = a/b
    return resultado

def elevar(a,b):
    resultado = a**b
    return resultado

def raizQuadrada(a):
    resultado = a ** 0.5
    return resultado

valor1 = int(input("Digite um primeiro número para somar: "))
valor2 = int(input("Digite um segundo número para somar: "))
soma = somar(valor1, valor2)
print("Soma:", soma)

valor1 = int(input("Digite um primeiro número para multiplicar: "))
valor2 = int(input("Digite um segundo número para multiplicar: "))
multiplica = multiplicar(valor1, valor2)
print("Multiplicação:", multiplica)

valor1 = int(input("Digite um primeiro número para dividir: "))
valor2 = int(input("Digite um segundo número para dividir: "))
divide = dividir(valor1, valor2)
print("Divisão:", divide)

valor1 = int(input("Digite um primeiro número como base: "))
valor2 = int(input("Digite um segundo número para elevar: "))
eleva = elevar(valor1, valor2)
print("Potência:", eleva)

valor1 = int(input("Digite um valor para a tirar a raiz: "))
raiz = raizQuadrada(valor1)
print("Raiz Quadrada:", raiz)


    
