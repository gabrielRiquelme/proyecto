import pickle

class Persona:
    def __init__(self,nombre,edad,sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    def datos_Personales(self):
        print(f'El nombre de la persona es: {self.nombre}')
        print(f'La edad de la persona es: {self.edad}')
        print(f'El sexo de la persona es: {self.sexo}')

miPersona = Persona('Martin',22,'Masc')
miPersona2 = Persona('Maria',23,'FEM')
miPersona3 = Persona('Emilia',26,'Marciano')

listaPersonas = [miPersona,miPersona2,miPersona3]

fichero = open('Personas','wb')
pickle.dump(listaPersonas,fichero)
fichero.close()
del(fichero)

ficheroLeer = open('Personas','rb')
miPersona = pickle.load(ficheroLeer)
ficheroLeer.close()

for i in miPersona:
    print(i.datos_Personales())