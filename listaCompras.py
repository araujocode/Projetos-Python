lista = []

while True:
    print("Menu")
    print("1. Adicionar um item")
    print("2. Remover um item")
    print("3. Visualizar a lista")
    print("4. Ordenar a lista")
    print("5. Sair")

    opcao = int(input("Digite a opção desejada: "))

    # Adicionar um item
    if opcao == 1:
        nome = input("Digite o nome do item: ").lower()
        quantidade = int(input("Digite a quantidade: "))
        lista.append((nome, quantidade))
        print("Item adicionado com sucesso.\n")

    # Remover um item
    elif opcao == 2:
        nome = input("Digite o nome do item a ser removido: ").lower()

        itemEncontrado = False
        for item in lista:
            if nome == item[0]: #item[0] é o "nome" do item salvo na lista → (nome, quantidade)
                lista.remove(item)
                itemEncontrado = True
                print("Item removido com sucesso.\n")
                break

        if not itemEncontrado:
            print("Item não encontrado na lista.\n")

    # Visualizar a lista
    elif opcao == 3:
        if not lista:
            print("Lista vazia.\n")
        else:
            for item in lista:
                print(f"\nItem: {item[0]} - Quantidade: {item[1]}\n")

    # Ordenar a lista
    elif opcao == 4:
        if not lista:
            print("Lista vazia.\n")
        else:
            lista.sort()
            print("A lista foi ordenada.\n")

            for item in lista:
                print(f"\nItem: {item[0]} - Quantidade: {item[1]}\n")

    # Sair
    elif opcao == 5:
        print("Você saiu")
        break

    else:
        print("Opção inválida\n")
