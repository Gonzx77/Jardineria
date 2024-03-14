from tabulate import tabulate
import modules.postCliente as postCli
import requests
import os

def getAllDataCliente():
    peticion = requests.get("http://172.16.104.33:5503/")
    data = peticion.json()
    return data
def getAllDataEmpleado():
    peticion = requests.get("http://172.16.104.33:5502/")
    data = peticion.json()
    return data
def getAllDataPago():
    peticion = requests.get("http://172.16.104.33:5501/")
    data = peticion.json()
    return data

def getClientePais(x):
    result = []
    for val in getAllDataCliente():
        if(val.get("pais") == x):
            result.append([
                val.get("codigo_cliente"),
                val.get("nombre_cliente"),
                val.get("nombre_contacto"),
                val.get("telefono"),
                val.get("ciudad"),
                val.get("region"),
                val.get("pais")
            ])
    return result

def getClienteSinRegion():
    result = []
    for val in getAllDataCliente():
        if(val.get("region") == None):
            result.append([
                val.get("codigo_cliente"),
                val.get("nombre_cliente"),
                val.get("nombre_contacto"),
                val.get("telefono"),
                val.get("ciudad")
            ])
    return result

def getClienteRegion(x):
    result = []
    for val in getAllDataCliente():
        if(val.get("region") == x):
            result.append([
                val.get("codigo_cliente"),
                val.get("nombre_cliente"),
                val.get("nombre_contacto"),
                val.get("telefono"),
                val.get("ciudad"),
                val.get("region"),
                val.get("pais")
            ])
    return result

def getClienteCiudad(x):
    result = []
    for val in getAllDataCliente():
        if(val.get("ciudad") == x):
            result.append([
                val.get("codigo_cliente"),
                val.get("nombre_cliente"),
                val.get("nombre_contacto"),
                val.get("telefono"),
                val.get("ciudad"),
                val.get("region"),
                val.get("pais")
            ])
    return result

def getClientesRepresentantes():
    result = []
    for val in getAllDataCliente():
        codigo = val.get("codigo_empleado_rep_ventas")
        r1 = val.get("codigo_cliente")
        r2 = val.get("nombre_cliente")
        for val in getAllDataEmpleado():
            if codigo == val.get("codigo_empleado"):
                result.append([
                r1,
                r2,
                val.get("codigo_empleado"),
                val.get("nombre"),
                f"{val.get('apellido1')} {val.get('apellido2')}"
                ])
                
    return result

def getClientesRepresentantesPago():
    result = []
    for val in getAllDataCliente():
        codigoRepresentante = val.get("codigo_empleado_rep_ventas")
        codigoCliente = val.get("codigo_cliente")
        r1 = val.get("codigo_cliente")
        r2 = val.get("nombre_cliente")
        for val in getAllDataPago():
            if codigoCliente == val.get("codigo_cliente"):
                for val in getAllDataEmpleado():
                    if codigoRepresentante == val.get("codigo_empleado"):
                        result.append([
                        r1,
                        r2,
                        val.get("codigo_empleado"),
                        val.get("nombre"),
                        f"{val.get('apellido1')} {val.get('apellido2')}"
                        ])       
    return result

def getClientesRepresentantesNoPago():
    result = []
    listCodigoClientePago = []
    
    for val in getAllDataPago():
        if val.get("codigo_cliente") not in listCodigoClientePago:
            listCodigoClientePago.append(val.get("codigo_cliente"))
            print(listCodigoClientePago)
    
    for val in getAllDataCliente():
        codigoRepresentante = val.get("codigo_empleado_rep_ventas")
        codigoCliente = val.get("codigo_cliente")
        r1 = val.get("codigo_cliente")
        r2 = val.get("nombre_cliente")
        if codigoCliente not in listCodigoClientePago:
            for val in getAllDataEmpleado():
                if codigoRepresentante == val.get("codigo_empleado"):
                    if codigoCliente not in result:
                        result.append([
                        r1,
                        r2,
                        val.get("codigo_empleado"),
                        val.get("nombre"),
                        f"{val.get('apellido1')} {val.get('apellido2')}"
                        ])
                               
    return result

def menu():
    os.system("clear")
    listPais = []
    listRegion = []
    listCiudad = []
    for val in getAllDataCliente():
        if val.get("pais") not in listPais:
            listPais.append(val.get("pais"))
    for val in getAllDataCliente():
        if val.get("region") not in listRegion:
            listRegion.append(val.get("region"))
    for val in getAllDataCliente():
        if val.get("ciudad") not in listCiudad:
            listCiudad.append(val.get("ciudad"))

    print(f"""
        --- Menu Cliente ---
          
            1. Consultar
            2. Editar Datos Cliente
          """)

    opP = input("Ingrese opcion: ")
    
    if opP == "1":
        os.system("clear")
        print(f"""
        1. Obtener clientes de un pais
        2. Obtener clientes con region indefinida
        3. Obtener clientes de una region
        4. Obtener clientes de una ciudad
        5. Obtener clientes junto con su representante de ventas
        6. Obtener clientes que hayan realizado compras junto con su representante de ventas
        7. Obtener clientes que no hayan realizado compras junto con su representante de ventas
        0. Salir
        """)

    elif opP == "2":
        os.system("clear")
        print(f"""
        1. Añadir Cliente
        """)
    
    op = input("Ingrese opcion: ")
    while True:
        if opP == "1":
            if op == "1":
                x = input("Ingrese el pais en el que desea buscar: ")
                if x in listPais:
                    print("\n" + tabulate(getClientePais(x), headers=["Codigo", "Nombre", "Contacto", "Telefono", "Ciudad", "Region", "Pais"], tablefmt="github"))
                    input("Presiona cualquier tecla para continuar...")
                    os.system("clear")
                    break
                else:
                    print(f"""Error: Este pais no existe, los paises existentes son:
                        {listPais}""")
                    
            elif op == "2":
                print("\n" + tabulate(getClienteSinRegion(), headers=["Codigo", "Nombre", "Contacto", "Telefono", "Ciudad"], tablefmt="github"))
                input("Presiona cualquier tecla para continuar...")
                os.system("clear")
                break
                
            elif op == "3":
                x = input("Ingrese la region en la que desea buscar: ")
                if x in listRegion:
                    print("\n" + tabulate(getClienteRegion(x), headers=["Codigo", "Nombre", "Contacto", "Telefono", "Ciudad", "Region", "Pais"], tablefmt="github"))
                    input("Presiona cualquier tecla para continuar...")
                    os.system("clear")
                    break
                else:
                    print(f"""Error: Esta region no existe, las regiones existentes son:
                        {listRegion}""")
                    
            elif op == "4":
                x = input("Ingrese la ciudad en la que desea buscar: ")
                if x in listCiudad:
                    print("\n" + tabulate(getClienteCiudad(x), headers=["Codigo", "Nombre", "Contacto", "Telefono", "Ciudad", "Region", "Pais"], tablefmt="github"))
                    input("Presiona cualquier tecla para continuar...")
                    os.system("clear")
                    break
                else:
                    print(f"""Error: Esta ciudad no existe, las ciudades existentes son:
                        {listCiudad}""")
                    
            elif op == "5":
                print("\n" + tabulate(getClientesRepresentantes(), headers=["Codigo Cliente", "Nombre", "Codigo Empleado", "Nombre", "Apellidos"], tablefmt="github"))
                input("Presiona cualquier tecla para continuar...")
                os.system("clear")
                break
            
            elif op == "6":
                print("\n" + tabulate(getClientesRepresentantesPago(), headers=["Codigo Cliente", "Nombre", "Codigo Empleado", "Nombre", "Apellidos"], tablefmt="github"))
                input("Presiona cualquier tecla para continuar...")
                os.system("clear")
                break
            
            elif op == "7":
                print("\n" + tabulate(getClientesRepresentantesNoPago(), headers=["Codigo Cliente", "Nombre", "Codigo Empleado", "Nombre", "Apellidos"], tablefmt="github"))
                input("Presiona cualquier tecla para continuar...")
                os.system("clear")
                break
                    
            elif op == "0":
                input("Presiona cualquier tecla para continuar...")
                os.system("clear")
                break
            
            else:
                print("Esta opcion no existe")
                op = input("Ingrese opcion: ")


        elif opP == "2":
            if op == "1":
                print(postCli.postCliente())
                input("Presiona cualquier tecla para continuar...")
                os.system("clear")
                break
        
        
        
    again = input(f""" \n Desea realizar otra consulta? (Si / No): """)
        
    if again.lower() != "si":
        print(f"""
            Gracias por usar nuestro sistema!
            """)
        exit()