select idFactura, sum(precioUnitario * cantidad) as total
from detalle_factura
group by idFactura
having total > 14;