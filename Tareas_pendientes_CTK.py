import tkinter as tk
import customtkinter as ctk
import os
import sys

#Funciones

def resource_path(relative_path):
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






# Ventana principal

root=ctk.CTk()
root.geometry("580x650")
root.title("Tareas pendientes")
root.resizable(False,False)
icon_path = resource_path("tareas.ico")
root.iconbitmap(icon_path)
ctk.set_appearance_mode("light")

root.mainloop()


