class Universidad():
    def __init__(self,nombreUni):
        self._nombreUniversidad = nombreUni

class Carrera():
    def __init__(self,especialidad):
        self._especialidad = especialidad

class Estudiante():
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad

class Persona(Universidad, Carrera, Estudiante):
    def __init__(self, nombreUni, especialidad, nombre, edad):
        Universidad.__init__(self, nombreUni)
        Carrera.__init__(self, especialidad)
        Estudiante.__init__(self, nombre, edad)

    def imprimir_atributos(self):
        print(f'Universidad: {self._nombreUniversidad}')
        print(f'Especialidad: {self._especialidad}')
        print(f'Nombre: {self._nombre}')
        print(f'Edad: {self._edad}')

juan = Persona('UNGS','Lic.Sistemas','Juan',21)
juan.imprimir_atributos()
       

