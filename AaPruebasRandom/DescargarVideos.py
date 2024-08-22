import youtube_dl

# URL del video
url = input('Ingrese la URL del video: ')
name = input('Ingrese nombre: ')

# Configuración para descargar el video
ydl_opts = {
    'format':'best',
    'outtmpl': f'C:/Users/sofia/Videos/Descargas/{name}.%(ext)s',
}

# Crea un objeto YoutubeDL y descarga el video
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Descarga completada.")
