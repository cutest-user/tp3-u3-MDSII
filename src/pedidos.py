"""Calculo de totales de pedidos (version refactorizada)."""

DESCUENTOS = {
    "libros": {"premium": 0.15, "regular": 0.05},
    "electro": {"premium": 0.20, "regular": 0.10},
    "ropa": {"premium": 0.25, "regular": 0.08},
}
CUPONES = {"PROMO10": 0.10, "PROMO20": 0.20}
IMPUESTOS = {"AR": 0.21, "UY": 0.22, "CL": 0.19, "BR": 0.17}


def subtotal_item(item, tipo_cliente):
    bruto = item["precio"] * item["cantidad"]
    desc = DESCUENTOS.get(item["categoria"], {}).get(tipo_cliente, 0)
    return bruto * (1 - desc)


def calcular_total(items, tipo_cliente, pais, cupon):
    total = sum(subtotal_item(it, tipo_cliente) for it in items)
    total *= 1 - CUPONES.get(cupon, 0)
    total *= 1 + IMPUESTOS.get(pais, 0)
    return round(total, 2)
