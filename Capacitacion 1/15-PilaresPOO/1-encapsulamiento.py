class A():
    def __init__(self):
        self.contador=0

    def incrementar(self):
        self.contador += 1
    
    def cuenta(self):
        return self.contador
    
class B():
    def __init__(self):
        self.__contador=0

    def incrementar(self):
        self.__contador += 1
    
    def cuenta(self):
        return self.__contador
    
a = A()

print(a.cuenta())
a.incrementar()
print(a.cuenta())
print(a.contador)

print( '*'*20 +'OBJETO 2'+ '*'*20)
b = B()
print(b.cuenta())
b.incrementar()
print(b.cuenta())

#Encapsular atributos es una buena practica, dado que no se DEBE acceder a atributos POR FUERA DE LA CLASE como se realizo en linea 26, para esto agregamos "__" previo al nombre#
