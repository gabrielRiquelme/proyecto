SELECT
cliente.nombre as cliente,
factura.idFactura as factura
from cliente
right join factura on factura.idCliente = cliente.idCliente
order by factura.idFactura;

