class Persona:
    def __init__(self,nombre,edad,sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    def datos_Personales(self):
        print(f'El nombre de la persona es: {self.nombre}')
        print(f'La edad de la persona es: {self.edad}')
        print(f'El sexo de la persona es: {self.sexo}')

per1 = Persona('Juan',21,'Masc')
per1.datos_Personales()
print('')
per2 = Persona('Juana',22,'fem')
per2.datos_Personales()
print('')
per3 = Persona('Cristina',24,'fem')
per3.datos_Personales()
