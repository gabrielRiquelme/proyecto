class Calculadora():
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2
    
    
    def suma(self):
        print('La suma de:{} + {} es igual a: {}'.format(self._num1, self._num2, (self._num1 + self._num2)))
    
    
    def resta(self):
        print('La resta de:{} - {} es igual a: {}'.format(self._num1, self._num2, (self._num1 - self._num2)))
    
    
    def multiplicacion(self):
        print('La multiplicacion de:{} * {}es igual a: {}'.format(self._num1, self._num2, (self._num1 * self._num2)))

    
    def division(self):
        print('La division de:{} / {}es igual a: {}'.format(self._num1, self._num2, (self._num1 / self._num2)))

a = Calculadora(10 , 5)

a.suma()
a.resta()
a.multiplicacion()
a.division()

