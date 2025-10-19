def calcular_elemento(año):
     num_ultimo=año % 10
     if num_ultimo==0 or num_ultimo== 1: return "metal"
     elif num_ultimo== 2 or num_ultimo==3: return "agua"
     elif num_ultimo== 4 or num_ultimo==5: return "madera"
     elif num_ultimo== 6 or num_ultimo==7: return "fuego"
     elif num_ultimo== 8 or num_ultimo== 9: return "tierra"
     else: 
      return "none"
        
def generar_prediccion( nombre, elemento, numero_suerte):
     match numero_suerte:
         case 1: print(f"Querido {nombre}, veo que tu elemento es {elemento}! Segun mis fuentes, este dia te pasara algo sorpendente que te caeras para atras")
         case 2: print(f"Ohh, siento una gran energia viniendo de ti, {nombre}. Debe ser tu gran elemento de {elemento}! Este es solo para los mas fuertes, asi que ve para adelante y haz esa cosa que te da miedo hacer.")
         case 3: print(f"{nombre}, tienes un elemento excepcional! el {elemento} indica que las penas desapareceran este dia, porque las riquezas se avecinan ;)")
         case 4: print(f"Vaya vaya, {nombre} tienes un elemento peculiar, el {elemento} siempre indica misterio~ sera un dia muy peculiar.")
         case _: print ("No es posible, intentelo de nuevo")
                          
def iniciar_oraculo():
     while True:
             
        print("Bienvenido a este oraculo :) ")
        respuesta= input ("DESEA CONTINUAR? (Si/No) ")
        if respuesta== "no":
         print ("Okey, adios.")
         break

        nombre= input("Usuario, escriba su nombre por favor: ")
        año= int(input("Ahora su año de nacimiento: "))
        numero_suerte=int( input("Por ultimo, escoja un número del 1 al 4: "))
        print ("*"*30)
        print ("*"*30)
        edad= 2025 - año
        print(f"{nombre}, al parecer tienes...", edad, "años.")

        elemento=calcular_elemento(año)
        
        generar_prediccion(nombre,elemento, numero_suerte)
iniciar_oraculo()