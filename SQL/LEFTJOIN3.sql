select
factura.idFactura as factura,
cliente.nombre as cliente,
idProducto as producto
from cliente
left join factura on factura.idCliente = cliente.idCliente
left join detalle_factura on detalle_factura.idFactura = factura.idFactura
order by cliente.nombre,factura ASC;