
def calcularDesconto(preco, taxa=10):
    return preco - ((preco * taxa)/100)


print(f"{calcularDesconto(200)}")
print(f"{calcularDesconto(200, 15)}")


