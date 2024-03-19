import requests



def Cliente():
    peticion = requests.get("http://172.16.100.138:5501/cliente")
    data = peticion.json()
    return data
def DetallePed():
    peticion = requests.get("http://172.16.100.138:5502/detalle")
    data = peticion.json()
    return data
def Empleado():
    peticion = requests.get("http://172.16.100.138:5503/empleado")
    data = peticion.json()
    return data
def Gama():
    peticion = requests.get("http://172.16.100.138:5504/gama")
    data = peticion.json()
    return data
def Oficina():
    peticion = requests.get("http://172.16.100.138:5505/oficina")
    data = peticion.json()
    return data
def Pago():
    peticion = requests.get("http://172.16.100.138:5506/pago")
    data = peticion.json()
    return data
def Pedido():
    peticion = requests.get("http://172.16.100.138:5507/pedido")
    data = peticion.json()
    return data
def Producto():
    peticion = requests.get("http://172.16.100.138:5508/producto")
    data = peticion.json()
    return data