select concat(nombre,' ',apellido) as nombre from empleado;

select concat_ws(' ',nombre,apellido) as nombre from empleado;

select instr(nombre,'R') as posicion from producto where idProducto = 2;

select nombre,length(nombre) as longitudNombre from producto;