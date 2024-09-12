import sqlite3

conexion = sqlite3.connect('MisProductos.db') #Primer conexion DB#
cursor=conexion.cursor()
'''


cursor.execute('CREATE TABLE MISPRODUCTOS (ID INTEGER PRIMARY KEY AUTOINCREMENT,NOMBRE VARCHAR(20),SECCION VARCHAR(20))')
'''
productos= [
    ('Asado','Carniceria'),
    ('Frutas','Verduleria'),
    ('Torta','Reposteria'),
]

cursor.executemany('INSERT INTO MISPRODUCTOS VALUES(NULL,?,?)',productos)


conexion.commit()

conexion.close()