import math
valores = []
centavos = []
while(True):
    preco = float(input("Informe o Preço do Produto: "))
    valores.append(preco)

    for i in valores:
        inicio = preco // preco
        centavos.append(inicio) 

    continuar = input("Inserir outro valor: ")
    if(continuar == "nao"):
        print(f"{centavos}")
        break 
