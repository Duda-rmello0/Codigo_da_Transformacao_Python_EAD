print("1 - soma")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão")


opcao = input ("Escolha uma das operações (1, 2, 3 ou 4):")

if opcao == "1":
    n1 = float(input("Numero 1: "))
    n2 = float(input("Numero 2: "))
    print("Resultado:", n1 + n2)

elif opcao == "2":
    n1 = float(input("Numero 1: "))
    n2 = float(input("Numero 2: "))
    print("Resultado:", n1 - n2)    

elif opcao == "3":
    n1 = float(input("Numero 1: "))
    n2 = float(input("Numero 2: "))
    print("Resultado:", n1 * n2) 

elif opcao == "4":
    n1 = float(input("Numero 1: "))
    n2 = float(input("Numero 2: "))
    print("Resultado:", n1 / n2) 

else:
    print("erro")   