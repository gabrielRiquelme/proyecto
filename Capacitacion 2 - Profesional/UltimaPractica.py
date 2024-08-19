# File path
file_path = r'C:\Users\sofia\OneDrive\Documentos\Riki\proyecto\Capacitacion 2 - Profesional\doc.txt'
# Open the file in 'r' mode (read mode)
file = open(file_path, 'r')
# Read the content of the file
content = file.read()
with open('fichero.txt', 'w') as archivo:
    # Escribe texto en el archivo
    archivo.write(content)
print(f'Contenido de archivo DOC.TXT{content}')
print(f'Contenido de archivo FICHERO.TXT{content}')