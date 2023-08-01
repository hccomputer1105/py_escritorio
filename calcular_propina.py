import tkinter as tk

def calcular_propina():
    try:
        monto_total = float(entry_monto_total.get())
        porcentaje_propina = float(entry_porcentaje_propina.get())

        propina = monto_total * (porcentaje_propina / 100)
        total_a_pagar = monto_total + propina

        label_resultado_propina.config(text=f"Propina: ${propina:.2f}")
        label_resultado_total.config(text=f"Total a pagar: ${total_a_pagar:.2f}")

    except ValueError:
        label_resultado_propina.config(text="Error: Ingresa números válidos.")
        label_resultado_total.config(text="")

# Crear la ventana de la aplicación
ventana = tk.Tk()
ventana.title("Calculadora de Propinas")

# Etiqueta e Input para ingresar el monto total
label_monto_total = tk.Label(ventana, text="Monto Total:")
label_monto_total.pack()
entry_monto_total = tk.Entry(ventana)
entry_monto_total.pack()

# Etiqueta e Input para ingresar el porcentaje de propina
label_porcentaje_propina = tk.Label(ventana, text="Porcentaje de Propina:")
label_porcentaje_propina.pack()
entry_porcentaje_propina = tk.Entry(ventana)
entry_porcentaje_propina.pack()

# Botón para calcular la propina
boton_calcular = tk.Button(ventana, text="Calcular Propina", command=calcular_propina)
boton_calcular.pack()

# Resultados de la calculadora
label_resultado_propina = tk.Label(ventana, text="")
label_resultado_propina.pack()
label_resultado_total = tk.Label(ventana, text="")
label_resultado_total.pack()

# Ejecutar la ventana de la aplicación
ventana.mainloop()

        
        
        
        
        