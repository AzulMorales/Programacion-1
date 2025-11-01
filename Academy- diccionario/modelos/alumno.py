def agregar_alumno():
    nombre_alumno=input("Ingrese el nombre del alumno: ")
    edad_alumno=int(input("Ingrese la edad del alumno: "))
    semestre_alumno=int(input("Ingrese el semestre del alumno: "))
    id_alumno=int(input("Ingrese el ID del alumno: "))
    carrera_alumno=input("Ingrese la carrera del alumno: ")
    
    alumno= {
                "nombre": nombre_alumno,
                "edad": edad_alumno,
                "semestre": semestre_alumno,
                "id": id_alumno,
                "carrera": carrera_alumno
           }
    return alumno
