SELECT
factura.idFactura as factura,
empleado.nombre as empleado
from factura
right join empleado on factura.idEmpleado = empleado.idEmpleado
ORDER BY factura.idFactura;