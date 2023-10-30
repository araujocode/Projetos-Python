import random
 
 
 
def jogoAdivinhacao():
 
    numero = random.randint(1,100)
 
    vezes = 0
    print(numero)
 
 
    print("Selecione um número inteiro entre 0 e 100: ")
 
 
 
    while True:
 
        try:
 
            tentativa = int(input("Digite o seu palpite: "))
 
        except ValueError:
 
            print("Digite um número válido")            
 
            continue
 
 
 
        vezes += 1
        

 
 
 
        if tentativa < numero:
 
            print("O número secreto é maior")
 
        elif tentativa > numero:
 
            print("O número secreto é menor")
 
        else:
 
            print("Parabéns, você acertou!")
 
            print("Você conseguiu acertar em", vezes, "tentativas")
 
            break;
       

if __name__ == "__main__":
    jogoAdivinhacao()