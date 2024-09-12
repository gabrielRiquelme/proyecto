import sqlite3

conexion = sqlite3.connect('Productos.db') #Primer conexion DB#
cursor=conexion.cursor()

'''

cursor.execute('CREATE TABLE PRODUCTOS (CODIGO_P VARCHAR(20) PRIMARY KEY,NOMBRE_P VARCHAR(20),SECCION_P VARCHAR(20))')

productos= [
    ('AR1','Leche','Lacteos'),
    ('AR2','Facturas','Panaderia'),
    ('AR3','Asado','Carniceria'),
]

cursor.executemany('INSERT INTO PRODUCTOS VALUES(?,?,?)',productos)

'''

cursor.execute('INSERT INTO PRODUCTOS VALUES("AR4","Gaseosa","Bebidas")')

conexion.commit()

conexion.close()