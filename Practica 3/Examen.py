correcto = 0
incorrecto = 0


print("1. ¿Cuál de los siguientes componentes NO es parte fundamental de la arquitectura de Von Neuman?")
print ("a) Tarjeta gráfica.")
print ("b) Memoria principal.")
print ("c) Sistema de entrada/salida.")
print ("d) CPU.")

Respuesta_1= (input("Escriba el inciso: "))
match Respuesta_1:
    case "a": 
        print("Correcto!")
        correcto += 1
    case "b": 
        print("Incorrecto")
        incorrecto += 1
    case "c": 
        print("Incorrecto")
        incorrecto += 1
    case "d": 
        print("Incorrecto")
        incorrecto += 1
    case _:
        print("Respuesta inválida") 
        incorrecto+=1


print("2. El lenguaje maquina esta compuesto por:")
print ("a) Simbolos lógicos y matemáticos.")
print ("b) Pseudocódigo.")
print ("c) Instrucciones en inglés abreviado.")
print ("d) Código binario.")
Respuesta_2= (input("Escriba el inciso: "))

match Respuesta_2:
    case "a": 
        print("Incorrecto")
        incorrecto +=1
    case "b": 
        print("Incorrecto")
        incorrecto +=1
    case "c": 
        print("Incorrecto")
        incorrecto +=1
    case "d": 
        print("Correcto!")
        correcto +=1
    case _:
        print("Respuesta inválida") 
        incorrecto+=1


print("3. Un lenguaje de programacion de alto nivel se caracteriza por:")
print ("a) Ser el más rápido en tiempo de ejecución.")
print ("b) Tener un control directo y preciso sobre el hardware.")
print ("c) Ser independiente de la arquitectura de la computadora.")
print ("d) Ser muy dificl de aprender y leer.")
Respuesta_3= (input("Escriba el inciso: "))

match Respuesta_3:
    case "a": 
        print("Incorrecto")
        incorrecto +=1
    case "b": 
        print("Incorrecto")
        incorrecto +=1
    case "c": 
        print("Correcto!")
        correcto += 1
    case "d": 
        print("Incorrecto")
        incorrecto += 1
    case _:
        print("Respuesta inválida")
        incorrecto+=1 


print("4. ¿Qué es un algoritmo?")
print ("a) Una secuencia de pasos finitos y bien definidos para resolver un problema.")
print ("b) Un lenguaje de programacion específico.")
print ("c) El código fuente de un programa de computadora.")
print ("d) Un conjunto de instrucciones escritas en código binario.")
Respuesta_4= (input("Escriba el inciso: "))

match Respuesta_4:
    case "a": 
        print("Correcto!")
        correcto += 1
    case "b": 
        print("Incorrecto")
        incorrecto += 1
    case "c": 
        print("Incorrecto")
        incorrecto += 1
    case "d": 
        print("Incorrecto")
        incorrecto += 1
    case _:
        print("Respuesta inválida") 
        incorrecto+=1


print("5. En pseudocódigo, ¿qué estructura de control se utiliza para ejecutar un bloque de código solo si se cumple una condición específica?")
print ("a) Repetitiva Mientras.")
print ("b) Repetitiva Para.")
print ("c) Secuencial.")
print ("d) Condicional o de selección.")
Respuesta_5= (input("Escriba el inciso: "))

match Respuesta_5:
    case "a": 
        print("Incorrecto")
        incorrecto += 1
    case "b": 
        print("Incorrecto")
        incorrecto +=1 
    case "c": 
        print("Incorrecto")
        incorrecto +=1
    case "d": 
        print("Correcto!")
        correcto +=1
    case _:
        print("Respuesta inválida")


print("6. El propósito principal del pseudocódigo es:")
print ("a) Traducir automáticamente código de alto nivel a lenguaje máquina.")
print ("b) Planificar y describir la lógica de un algoritmo de forma legible para los humanos.")
print ("c) Ejecutar programas de forma más eficiente que un lenguaje compilado.")
print ("d) Proporcionar un control directo sobre los registros del procesador.")
Respuesta_6= (input("Escriba el inciso: "))

match Respuesta_6:
    case "a": 
        print("Incorrecto")
        incorrecto +=1
    case "b": 
        print("Correcto!")
        correcto +=1
    case "c": 
        print("Incorrecto")
        incorrecto +=1
    case "d": 
        print("Incorrecto")
        incorrecto +=1
    case _:
        print("Respuesta inválida") 
        incorrecto+=1


print("7. Un programa de computadora es esencialmente:")
print ("a) Una colección de algoritmos.")
print ("b) El sistema operativo de una computadora.")
print ("c) Un dispositivo de hardware.")
print ("d) Una secuencia de instrucciones que la computadora ejecuta.")
Respuesta_7= (input("Escriba el inciso: "))

match Respuesta_7:
    case "a": 
        print("Incorrecto")
        incorrecto +=1
    case "b": 
        print("Incorrecto")
        incorrecto +=1
    case "c": 
        print("Incorrecto")
        incorrecto +=1
    case "d": 
        print("Correcto!")
        correcto +=1
    case _:
        print("Respuesta inválida")
        incorrecto+=1

print("8. ¿Cuál es la principal diferencia entre un bucle Mientras(while) y un bucle Repetir(do-while)?")
print ("a) No hay ninguna diferencia, son intercambiales.")
print ("b) El bucle Repetir solo usa números, mientras que el Mientras puede usar cualquier condición.")
print ("c) El bucle Mientras es más rápido que el Repetir.")
print ("d) El bucle Mientras puede no ejecutarse, mientras que el Repetir se ejecuta al menos una vez.")
Respuesta_8= (input("Escriba el inciso: "))

match Respuesta_8:
    case "a": 
        print("Incorrecto")
        incorrecto+=1
    case "b": 
        print("Incorrecto") 
        incorrecto+=1
    case "c": 
        print("Incorrecto")
        incorrecto+=1
    case "d": 
        print("Correcto!")
        correcto+=1
    case _:
        print("Respuesta inválida")
        incorrecto+=1


print("9. El lenguaje Ensamblador es considerado un lenguaje de nivel..")
print("a) Medio.")
print("b) Alto.")
print("c) Bajo.")
print("d) Muy alto.")

Respuesta_9= (input("Escriba el inciso: "))

match Respuesta_9:
    case "a": 
        print("Incorrecto")
        incorrecto+=1
    case "b": 
        print("Incorrecto")
        incorrecto+=1
    case "c": 
        print("Correcto!")
        correcto+=1
    case "d": 
        print("Incorrecto")
        incorrecto+=1
    case _:
        print("Respuesta inválida")
        incorrecto+=1


print("10. ¿Qué estructura de control es más adecuada para iterar sobre una secuencia de elementos un número de veces conocido de antemano?")
print("a) Bucle para.")
print("b) Sentencia condicional SI.")
print("c) Bucle repetir.")
print("d) Bucle mientras.")

Respuesta_10= (input("Escriba el inciso: "))

match Respuesta_10:
    case "a": 
        print("Correcto!")
        correcto+=1
    case "b": 
        print("Incorrecto")
        incorrecto+=1
    case "c": 
        print("Incorrecto")
        incorrecto+=1
    case "d": 
        print("Incorrecto")
        incorrecto+=1
    case _:
        print("Respuesta inválida")
        incorrecto+=1

print("Respuestas correctas:", correcto)
print("Respuestas incorrectas:", incorrecto)