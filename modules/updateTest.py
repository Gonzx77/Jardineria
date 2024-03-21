import json
import requests


import re
patronTransaccion = re.compile(r"^[A-Za-z]{2}-[A-Za-z]{3}-\d{6}")
patronFecha = re.compile(r"\d{4}-\d{2}-\d{2}$")
patronCodigoProducto = re.compile(r"^[A-Z]{2}-\d{3}$")
patronCodigoOficina = re.compile(r"^[A-Za-z]{3}-[A-Za-z]{2,3}$")

# P A G O
def Pago(id):
    response = requests.get(f"http://154.38.171.54:5006/pagos/{id}")
    if response.status_code == 200:
        pago = response.json()
        print("Cliente actual:")
        print(pago)
    
    
    while True:
        try:
            r = input("Ingrese codigo del cliente: ").strip()
            if r:
                pago["codigo_cliente"] = int(r)
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            r = input("Ingrese forma de pago: ").strip()
            if r:
                pago["forma_pago"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese ID de transaccion, en el siguiente formato: (AA-AAA-000000) ").strip()
            r = r.lower()
            if r:
                if patronTransaccion.match(r):
                    pago["id_transaccion"] = r
                    print("-Modificiado")
                    break
                else:
                    print("Error, no cumples con el formato de transaccion !")
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese fecha del pago, en el sigueinte formato: (YYY-MM-DD): ").strip()
            if r:
                if patronFecha.match(r):
                    pago["fecha_pago"] = r
                    print("-Modificado")
                    break
                else:
                    print("Error, no cumples con el formato de fecha !")
            else:
                print("-Conservado")
                break
        except ValueError:
            PermissionError("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese valor total del pago: ").strip()
            if r:
                pago["total"] = int(r)
                print("-Modificiado")
                break
            else:
                print("-Comservado")
                break
        except ValueError:
            print("Error, solo valores enteros !")
            

    print(pago)

    peticion = requests.put(f"http://154.38.171.54:5006/pagos/{id}", json=pago)
    res = peticion.json()
    res["Mensaje"] = "Pago Guardado"
    return [res]



# E M P L E A D O
def Empleado(id):
    response = requests.get(f"http://154.38.171.54:5003/empleados/{id}")
    if response.status_code == 200:
        empleado = response.json()
        print("Cliente actual:")
        print(empleado)
    
    while True:
        try:
            r = input("Ingrese codigo del empleado: ").strip()
            if r:
                empleado["codigo_empleado"] = int(r)
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            r = input("Ingrese nombre del empleado: ").strip()
            if r:
                empleado["nombre"] = r
                print("-Modificado")
                break
            else:
                print("-Comservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese apellido 1 del empleado: ").strip()
            if r:
                empleado["apellido1"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese apellido 2 del empleado: ").strip()
            if r:
                empleado["apellido2"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingresa la extension del empleado: ").strip()
            if r:
                empleado["extension"] = r
                print("-Modificaco")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese email del empleado: ").strip()
            if r:
                empleado["email"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese el codigo de la oficina del empleado (AAA-AA) o (AAA-AAA): ").strip()
            if r:
                if patronCodigoOficina.match(r):
                    empleado["codigo_oficina"] = r
                    print("-Modificado")
                    break
                else:
                    print("Error, debe seguir el formato de oficina !")
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese codigo del jefe: ").strip()
            if r:
                empleado["codigo_jefe"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            r = input("Ingrese puesto del empleado: ").strip()
            if r:
                empleado["puesto"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")

    peticion = requests.put(f"http://154.38.171.54:5003/empleados/{id}", json=empleado)
    res = peticion.json()
    res["Mensaje"] = "Empleado Guardado"
    return [res]



# C L I E N T E
def Cliente(id):
    response = requests.get(f"http://154.38.171.54:5001/cliente/{id}")
    if response.status_code == 200:
        cliente = response.json()
        print("Cliente actual:")
        print(cliente)
    
    while True:
        try:
            r = input("Ingrese codigo del cleinte: ").strip()
            if r:
                cliente["codigo_cliente"] = int(r)
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            r = input("Ingrese nombre del cliente: ").strip()
            if r:
                cliente["nombre_cliente"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese nombre del contacto del cliente: ").strip()
            if r:
                cliente["nombre_contacto"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese apellido del contacto del cliente: ").strip()
            if r:
                cliente["apellido_contacto"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese el telefono del cliente: ").strip()
            if r:
                cliente["telefono"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos")
    while True:
        try:
            r = input("Ingresa el fax del cliente: ").strip()
            if r:
                cliente["fax"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingresa direccion 1 del cliente: ").strip()
            if r:
                cliente["linea_direccion1"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingresa direccion 2 del cliente: ").strip()
            if r:
                cliente["linea_direccion2"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingresa la ciudad del cliente: ").strip()
            if r:
                cliente["ciudad"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingresa la region del cliente: ").strip()
            if r:
                cliente["region"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese pais del cliente: ").strip()
            if r:
                cliente["pais"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese codigo postal del cliente: ").strip()
            if r:
                cliente["codigo_postal"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese codigo del representante de ventas: ").strip()
            if r:
                cliente["codigo_empleado_rep_ventas"] = int(r)
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            r = input("Ingrese limite de credito del cliente: ").strip()
            if r:
                cliente["limite_credito"] = float(r)
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, solo valores numericos !")

    peticion = requests.put(f"http://154.38.171.54:5001/cliente/{id}", json=cliente)
    res = peticion.json()
    res["Mensaje"] = "Cliente Guardado"
    return [res]



# O F I C I N A
def Oficina(id):
    response = requests.get(f"http://154.38.171.54:5005/oficinas/{id}")
    if response.status_code == 200:
        oficina = response.json()
        print("Cliente actual:")
        print(oficina)
    
    while True:
        try:
            r = input("Ingrese codigo de la oficina, usando el siguiente formato: (AAA-AAA o AAA-AA): ").strip()
            if r:
                r = r.upper()
                if patronCodigoOficina.match(r):
                    oficina["codigo_oficina"] = r
                    print("-Modificado")
                    break
                else:
                    print("Error, debe seguir el formato indicado !")
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese ciudad de la oficina: ").strip()
            if r:
                oficina["ciudad"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese pais de la oficina: ").strip()
            if r:
                oficina["pais"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese region de la oficina: ").strip()
            if r:
                oficina["region"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese codigo postal de la oficina: ").strip()
            if r:
                oficina["codigo_postal"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese telefono de la oficina: ").strip()
            if r:
                oficina["telefono"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese direccion 1 de la oficna: ").strip()
            if r:
                oficina["linea_direccion1"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese direccion 2 de la oficina: ").strip()
            if r:
                oficina["linea_direccion2"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    

    peticion = requests.put(f"http://154.38.171.54:5005/oficinas/{id}", json=oficina)
    res = peticion.json()
    res["Mensaje"] = "Oficina Guardada"
    return [res]



# P E D I D O
def Pedido(id):
    response = requests.get(f"http://154.38.171.54:5007/pedidos/{id}")
    if response.status_code == 200:
        pedido = response.json()
        print("Cliente actual:")
        print(pedido)
    
    while True:
        try:
            r = input("Ingrese codigo del pedido: ").strip()
            if r:
                pedido["codigo_pedido"] = int(r)
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            r = input("Ingrese fecha del pedido, en el siguiente formato: (YYYY-MM-DD): ").strip()
            if r:
                if patronFecha.match(r):
                    pedido["fecha_esperada"] = r
                    print("-Modificado")
                    break
                else:
                    print("Error, debe seguir el formato !")
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese fecha de entrega del pedido, en el siguiente formato: (YYYY-MM-DD): ").strip()
            if r:
                if patronFecha.match(r):
                    pedido["fecha_entrega"] = r 
                    print("-Modificado")
                    break
                else:
                    print("Error, debe seguir el formato !")
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese estado del pedido: ").strip()
            if r:
                pedido["estado"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese comentario del pedido: ").strip()
            if r:
                pedido["comentario"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese codigo del cliente: ").strip()
            if r:
                pedido["codigo_cliente"] = int(r)
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, solo valores enteros !")

    peticion = requests.put(f"http://154.38.171.54:5007/pedidos/{id}", json=pedido)
    res = peticion.json()
    res["Mensaje"] = "Pedido Guardado"
    return [res]



# P R O D U C T O
def Producto(id):
    response = requests.get(f"http://154.38.171.54:5008/productos/{id}")
    if response.status_code == 200:
        producto = response.json()
        print("Cliente actual:")
        print(producto)
    
    while True:
        try:
            r = input("Ingrese codigo del producto, con el sgieuiente formato: (AA-000): ").strip()
            if r:
                r = r.upper()
                if patronCodigoProducto.match(r):
                    producto["codigo_producto"] = r
                    print("-Modificado")
                    break
                else:
                    print("Error, debe segir el formato !")
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese nombre del pedido: ").strip()
            if r:
                producto["nombre"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese gama del producto: ").strip()
            if r:
                producto["gama"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese la dimension del producto: ").strip()
            if r:
                producto["dimensiones"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese proveedor del prodcuto: ").strip()
            if r:
                producto["proveedor"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese descripcion del producto: ").strip()
            if r:
                producto["descripcion"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese cantidad en stock: ").strip()
            if r:
                producto["cantidadEnStock"] = int(r)
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            r = input("Ingrese precio de venta: ").strip()
            if r:
                producto["precio_venta"] = int(r)
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            r = input("Ingrese precio de proveedor: ").strip()
            if r:
                producto["precio_proveedor"] = int(r)
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, solo valores enteros !")

    peticion = requests.put(f"http://154.38.171.54:5008/productos/{id}", json=producto)
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]



# G A M A
def Gama(id):
    response = requests.get(f"http://154.38.171.54:5004/gama/{id}")
    if response.status_code == 200:
        gama = response.json()
        print("Cliente actual:")
        print(gama)
    
    while True:
        try:
            r = input("Ingrese nombre de la gama: ").strip()
            if r:
                gama["gama"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese descripcion de la gama: ").strip()
            if r:
                gama["descripcion_texto"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r =input("Descripcion HTML: ").strip()
            if r:
                gama["descripcion_html"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese imagen: ").strip()
            if r:
                gama["imagen"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")

    peticion = requests.put(f"http://154.38.171.54:5004/gama/{id}", json=gama)
    res = peticion.json()
    res["Mensaje"] = "Gama Guardada"
    return [res]



# D E T A L L E - P E D I D O
def DetallePed(id):
    response = requests.get(f"http://154.38.171.54:5002/detalle_pedido/{id}")
    if response.status_code == 200:
        detalle = response.json()
        print("Cliente actual:")
        print(detalle)
    
    while True:
        try:
            r = input("Ingrese codigo del pedido: ").strip()
            if r:
                detalle["codigo_pedido"] = int(r)
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            r = input("Ingrese codigo del producto: ").strip()
            if r:
                detalle["codigo_producto"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese la cantidad del producto: ").strip()
            if r:
                detalle["cantidad"] = int(r)
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            r = input("Ingrese precio por unidad de producto: ").strip()
            if r:
                detalle["precio_unidad"] = int(r)
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            r = input("Ingrese numero de linea: ").strip()
            if r:
                detalle["numero_linea"] = int(r)
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, solo valores enteros !")

    peticion = requests.put(f"http://154.38.171.54:5002/detalle_pedido/{id}", json = detalle)
    res = peticion.json()
    res["Mensaje"] = "Detalle de pedido Guardado"
    return [res]