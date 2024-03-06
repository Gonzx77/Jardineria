import storage.empleado as emp

def getClienteJefe7(N):
    result = []
    for val in emp.empleado:
        if(val.get("codigo_jefe") == N):
            result.append({
                "nombre": val.get("nombre"),
                "apellidos": f'{val.get("apellido1")}" "{val.get("apellido2")}'
            })
    return result

def getJefe():
    result = []
    for val in emp.empleado:
        if(val.get("codigo_jefe") == None):
            result.append({
                "puesto": val.get("puesto"),
                "nombre": val.get("nombre"),
                "apellidos": f'{val.get("apellido1")}" "{val.get("apellido2")}',
                "email": val.get("email")
            })
    return result