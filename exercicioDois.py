
filme = []

def menu(escolha):
    print("\n====MENU PRINCIPAL====\n")
    print(" 1. Incluir\n 2. Listar\n 3. Lista em Ordem Alfabetica\n 4. Remover\n 5. Sair\n ")
    print("===================")
    escolha = int(input("\nQual a sua opção: "))
    return escolha

def inclusao(nomeFilme):
    filme.append(nomeFilme)

    
def listagem():
    print("=== Voce acessou à listagem de filmes!! ===\n")
    for i in filme:
        print(i)



while(True):

    opcao = menu(f"escolha")

    if(opcao == 1 ):
        print("\n=======Voce acesso à inclusão de filmes!!=======\n")
        nomeFilme = input("Insira o nome do filme: ")
        inclusao(nomeFilme)
        print('Incluido com Sucesso!')

    elif(opcao == 2):
         listagem()

    elif(opcao == 3):
        print("=== Voce acessou à listagem de filmes em Ordem Alfabetica!! ===\n")

    elif(opcao == 4):
        print("Remover")
    elif(opcao == 5):
        break

         
        
        

    



