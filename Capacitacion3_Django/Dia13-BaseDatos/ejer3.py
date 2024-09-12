import sqlite3

conexion = sqlite3.connect('Personas.dbo') #Primer conexion DB#
cursor=conexion.cursor()

#CREAR#

persona= [
    ('44420810','LeoMessi',22,'Masculino'),
]

cursor.executemany('INSERT INTO PERSONAS VALUES(?,?,?,?)',persona)

cursor.execute('SELECT * FROM PERSONAS WHERE NOMBRE="SOfi"')
sof=cursor.fetchall()
print(sof)

cursor.execute('UPDATE PERSONAS SET DNI=44444444 WHERE DNI=44420810')


cursor.execute('DELETE FROM PERSONAS WHERE NOMBRE="Juana"')

conexion.commit()
conexion.close()