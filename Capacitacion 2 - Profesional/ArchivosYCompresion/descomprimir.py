import zipfile
from zipfile import ZipFile

with zipfile.ZipFile(r'C:\Users\sofia\OneDrive\Documentos\Riki\proyecto\Capacitacion 2 - Profesional\ArchivosYCompresion\archivo.zip', 'r') as file:
    file.extractall()

