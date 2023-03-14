
precos = []
categoria = []

while(True):
    descricao = input("Descricao do Produto: ")
    categoria.append(descricao)
    if(descricao == 'Fim'):
        break
    valores = int(input("Informe o Preço do Produto: "))
    precos.append(valores)
    
quantidade = len(precos)
total = sum(precos)
minimo = min(precos)
media = total/2
print(f"Quantidade de produtos: {quantidade}")
print(f"Total em valores: {total}")
print(f"Menor valor de produto: {minimo}")
print(f"Media de valores dos produtos: {media}")

for i in precos:
    print(i, end = ' ')

