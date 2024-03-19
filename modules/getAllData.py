import requests

def Cliente():
    peticion = requests.get("http://154.38.171.54:5001/cliente")
    data = peticion.json()
    return data
def DetallePed():
    peticion = requests.get("http://154.38.171.54:5002/detalle_pedido")
    data = peticion.json()
    return data
def Empleado():
    peticion = requests.get("http://154.38.171.54:5003/empleados")
    data = peticion.json()
    return data
def Gama():
    peticion = requests.get("http://154.38.171.54:5004/gama")
    data = peticion.json()
    return data
def Oficina():
    peticion = requests.get("http://154.38.171.54:5005/oficinas")
    data = peticion.json()
    return data
def Pago():
    peticion = requests.get("http://154.38.171.54:5006/pagos")
    data = peticion.json()
    return data
def Pedido():
    peticion = requests.get("http://154.38.171.54:5007/pedidos")
    data = peticion.json()
    return data
def Producto():
    peticion = requests.get("http://154.38.171.54:5008/productos")
    data = peticion.json()
    return data