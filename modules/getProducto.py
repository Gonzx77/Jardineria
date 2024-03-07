import storage.producto as pro

def getProductOrnamentales():
    result = []
    for val in pro.producto:
        if val.get("gama") == "Aromáticas" and val.get("cantidad_en_stock") > 100:
            result.append([
                val.get("codigo_producto"),
                val.get("cantidad_en_stock"),
                val.get("precio_venta")
            ])
            
    return result