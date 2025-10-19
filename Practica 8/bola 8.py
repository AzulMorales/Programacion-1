import random

print("Bienvenido a la bola 8")
print("*"*30)
while True: 
    pregunta=input("Desea continuar? (si/no): ")
    if pregunta== "no":
        print ("Okey, vuelva pronto")
        break 

    input("Haga una pregunta de si/no: ")
    a= random.randint(1,20)
 
    match a: 
        case 1:print("Es cierto")
        case 1:print("Es decididamente asi")
        case 3:print("Sin lugar a dudas")
        case 4: print("Si, definitivamente")
        case 5:print("Puedes confiar en ello")
        case 6: print("Como yo lo veo,si")
        case 7: print ("Lo mas probable")
        case 8: print("Perspectiva buena")
        case 9: print("Si")
        case 10: print ("Las señales apuntan a que si")
        case 11: print("Respuesta confusa, vuelve a intentarlo")
        case 12: print("Vuelve a preguntar mas tarde")
        case 13: print("Mejor no decirte nada")
        case 14: print("No se puede predecir ahora")
        case 15: print("Concentrate y vuelve a preguntar")
        case 16: print("No cuentes con ello")
        case 17: print("Mi respuesta es no")
        case 18: print("Mis fuentes dicen que noo")
        case 19: print("Las perspectivas no son muy buenas")
        case 20: print("Muy dudoso")