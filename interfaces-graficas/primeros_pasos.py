import tkinter

ventana = tkinter.Tk()
ventana.geometry("400x300")

def saludo(nombre):
    print('Que ondaaaaa!!!!' + nombre)

boton1 = tkinter.Button(ventana, text = "Presiona", command = lambda: saludo('Agripino'))
boton1.pack()

ventana.mainloop()
