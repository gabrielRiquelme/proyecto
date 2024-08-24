class Persona:
    def __init__(self,nombre,apellido,edad,sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo

    def datos_Personales(self):
        print(f'El nombre de la persona es: {self.nombre}')
        print(f'El nombre de la persona es: {self.apellido}')
        print(f'La edad de la persona es: {self.edad}')
        print(f'El sexo de la persona es: {self.sexo}')

class Empleado(Persona):
    def datosEmpleado(self,vacaciones,salario):
        print(f'Sus dias de vaciones son: {vacaciones}')
        print(f'Su salario es: {salario}')

miPersona = Persona('Raul',22,'Gonzales','Masculino')
miPersona.datos_Personales()
print('')
miEmpleado = Empleado('Juana','Riquelme',22,'FEM')
miEmpleado.datos_Personales()
miEmpleado.datosEmpleado(30,3000)