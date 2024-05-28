def  calcIva ():
    print('Funcion para determinar la factura con IVA ')
    factura = float(input('Ingrese el valor de la factura: '))
    iva = int(input('Ingrese el porcentaje de IVA: '))

    if iva != 0:
        if iva > 0:
            totalApagar = factura + ((factura * iva) / 100)
            return totalApagar
        else:
            return 'El monto de IVA es Negativo, no es posible avanzar'
    else:
        totalApagar = (factura * 0.21) + factura
        return totalApagar
    
print('Total + IVA = ',calcIva())
   