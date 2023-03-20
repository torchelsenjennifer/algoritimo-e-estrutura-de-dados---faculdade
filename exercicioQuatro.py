
def retornaCentavos(preco):
    return preco - (preco // 1)

while(True):
    preco = float(input("Informe o Preço do Produto ou 0 para finalizar: "))
    if(preco == 0):
        break 
    print(f"{retornaCentavos(preco):6.2f} centavos")



# import math
# def centavos(preco):
#     preco_sem_centavos = math.floor(preco)
#     return preco - preco_sem_centavos

# centavos(15.40)