import json
import requests

def Pago():
    newPago = {
        "codigo_cliente": int(input("Ingrese codigo del cliente: ")),
        "forma_pago": input("Ingrese forma de pago: "),
        "id_transaccion": input("Ingrese ID de transaccion: "),
        "fecha_pago": input("Ingrese fecha del pago: "),
        "total": int(input("Ingrese valor total del pago: "))
    }

    peticion = requests.post("http://192.168.1.43:5501/", data=json.dumps(newPago))
    res = peticion.json()
    res["Mensaje"] = "Pago Guardado"
    return [res]

def Empleado():
    newEmpleado = {
        "codigo_empleado": int(input("Ingrese codigo del empleado: ")),
        "nombre": input("Ingrese nombre del empleado: "),
        "apellido1": input("Ingrese apellido 1 del empleado: "),
        "apellido2": input("Ingrese apellido 2 del empleado: "),
        "extension": input("Ingresa la extension del empleado: "),
        "email": input("Ingrese email del empleado: "),
        "codigo_oficina": input("Ingrese el codigo de la oficina del empleado: "),
        "codigo_jefe": int(input("Ingrese codigo del jefe: ")),
        "puesto": input("Ingrese puesto del empleado: ")
    }

    peticion = requests.post("http://192.168.1.43:5502/", data=json.dumps(newEmpleado))
    res = peticion.json()
    res["Mensaje"] = "Empleado Guardado"
    return [res]

def Cliente():
    newCliente = {
        "codigo_cliente": int(input("Ingrese codigo del cleinte: ")),
        "nombre_cliente": input("Ingrese nombre del cliente: "),
        "nombre_contacto": input("Ingrese nombre del contacto del cliente: "),
        "apellido_contacto": input("Ingrese apellido del contacto del cliente: "),
        "telefono": input("Ingrese el telefono del cliente: "),
        "fax": input("Ingresa el fax del cliente: "),
        "linea_direccion1": input("Ingresa direccion 1 del cliente: "),
        "linea_direccion2": input("Ingresa direccion 2 del cliente: "),
        "ciudad": input("Ingresa la ciudad del cliente: "),
        "region": input("Ingresa la region del cliente: "),
        "pais": input("Ingrese pais del cliente: "),
        "codigo_postal": input("Ingrese codigo postal del cliente: "),
        "codigo_empleado_rep_ventas": int(input("Ingrese codigo del representante de ventas: ")),
        "limite_credito": float(input("Ingrese limite de credito del cliente: "))
    }

    peticion = requests.post("http://192.168.1.43:5503/", data=json.dumps(newCliente))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]

def Oficina():
    newOficina = {
        "codigo_oficina": input("Ingrese codigo de la oficina: "),
        "ciudad": input("Ingrese ciudad de la oficina: "),
        "pais": input("Ingrese pais de la oficina: "),
        "region": input("Ingrese region de la oficina: "),
        "codigo_postal": input("Ingrese codigo postal de la oficina: "),
        "telefono": input("Ingrese telefono de la oficina: "),
        "linea_direccion1": input("Ingrese direccion 1 de la oficna: "),
        "linea_direccion2": input("Ingrese direccion 2 de la oficina: ")
    }

    peticion = requests.post("http://192.168.1.43:5504/", data=json.dumps(newOficina))
    res = peticion.json()
    res["Mensaje"] = "Oficina Guardada"
    return [res]

def Pedido():
    newPedido = {
        "codigo_pedido": int(input("Ingrese codigo del pedido: ")),
        "fecha_pedido": input("Ingrese fecha del pedido: "),
        "fecha_esperada": input("Ingrese la fecha del pedido: "),
        "fecha_entrega": input("Ingrese fecha de entrega del pedido: "),
        "estado": input("Ingrese estado del pedido: "),
        "comentario": input("Ingrese comentario del pedido: "),
        "codigo_cliente": int(input("Ingrese codigo del cliente: "))
    }

    peticion = requests.post("http://192.168.1.43:5505/", data=json.dumps(newPedido))
    res = peticion.json()
    res["Mensaje"] = "Pedido Guardado"
    return [res]

def Producto():
    newProducto = {
        "codigo_producto": input("Ingrese codigo del producto: "),
        "nombre": input("Ingrese nombre del pedido: "),
        "gama": input("Ingrese gama del producto: "),
        "dimensiones": input("Ingrese la dimension del producto: "),
        "proveedor": input("Ingrese proveedor del prodcuto: "),
        "descripcion": input("Ingrese descripcion del producto: "),
        "cantidad_en_stock": int(input("Ingrese cantidad en stock: ")),
        "precio_venta": int(input("Ingrese precio de venta: ")),
        "precio_proveedor": int(input("Ingrese precio de proveedor: "))
    }

    peticion = requests.post("http://192.168.1.43:5506/", data=json.dumps(newProducto))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]

def Gama():
    newGama = {
        "gama": input("Ingrese nombre de la gama: "), 
        "descripcion_texto": input("Ingrese descripcion de la gama: "), 
        "descripcion_html": input("Descripcion HTML: "),
        "imagen": input("Ingrese imagen: ")
    }

    peticion = requests.post("http://192.168.1.43:5506/", data=json.dumps(newGama))
    res = peticion.json()
    res["Mensaje"] = "Gama Guardada"
    return [res]

def DetallePed():
    newDetallePed = {
    "codigo_pedido": int(input("Ingrese codigo del pedido: ")),
    "codigo_producto": input("Ingrese codigo del producto: "),
    "cantidad": int(input("Ingrese la cantidad del producto: ")),
    "precio_unidad": int(input("Ingrese precio por unidad de producto: ")),
    "numero_linea": int(input("Ingrese numero de linea: "))
    }

    peticion = requests.post("http://192.168.1.43:5506/", data=json.dumps(newDetallePed))
    res = peticion.json()
    res["Mensaje"] = "Detalle de pedido Guardado"
    return [res]