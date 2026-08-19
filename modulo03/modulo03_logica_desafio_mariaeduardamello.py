while True:
    print("\n---Menu---")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")


    opcao = input ("Escolha uma das operações (1, 2, 3, 4 ou 5):")

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

    elif opcao == "5":
        print("Saindo")
        break

    else:
        print("erro")   