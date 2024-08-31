from tkinter import *
from os.path import abspath

root=Tk()

imagen = PhotoImage(file=r'C:\Users\gabri\Documents\Python\Capacitacion3_Django\InterfazGrafica\prueba.gif')
label = Label(root, image=imagen)
label.pack()
'''
textoNuevo = StringVar()
textoNuevo.set('Python')

root.title('Bienvenidos')
root.config(width=400,height=300)

label = Label(root,text="Hola mundo")
label.place(x=100,y=30)
label.config(bg='blue',fg='red',font=('Verdana',20))


label = Label(root,text="Bienvenidos")
label.place(x=200,y=70)

label.config(bg='red',fg='blue',font=('Verdana',20),textvariable=textoNuevo)

'''


root.mainloop()