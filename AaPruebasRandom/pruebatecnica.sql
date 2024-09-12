CREATE TABLE Ocupacion_Vuelos (
    id INT PRIMARY KEY AUTO_INCREMENT,                  
    vuelo_id INT NOT NULL,                             --
    cliente_nif VARCHAR(9) NOT NULL,                   --
    fecha DATE NOT NULL,                               
    ocupacion INT NOT NULL,                            
    CONSTRAINT fk_vuelo FOREIGN KEY (vuelo_id) REFERENCES dbo.VUELOS(VUELO),  -- CE
    CONSTRAINT fk_cliente FOREIGN KEY (cliente_nif) REFERENCES dbo.CLIENTES(NIF),  -- CE
    CONSTRAINT uq_origen_destino_fecha UNIQUE (vuelo_id, fecha, (SELECT ORIGEN FROM dbo.VUELOS WHERE VUELO = vuelo_id), (SELECT DESTINO FROM dbo.VUELOS WHERE VUELO = vuelo_id))  -- Restricción de unicidad
);

INSERT INTO OCUPACION_VUELOS (VUELO_ID, ASIENTO, ESTADO, CLIENTE_ID)
VALUES
    (1, '2A', 'Ocupado', 123),
    (2, '5C', 'Disponible', NULL);

