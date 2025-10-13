texto=input("Escriba un texto: ")
if "python" in texto:
    print("se que escribiste python :)")
else:
    print("No se encontro python")

a=input("Ahora escriba una letra: ")
b=input("Escriba la segunda letra: ")
c=input("Escriba la tercera letra: ")

t= texto. lower()
l1= a. lower()
l2= b. lower()
l3= c. lower()

contador1=0
contador2= 0
contador3=0
contador4=0
for character in t:
    if character ==l1:
        contador1 += 1
    if character ==l2:
        contador2 += 1
    if character ==l3: 
        contador3 += 1

p= t. split() 
for _ in p:
    contador4 +=1
invertido= ""
for character in p:
    invertido= character+invertido

if p:
    primera=p[0] 
    ultima=p[-1]
else: 
    primera=""
    ultima=""

print("Número de",a, "encontradas: ", contador1)
print("Número de",b, "encontradas: ", contador2)
print("Número de",c,"encontradas: ", contador3)
print("Total de palabras: ", contador4)
print("primera letra del texto: ", primera)
print("Ultima letra del texto: ", ultima)
print("texto al reves: ", invertido )