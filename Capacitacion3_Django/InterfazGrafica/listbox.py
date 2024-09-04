from tkinter import*
def agregar():
    listaproductos.insert(END,entrada.get())


root = Tk()
root.geometry('400x400')

productos = Label(root,text='Productos')
productos.pack()

listaproductos = Listbox(root,width=50)
listaproductos.insert(0,'carne')
listaproductos.insert(2,'pollo')
listaproductos.insert(3,'verdura')
listaproductos.insert(4,'agua')
listaproductos.pack()

#ELiminar productos#

listaproductos.delete(0)

entrada = Entry(root,bd=10)
entrada.pack()

btn = Button(root,text='Agregar productos',bd=1,command=agregar)
btn.pack()








root.mainloop()