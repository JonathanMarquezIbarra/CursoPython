import tkinter

ventana = tkinter.Tk()
ventana.geometry("400x300")

caja_texto = tkinter.Entry(ventana)
caja_texto.pack()

def texto_in():
    mensaje = caja_texto.get()
    print(mensaje)

boton1 = tkinter.Button(ventana, text = 'Guardar', command = texto_in)
boton1.pack()



ventana.mainloop()
