SELECT *
FROM cliente
WHERE NOT EXISTS
(SELECT *
FROM factura
WHERE factura.id_cliente= cliente.id);

