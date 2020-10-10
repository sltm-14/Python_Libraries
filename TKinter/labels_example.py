import tkinter # only import tkinr

# Create a window
ventana = tkinter.Tk()
ventana.geometry("500x300") # tamaño de la ventana

etiqueta = tkinter.Label(ventana, text = "Hello, world!", bg = "pink") # Etiqueta que se presentara en ventana, bg es para el color del background
etiqueta.pack(side = tkinter.BOTTOM, fill = tkinter.BOTH, expand = True) # para hacer que el mensaje de arriba aparezca en pantalla, side indica dónde quiero que aparezca mi etiqueta



ventana.mainloop() # Lleva el registro de lo que succcede en  nuestra ventana
