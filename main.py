from tabulate import tabulate

import modules.getOficinas as Oficina
import modules.getEmpleados as Empleado
import modules.getClients as Cliente
import modules.getPedido as Pedido

#Devuelve un listado con el codigo de oficina y la ciudad donde hay oficinas
print("  #1  ",Oficina.getOficinaCiudad(), "\n")

#Devuelve un listado con la ciudad y el telefono de las oficinas de españa
print("  #2  ",Oficina.getCiudadTelefonoDEEspaña(), "\n")

#Devuelve un listado con el nombre, apellidos, y email de los empleados cuyo jefe tiene codigo igual a 7
print("  #3  ",Empleado.getEmpleadoJefe(7), "\n")

#Devuelve el nombre del puesto, nombre, y apellidos y email del jefe de la empresa
print("  #4  ",Empleado.getJefe7(), "\n")

#Devuelva un listado con el nombre, apellidos y puestos de aquellos empleados que no sean representantes de ventas
print("  #5  ",Empleado.getEmpleadoNoRepresntanteVentas(), "\n")

#Devuelve un listado con el nombre de todos los clientes españoles
print("  #6  ",Cliente.getClienteEspaña(), "\n")

#Devuelve un listado con los distintos estados por los que se puede pasar un pedido
print("  #7  ",Pedido.getEstadosPedido(), "\n")