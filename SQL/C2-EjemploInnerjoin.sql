SELECT factura.id,cliente.nombre
FROM factura
INNER JOIN cliente on factura.id_cliente = cliente.id
order by factura.id;