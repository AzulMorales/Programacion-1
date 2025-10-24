cursos=[]

while True: 
    decision= int(input("Bienvenido usuario, que desea hacer?: " \
    "1.Agregar " \
    "2.Modificar " \
    "3.Eliminar " \
    "4.Ver (cursos, lista de alumnos) " \
    "5.Salir " ))

    match decision: 
         case 1: 
            nombre=input("Ingrese el nombre del curso: ")
            instructor= input("Ingrese el nombre del instructor: ")
            aula= input("Ingrese el aula: ")
            alumnos= input("Ingrese todos los alumnos: ").split(",")
            curso=[]
            curso.append([nombre, instructor, aula ,alumnos])
            cursos.append([nombre, instructor, aula,alumnos])
            print("El curso se ha añadido correctamente")

         case 2:
            decision_2= int(input("¿Que desea modificar?" \
            "1.Instructor " \
            "2.Aula " \
            "3.Dar de alta a un alumno " \
            "4.Dar de baja a un alumno " \
            "5.Nombre del curso " \
            "6.Nombre de un alumno "))
            if decision_2== 1:
                indice=int(input("Cual curso elegira? (0,1,2..) "))
                cursos[indice][1]= input("Ingrese el nuevo nombre del instructor: ")
                print("El instructor se ha cambiado correctamente")

            elif decision_2 == 2:
               indice=int(input("Cual curso elegira? (0,1,2..) "))
               cursos[indice][2] = input("Ingrese la nueva aula: ")
               print("El aula se ha cambiado correctamente")

            elif decision_2 == 3:
               indice=int(input("Cual curso elegira? (0,1,2..) "))
               nuevo_alumno = input("Ingrese el nombre del alumno a dar de alta: ")
               cursos[indice][3].append(nuevo_alumno)
               print("El alumno se ha dado de alta correctamente")

            elif decision_2 == 4:
               indice=int(input("Cual curso elegira? (0,1,2..) "))
               print("lista de alumnos:", cursos[indice][3])
               alumno_baja = input("Ingrese el nombre del alumno a dar de baja: ")
               if alumno_baja in cursos[indice][3]:
                  cursos[indice][3].remove(alumno_baja)
                  print("El alumno se ha dado de baja correctamente ")
               else:
                    print("El alumno no se encuentra en la lista")
                    
            elif decision_2==5:
                indice=int(input("Cual curso elegira? (0,1,2..) "))
                cursos[indice][0]= input("Ingrese el nuevo nombre del curso: ")
                print("El nombre del curso se ha cambiado correctamente")
                    
            elif decision_2==6:
                indice=int(input("Cual curso elegira? (0,1,2..) "))
                print("Lista de alumnos: ", cursos[indice][3])
                antes_nombre= input("Ingrese el nombre del alumno que desea cambiar: ")
                if antes_nombre in cursos[indice][3]:
                    nuevo_nombre= input("Ingrese el nuevo nombre: ")
                    cursos[indice][3].remove(antes_nombre)
                    cursos[indice][3].append(nuevo_nombre)
            
            else:
               print("Opcion no valida.")
            
         case 3:
          indice=int(input("¿Cual curso desea eliminar? "))
          if 0<= indice < len(cursos):
             cursos.pop(indice)
             print("El curso se ha eliminado correctamente")
          else:
              print("Curso no encontrado")
            
         case 4:
          decision_3=int(input("Eliga una opcion: " \
          "1.Ver los cursos " \
          "2.Ver el listado de alumnos "))
          if decision_3== 1:
             print("Aqui tiene los cursos: ")
             for i, curso in enumerate(cursos):
                    print(f"{i}. {curso[0]} (Instructor: {curso[1]}, Aula: {curso[2]})")
                    
          elif decision_3 == 2:
             indice = int(input("¿De qué curso desea ver los alumnos? (0,1,2..): "))
             if 0<= indice < len(cursos):
                print("Lista de alumnos:", cursos[indice][3])
             else:
                print("Curso no válido")

         case 5:
          break
         case _:
          print("Opcion no valida.")

