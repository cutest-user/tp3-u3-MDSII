# version original, sin refactorizar
def calcular_total(items, tipo_cliente, pais, cupon):
    total = 0
    for it in items:
        if it["categoria"] == "libros":
            if tipo_cliente == "premium":
                total = total + it["precio"] * it["cantidad"] * 0.85
            elif tipo_cliente == "regular":
                total = total + it["precio"] * it["cantidad"] * 0.95
            else:
                total = total + it["precio"] * it["cantidad"]
        elif it["categoria"] == "electro":
            if tipo_cliente == "premium":
                total = total + it["precio"] * it["cantidad"] * 0.80
            elif tipo_cliente == "regular":
                total = total + it["precio"] * it["cantidad"] * 0.90
            else:
                total = total + it["precio"] * it["cantidad"]
        elif it["categoria"] == "ropa":
            if tipo_cliente == "premium":
                total = total + it["precio"] * it["cantidad"] * 0.75
            elif tipo_cliente == "regular":
                total = total + it["precio"] * it["cantidad"] * 0.92
            else:
                total = total + it["precio"] * it["cantidad"]
        else:
            total = total + it["precio"] * it["cantidad"]
    if cupon == "PROMO10":
        total = total * 0.90
    elif cupon == "PROMO20":
        total = total * 0.80
    elif cupon != "" and cupon is not None:
        pass
    if pais == "AR":
        total = total * 1.21
    elif pais == "UY":
        total = total * 1.22
    elif pais == "CL":
        total = total * 1.19
    elif pais == "BR":
        total = total * 1.17
    return round(total, 2)
