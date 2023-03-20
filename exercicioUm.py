# biblioteca statistics para uso de funcoes de calculos
from statistics import fmean

precos = []
categoria = []

while(True):
    descricao = input("Descricao do Produto: ")
    categoria.append(descricao)
    #nao precisa ser logo abaixo
    if(descricao == 'Fim'):
        break
    valores = float(input("Informe o Preço do Produto: "))
    precos.append(valores)

print()
print("-"*30)

quantidade = len(precos)
total = sum(precos)
maior = max(precos)
#segunda possibilidade de calcular média
#media = fmean(precos)
media = total/quantidade


try:
    indice_maior = precos.index(maior) 
    produto_maior = categoria[indice_maior]
except ValueError:
    print("Erro")

print(f"Quantidade de produtos: {quantidade}")
print(f"Total em valores: {total}")
print(f"Maior valor de produto: {maior:6.2f} - {produto_maior}")
print(f"Media de valores dos produtos: {media}")


for i in precos:
    print(i, end = ' ')

