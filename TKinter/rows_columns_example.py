import tkinter

ventana = tkinter.Tk()
ventana.geometry("500x250")

boton_1 = tkinter.Button(ventana, text = "boton_1", width = 10, height = 5)
boton_2 = tkinter.Button(ventana, text = "boton_2", width = 10, height = 5)
boton_3 = tkinter.Button(ventana, text = "boton_3", width = 10, height = 5)

boton_1.grid(row = 0, column = 0)
boton_2.grid(row = 1, column = 0)
boton_3.grid(row = 2, column = 0)

ventana.mainloop()
