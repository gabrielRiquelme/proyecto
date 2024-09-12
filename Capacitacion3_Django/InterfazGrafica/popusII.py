from tkinter import*
from tkinter import filedialog

root = Tk()


def abrir():
    archivo=filedialog.askopenfilename(title='Abrir',filetypes=(("Documento Texto","*.txt"),(("Hoja calculo","*.xlsx"))))
    print(archivo)

Button(root,text='Archivos',command=abrir).pack()


    


root.mainloop()