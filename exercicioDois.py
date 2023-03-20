
filme = []

#=============================================================================================================
#FUNCOES


def inserirFilme(nomeFilme):
    filme.append(nomeFilme)

    
def listarFilme(filme):
    print("=== Voce acessou à listagem de filmes!! ===\n")
    for i, filme in enumerate(filme, start=1):
        print(f"{i} - {filme}")

def ordemAlfabetica(filme):
    filmes2 = sorted(filme)
    for i, filme in enumerate(filmes2, start=1):
        print(f"{i} - {filme}")

def removeFilme(nomeRemove,filme):
    filme.remove(nomeRemove)
    for i in filme:
        print(i)

# ==============================================================================================================
while(True):

    print()   
    print("Cadastro de Filmes")
    print("-"*30)
    print("1. Incluir Filmes")
    print("2. Listar Filmes")
    print("3. Listar em Ordem")
    print("4. Remover Filme")
    print("5. Sair")

    opcao = int(input("Opção: "))

    if(opcao == 1 ):
        print("\n=======Voce acesso à inclusão de filmes!!=======\n")
        nomeFilme = input("Insira o nome do filme: ")
        inserirFilme(nomeFilme)
        print('Incluido com Sucesso!')

    elif(opcao == 2):
         listarFilme(filme)

    elif(opcao == 3):
        print("=== Voce acessou à listagem de filmes em Ordem Alfabetica!! ===\n")
        ordemAlfabetica(filme)

    elif(opcao == 4):
        print("=== Você acessou para remoção de filme! ===\n")
        nomeRemove = input("Insira o nome do filme para remover: ")
        removeFilme(nomeRemove, filme)

    elif(opcao == 5):
        break
