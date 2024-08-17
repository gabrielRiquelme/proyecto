class Personal:
    def __init__(self,antiguedad,especialidad):
        self.antiguedad = antiguedad
        self.especielidad = especialidad

    def Sueldo(self):
        if (self.especielidad == 'BF'):
            return 10 * self.antiguedad
        else:
            return 15 * self.antiguedad
        
class Supervisor(Personal):
    def __init__(self,cargo):
        super().__init__(5,cargo)

class Operador(Personal):
    def __init__(self,cargo):
        super().__init__(2,cargo)

if __name__ == '__main__':

    personal1 = Personal(10, 'Jefe de desarrollo')
    print(f'Sueldo del personal completo es : {personal1.Sueldo()}')

    supervisor1 = Supervisor('BF')

    print(f'El sueldo del supervisor es: {supervisor1.Sueldo()}')

    operador1 = Operador('Programador')

    print(f'El sueldo del operador es: {operador1.Sueldo()}')