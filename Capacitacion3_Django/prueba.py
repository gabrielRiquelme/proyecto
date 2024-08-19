import yt_dlp

# URL del video
url = 'https://portaldevideos.ffyb.uba.ar/video/bcm-2023-biomembranas'

# Configuración para descargar el video
ydl_opts = {
    'outtmpl': 'Descargas/PruebaVid.%(ext)s',
}

# Crea un objeto YoutubeDL y descarga el video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Descarga completa.")
