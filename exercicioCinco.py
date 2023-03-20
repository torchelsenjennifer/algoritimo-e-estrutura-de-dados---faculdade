def idadeObrigatorio(nome = 'jennifer', cidade='Pelotas', idade=10):
     if(idade>=18):
          return 'É maior de idade!'
     else:
          return 'É menor de idade!'

     
print(f"{idadeObrigatorio()}")

# def mostra_dados(idade, nome="", cidade=""):
#      if nome != "":
#           print(f"Nome: {nome}")
#      if cidade != "":
#           print(f"Cidade: {cidade}")
#      if idade>18:
#           print("Voce é maior de idade")
#      else:
#           print("Voce é menor de idade")

# mostra_dados(cidade="pelotas", idade=20, nome="Beatriz")
     
     