lista = []




while True: 
    lista = input("Digite um item (ou sair):")

    if lista.lower() == "sair": 
        break 
    lista.append("") 
    lista.sort() 
    print("\nLista de tarefas:") 
    for t in lista: 
        print(f"- {t}")