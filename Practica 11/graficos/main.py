import tkinter as tk
from tkinter import font, filedialog, messagebox
from config import TITULO, COLOR_BARRA_SUPERIOR, COLOR_PANEL_PRINCIPAL, COLOR_MENU_LATERAL
from util.util_ventana import centrar_ventana 
from util.util_imagenes import leer_imagen
import pygame
import os

def bind_hover_events(button):
    button.bind("<Enter>", lambda event: on_enter(event, button))
    button.bind("<Leave>", lambda event: on_leave)

def on_enter(event, button):
    button.config(bg="#0099cc")

def on_leave(event, button):
    button.config(bg=COLOR_MENU_LATERAL)

def toggle_panel():
    if menu_lateral.winfo_ismapped():
        menu_lateral.pack_forget()
    else:
        menu_lateral.pack(side=tk.LEFT, fill="y")

def limpiar_panel(panel):
    for widget in panel.winfo_children():
        widget.destroy()

def mostrar_inicio():
    limpiar_panel(panel_principal)
    label_imagen_principal= tk.Label(panel_principal, text="Inicio")
    label_imagen_principal.pack()
def mostrar_ventas():
    limpiar_panel(panel_principal)
    label_imagen_principal= tk.Label(panel_principal, text="Ventas")
    label_imagen_principal.pack()
    
def mostrar_productos():
    limpiar_panel(panel_principal)
    label_imagen_principal= tk.Label(panel_principal, text="Productos")
    label_imagen_principal.pack()

def mostrar_reportes():
    limpiar_panel(panel_principal)
    label_imagen_principal= tk.Label(panel_principal, text="Reportes")
    label_imagen_principal.pack()

def mostrar_usuarios():
    limpiar_panel(panel_principal)
    label_imagen_principal= tk.Label(panel_principal, text="Usuarios")
    label_imagen_principal.pack()

def mostrar_salir():
    limpiar_panel(panel_principal)
    label_imagen_principal= tk.Label(panel_principal, text="Salir")
    label_imagen_principal.pack()


def cargar_cancion():
    ruta=filedialog.askopenfile(title="Elige un MP3", filetypes=[("Archhivos MP3", "*.mp3")])
    if ruta:
        return (ruta,os.path.basename(ruta))
    
def reproducir(ruta, estado):
    if ruta:
        try:
            if estado== "pause":
                #si estaba pausado, le quitamos el pause
                pygame.mixer_music.unpause()
                estado="play"
            else:
                pygame.mixer_music.load(ruta)
                pygame.mixer_music.play()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo reproducir el archivo {e}")
    else: 
        messagebox.showwarning("Atencion", "Primerp debes cargar una cancion")

def pausar():
    pygame.mixer_music.pause()
    return "pause"

def detener():
    pygame.mixer_music.stop()
    return "stop"

def cambiar_volumen():
    #el volumen va de 1 a 100
    pygame.mixer.set

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

btn_menu=tk.Button(barra_superior, text="\uf0c9", font=fontawesome, bg=COLOR_BARRA_SUPERIOR,
                   fg= "#f2f2f2")
btn_menu.pack(padx=10, pady=10, side=tk.LEFT)

label= tk.label(barra_superior, text="pROGRAMACION 1", font="Roboto 24"
                ,bg=COLOR_BARRA_SUPERIOR, fg="#f2f2f2")
label.pack(padx=10, pady=10, side=tk.LEFT)

btn_stop=tk.Button(barra_superior, text="\uf04d", font="fontawesome", bg= COLOR_BARRA_SUPERIOR
                   , fg="#f2f2f2", bd=0)

btn_play=tk.Button(barra_superior, text="\uf04b", font="fontawesome", bg= COLOR_BARRA_SUPERIOR
                   , fg="#f2f2f2", bd=0)

btn_pause=tk.Button(barra_superior, text="\uf04c", font="fontawesome", bg= COLOR_BARRA_SUPERIOR
                   , fg="#f2f2f2", bd=0)

volumen= tk.Scale(barra_superior, from_=0, to=100, bg=COLOR_BARRA_SUPERIOR, fg="#f2f2f2",
                  bd=0, border=0, resolution=1, orient="horizontal")

volumen.pack(padx=4, pady=10, side=tk.RIGHT)
btn_pause.pack(padx=4, pady=10, side=tk.RIGHT)
btn_play.pack(padx=4, pady=10, side=tk.RIGHT)
btn_stop.pack(padx=4, pady=10, side=tk.RIGHT)

imagen_perfil= leer_imagen("./imagenes/user.png", (100,100))
label_perfil= tk.Label(menu_lateral, bg=COLOR_MENU_LATERAL, image=imagen_perfil)

label_perfil.pack




btn_inicio=tk.Button(menu_lateral, text="\uf015 Inicio",  font=fontawesome,
                     bg=COLOR_MENU_LATERAL, fg="#f2f2f2", bd=0, width=10,
                     command=mostrar_inicio)
btn_inicio.pack(side=tk.TOP)

btn_ventas=tk.Button(menu_lateral, text="\uf81d Ventas",  font=fontawesome,
                     bg=COLOR_MENU_LATERAL, fg="#f2f2f2", bd=0, width=12)
btn_ventas.pack(side=tk.TOP)

btn_productos=tk.Button(menu_lateral, text="\uf201 Productos",  font=fontawesome,
                     bg=COLOR_MENU_LATERAL, fg="#f2f2f2", bd=0, width=12)
btn_productos.pack(side=tk.TOP)

btn_reportes=tk.Button(menu_lateral, text="\uf15b Inicio", font=fontawesome,
                     bg=COLOR_MENU_LATERAL, fg="#f2f2f2", bd=0, width=12)
btn_reportes.pack(side=tk.TOP)

btn_usuarios=tk.Button(menu_lateral, text="\uf2f6 Usuarios",  font=fontawesome,
                     bg=COLOR_MENU_LATERAL, fg="#f2f2f2", bd=0, width=12)
btn_usuarios.pack(side=tk.TOP)

btn_salir=tk.Button(menu_lateral, text="\uf2f5 Salir", font=fontawesome,
                     bg=COLOR_MENU_LATERAL, fg="#f2f2f2", bd=0, width=12)
btn_salir.pack(side=tk.BOTTOM)

bind_hover_events(btn_inicio)
bind_hover_events(btn_ventas)
bind_hover_events(btn_productos)
bind_hover_events(btn_reportes)
bind_hover_events(btn_usuarios)
bind_hover_events(btn_salir)




root.mainloop()
