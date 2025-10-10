while True:
    print("Calculadora Interactiva")
    print("1 . suma")
    print("2 . restar")
    print("3 . multiplicar")
    print("4 . dividir")
    print("5 . salir")

    op=(input("Eliga una opción (1 2,3,4,5): "))
    if op=="1":
        a=int(input("Elegiste sumar, indique un número: "))
        b=int(input("Otro número: "))
        c= a + b
        print("Su resultado es: ",c)
    elif op=="2":
        d=int(input("Elegiste restar, indique un número: "))
        e=int(input("Otro número: "))
        f= d - e
        print("Su resultado es: ",f)
    elif op=="3":
        g=int(input("Elegiste multiplicar, indique un número: "))
        h=int(input("Otro número: "))
        i= g * h
        print("Su resultado es: ",i)
    elif op=="4":       
        j=int(input("Elegiste dividir, indique un número: "))
        k=int(input("Otro número: "))
        l= j / k
        print("Su resultado es: ",l)
    elif op=="5":
        print("Eligio salir, adios.") 
        break
    else: 
        print("Opción no valida.")         