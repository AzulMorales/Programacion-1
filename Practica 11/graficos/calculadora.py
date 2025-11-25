import tkinter as tk
#1. Creacion de la ventana principal
root= tk.Tk()
root.title("Calculadora")
root.geometry("305x500")

#Agregar los widgets
botones_texto= ("C","/","X","-",
                "7","8","9","+",
                "4","5","6","",
                "1","2","3","=",
                "0",".","","")

historico= tk.Label(root,bg="#63B4FF", font= "Roboto 14",width=15, bd=0)

historico.pack(pady=5, padx=10, fill="x")

resultado=tk.Entry(root,bg="#afb5fc", bd=1,font="Roboto 24", width=15, justify="right")
resultado.pack(padx=10, fill="x")


contenedor_botones= tk.Frame(root, bg="#63B4FF")
contenedor_botones.pack(pady=5, padx=10, fill="both")

acumulador=0
for row in range(5):    
    for column in range(4):
        boton= tk.Button(contenedor_botones
                         ,text=botones_texto[acumulador] 
                         ,bg="#30378f"
                        ,fg="#afb5fc"
                        ,font="Roboto 20"
                        ,bd=0
                        , width=4)

 #pintar los botones de colores
        if botones_texto[acumulador]=="C":
             boton.config(bg="#bd7250")
        elif botones_texto[acumulador] in ("/","X","-","+"):
             boton.config(bg="#1e1a61")


        if botones_texto[acumulador]!= "":

            if botones_texto[acumulador]== "+":
                  boton.config(height=3)
                  boton.grid(row=row, column=column, rowspan=2,padx=1, pady=5)
              
            elif botones_texto[acumulador]== "=":
                 boton.config(height=3, bg="#7a2f2f")
                 boton.grid(row=row, column=column, rowspan=2,padx=1, pady=5)

            elif botones_texto[acumulador]== "0":
                     boton.config(width=8)
                     boton.grid(row=row, column=column,columnspan=2, padx=1, pady=5)

            elif botones_texto[acumulador] == ".":
                 boton.grid(row=row, column=column+1, padx=1, pady=5)

            else:
                boton.grid(row=row, column=column, padx=1, pady=5)



        acumulador+=1
        

root.mainloop() #Escuchador de eventos de tkinter