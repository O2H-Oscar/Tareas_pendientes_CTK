import tkinter as tk            # Importar tkinter para crear la GUI
import customtkinter as ctk     # Importar customtkinter para una apariencia más moderna
from tkinter import ttk         # Importa el submódulo de ttk para una apariencia mejorada de los widgets
import os                       # Importar os para manejar rutas de archivos
import sys                      # Importar sys para manejar el sistema y rutas de archivos




# Funciones

def resource_path(relative_path):  # Función para obtener la ruta absoluta de un recurso

    """Obtiene la ruta absoluta al recurso, trabajando tanto en desarrollo como en el ejecutable."""
    try:
        # PyInstaller crea una carpeta temporal y guarda el archivo dentro de ella
        base_path = sys._MEIPASS
    except AttributeError:
        # Obtiene la carpeta donde se encuentra el script
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    # Combina la carpeta base con el recurso relativo
    final_path = os.path.join(base_path, relative_path)
    
 
    return final_path  # Devuelve la ruta completa para usarla luego

# Llamada a la función con el archivo que necesitas
resource_path("tareas.ico")  # Aquí pasa el nombre del recurso


def leyenda(canvas):
    # Dibujar la leyenda en el Canvas
    colores= {
        1:('deep sky blue', '> 3 días'),
        2:('yellow3','1 - 3 días'),
        3:('red2',' <  1'),
    }

    tamanno = 10
    margen = 10
    espacio = 70

    for estado,(color,texto) in colores.items():
        x = espacio + (estado-1)*(tamanno + estado + 180)
        y = margen

        canvas.create_rectangle(x,y,x+tamanno,y+tamanno,fill=color)
        canvas.create_text(x+25,tamanno + 5,text=texto, anchor='w', font=('Arial',9))





# Ventana principal

root=ctk.CTk()                                  # Crear la ventana principal
root.geometry("580x650")                        # Establecer el tamaño de la ventana
root.title("Tareas pendientes")                 # Establecer el título de la ventana
root.resizable(False,False)                     # Hacer la ventana no redimensionable
icon_path = resource_path("tareas.ico")         # Obtener la ruta del icono
root.iconbitmap(icon_path)                      # Establecer el icono de la ventana
ctk.set_appearance_mode("light")                # Establecer el modo de apariencia a claro


# Frames


frame_superior=ctk.CTkFrame(root,fg_color="light blue",height = 240)          # Crear un frame superior con color de fondo azul claro y altura de 240
frame_superior.pack(side="top",fill="both")                                   # Empaquetar el frame en la parte superior y llenar el espacio disponible
frame_superior.pack_propagate(False)                                          # Evita que el frame cambie de tamaño

frame_interior=ctk.CTkFrame(frame_superior,fg_color="light blue",height = 80,width=560)      # Crear un frame interior con color de fondo azul claro y tamaño específico
frame_interior.pack(side="top",padx=5,pady=5)                                                # Empaquetar el frame interior en la parte superior con un margen de 5 píxeles
frame_interior.pack_propagate(False)  # Evita que el frame cambie de tamaño

frame_inferior=ctk.CTkFrame(root,fg_color="light blue")                       # Crear un frame inferior con color de fondo azul claro
frame_inferior.pack(side="bottom",fill="both",expand="True")                  # Empaquetar el frame en la parte inferior y llenar el espacio disponible
frame_inferior.pack_propagate(False)                                          # Evita que el frame cambie de tamaño


# Etiquetas

etiqueta_fecha=ctk.CTkLabel(frame_interior,text="Fecha",font=("Arial",14,'bold'))     # Crear una etiqueta con el texto "Fecha" y fuente Arial de tamaño 14 y negrita
etiqueta_fecha.pack(side="left",padx=(32,5),pady=(30,10))                             # Empaquetar la etiqueta a la izquierda con un margen de 32 píxeles a la derecha y 30 píxeles arriba y 10 píxeles abajo

# Entradas

entrada_fecha=ctk.CTkEntry(frame_interior,placeholder_text="DD-MM-YYYY",width=80,font=("Arial",10,'bold'))  # Crear una entrada de texto con un marcador de posición "DD-MM-YYYY" y fuente Arial de tamaño 10 y negrita
entrada_fecha.pack(side="left",padx=(2,0),pady=(30,10))                           # Empaquetar la entrada a la izquierda con un margen de 2 píxeles a la derecha y 30 píxeles arriba y 10 píxeles abajo

# TextBox
entrada_texto = ctk.CTkTextbox(frame_superior,width=560,height=90,corner_radius=5,font=("Arial",14))  # Crea un cuadro de texto con una fuente Arial 14 para escribir las tareas pendientes
entrada_texto.pack(side="top",pady=(25,10))  # Posiciona el cuadro de texto en la ventana principal con 25 píxeles en la parte superior del eje Y y 10 píxeles en la parte inferior del mismo eje

# Crear una variable de control para el OptionMenu
menu_opcines_var = ctk.StringVar(value="Ordenar por...")  # Crear una variable de control para el OptionMenu con un valor inicial


optionmenu = ctk.CTkOptionMenu(frame_interior, 
                              values=["Fecha","Creación"],
                                variable=menu_opcines_var ,
                                width=90,
                                fg_color='DodgerBlue3',
                                button_color='firebrick1',
                                dropdown_fg_color="DodgerBlue3",
                                dynamic_resizing=True,
                                text_color='White',
                                corner_radius=5,
                                dropdown_text_color='White',
                                font=('Arial',12),
                                dropdown_hover_color='firebrick1')

#Ubicación del menú de opciones
optionmenu.pack(side='right',padx=(0,50),pady=(30,10))


# Botones 

boton_guardar=ctk.CTkButton(frame_interior,text="💾  Guardar",fg_color="DodgerBlue3",width=85,hover_color="RoyalBlue2") # Crear el botón Guardar, al hacer clic en el se ejecutará la función guardar_nota
boton_guardar.pack(side="left",padx=(80,0),pady=(30,10))                          # Empaquetar el botón a la izquierda con un margen de 80 píxeles a la derecha y 30 píxeles arriba y 10 píxeles abajo


# Canvas
canvas= tk.Canvas(frame_inferior,width=580,height=50,bg="light blue", highlightthickness=0,bd=0)   # Crea el widget Canvas donde se plasmará la leyenda de descripción de la columna "Estado"
canvas.pack(side="bottom",pady=(0,10))



# Treeview

# Estilos

style = ttk.Style()
#style.theme_use("clam")
style.configure("Treeview",background="white",foreground="black",font=('Arial',10),rowheight=100)  # configura el estilo de cuerpo de Treeview 
style.configure("Treeview.Heading",font=('Arial',12,'bold')) # Configura el estilo de las cabeceras de las columnas del Treeview
style.map("Treeview",background=[("selected","sky blue")])  # Color de fondo al seleccionar una fila

# Definiendo Treeview
tree = ttk.Treeview(frame_inferior,columns=("TAREA","FECHA"),show="tree headings",style="Treeview")  # Se crea una instancia de la clase Treeview y se definen las columnas, la estructura del widget y el estilo

# Definir encabezados
tree.heading("#0",text="Estado",anchor="center")
tree.heading("TAREA",text="Tarea",anchor="center")
tree.heading("FECHA",text="Fecha",anchor="center")

# Configuración de las columnas
tree.column("#0",width=2,anchor="center")
tree.column("TAREA",width=300,anchor="center")
tree.column("FECHA",width=20,anchor="center")

# Ubicación Treeview
tree.pack(fill="both",expand=True,pady=(0,20))
                      









# Llamada de funciones

leyenda(canvas)





root.mainloop()


