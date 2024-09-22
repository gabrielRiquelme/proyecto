select
cliente.idCliente as id,
cliente.nombre as nombre,
factura.idFactura as factura
from cliente
left join factura on factura.idCliente = cliente.idCliente
AND cliente.idCliente = 1;