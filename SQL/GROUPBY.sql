select idFactura, SUM(precioUnitario * cantidad) as total from detalle_factura GROUP BY idFactura;

select idCliente,count(idFactura)as facturas from factura GROUP BY idCliente;