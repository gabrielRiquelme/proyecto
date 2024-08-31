from tkinter import *
from os.path import *

root = Tk() #Declaro ventana#

root.title('Riki')

#root.resizable(0,0) #Manejo de extension de ventan#

root.iconbitmap(r"C:\Users\gabri\Documents\Python\Capacitacion3_Django\InterfazGrafica\lm10.ico")
#root.geometry("600x350") Seteo automatico de tamaño al momento de abrirse la pestaña
miFrame= Frame(root)
miFrame.pack(fill="x", expand=True)
miFrame.config(width=400,height=300)
miFrame.config(cursor='pirate')
miFrame.config(bg='red')
miFrame.config(bd="20")
miFrame.config(relief="ridge")

root.config(cursor='boat')
root.config(bg='blue')
root.config(bd="20")
root.config(relief="ridge")



root.mainloop() #Sentencia para que queda abierta la ventana#