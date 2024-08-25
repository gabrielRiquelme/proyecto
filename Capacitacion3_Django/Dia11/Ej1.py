from io import open

fichero = open('archivo.py','w')
texto= 'print("Hola mundo")'
fichero.write(texto)
fichero.close()