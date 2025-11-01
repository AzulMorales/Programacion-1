import modelos.curso
from modelos.curso import agregar_curso
from modelos.alumno import agregar_alumno
cursos = {}
alumnos = {}
while True:
    print("*" * 30)
    print("Bienvenido a isw Acaddemy")
    print("*" * 30)
    op1 = int(input("¿Que desea hacer? " \
        "1.Agregar, " \
        "2.Modificar, " \
        "3.Eliminar, " \
        "4.Ver (cursos, lista de alumnos), " \
        "5.Salir "))
    match op1:
        case 1:
            op2 = int(input("Que desea agregar? " \
                "1.Curso, " \
                "2.Alumno "))
            if op2 == 1:
                if op2 == 1:
                    nuevo_curso = agregar_curso()
                    cantidad=int(input("Cuantos alumnos desea agregar al curso? "))
                    for _ in range(cantidad):
                        nuevo_alumno = agregar_alumno()
                        id_alumno = nuevo_alumno["id"]
                        nuevo_curso["Alumnos"][id_alumno] = nuevo_alumno
                        print("Alumnos agregado al curso")
                    clave = nuevo_curso["aula"]
                    cursos[clave] = nuevo_curso
                    print("Curso agregado")
            elif op2 == 2:
                nuevo_alumno = agregar_alumno()
                clave = nuevo_alumno["id"]
                alumnos[clave] = nuevo_alumno
                print("Alumno agregado ;)")

        case 2:
            op3 = int(input("¿Que desea modificar?" \
                "1.Instructor, " \
                "2.Aula, " \
                "3.Nombre del curso, " \
                "4.Datos del alumno "))
            if op3 == 1:
                print(cursos["aula"])
                indice = int(input("Ingrese el número de aula del curso a modificar: "))
                if indice in cursos:
                    nuevo_instructor = input("Ingrese el nuevo nombre del instructor: ")
                    cursos[indice]["Instructor"]["nombre"] = nuevo_instructor
                    print("Instructor modificado")
            elif op3 == 2:
                print(cursos["aula"])
                indice = int(input("Ingrese el número de aula del curso a modificar: "))
                if indice in cursos:
                    nueva_aula = int(input("Ingrese el nuevo número de aula: "))
                    cursos[nueva_aula] = cursos.pop(indice)
                    cursos[nueva_aula]["aula"] = nueva_aula
                    print("Aula modificada")
            elif op3 == 3:
                print(cursos["aula"])
                indice = int(input("Ingrese el número de aula del curso a modificar: "))
                if indice in cursos:
                    nuevo_nombre = input("Ingrese el nuevo nombre del curso: ")
                    cursos[indice]["Nombre del curso"] = nuevo_nombre
                    print("Nombre del curso modificado")
            elif op3 == 4:
                id_alumno = int(input("Ingrese el ID del alumno a modificar: "))
                if id_alumno in alumnos:
                    nuevo_nombre = input("Ingrese el nuevo nombre del alumno: ")
                    alumnos[id_alumno]["nombre"] = nuevo_nombre
                    print("Nombre del alumno modificado")

        case 3:
            op4 = int(input("Que desea eliminar? " \
                "1. curso, " \
                "2. alumno "))
            if op4 == 1:
                print(cursos["aula"])
                indice = int(input("Ingrese el número de aula del curso a eliminar: "))
                if indice in cursos:
                    curso_eliminado = cursos.pop(indice)
                    print("Curso eliminado")
            elif op4 == 2:
                print(alumnos["id"])
                id_alumno = int(input("Ingrese el ID del alumno a eliminar: "))
                if id_alumno in alumnos:
                    alumno_eliminado = alumnos.pop(id_alumno)
                    print("Alumno eliminado")

        case 4:
            op5 = int(input("Eliga una opcion: " \
                "1.Ver los cursos " \
                "2.Ver el listado de alumnos de un curso "))
            if op5 == 1:

                    print(cursos)
            elif op5 == 2:
                print(cursos["aula"])
                indice = int(input("Ingrese el número de aula del curso para ver sus alumnos: "))
                if indice in cursos:
                    print("Alumnos del curso:")
                    print(cursos[indice]["Alumnos"])

        case 5:
            break
        case _:
            print("Opcion no valida.")
