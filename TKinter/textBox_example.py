import tkinter # only import tkinr

def textoDeEntrada():
    texto = cajaTexto.get()
    print(texto)

ventana = tkinter.Tk()
ventana.geometry("500x300")

cajaTexto = tkinter.Entry(ventana,font = "Helvetica 20") #ventana en la que se muestra, fuente tamaño de letra
cajaTexto.pack()


boton = tkinter.Button(ventana,text = "click",command = textoDeEntrada)
boton.pack()

ventana.mainloop()
