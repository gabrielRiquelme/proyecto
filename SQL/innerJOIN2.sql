select
factura.idFactura as factura,
cliente.nombre as cliente,
empleado.nombre as empleado
from factura
inner join cliente on cliente.idCliente = factura.idCliente
inner join empleado on empleado.idEmpleado = factura.idEmpleado
order by factura.idFactura;