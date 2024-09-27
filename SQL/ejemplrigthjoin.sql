SELECT factura.id as factura, cliente.id, cliente.nombre
FROM cliente
RIGHT JOIN factura on factura.id_cliente = cliente.id
order by factura.id;