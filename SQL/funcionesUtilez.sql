SELECT replace(nombre,'Jugo','extracto') as nombre from producto where idProducto = 12;

select concat(nombre,repeat('0',3), YEAR(NOW())) AS CODIGO from empleado;

select reverse (nombre) as inverso from producto;

select substring(nombre,9,3) as subcadena from producto where idProducto=12;