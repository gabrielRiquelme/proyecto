from tkinter import*

root = Tk()

barraMenu = Menu(root)
root.config(menu=barraMenu)

archivoMenu=Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
archivoMenu.add_command(label="nuevo Archivo")
archivoMenu.add_command(label="nueva Ventana")
archivoMenu.add_separator()
archivoMenu.add_command(label="SAlir")


archivoEditar=Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Editar",menu=archivoEditar)
archivoEditar.add_command(label="Deshacer")
archivoEditar.add_command(label="Rehacer")
archivoEditar.add_separator()
archivoEditar.add_command(label="SAlir")


archivoAyuda=Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)
archivoAyuda.add_command(label="Acerca de")
archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_separator()
archivoAyuda.add_command(label="SAlir")

root.mainloop()