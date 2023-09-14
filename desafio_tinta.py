def tinta(rend,alt,larg):
    a = larg*alt
    qt = a/rend
    return qt

rend = float(input('Informe rendimento de tinta = '))
altura= float(input('Informe altura da parede: '))
largura = float(input("Informe a largura da parede: "))

t = tinta(rend,altura,largura)
print("Voce vai precisar de {}L de tinta".format(t))