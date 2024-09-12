from tkinter import*

def eleccion():
    elegir=""

    #if pizza.get()==1:
     #   elegir+=" Has elegido pizza\n"
    
    if hambu.get()==1:
        elegir+=" Has elegido hamburguesa\n"

    if vacio.get()==1:
        elegir+=" Has elegido vacio\n"
    

    if hambu.get() == 1 and vacio.get()==1:
        elegir+="tu orden final es: pizza,hamburguesa y vacio"

    imprimir.config(text=elegir)

root = Tk()

root.geometry("400x300")

frame = Frame(root)
frame.pack()

pizza = IntVar()
hambu = IntVar()
vacio = IntVar()


#foto1=PhotoImage(file=r'/home/jriquelme/Documentos/proyecto/Capacitacion3_Django/InterfazGrafica/pizza-margarita.gif')
foto2=PhotoImage(file=r'/home/jriquelme/Documentos/proyecto/Capacitacion3_Django/InterfazGrafica/hamburguesa.gif')
foto3=PhotoImage(file=r'/home/jriquelme/Documentos/proyecto/Capacitacion3_Django/InterfazGrafica/vacio.gif')

#Label(root,image=foto1).pack()
Label(root,image=foto2).pack()
Label(root,image=foto3).pack()

#Checkbutton(frame, text="Pizza",variable=pizza,onvalue=1 , offvalue=0,command=eleccion ).pack(side="right")
Checkbutton(frame, text="Hamburguesa",variable=hambu,onvalue=1 , offvalue=0,command=eleccion ).pack(side="right")
Checkbutton(frame, text="Asado",variable=vacio,onvalue=1 , offvalue=0,command=eleccion ).pack(side="right")

imprimir = Label(root)
imprimir.pack()




root.mainloop()