class Clase1:
    def metodo1(self):
        print('Hola desde Metodo 1')

class Clase2:
    def metodo2(self):
        print('Hola desde Metodo 2')

class Clase3(Clase2,Clase1):
    def metodo3(self):
        print('Hola desde Metodo 3')

c = Clase3()

c.metodo1()
c.metodo2()
c.metodo3()
