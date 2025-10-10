a=(input("¿Qué día de la semana es? "))
b= (input("¿Cuál es el clima? "))
match a:
 case "lunes":
     if b=="lluvioso": 
      print("Trabaja desde casa.")
     elif b=="nublado": print("Disfruta tu día trabajando.")
     else:("soleado",print("Ve a trabajar."))
 case "martes":
     if b=="lluvioso": print("Juega videojuegos.")  
     elif b=="nublado": print("Juega afuera.")
     else: ("soleado", print("Juega afuera con amigos."))

 case "miercoles":
     if b=="lluvioso": print("Duerme un rato más.")  
     elif b=="nublado": print("Mira una pelicula.")
     else: ("soleado", print("Duerme temprano."))

 case "jueves":
     if b=="lluvioso": print("Mira una serie .")  
     elif b=="nublado": print("Invita a tus amigos a tu casa.")
     else: ("soleado", print("LLama a tus amigos."))

 case "viernes":
     if b=="lluvioso": print("Haz una lista de compras.")  
     elif b=="nublado": print("Haz las compras semanal.")
     else: ("soleado" ,print("Compra en línea."))

 case "sabado":
     if b=="lluvioso": print("Haz de comer.")  
     elif b=="nublado": print("Ve a una pijamada.")
     else: ("soleado", print("Termina tu tarea."))

 case "domingo":
     if b=="lluvioso": print("Duerme tarde.")  
     elif b=="nublado": print("Come con amigos.")
     else: ("soleado", print("Ve a la playa."))
 case _: 
      print("no valido")




