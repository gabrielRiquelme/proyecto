class Estudiante():
    def __init__(self,nombre,notaAlumnos):
        self._nombre = nombre
        self._notaAlumno = notaAlumnos

    @property    #Creacion metodo GET, el cual muestra el nombre
    def nombre(self):
        return self._nombre
    
    @property     #Creacion metodo GET, el cual muestra la nota
    def notaAlumno(self):
        return self._notaAlumno
    
    @nombre.setter #Creacion metodo SET, el cual modifica el nombre
    def nombre(self, nombre):
        self._nombre = nombre

    @notaAlumno.setter #Creacion metodo SET, el cual modifica la nota
    def notaAlumno(self, notaAlumno):
        self._notaAlumno = notaAlumno

    def resultado(self):
        if self.notaAlumno >= 4:
            print('Estimado {} usted aprobo con:{}'.format(self.nombre,self.notaAlumno))
        else:
            print('Usted no ha aprobado')

alumno = Estudiante('Juan',9) #Genero el objeto alumno, de la clase estudiante#
alumno.resultado()

alumno2 = Estudiante('Sofia',10) #Genero el objeto alumno2, de la clase estudiante#
alumno2.resultado()