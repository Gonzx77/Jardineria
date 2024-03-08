import storage.empleado as emp
from tabulate import tabulate

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

def getJefe():
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

def menu():
    print(f"""
          1. Obtener empleados cuyo jefe es el jefe #7
          2. Obtener jefe
          3. Obtener empleados que no son representantes de ventas""")
    
    op = int(input("Ingrese opcion: "))
    if op == 1:
        print(tabulate(getEmpleadoJefe(7), headers=["Nombre", "Apellido 1", "Apellido 2"], tablefmt="grid"))
    elif op == 2:
        print(tabulate(getJefe(), headers=["Nombre", "Apellido 1", "Apellido 2", "Email"], tablefmt="grid"))
    elif op == 3:
        print(tabulate(getEmpleadoNoRepresntanteVentas(), headers=["Nombre", "Apellido 1", "Apellido 2", "Puesto"], tablefmt="grid"))