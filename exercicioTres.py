desconto = 10
valor = []
novoValor = []

while(True):
    preco = int(input("Qual é o valor: "))
    valor.append(preco)

    for i in valor:
        valorDesconto = (i - desconto)
        novoValor.append(valorDesconto)

    continuar = input("Inserir outro valor: ")
    if(continuar == "nao"):
        print(f"{novoValor}")
        break


