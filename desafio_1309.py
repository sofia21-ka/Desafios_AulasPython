def dobroNum(num):
    
    res = num*2
    return res

def quadNum(num):
    dob = dobroNum(num)
    res = num **dob
    return res,dob

num = int (input("num: "))

resultado_quad, resultado_dobro = quadNum(num)

# Exibir os resultados
print(f'O dobro de {num} é {resultado_dobro}')
print(f'O quadrado do dobro de {num} é {resultado_quad}')




