import tkinter as tk

def enviar_formulario():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    correo = entry_correo.get()
    genero = var_genero.get()
    
    mensaje = f"Nombre: {nombre}\n Apellido: {apellido}\n Correo Electronico {correo}\n Genero: {genero}"
    label_resultado.config(text=mensaje)
    
#creando la ventana de la aplicacion
 
ventana = tk.Tk()
ventana.title('formulario de registro de ususario')

#impu para ingresar nombre 

label_nombre = tk.Label(ventana, text = "Nombre: ")
label_nombre.pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

#impu para ingresar apellido

label_apellido = tk.Label(ventana, text = "Apellido: ")
label_apellido.pack()
entry_apellido = tk.Entry(ventana)
entry_apellido.pack()

#impu para ingresar correo 

label_correo = tk.Label(ventana, text="correo Electronico: ")
label_correo.pack()
entry_correo = tk.Entry(ventana)
entry_correo.pack()

#etiqueta de radio para seleccionar el generoi 

label_genero = tk.Label(ventana, text="Genero: ")
label_genero.pack()

var_genero = tk.StringVar()
var_genero.set("Masculino") #valor predeterminado

radio_masculino = tk.Radiobutton(ventana, text="Masculino", variable=var_genero, value ="Masculino")
radio_masculino.pack()

radio_femenino = tk.Radiobutton(ventana, text="Femenino", variable=var_genero, value="Femenino" )
radio_femenino.pack()

# boton par enviar el formulario 

boton_enviar = tk.Button(ventana, text="enviar", command=enviar_formulario)
boton_enviar.pack()

# Etiqueta para mostrar el Resultado

label_resultado = tk.Label(ventana, text="")
label_resultado.pack()

#ejecutar la ventana de la aplicacion
ventana.mainloop() 