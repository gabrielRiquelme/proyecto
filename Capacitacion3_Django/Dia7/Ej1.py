class Persona:
    def __init__(self,nombre,edad,sexo,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.nacionalidad = nacionalidad

    def datos_Personales(self):
        print(f'El nombre de la persona es: {self.nombre}')
        print(f'La edad de la persona es: {self.edad}')
        print(f'El sexo de la persona es: {self.sexo}')
        print(f'El sexo de la persona es: {self.nacionalidad}')

persona1 = Persona('Juan',21,'Masc','ARG')
persona1.datos_Personales()


