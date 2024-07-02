monto_sin_IGV = float(input("digite monto sin IGV: "))
porcentaje_IGV = float(input("digite porcentaje de IGV (opcional, default 18%): ") or 18)

def calcular_total_factura(monto, porcentaje_IGV=18):
    igv = (monto * porcentaje_IGV) / 100
    return monto + igv

factura_total = calcular_total_factura(monto_sin_IGV, porcentaje_IGV)

print(f"El total de la factura es:", {factura_total})