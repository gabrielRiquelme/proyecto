class Persona():
    def __init__(self):
        pass

    @classmethod
    def saludar(cls,nombre):
        print('Te saludo desde un metodo de clase', nombre)


Persona.saludar('Juan')