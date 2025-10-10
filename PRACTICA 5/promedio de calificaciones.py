total_calificaciones= 0
alumnos= 0
while alumnos<10: 
    a= int(input("Indique la calificación: "))

    total_calificaciones= total_calificaciones + a
    alumnos= alumnos +1

promedio= total_calificaciones/10
print("El promedio de calificaciones es: ", promedio)