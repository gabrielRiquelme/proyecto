class A():
    def __init__(self):
        self._contador = 0 #Buena practica agregar el _ #
        self._cuenta = 0

    def incrementar(self):
        self._contador += 1

    def cuenta(self):
        return self._contador

a = A()
print(a._cuenta)
a._cuenta = 20
print(a._cuenta)
#print(a.cuenta)#

#a._cuenta = 20 #Ejemplo de mala practica, no se llama y se modifican atributos de esta manera. Se realiza con metodos set#

#print(a.cuenta)#



    