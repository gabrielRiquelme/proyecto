import youtube_dl
from tkinter import *

def descargarvidedos():
    ydl_opts = {
    'format':'best',
    'outtmpl': f'/Descargas/{name.get()}.%(ext)s',
    }

    # Crea un objeto YoutubeDL y descarga el video
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url.get()])

    print("Descarga completada.")



root = Tk()
frame= Frame(root)
frame.pack()

url = StringVar()
name = StringVar()

entradaUrl = Entry(frame)
entradaUrl.pack()
entradaUrl.config(bd=8,font='Curier,20',textvariable=url)

entradaUrl = Entry(frame)
entradaUrl.pack()
entradaUrl.config(bd=8,font='Curier,20',textvariable=name)

envio = Button(frame, text='Enviar')
envio.pack()
envio.config(bd=5,font='Curier,10',command=descargarvidedos)

root.mainloop()