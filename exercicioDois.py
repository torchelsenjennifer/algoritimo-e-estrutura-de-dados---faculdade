
filme = []

def menu(escolha):
    print("\n====MENU PRINCIPAL====\n")
    print(" 1. Incluir\n 2. Listar\n 3. Lista em Ordem Alfabetica\n 4. Remover\n 5. Sair\n ")
    print("===================")
    escolha = int(input("\nQual a sua opção: "))
    return escolha

def inclusao(nomeFilme):
     print("\n=======Voce acesso à inclusão de filmes!!=======\n")
     nomeFilme = input("Insira o nome do filme: ")
     return nomeFilme
    #  ainda = input("Ainda inserir filmes: ")
    #  if(ainda == "sim"):
    #   return filme
    #  else:
    #      return nome filme
    
def listagem(filme):
    print("=== Voce acesso à listagem de filmes!! ===\n")
    for i in filme:
        print(i, end = ' ')

while(True):

    opcao = menu(f"escolha")
    if(opcao == 1 ):
        inclusao( f"nomeFilme")
        filme.append("nomeFilme")
        print('Incluido com Sucesso!')

    elif(opcao == 2):
         listagem(filme)

    elif(opcao == 3):
        print("=== Voce acessou à listagem de filmes em Ordem Alfabetica!! ===\n")

    elif(opcao == 4):
        print("Remover")
    elif(opcao == 5):
        break

         
        
        

    



