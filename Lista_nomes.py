import os

nomes = []

while True:
    print("\n1 - Listar todos os nomes.")
    print("2 - Cadastrar novo Nome.")
    print("3 - Pesquisar nome cadastrado.")
    print("4 - Alterar Nome cadastrado.")
    print("5 - Excluir nome cadastrado.")
    print("6 - Sair do Programa.")

    opcao = input("\nOpção do Usuário: ")

    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
            if nomes:
                for i in range(len(nomes)):
                    print(f"Nome de Índice {i}: {nomes[i]}")
                    continue
            else:
                print("Nenhum nome cadastrado.")
                
        case "2":
            try:
                novo_nome = input("Informe o novo nome: ").capitalize()
                nomes.append(novo_nome)
                print(f"Nome {novo_nome} cadastrado com sucesso.")
            except:
                print("Não foi possível cadastrar o nome.")
                
        case "3":
            nome_procurado = input("Informe o nome a pesquisar: ")
            contador = nomes.count(nome_procurado)
            print(f"{nome_procurado} foi encontrado {contador} vezes.")
            
        case "4":
            try:
                indice = int(input("Informe o índice a alterar: "))
                nomes[indice] = input("Informe o novo nome: ")
                print("Nome alterado com sucesso.")
            except:
                print("Não foi possível alterar o nome.")
                
        case "5":
            try:
                indice = int(input("Informe o índice a excluir: "))
                del(nomes[indice])
                print("Nome excluído com sucesso.")
            except:
                print("Não foi possível excluir o nome.")
                
        case "6":
            print("Programa encerrado com sucesso.")
            break
            
        case _:
            print("Opção inválida, digite uma opção válida.\n")
