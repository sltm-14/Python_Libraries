import tkinter # only import tkinr

def saludo_1():
    print("Botón 1")


# Create a window
ventana_1 = tkinter.Tk()
ventana_1.geometry("500x300") # tamaño de la ventana

boton_1 = tkinter.Button(ventana_1, bg = "pink", text = "Botón 1",padx = 50, pady = 20, command = saludo_1)
boton_1.pack()



def saludo_2(nombre):
    print("Botón 2 " + nombre)

ventana_2 = tkinter.Tk()
ventana_2.geometry("500x300")

boton_2 = tkinter.Button(ventana_2, bg = "blue", text = "Botón 2",padx = 50, pady = 20, command = lambda: saludo_2(":D"))
boton_2.pack()




ventana_3 = tkinter.Tk()
ventana_3.geometry("500x300")

boton_3 = tkinter.Button(ventana_3, bg = "green", text = "Botón 3",padx = 50, pady = 20, command = lambda: print("Botón 3"))
boton_3.pack()



ventana_1.mainloop() # Lleva el registro de lo que succcede en  nuestra ventana
ventana_2.mainloop()
ventana_3.mainloop()
