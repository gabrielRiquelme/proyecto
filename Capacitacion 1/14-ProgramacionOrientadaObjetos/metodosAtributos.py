#Definicion clase y creacion de atributos#
class FabricaTelefonos():
    marca = "Samsung"
    color = "Negro"
    mRam = 64
    almacenamiento = 128
    
    #Creacion de metodos(Funciones que realiza mi objeto)#
    
    def llamar(self, mensaje): #Todos los metodos llevan self##Metodo instancia#
        return mensaje
    
    def escucharMusica(self):
        print('Estas escuchando Música')

#Asignacion de atributos de mi molde (Clase)#
telefono = FabricaTelefonos()
telefono.marca
telefono.color
telefono.mRam
telefono.almacenamiento

#Uso metodos generados en clase#
print(telefono.llamar('Hola, Con quien hablo?'))
telefono.escucharMusica()

#Muestra atributos de mi objeto#
print(telefono.marca)
print(telefono.color)
print(telefono.mRam)
print(telefono.almacenamiento)
 
