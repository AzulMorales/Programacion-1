#if else if
edad = int(input("Dime tu edad: "))

if edad>= 25 and edad <18: 
    print ("Eres un adolescente.")
elif edad >= 18:
    print ("Eres un adulto.")
    print ("Tienes que trabajal.")
else:
  print("Todavia eres un niño.")



#match

opcion = int(input("""
1. Agregar   
2. Editar
3. Eliminar
4. Leer
5. Finalizar
"""))

match opcion: 
   case 1: 
      print ("se ha agregado correctamente.")
   case 2: 
      print ("Se ha modificado correctamente. ")
   case 3: 
      print ("Se ha eliminado correctamente. ")
   case 4: 
     print ("El usuario registrado se llama Jorge. ")
   case _:
     print ("Terminar")