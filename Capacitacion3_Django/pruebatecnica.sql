CREATE TABLE Ocupacion_Vuelos (
    id INT PRIMARY KEY AUTO_INCREMENT,                  -- Clave primaria
    vuelo_id INT NOT NULL,                             -- Identificador del vuelo
    cliente_nif VARCHAR(9) NOT NULL,                   -- NIF del cliente (clave externa)
    fecha DATE NOT NULL,                               -- Fecha del vuelo
    ocupacion INT NOT NULL,                            -- Ocupación del vuelo
    CONSTRAINT fk_vuelo FOREIGN KEY (vuelo_id) REFERENCES dbo.VUELOS(VUELO),  -- Clave externa a VUELOS
    CONSTRAINT fk_cliente FOREIGN KEY (cliente_nif) REFERENCES dbo.CLIENTES(NIF),  -- Clave externa a CLIENTES
    CONSTRAINT uq_origen_destino_fecha UNIQUE (vuelo_id, fecha, (SELECT ORIGEN FROM dbo.VUELOS WHERE VUELO = vuelo_id), (SELECT DESTINO FROM dbo.VUELOS WHERE VUELO = vuelo_id))  -- Restricción de unicidad
);