class Persona():
    nacionalidad = 'Arg'
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def correr(self):
        print('Estoy corriendo...')


persona1 = Persona('Juan',20)

persona1.correr()