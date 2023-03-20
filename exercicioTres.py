
def calcularDesconto(preco, taxa=10):
    return preco - ((preco * taxa)/100)


print(f"{calcularDesconto(200)}")
print(f"{calcularDesconto(200, 15)}")


# def calcula_desconto(valor, desconto=10):
#     valor_desconto = valor * (desconto/100)
#     novo_valor = valor - valor_desconto
#     print(f"Valor com Desconto: {novo_valor}")

