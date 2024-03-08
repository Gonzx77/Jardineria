import modules as modules
import sys

import modules.getOficinas as Oficina
import modules.getEmpleados as Empleado
import modules.getClientes as Cliente
import modules.getPedido as Pedido
import modules.getPago as Pago
import modules.getProducto as Producto


def menu():
    print(f"""
          
        --- Menu Principal ---
        
        1. Clientes
        2. Empleados
        3. Oficina
        4. Pago
        5. Pedido
        6. Producto""")
    
    op = int(input("Ingrese opcion: "))
    if op == 1:
        Cliente.menu()
    elif op == 2:
        Empleado.menu()
    elif op == 3:
        Oficina.menu()
    elif op == 4:
        Pago.menu()
    elif op == 5:
        Pedido.menu()
    elif op == 6:
        Producto.menu()
           
menu()