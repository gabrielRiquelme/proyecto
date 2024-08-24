class Empleado:
    def __init__(self,ocupacion,salario,vacaciones):
        self.__ocupacion = ocupacion
        self.__salario = salario
        self.__vacaciones = vacaciones

    def datos_Empleado(self):
        print(f'El nombre de la persona es: {self.__ocupacion}')
        print(f'La edad de la persona es: {self.__salario}')
        print(f'El sexo de la persona es: {self.__vacaciones}')