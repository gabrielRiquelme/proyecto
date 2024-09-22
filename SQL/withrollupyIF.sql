SELECT 
if(grouping(idCliente),'Total',idCliente) as cliente,
count(idFactura) as facturas from factura group by idCliente with rollup;