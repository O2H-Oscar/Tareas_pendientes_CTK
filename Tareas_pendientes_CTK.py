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


# Frames


frame_superior=ctk.CTkFrame(root,fg_color="light blue",height = 240)
frame_superior.pack(side="top",fill="both")
frame_superior.pack_propagate(False)  # Evita que el frame cambie de tamaño

frame_interior=ctk.CTkFrame(frame_superior,fg_color="light blue",height = 80,width=560)
frame_interior.pack(side="top",padx=5,pady=5)
frame_interior.pack_propagate(False)  # Evita que el frame cambie de tamaño

frame_inferior=ctk.CTkFrame(root,fg_color="light blue")
frame_inferior.pack(side="bottom",fill="both",expand="True")
frame_inferior.pack_propagate(False)  # Evita que el frame cambie de tamaño


# Etiquetas

etiqueta_fecha=ctk.CTkLabel(frame_interior,text="Fecha",font=("Arial",14,'bold'))
etiqueta_fecha.pack(side="left",padx=(32,0),pady=(30,10))

# Entradas

entrada_fecha=ctk.CTkEntry(frame_interior,placeholder_text="DD-MM-YYYY",width=80,font=("Arial",10,'bold'))
entrada_fecha.pack(side="left",padx=(2,0),pady=(30,10))




#Botones



#Treeview




# Llamada de funciones







root.mainloop()


