
def retornaCentavos(preco):
    return preco - (preco // 1)

while(True):
    preco = float(input("Informe o Preço do Produto ou 0 para finalizar: "))
    if(preco == 0):
        break 
    print(f"{retornaCentavos(preco):6.2f} centavos")