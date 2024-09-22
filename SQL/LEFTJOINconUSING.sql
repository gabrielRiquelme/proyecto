select cliente.idCliente as id,
cliente.nombre as nombre,
factura.idFactura as factura
from cliente
left join factura using(idCliente)
where idCliente=1;