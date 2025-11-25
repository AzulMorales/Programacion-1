import tkinter as tk
from tkinter import font
from config import TITULO, COLOR_BARRA_SUPERIOR, COLOR_PANEL_PRINCIPAL, COLOR_MENU_LATERAL
from util.util_ventana import centrar_ventana 

root= tk.Tk()
root.title(TITULO)
icon= tk.PhotoImage(file="C:/Users/alumnog/Documents/GitHub/Programacion-1/Practica 11/graficos/imagenes") #No se redimensiona

root.iconbitmap(False, icon)
#Geometry
centrar_ventana(root, 1024,600)

barra_superior= tk.Frame(root, height=50, bg= COLOR_BARRA_SUPERIOR)
barra_superior.pack(side=tk.TOP, fill="both")

menu_lateral= tk.Frame(root, width=150, bg=COLOR_MENU_LATERAL)
menu_lateral.pack(side=tk.LEFT, fill="both", expand=False)

panel_principal= tk.Frame(root, width=150,bg= COLOR_PANEL_PRINCIPAL)
panel_principal.pack(side=tk.RIGHT, fill="both", expand=True)


#fuentes_disponibles= list(font.families())
#fa_fonts= [f for f in fuentes_disponibles if "Awesome" in f]
#print(fa_fonts)
fontawesome= font("Font Awesome 7 Free", 20)
label= tk.label(barra_superior, text="f0c9", font= fontawesome)
label.pack(padx=10, pady=10)


root.mainloop()
