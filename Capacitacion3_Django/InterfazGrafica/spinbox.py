from tkinter import*

root = Tk()
root.geometry("400x300")

w = Spinbox(root,values=("Python","HTML5","JAVASCRIPT"))
w.pack()

w = Spinbox(root,values=("boca","river","Independiente"))
w.pack()



root.mainloop()