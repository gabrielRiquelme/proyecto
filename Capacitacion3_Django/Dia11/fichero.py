from io import open

'''
fichero = open('archivo.txt','w') #Creacion y apertura de archivo#
texto= 'Hola Mundo\nEstoy estudiando Python'#Manipulacion#
fichero.write(texto)
fichero.close()#Cierre de archivo.#
'''
'''
fichero = open('archivo.txt','r')#Creacion y apertura de archivo con permisos de leer#
#texto = fichero.read()#asignamos a texto el contenido de fichero#
linea = fichero.readlines()
fichero.close()
print(linea[1])
'''
fichero = open('archivo.txt','a')
fichero.write('\nEste es el metodo append')
fichero.close()
print(fichero)