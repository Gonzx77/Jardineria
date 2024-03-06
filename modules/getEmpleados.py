import storage.empleado as emp

def getEmpleadoJefe(N):
    result = []
    for val in emp.empleado:
        if(val.get("codigo_jefe") == N):
            result.append([
                val.get("nombre"),
                val.get("apellido1"),
                val.get("apellido2")
            ])
    return result

def getJefe7():
    result = []
    for val in emp.empleado:
        if(val.get("codigo_jefe") == None):
            result.append([
                val.get("puesto"),
                val.get("nombre"),
                val.get("apellido1"),
                val.get("apellido2"),
                val.get("email")
            ])
    return result

def getEmpleadoNoRepresntanteVentas():
    result = []
    for val in emp.empleado:
        if(val.get("puesto") != "Representante Ventas"):
            result.append([
                val.get("nombre"),
                val.get("apellido1"),
                val.get("apellido2"),
                val.get("puesto")
            ])
    return result
