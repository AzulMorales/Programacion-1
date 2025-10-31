from modelos.alumno import agregar_alumno

from modelos.curso import agregar_curso

cursos={}
while True:
    print("Bienvenido a isw Acaddemy")
    print("*"*30)
    op1= int(input("¿Que desea hacer? " \
        "1.Agregar, " \
        "2.Modificar, " \
        "3.Eliminar, " \
        "4.Ver (cursos, lista de alumnos), " \
        "5.Salir " ))
    match op1:
        case 1:
            op2=(int(input("Que desea agregar? " \
            "1.Curso, " \
            "2.Alumno ")))
            if op2==1:
                nuevo_curso= agregar_curso()

            elif op2==2:
                nuevo_alumno= agregar_alumno()
            
            else: print("respuesta no valida")

        case 2:
                op3= int(input("¿Que desea modificar?" \
                "1.Instructor, " \
                "2.Aula, " \
                "3.Nombre del curso, " \
                "4.Datos del alumno "))


        case 3:
            op4=int(input("Que desea eliminar? " \
            "1. curso, " \
            "2. alumno "))


        case 4:
            op5=int(input("Eliga una opcion: " \
            "1.Ver los cursos " \
            "2.Ver el listado de alumnos "))

        
        case 5:
            break
        case _:
            print("Opcion no valida.")


