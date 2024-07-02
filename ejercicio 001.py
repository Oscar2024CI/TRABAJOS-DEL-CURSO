monto_sin_IGV = float(input("digite monto sin IGV: "))
porcentaje_IGV = float(input("digite porcentaje de IGV : ") or 18)

def calcul_factura_total(monto, porcentaje_IGV=18):
    igv = (monto * porcentaje_IGV) / 100
    return monto + igv

factura_total = calcul_factura_total(monto_sin_IGV, porcentaje_IGV)

print("El total de la factura es:", factura_total)