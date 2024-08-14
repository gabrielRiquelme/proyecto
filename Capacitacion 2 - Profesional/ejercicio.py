class Persona ():
    dni = 0
    nac = ''

    def __init__(self,nombre,edad,nacionalidad,dni): #variable de instancia#
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.dni = dni

    def devuelve_nombre(self):
        print(f'Nombre: {self.nombre}')

    def devuelve_edad(self):
        print(f'edad: {self.edad}')

    @classmethod
    def devuelve_DNI(cls,dn):
        print('Mi dni es:', dn)
   
    @classmethod
    def devuelve_nacionalidad(cls,nacio):
        print('Mi pais es:', nacio)

    def __str__(self): #Muestra mensaje al llamar al objeto#
        return f'Nombre:{self.nombre}\n Edad:{self.edad}\n Nacionalidad:{self.nacionalidad}\n DNI:{self.dni}\n'



persona1 = Persona('Juan',20,'Argentino',44420810)

print(persona1)

persona1.devuelve_nombre()
persona1.devuelve_edad()
Persona.devuelve_DNI(44420810)
Persona.devuelve_nacionalidad('Alemania')