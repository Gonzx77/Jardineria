import storage.empleado as emp

def getEmpleadoJefe(N):
    result = []
    for val in emp.empleado:
        if(val.get("codigo_jefe") == N):
            result.append({
                "nombre": val.get("nombre"),
                "apellidos": f'{val.get("apellido1")}" "{val.get("apellido2")}'
            })
    return result

def getJefe7():
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

def getEmpleadoNoRepresntanteVentas():
    result = []
    for val in emp.empleado:
        if(val.get("puesto") != "Representante Ventas"):
            result.append({
                "nombre": val.get("nombre"),
                "apellidos": f'{val.get("apellido1")}" "{val.get("apellido2")}',
                "puesto": val.get("puesto")
            })
    return result
