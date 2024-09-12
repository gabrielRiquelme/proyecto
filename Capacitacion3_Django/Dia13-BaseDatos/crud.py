'''
C = CREATE = Crear
R = READ = Leer
U = UPDATE = Actualizar
D = DELETE = Eliminar
'''

import sqlite3

conexion = sqlite3.connect('MisProductos.db')

cursor = conexion.cursor()
'''
cursor.execute('SELECT * FROM MISPRODUCTOS WHERE SECCION="Lacteos"') SELECCIONAR PRODUCTO
'''

#cursor.execute('UPDATE MISPRODUCTOS SET SECCION="Lacteos" WHERE SECCION="Lacteo"') Actualizar nombre o algun campo
#productos=cursor.fetchall()
#print(productos)

cursor.execute('DELETE FROM MISPRODUCTOS WHERE ID=6')

conexion.commit()
conexion.close()
