class A():
    def __init__(self):
        self._cuenta = 0  #Buena practica agregar el _ #
        self._contador = 0 #Buena practica agregar el _ #
    
    @property    #Palbra reservada para lamar sin ()#
    def cuenta(self): #Metodo para mostrar atributo CUENTA, se genera uno por cada atributo a mostrar#
        return self._cuenta    
    
    @property    #Palbra reservada para lamar sin ()#
    def contador(self): #Metodo para mostrar atributo CUENTA, se genera uno por cada atributo a mostrar#
        return self._contador    


a = A()
#print(a._cuenta)

print(a.cuenta) #Llamado atravez de metodo#
print(a.contador) #Llamado atravez de metodo#
