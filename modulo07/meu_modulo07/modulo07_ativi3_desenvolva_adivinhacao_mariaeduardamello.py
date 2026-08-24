import random
import math

numero = random.randint (1, 24)
tentativas = 0
limite_tentativas = 6

print("JOGO DE ADIVINHAÇÃO")
print("Tente adivinhar o número entre 1 e 24. VOcê tem 6 tentativas")

while tentativas < limite_tentativas:
    chute = int(input(f"Tentativa{tentativas + 1} de {limite_tentativas}. DIgite seu palpite:"))

    if chute == numero:
        print(f"Você acertou o número {numero} em {tentativas} tentativa(s)")
        break
    else:
        distancia = math.fabs(numero - chute)
        
    if chute < numero:
        print("O número é maior")
    else:
        print("O número é menor")

    if distancia <= 3:
        print("Você está MUITO PERTO!")  
    elif distancia <= 5:
        print("Você está perto")
    else:
        print("Você está distante")          
    

if chute != numero:
    print(f"\n Suas chances acabaram. O número era {numero}")


