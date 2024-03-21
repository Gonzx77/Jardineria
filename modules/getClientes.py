from tabulate import tabulate
import modules.postAll as post
import modules.removeAll as remove
import modules.updateTest as edit
import modules.getAllData as data
import os




def getClientePais(x):
    result = []
    for val in data.Cliente():
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
    for val in data.Cliente():
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
    for val in data.Cliente():
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
    for val in data.Cliente():
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
    for val in data.Cliente():
        codigo = val.get("codigo_empleado_rep_ventas")
        r1 = val.get("codigo_cliente")
        r2 = val.get("nombre_cliente")
        for val in data.Empleado():
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
    for val in data.Cliente():
        codigoRepresentante = val.get("codigo_empleado_rep_ventas")
        codigoCliente = val.get("codigo_cliente")
        r1 = val.get("codigo_cliente")
        r2 = val.get("nombre_cliente")
        for val in data.Pago():
            if codigoCliente == val.get("codigo_cliente"):
                for val in data.Empleado():
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
    
    for val in data.Pago():
        if val.get("codigo_cliente") not in listCodigoClientePago:
            listCodigoClientePago.append(val.get("codigo_cliente"))
    
    for val in data.Cliente():
        codigoRepresentante = val.get("codigo_empleado_rep_ventas")
        codigoCliente = val.get("codigo_cliente")
        r1 = val.get("codigo_cliente")
        r2 = val.get("nombre_cliente")
        if codigoCliente not in listCodigoClientePago:
            for val in data.Empleado():
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
    for val in data.Cliente():
        if val.get("pais") not in listPais:
            listPais.append(val.get("pais"))
    for val in data.Cliente():
        if val.get("region") not in listRegion:
            listRegion.append(val.get("region"))
    for val in data.Cliente():
        if val.get("ciudad") not in listCiudad:
            listCiudad.append(val.get("ciudad"))

    while True:
        os.system("clear")
        print(f"""
            --- Menu Cliente ---
            
            1. Consultar
            2. Editar Datos Cliente
            
            0. Salir
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
            break

        elif opP == "2":
            os.system("clear")
            print(f"""
            1. Añadir Cliente
            2. Eliminar Cliente
            3. Editar Cliente
            
            0. Salir
            """)
            break
        elif opP == "0":
            break

        else:
            print("Esta opcion no existe")
            input("Presione cualquier tecla para continuar...")
    
    while True:
        if opP == "1":
            op = input("Ingrese opcion: ")
            if op == "1":
                while True:
                    x = input("Ingrese el pais en el que desea buscar: ")
                    if x in listPais:
                        os.system("clear")
                        print("\n" + tabulate(getClientePais(x), headers=["Codigo", "Nombre", "Contacto", "Telefono", "Ciudad", "Region", "Pais"], tablefmt="github"))
                        input(f"""
        Presiona cualquier tecla para continuar...""")
                        os.system("clear")
                        break
                    else:
                        print(f"""Error: Este pais no existe, los paises existentes son:
                            {listPais}""")
                break
            elif op == "2":
                print("\n" + tabulate(getClienteSinRegion(), headers=["Codigo", "Nombre", "Contacto", "Telefono", "Ciudad"], tablefmt="github"))
                input(f"""
    Presiona cualquier tecla para continuar...""")
                os.system("clear")
                break
                
            elif op == "3":
                while True:
                    x = input("Ingrese la region en la que desea buscar: ")
                    if x in listRegion:
                        os.system("clear")
                        print("\n" + tabulate(getClienteRegion(x), headers=["Codigo", "Nombre", "Contacto", "Telefono", "Ciudad", "Region", "Pais"], tablefmt="github"))
                        input(f"""
        Presiona cualquier tecla para continuar...""")
                        os.system("clear")
                        break
                    else:
                        print(f"""Error: Esta region no existe, las regiones existentes son:
                            {listRegion}""")
                break
                    
            elif op == "4":
                while True:
                    x = input("Ingrese la region en la que desea buscar: ")
                    if x in listCiudad:
                        os.system("clear")
                        print("\n" + tabulate(getClienteCiudad(x), headers=["Codigo", "Nombre", "Contacto", "Telefono", "Ciudad", "Region", "Pais"], tablefmt="github"))
                        input(f"""
        Presiona cualquier tecla para continuar...""")
                        os.system("clear")
                        break
                    else:
                        print(f"""Error: Esta ciudad no existe, las ciudades existentes son:
                            {listCiudad}""")
                break
                    
            elif op == "5":
                os.system("clear")
                print("\n" + tabulate(getClientesRepresentantes(), headers=["Codigo Cliente", "Nombre", "Codigo Empleado", "Nombre", "Apellidos"], tablefmt="github"))
                input(f"""
    Presiona cualquier tecla para continuar...""")
                os.system("clear")
                break
            
            elif op == "6":
                os.system("clear")
                print("\n" + tabulate(getClientesRepresentantesPago(), headers=["Codigo Cliente", "Nombre", "Codigo Empleado", "Nombre", "Apellidos"], tablefmt="github"))
                input(f"""
    Presiona cualquier tecla para continuar...""")
                os.system("clear")
                break
            
            elif op == "7":
                os.system("clear")
                print("\n" + tabulate(getClientesRepresentantesNoPago(), headers=["Codigo Cliente", "Nombre", "Codigo Empleado", "Nombre", "Apellidos"], tablefmt="github"))
                input(f"""
    Presiona cualquier tecla para continuar...""")
                os.system("clear")
                break
                    
            elif op == "0":
                break
            
            else:
                print("Esta opcion no existe")


        elif opP == "2":
            op = input("Ingrese opcion: ")
            if op == "1":
                os.system("clear")
                print(post.Cliente())
                input(f"""
    Presiona cualquier tecla para continuar...""")
                os.system("clear")
                break
            elif op == "2":
                os.system("clear")
                while True:
                    try:
                        id = input("Ingresa ID del Cliente a eliminar: ")
                        remove.Cliente(id)
                        break
                    except ValueError:
                        print("Error, caracteres invalidos !")
                input(f"""
    Presiona cualquier tecla para continuar...""")
                os.system("clear")
                break
            elif op == "3":
                os.system("clear")
                while True:
                    try:
                        id = input("Ingresa ID del Cliente a eliminar: ")
                        edit.Cliente(id)
                        break
                    except ValueError:
                        print("Error, caracteres invalidos !")
                input(f"""
    Presiona cualquier tecla para continuar...""")
                os.system("clear")
                break
            elif op == "0":
                break
            else:
                print("Esta opcion no existe")

        elif opP == "0":
            break
        
        
        
    again = input(f""" \n Desea realizar otra consulta? (Si / No): """)
        
    if again.lower() != "si":
        print(f"""
            Gracias por usar nuestro sistema!
            """)
        exit()