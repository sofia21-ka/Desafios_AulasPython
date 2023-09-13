print("-"*30)
print("\t DESAFIO 18")
print("-"*30)
carros =['BMW X6','BMW I5','BMW I8']
car =  (input("Informe o carro desejado: ")).upper()
#Posso usar o in aqui p percorrer a lista, sem precisar do for
if car in carros:
#Aqui  significa se car estiver em carros, mostre ...
    print("Este carro está disponível")
else:
    print("Desculpe, este carro não está disponível")