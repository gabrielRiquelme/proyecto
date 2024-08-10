class A():
    def __init__(self):
        self._cuenta = 0  #Buena practica agregar el _ #
        self._contador = 0 #Buena practica agregar el _ #
    
    @property    
    def cuenta(self):
        return self._cuenta
    
    @cuenta.setter #Creacion metodo SET#
    def cuenta(self, cuenta):
        self._cuenta = cuenta

    @property    
    def contador(self):
        return self._contador    

    @contador.setter #Creo metodo SET para modificar valores#
    def contador (self,contador):
        self._contador = contador

a = A()
#print(a._cuenta)

print('Valor de cuenta: ', a.cuenta) #Llamado atravez de metodo#
print('Valor de contador: ', a.contador) 
a.cuenta = 20 #Asigno valor utilizando metodo SET#
a.contador = 50 #Asigno valor utilizando metodo SET#
print('Valor de cuenta: ', a.cuenta)#Llamado atravez de metodo#
print('Valor de contador: ',a.contador) 

#Metodo get de lectura, NO puede faltar#
#Metodo set puede faltar#