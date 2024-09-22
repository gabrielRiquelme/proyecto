SELECT
factura.idFactura as factura,
idProducto as producto
from factura
left join detalle_factura on factura.idFactura = detalle_factura.idFactura
AND factura.idFactura =1;