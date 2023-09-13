#lista
#armazenar mais de uma informação em variaveis
#manter as sequencias dos dados em uma variavel

cidade = 'Rio de Janeiro'
cd2 = 'São Paulo'
cd3 = 'Salvador'
cds = ['Rio de Janeiro', 'São Paulo', 'Salvador']
print(cds)
#cds.append("Santa Cantarina")
#cds.remove('salvador')
#cds.insert(2,'manaus)
#cds.pop(0)
cds.sort()
print(cds)

let = ['a','b','c','d']
num = [1,2,3,4]

#final é  num + let
num.extend(let)
print(num)