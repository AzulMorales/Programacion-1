import random
palabras= ("abeja","araña", "burro","cabra", "cerdo", "cisne"
           ,"erizo","zorro","gallo","mosca","rosal","avion","lunes"
           ,"chica","nariz","dedos","reloj","verde","brazo")

while True: 
    palabra= palabras[random.randint(0,len(palabras)-1)]
    wordle= list(palabra)
    print("""\033[1;34;47m
===========================================[WORDLE]===========================================
    Bienvenido ya he elegido la palabra secreta. Tienes 5 intentos para adivinar la palabra 
==============================================================================================\033[0;37;40m""")
    for i in range(5):
        intento= input("Ingrese una palabra de 5 letras sin acento: ").lower()[:5]
        indice= 0 
        correctas= 0
        resultado= ""
        for letra in intento:
            if letra == wordle[indice]:
                correctas+=1
                resultado +="\033[1;32m"+letra+"\033[0;40m"
            elif letra in wordle:
                resultado +="\033[1;33m"+letra+"\033[0;40m"
            else:
                resultado +="\033[1;31m"+letra+"\033[0;40m"
            indice+=1
        print(resultado)
        if correctas ==5:
            break

    if correctas==5:
        print(f"Felicidades la palabra era: \033[1;32m{palabra}\033[0;40m has acertado")
    else:
        print(f"lo siento, has fallado. La palabra era: \033[1;31m{palabra}\033[0;30m ")
        
    opcion=input("Desea jugar de nuevo? (si/no) ").lower()
    if opcion== "no":
        break