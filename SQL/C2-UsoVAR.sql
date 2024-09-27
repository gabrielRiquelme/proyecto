SELECT avg(puntuacion) INTO @promedio_puntuacion FROM libro;

select @promedio_puntuacion;

Select * FROM libro 
WHERE puntuacion > @promedio_puntuacion
ORDER BY puntuacion DESC;

--
-- USO DE VARIABLES, ALAMCENAR Y REUTILIZAR VALORES DENTRO DE UNA CONSULTA.
-- 