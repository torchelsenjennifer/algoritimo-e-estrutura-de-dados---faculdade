
filmes = []

def incluir():
    print()
    print('Inclusao de Filme')
    print("-"*30)
    x = input("Titulo do Filme: ")
    filmes.append(x)

def listar():
    print()
    print('Listar de Filme')
    print("-"*30)
    for i, filme in enumerate(filmes, start=1):
        print(f"{i} - {filme}")

def listar_ordem():
    print()
    print('Listar de Filme em ordem alfabetica')
    print("-"*30)
    filmes2 = sorted(filmes)
    for i, filme in enumerate(filmes2, start=1):
        print(f"{i} - {filme}")

def remover():
    listar()
    num = int(input("Qual filme remover (0, para sair): "))
    if num == 0:
        return
    elif num > len(filmes):
        print("Erro... Informe um numero existente na lista")
        filmes.pop(num - 1)
        print('Ok. Filme Removido')

while(True):
    print()   
    print("Cadastro de Filmes")
    print("-"*30)
    print("1. Incluir Filmes")
    print("2. Listar Filmes")
    print("3. Listar em Ordem")
    print("4. Remover Filme")
    print("5. Sair")

    opcao = int(input("Opição: "))

    if opcao == 1:
        incluir()
    
    elif opcao == 2:
        listar()

    elif opcao == 3:
        listar_ordem()

    elif opcao == 4:
        remover()
    else:
        break

    