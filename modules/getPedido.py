from datetime import datetime
from tabulate import tabulate
import modules.getAllData as data
import modules.postAll as post
import os




def getEstadosPedido():
    result = []
    for val in data.Pedido():
        if [val.get("estado")] in result:
            result
        else:
            result.append([val.get("estado")])
    return result

def getPedidosTarde():
    result = []
    for val in data.Pedido():
        if val.get("fecha_entrega") != None:
            fechaI = "/".join(val.get("fecha_esperada").split("-")[::-1])
            fechaF = "/".join(val.get("fecha_entrega").split("-")[::-1])
            
            start = datetime.strptime(fechaI, "%d/%m/%Y")
            end = datetime.strptime(fechaF, "%d/%m/%Y")
            
            dif = start.date() - end.date()
            dif = dif.days
            
            if dif < 0:
                if val.get("comentario") != None:
                    result.append([
                        val.get("codigo_pedido"),
                        val.get("codigo_cliente"),
                        val.get("fecha_esperada"),
                        val.get("fecha_entrega"),
                        dif,
                        val.get("comentario")
                        ])
                else:
                        result.append([
                        val.get("codigo_pedido"),
                        val.get("codigo_cliente"),
                        val.get("fecha_esperada"),
                        val.get("fecha_entrega"),
                        dif,
                        "No hay comentario"
                        ])
    return result

def getPedidos2DiasTarde():
    result = []
    for val in data.Pedido():
        if val.get("fecha_entrega") != None:
            fechaI = "/".join(val.get("fecha_esperada").split("-")[::-1])
            fechaF = "/".join(val.get("fecha_entrega").split("-")[::-1])
            print(fechaI)
            
            start = datetime.strptime(fechaI, "%d/%m/%Y")
            end = datetime.strptime(fechaF, "%d/%m/%Y")
            
            dif = start.date() - end.date()
            dif = dif.days
            
            print(dif)
            
            if dif < -2:
                if val.get("comentario") != None:
                    result.append([
                        val.get("codigo_pedido"),
                        val.get("codigo_cliente"),
                        val.get("fecha_esperada"),
                        val.get("fecha_entrega"),
                        dif,
                        val.get("comentario")
                        ])
                else:
                        result.append([
                        val.get("codigo_pedido"),
                        val.get("codigo_cliente"),
                        val.get("fecha_esperada"),
                        val.get("fecha_entrega"),
                        dif,
                        "No hay comentario"
                        ])
    return result

def getPedidosCanceladosAño(x):
    
    result = []
    for val in data.Pedido():
        estado = val.get("estado")
        fecha = "/".join(val.get("fecha_pedido").split("-")[::-1])
        fecha = datetime.strptime(fecha, "%d/%m/%Y")
        año = fecha.year
        
        if estado == "Rechazado" and str(año) == x:
            if val.get("comentario") == None:
                result.append([
                    val.get("fecha_pedido"),
                    val.get("codigo_pedido"),
                    "Ninguno"
                ])
            else:
                result.append([
                    val.get("fecha_pedido"),
                    val.get("codigo_pedido"),
                    val.get("comentario")
                ])
    return result

def getPedidosEnero():
    result = []   
    for val in data.Pedido():
        fecha = val.get("fecha_entrega")
        estado = val.get("estado")
        if estado == "Entregado" and fecha != None:
            fecha = datetime.strptime(fecha, "%Y-%m-%d")
            mes = fecha.month
            if mes == 1:
                if val.get("comentario") != None:
                    result.append([
                        val.get("codigo_pedido"),
                        val.get("comentario")
                    ])
                else:
                    result.append([
                        val.get("codigo_pedido"),
                        "Ninguno"
                    ])
    return result

def menu():
    listAños = []
    for val in data.Pedido():
        fecha = "/".join(val.get("fecha_pedido").split("-")[::-1])
        fecha = datetime.strptime(fecha, "%d/%m/%Y")
        año = fecha.year
        if año not in listAños:
            listAños.append(año)
    
    while True: 
        os.system("clear")
        print(f"""
            1. Consulta
            2. Editar Datos Pedido
            
            0. Salir
            """)
        opP = input("Ingrese opcion: ")
        
        
        if opP == "1":
            os.system("clear")
            print(f"""
                1. Obtener todos los posibles estados de un pedido
                2. Obtener todos los pedidos que se entregaron tarde
                3. Obtener todos los pedidos que se entregaron 2 o mas dias tarde
                4. Obtener todos los pedidos cancelados en un año
                5. Obtener todos los pedidos entregados enero
                
                0. Salir
                """)
            break
        
        elif opP == "2":
            print(f"""
                1. Añadir Pedido
                
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
                os.system("clear")
                print(tabulate(getEstadosPedido(), headers=["Estados"], tablefmt="github"))
                input(f"""
    Presiona cualquier tecla para continuar...""")
                os.system("clear")
                break
            elif op == "2":
                os.system("clear")
                print(tabulate(getPedidosTarde(), headers=["Codigo pedido", "Codigo cliente", "fecha esperada", "fecha entregada", "Dias de retrazo", "Comentario"], tablefmt="github"))
                input(f"""
    Presiona cualquier tecla para continuar...""")
                os.system("clear")
                break
            elif op == "3":
                os.system("clear")
                print(tabulate(getPedidos2DiasTarde(), headers=["Codigo pedido", "Codigo cliente", "fecha esperada", "fecha entregada", "Dias antes", "Comentario"], tablefmt="github"))
                input(f"""
    Presiona cualquier tecla para continuar...""")
                os.system("clear")
                break
            elif op == "4":
                while True:
                    x = input("Ingrese año: ")
                    if x in str(listAños):
                        os.system("clear")
                        print(tabulate(getPedidosCanceladosAño(x), headers=["Codigo pedido", "Comentario"], tablefmt="github"))
                        input(f"""
        Presiona cualquier tecla para continuar...""")
                        os.system("clear")
                        break
                    
                
                    else:
                        print(f"""Error: Este año no existe, los años existentes son:
                            {listAños}""")
                break
                    
            
            elif op == "5":
                print(tabulate(getPedidosEnero(), headers=["Codigo pedido", "Comentario"], tablefmt="github"))
                break
            elif op == "0":
                break
            else:
                print("Esta opcion no existe")
                
        elif opP == "2":
            op = input("Ingrese opcion: ")
            if op == "1":
                os.system("clear")
                print(post.Pedido())
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