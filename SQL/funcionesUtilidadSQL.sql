select database();

select user();

select version();

select * from cliente;
select found_rows();

Insert into producto (nombre,idCategoria,precioUnitario) values('Arroz Yaman','2',4);

select last_insert_id();

Insert into producto (nombre,idCategoria,precioUnitario) values('Ciruela','6','2');

select row_count();