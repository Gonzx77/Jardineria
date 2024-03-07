from tabulate import tabulate

import modules.getOficinas as Oficina
import modules.getEmpleados as Empleado
import modules.getClients as Cliente
import modules.getPedido as Pedido
import modules.getPago as Pago

print("\n", "\n", "#1", "Devuelve un listado con el codigo de oficina y la ciudad donde hay oficinas")
print(tabulate(Oficina.getOficinaCiudad(), headers=["Codigo Oficina", "Ciudad"], tablefmt="grid"))
print("\n", "\n")

print("#2","Devuelve un listado con la ciudad y el telefono de las oficinas de españa")
print(tabulate(Oficina.getCiudadTelefonoDEEspaña(), headers=["Ciudad", "Telefono"], tablefmt="grid"))
print("\n", "\n")

print("#3", "Devuelve un listado con el nombre, apellidos, y email de los empleados cuyo jefe tiene codigo igual a 7")
print(tabulate(Empleado.getEmpleadoJefe(7), headers=["Nombre", "Apellido 1", "Apellido 2"], tablefmt="grid"))
print("\n", "\n")

print("#4", "Devuelve el nombre del puesto, nombre, y apellidos y email del jefe de la empresa")
print(tabulate(Empleado.getJefe7(), headers=["Puesto", "Nombre", "Apellido 1", "Apellido 2", "Email"], tablefmt="grid"))
print("\n", "\n")

print("#5", "Devuelva un listado con el nombre, apellidos y puestos de aquellos empleados que no sean representantes de ventas")
print(tabulate(Empleado.getEmpleadoNoRepresntanteVentas(), headers=["Nombre", "Apellido 1", "Apellido 2", "Puesto"], tablefmt="grid"))
print("\n", "\n")

print("#6", "Devuelve un listado con el nombre de todos los clientes españoles")
print(tabulate(Cliente.getClienteEspaña(), headers=["Nombre"], tablefmt="grid"))
print("\n", "\n")

print("#7", "Devuelve un listado con los distintos estados por los que se puede pasar un pedido")
print(tabulate(Pedido.getEstadosPedido(), headers=["Estados"], tablefmt="grid"))
print("\n", "\n")

print("#8", "Devuelva un listado con el codigo del cliente de aquellos clientes que realizaron algun pago en 2008. Tenga en cuenta que debera eliminar aquellos codigos de cliente que saldran repetidos")
print(tabulate(Pago.getPagos2008(), headers=["Codigo cliente"], tablefmt="grid"))
print("\n", "\n")

print("#9", "Devuelva un listado con el codigo del pedido, codigo de cliente, fecha esperada y fecha de entrega de los pedidos que no han sido entregado al tiempo")
print(tabulate(Pedido.getPedidosTarde(), headers=["Codigo pedido", "Codigo cliente", "fecha esperada", "fecha entregada", "Dias de retrazo", "Comentario"], tablefmt="grid"))
print("\n", "\n")

print("#10", "Devuelva un listado con el codigo del pedido, codigo de cliente, fecha esperada y fecha de entrega de los pedidos cuya fecha de entrega ha sido al menos 2 dias antes de la fecha entregada")
print(tabulate(Pedido.getPedidos2DiasTarde(), headers=["Codigo pedido", "Codigo cliente", "fecha esperada", "fecha entregada", "Dias antes", "Comentario"], tablefmt="grid"))
print("\n", "\n")