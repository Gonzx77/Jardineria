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

    peticion = requests.post(f"http://154.38.171.54:5003/empleados/{id}", json=empleado)
    res = peticion.json()
    res["Mensaje"] = "Empleado Guardado"
    return [res]



# C L I E N T E
def Cliente():
    newCliente = {}
    
    while True:
        try:
            r = input("Ingrese codigo del cleinte: ").strip()
            if r:
                newCliente["codigo_cliente"] = int(r)
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
                newCliente["nombre_cliente"] = r
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
                newCliente["nombre_contacto"] = r
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
                newCliente["apellido_contacto"] = r
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
                newCliente["telefono"] = r
                print("-Modificado")
                break
            else:
                print("-Conservado")
                break
        except ValueError:
            print("Error, caracteres invalidos")
    while True:
        try:
            newCliente["fax"] = input("Ingresa el fax del cliente: ")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newCliente["linea_direccion1"] = input("Ingresa direccion 1 del cliente: ")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newCliente["linea_direccion2"] = input("Ingresa direccion 2 del cliente: ")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newCliente["ciudad"] = input("Ingresa la ciudad del cliente: ")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newCliente["region"] = input("Ingresa la region del cliente: ")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newCliente["pais"] = input("Ingrese pais del cliente: ")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newCliente["codigo_postal"] = input("Ingrese codigo postal del cliente: ")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newCliente["codigo_empleado_rep_ventas"] = int(input("Ingrese codigo del representante de ventas: "))
            break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            newCliente["limite_credito"] = float(input("Ingrese limite de credito del cliente: "))
            break
        except ValueError:
            print("Error, solo valores numericos !")

    peticion = requests.post("http://154.38.171.54:5001/cliente", data=json.dumps(newCliente))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]



# O F I C I N A
def Oficina():
    newOficina = {}
    
    while True:
        try:
            r = input("Ingrese codigo de la oficina, usando el siguiente formato: (AAA-AAA o AAA-AA): ")
            r = r.upper()
            if patronCodigoOficina.match(r):
                newOficina["codigo_oficina"] = r
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newOficina["ciudad"] = input("Ingrese ciudad de la oficina: ")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newOficina["pais"] = input("Ingrese pais de la oficina: ")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newOficina["region"] = input("Ingrese region de la oficina: ")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newOficina["codigo_postal"] = input("Ingrese codigo postal de la oficina: ")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newOficina["telefono"] = input("Ingrese telefono de la oficina: ")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newOficina["linea_direccion1"] = input("Ingrese direccion 1 de la oficna: ")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newOficina["linea_direccion2"] = input("Ingrese direccion 2 de la oficina: ")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    

    peticion = requests.post("http://154.38.171.54:5005/oficinas", data=json.dumps(newOficina))
    res = peticion.json()
    res["Mensaje"] = "Oficina Guardada"
    return [res]



# P E D I D O
def Pedido():
    newPedido = {}
    
    while True:
        try:
            newPedido["codigo_pedido"] = int(input("Ingrese codigo del pedido: "))
            break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            r = input("Ingrese fecha del pedido, en el siguiente formato: (YYYY-MM-DD): ")
            if patronFecha.match(r):
                newPedido["fecha_esperada"] = r
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            r = input("Ingrese fecha de entrega del pedido, en el siguiente formato: (YYYY-MM-DD): ")
            if patronFecha.match(r):
                newPedido["fecha_entrega"] = r 
                break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newPedido["estado"] = input("Ingrese estado del pedido: ")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newPedido["comentario"] = input("Ingrese comentario del pedido: ")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newPedido["codigo_cliente"] = int(input("Ingrese codigo del cliente: "))
            break
        except ValueError:
            print("Error, solo valores enteros !")

    peticion = requests.post("http://154.38.171.54:5007/pedidos", data=json.dumps(newPedido))
    res = peticion.json()
    res["Mensaje"] = "Pedido Guardado"
    return [res]



# P R O D U C T O
def Producto():
    newProducto = {}
    
    while True:
        try:
            r = input("Ingrese codigo del producto, con el sgieuiente formato: (AA-000): ")
            r = r.upper()
            if patronCodigoProducto.match(r):
                newProducto["codigo_producto"] = r
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newProducto["nombre"] = input("Ingrese nombre del pedido: ")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newProducto["gama"] = input("Ingrese gama del producto: ")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newProducto["dimensiones"] = input("Ingrese la dimension del producto: ")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newProducto["proveedor"] = input("Ingrese proveedor del prodcuto: ")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newProducto["descripcion"] = input("Ingrese descripcion del producto: ")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newProducto["cantidadEnStock"] = int(input("Ingrese cantidad en stock: "))
            break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            newProducto["precio_venta"] = int(input("Ingrese precio de venta: "))
            break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            newProducto["precio_proveedor"] = int(input("Ingrese precio de proveedor: "))
            break
        except ValueError:
            print("Error, solo valores enteros !")

    peticion = requests.post("http://154.38.171.54:5008/productos", data=json.dumps(newProducto))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]



# G A M A
def Gama():
    newGama = {}
    
    while True:
        try:
            newGama["gama"] = input("Ingrese nombre de la gama: ")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newGama["descripcion_texto"] = input("Ingrese descripcion de la gama: ")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newGama["descripcion_html"] = input("Descripcion HTML: ")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newGama["imagen"] = input("Ingrese imagen: ")
            break
        except ValueError:
            print("Error, caracteres invalidos !")

    peticion = requests.post("http://154.38.171.54:5004/gama", data=json.dumps(newGama))
    res = peticion.json()
    res["Mensaje"] = "Gama Guardada"
    return [res]



# D E T A L L E - P E D I D O
def DetallePed():
    newDetallePed = {}
    
    while True:
        try:
            newDetallePed["codigo_pedido"] = int(input("Ingrese codigo del pedido: "))
            break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            newDetallePed["codigo_producto"] = input("Ingrese codigo del producto: ")
            break
        except ValueError:
            print("Error, caracteres invalidos !")
    while True:
        try:
            newDetallePed["cantidad"] = int(input("Ingrese la cantidad del producto: "))
            break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            newDetallePed["precio_unidad"] = int(input("Ingrese precio por unidad de producto: "))
            break
        except ValueError:
            print("Error, solo valores enteros !")
    while True:
        try:
            newDetallePed["numero_linea"] = int(input("Ingrese numero de linea: "))
            break
        except ValueError:
            print("Error, solo valores enteros !")

    peticion = requests.post("http://154.38.171.54:5002/detalle_pedido", data=json.dumps(newDetallePed))
    res = peticion.json()
    res["Mensaje"] = "Detalle de pedido Guardado"
    return [res]