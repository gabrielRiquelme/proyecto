select sum(cantidad) as total from detalle_factura;

select sum(cantidad) as total from detalle_factura where idProducto=2;

select count(*) as producto from producto where idCategoria=2;

select count(distinct IdCategoria) from categoria;