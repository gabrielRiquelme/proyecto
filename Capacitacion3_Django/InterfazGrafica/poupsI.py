from tkinter import*
from tkinter import messagebox

def salir():
    i = messagebox.askquestion("Salir","Estas seguro de que queres salir?")
    if i == "yes":
        root.destroy()

def acerca():
    messagebox.showinfo("Informacion","Creado por Juan R.")


def licencia():
    messagebox.showinfo("licencia","Licencia vigente hasta 2025")

def error():
    messagebox.showerror("error","Se ha producido un error fatal")

def deshacer():
    messagebox.askquestion("EStas seguro de querer deshacer?","Deshacer")


root = Tk()

barraMenu = Menu(root)
root.config(menu=barraMenu)

archivoMenu=Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
archivoMenu.add_command(label="nuevo Archivo")
archivoMenu.add_command(label="nueva Ventana",command=error)
archivoMenu.add_separator()
archivoMenu.add_command(label="SAlir",command=salir)


archivoEditar=Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Editar",menu=archivoEditar)
archivoEditar.add_command(label="Deshacer",command=deshacer)
archivoEditar.add_command(label="Rehacer")
archivoEditar.add_separator()
archivoEditar.add_command(label="SAlir",command=salir)


archivoAyuda=Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)
archivoAyuda.add_command(label="Acerca de",command=acerca)
archivoAyuda.add_command(label="Licencia",command=licencia)
archivoAyuda.add_separator()
archivoAyuda.add_command(label="SAlir",command=salir)

root.mainloop()