UPDATE empleado
SET email = REPLACE(email,'@bicitemp.com', '@libreriatest.com')
where email LIKE '%@bicitemp.com%';

SET SQL_SAFE_UPDATES = 0;