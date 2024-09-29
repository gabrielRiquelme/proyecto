SELECT *
FROM cliente
LEFT JOIN factura
	ON factura.id_cliente = cliente.id
    WHERE factura.id_cliente IS NULL;
    