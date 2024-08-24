class Persona:
    def __init__(self,nombre,edad,sexo):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo

    def datos_Personales(self):
        print(f'El nombre de la persona es: {self.__nombre}')
        print(f'La edad de la persona es: {self.__edad}')
        print(f'El sexo de la persona es: {self.__sexo}')