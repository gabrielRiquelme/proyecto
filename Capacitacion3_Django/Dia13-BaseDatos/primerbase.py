import sqlite3

conexion = sqlite3.connect('Mibase.db') #Primer conexion DB#
cursor=conexion.cursor()

#cursor.execute('CREATE TABLE USUARIOS(Nombre varchar(50),Edad integer,Sexo varchar(50))')

#cursor.execute("INSERT INTO USUARIOS VALUES('Maria',26,'Masculino')")

#cursor.execute('SELECT * FROM USUARIOS')
#usuarios = cursor.fetchone()
#print(usuarios)

#usuarios = [
#    ('Pepe',25,'Masculino'),
#    ('Rodrigo',30,'Masculino'),
#    ('Ana',29,'Femenino'),
#]

#cursor.executemany('INSERT INTO USUARIOS VALUES(?,?,?)',usuarios)

cursor.execute('SELECT * FROM USUARIOS')
usuarios = cursor.fetchall()
print(usuarios)

conexion.commit()

conexion.close()