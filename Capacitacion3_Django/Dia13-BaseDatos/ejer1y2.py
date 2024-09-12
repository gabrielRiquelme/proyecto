import sqlite3

conexion = sqlite3.connect('Personas.dbo') #Primer conexion DB#
cursor=conexion.cursor()

cursor.execute('CREATE TABLE PERSONAS (DNI INTEGER PRIMARY KEY UNIQUE,NOMBRE VARCHAR(20),EDAD INTEGER,SEXO VARCHAR(20))')

personas= [
    ('44508393','Juan',22,'Masculino'),
    ('44522213','Juana',23,'Femenino'),
    ('42372382','SOfi',22,'Femenino'),
    ('45783838','Joan',18,'Masculino'),
    ('23823832','SAbrina',22,'Femenino'),
    ('44503393','Lautaro',22,'Masculino'),
    ('27678903','Abril',22,'Femenino'),
    ('12646788','Juance',47,'Masculino'),
    ('47388383','jincho',28,'Masculino'),
    ('28910920','Pipo',68,'Masculino'),
]

cursor.executemany('INSERT INTO PERSONAS VALUES(?,?,?,?)',personas)



conexion.commit()
conexion.close()