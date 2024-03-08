from tabulate import tabulate

import modules.getOficinas as Oficina
import modules.getEmpleados as Empleado
import modules.getClients as Cliente
import modules.getPedido as Pedido
import modules.getPago as Pago
import modules.getProducto as Producto

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

print("#11", "Devuelve un listado de todos los pedidos que fueron rechazados en 2009")
print(tabulate(Pedido.getPedidosCancelados(), headers=["Codigo pedido", "Comentario"], tablefmt="grid"))
print("\n", "\n")

print("#12", "Devuelve un listado de todos los pedidos que han sido entregado en el mes de enero de cualquier año")
print(tabulate(Pedido.getPedidosEnero(), headers=["Codigo pedido", "Comentario"], tablefmt="grid"))
print("\n", "\n")

print("#13", "Devuelve un listado con todos los pagos que se realizaron en el 2008 mediante paypal ordene el resultado de mayor a menor")
print(tabulate(Pago.getPagoPaypal2008(), headers=["Codigo cliente", "ID", "Total"], tablefmt="grid"))
print("\n", "\n")

print("#14", "Devuelve un listado con todas las formas de pago, tenga en cuenta que no deben salir formas repetidas")
print(tabulate(Pago.getFormasPago(), headers=["Formas de pago"], tablefmt="grid"))
print("\n", "\n")

print("#15", "Devuelve un listado con todos los productos que forman parte de la gama Ornamentales, y que tienen mas de 100 unidades en stock ordenados de mayor a menor segun su precio")
print(tabulate(Producto.getProductOrnamentales(), headers=["ID producto", "Cantidad en stock", "Precio"], tablefmt="grid"))
print("\n", "\n")