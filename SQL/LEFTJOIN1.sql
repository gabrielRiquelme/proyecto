select
cliente.nombre as cliente,
factura.idFactura as factura
from cliente
left join factura on cliente.idCliente = factura.idCliente
where factura.idFactura IS NULL
order by cliente.nombre;