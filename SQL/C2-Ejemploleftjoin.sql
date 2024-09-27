SELECT factura.id as factura, cliente.id, cliente.nombre
FROM cliente
LEFT JOIN factura on factura.id_cliente = cliente.id
WHERE factura.id is NULL
order by factura.id;