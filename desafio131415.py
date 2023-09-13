print("\n \t Desafio 13 \n")
i = 1
while (i<=10):
    print("numero = ",i)
    i=i+1
   

print("\n \t Desafio 14 \n")
l = 0

while (l<=10):
    l=l+1
   
    if(l==5):
        break
    print("1º loop: ",l)
l=0 
while l<10:
    l=l+1
    if l==5:
        continue
    print("2º loop sem 5: \t",l)

print("\t \n Desafio 15 \n")
#Nesse desafio tinha que contar quantas frutas se repetia qual era

fruts = [ 'maça','maça','maça','maça','laranja','laranja','acerola', "tomate"]
#foi informado o vetor e suas frutas
unico = set(fruts)
#usada a função de remover do vetor todas as frutas que se repetem
print('unico = ', unico)
#aqui eu printo a nova lista sem repetição, para poder depois fazer a comparação
v=0
#Inicion uma contadora com zer
for frut in unico:
#Meu primeiro for para percorrer a lista 'unico'
    for frut2 in fruts:
#Meu 2 for para percorrer a lista fruts
        if frut == frut2:
    #Aqui comparo o elemento da lista 'unico' com os elementos da lista 'fruts' se sao iguais
            v=v+1
        #A contadora inicia a guardar cada vez que o elemento se repete
    print("Foi encontrada: {}x  {} ".format(v,frut))
#Mostro na tela a fruta e sua quantidade de repetiçao
    v =0
#Zero minha contadora de novo para ela poder contar e armazenar de novo os elementos que se repetem
   
