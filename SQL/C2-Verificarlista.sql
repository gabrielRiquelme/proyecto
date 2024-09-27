	SELECT * FROM libro where titulo like '%CREADORES Y HEREDEROS%' ;
    
    select count(*) as existe FROM libro
    where titulo like '%CREADORES Y HEREDEROS%' ;
    
    select exists(
		SELECT 1
        FROM libro
        where titulo like '%CREADORES Y HEREDEROS%'
    )as existe;