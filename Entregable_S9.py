
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

        def printname(self):
            print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, clave):
        super().__init__(fname + ' :C', lname)
        self._carrera = 'derecho'

    def getClave(self):
        return '161444'

    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

        def printname(self):
            print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, clave):
        super().__init__(fname + ' :C', lname)
        self._carrera = 'derecho'
        self._clave = clave

    def getClave(self):
        return self._clave

    def setClave(esta, clave):
        esta._clave = clave

    def getCarrera(self):
        return self._carrera

    def setCarrera(esta, carrera):
        esta._carrera = 'carrera' 

    def printname(self):
        self.lastname = 'Quintanar'
        super().printname() 
        print('soy estudiante') 
    
x = Student("Luis", "Quintanar", 161444)


print('clave alumno:', x.getClave())
x.setClave(161444)
print('clave alumno:', x.getClave())
