def agregar_curso():
    nombre_curso = input("Ingrese el nombre del curso: ")
    nombre_maestro = input("Ingrese el nombre del instructor: ")
    titulo = input("Ingrese el titulo del instructor: ")
    edad_maestro = int(input("Ingrese la edad del instructor: "))
    aula = int(input("Ingrese el numero de aula: "))

    curso = {
        "Nombre del curso": nombre_curso,
        "Instructor": {
            "nombre": nombre_maestro,
            "titulo": titulo,
            "edad": edad_maestro
        },
        "aula": aula,
        "Alumnos": {}
    }
    return curso

