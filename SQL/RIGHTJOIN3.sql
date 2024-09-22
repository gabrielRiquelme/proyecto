select
detalle_factura.idFactura as factura,
producto.nombre as nombre,
detalle_factura.cantidad as cantidad
from detalle_factura
right join producto on detalle_factura.idProducto = producto.idProducto
order by factura;