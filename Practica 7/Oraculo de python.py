def iniciar_oraculo():
     print("¡Bienvenido a este oraculo :)))!")
     while True:
       input("¿Está seguro que desea continuar para conocer su destino???? (si/no): ")
       nombre= input("Primero, por favor escriba su nombre: ")
       elemento= int(input("Y su año de nacimiento: "))
       numSuerte=int(input("¡Excelente! por ultimo elija un numero del (1,4): "))

       edad= 2025-elemento
       print(f"querido {nombre}, se que tienes....{edad} años ;)")

       def calcular_elemento(elemento):
           año= elemento%10
           if año== 0 or 1:
               return "metal"
           elif año== 2 or 3:
               return "agua"
           elif año== 4 or 5:
               return "madera"
           elif año== 6 or 7:
               return "fuego"
           elif año== 8 or 9:
               return "tierra"
           
           def generar_prediccion(nombre, calcular_elemento, numSuerte):
                 match numSuerte:
                     case 1: 
                         print(f"**** {nombre}, veo que eres del elemento {elemento} querido usuario, ese elemento solo lo tienen los trabajadores determinados! sigue asi con ese gran esfuerzo. **** ")
                     case 2: 
                         print(f"**** Ohhh, querido {nombre}, tienes el elemento de las personas sensibles, el elemento {elemento}! ten cuidado con tus dulces sentimientos~****")
                     case 3: 
                         print(f"**** {nombre} asi que eres del elemento {elemento}, significa que eres una persona confiable! deberias confiar mucho más en ti ;) ****")
                     case 4: 
                         print(f"**** {nombre}, eres del elemento {elemento}, significa que tu corazon es muy grande! no te contengas con nada y haz eso que deseas hacer ^^ ****")

                   




