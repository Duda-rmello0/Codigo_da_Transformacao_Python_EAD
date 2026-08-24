agenda = {}

while True:
    print("\n--- AGENDA DE CONTATOS ---")
    print("1. Adicionar contato")
    print("2. Remover contato")
    print("3. Buscar contato")
    print("4. Listar todos os contatos")
    print("5. Sair")
    
    opcao = input("Escolha uma opção (1-5): ")

    if opcao == "1":
        nome = input("Digite o nome: ").strip()
        telefone = input("Digite o telefone: ").strip()
        agenda[nome] = telefone
        print(f"Contato '{nome}' adicionado com sucesso!")

    elif opcao == "2":
        nome = input("Digite o nome do contato a remover: ").strip()
        if nome in agenda:
            del agenda[nome]
            print(f"Contato '{nome}' removido com sucesso!")
        else:
            print("Contato não encontrado.")

    elif opcao == "3":
        nome = input("Digite o nome para buscar: ").strip()
        if nome in agenda:
            print(f"Telefone de {nome}: {agenda[nome]}")
        else:
            print("Contato não encontrado.")

    elif opcao == "4":
        if agenda:
            print("\nLista de Contatos:")
            for nome, telefone in agenda.items():
                print(f"- {nome}: {telefone}")
        else:
            print("A agenda está vazia.")

    elif opcao == "5":
        print("Saindo da agenda...")
        break
    else:
        print("Opção inválida! Tente novamente.")