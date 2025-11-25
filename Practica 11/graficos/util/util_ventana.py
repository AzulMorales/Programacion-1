#Crear una funcion para centrar la ventana

def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho=ventana.winfo_screenwidth()
    pantalla_largo=ventana.winfo_screenheight()
    x= int((pantalla_ancho/2) - (ancho/2)) #Determina el centro de la pantalla horizontalmente
    y= int((pantalla_largo/2) - (alto/2)) #Determina el centro de la pantalla verticalmente
    return ventana.geometry (f"{ancho} X {alto} + {x} + {y}") #WxH+X+Y