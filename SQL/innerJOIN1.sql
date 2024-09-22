select 
categoria.nombre as categoria,
producto.nombre as producto
from producto
inner join categoria on categoria.idCategoria = producto.idCategoria;
