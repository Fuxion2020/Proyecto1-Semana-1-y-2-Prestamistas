
from Cliente import *
import datetime

class Administracion:
    #Listas que usará el programa para guardar clientes y préstamos 
    def __init__(self):
        #Aqui se guardan los clientes
        self.clientes = []
    
    def buscar_cliente(self, nombre, cedula):
        """Busca un cliente por su nombre y cédula."""
        for cliente in self.clientes:
            if cliente.nombre == nombre and cliente.cedula == cedula:
                return cliente
        return None

    def menucito(self,opciones):
        #Es para que se lea la lista "opciones" y las numerice, así en el input solo hay que poner el número de la selcción
        print("----------------------------")
        for opcion in range(len(opciones)):
                print(f"{opcion+1} / {opciones[opcion]}")
                print("----------------------------")
    
                  
                
    def menu(self):
        #Listas que usará el programa para guardar clientes y préstamos 
        opciones = ["Registrar cliente", "Realizar préstamo", "Revisar corte", "Ver clientes registrados", "Salir"]
        final = 0
        while final == 0:
            print(f"""
                    HOLA! 
                BIENVENIDO A
               "Préstamos C.A"

                """)
            self.menucito(opciones)

            eleccion = input("Ingrese el número de la opción que desee: ")
            if eleccion == "1":
                self.registrar_cliente()
                self.pause()       
            elif eleccion == "2":
                self.registrar_préstamo()
                self.pause()  
            elif eleccion == "3":
                self.revisar_corte()
                self.pause()      
            elif eleccion == "4":
                self.mostrar_clientes()
                self.pause()   
            elif eleccion == "5":
                final = final + 1
                print("Fin")
            else:
                print("Error, seleccione un número válido")
                self.pause()
                
    def mostrar_clientes(self):
        #Aqui lee la lista de clientes y los va leyendo
        print("----------------------------")
        for i in range(len(self.clientes)):
            print(f"{i+1}. {self.clientes[i].show()}")
            print("----------------------------")
    
    
    def registrar_cliente(self):
        #Si se desea añadir más de un cliente
        qty = (input("Cuántos clientes deseas agregar?: "))
        #Para no permitir letras ni símbolos
        while any(chr.isalpha() for chr in qty) or not qty.isdigit():
            qty = input("Error! Ingrese un numero: ")
        qty = int(qty)
        for i in range(qty):
            #Validacion de nombre
            nombre=input("Ingrese el nombre del cliente: ")
            nombre=nombre.lower()
            nombre=nombre.title()
            #Para no permitir números ni símbolos
            while any(chr.isdigit() for chr in nombre) or not nombre.isalpha():
                nombre = input("Error! Ingrese el nombre del cliente: ")
                nombre=nombre.lower()
                nombre=nombre.title()
                
            #Validacion de DNI
            cedula =input("Ingrese el DNI del cliente: ")
            #Validacion si el DNI tiene solo números
                    
            while any(chr.isalpha() for chr in cedula) or not cedula.isdigit():
                cedula = input("Error! Ingrese el DNI del cliente:  ")

            saldo = (input("Ingrese el saldo a ingresar del cliente: ")) 
            #Revisa que el saldo sea un número
            while any(chr.isalpha() for chr in saldo) or not saldo.isdigit():
                saldo = input("Error! Ingrese un monto ")
            #tengo que ver como agregar esto
            prestamos = []   #////// REVISAR

            nuevo_cliente = Cliente(nombre,cedula,saldo,prestamos)
            self.clientes.append(nuevo_cliente)
            print(f"Se ha registrado un nuevo cliente: {nombre} ")
            
    def pause(self):
        #Pausa activa que se usan en casi todos los metodos, así la pantalla se ve más organizada al hacerle run
        print("Toque cualquier botón para volver al menú")
        pause = input(" ")
        if pause == "":
         pass
        else:
         pass
    


    def registrar_préstamo(self):
        #Pide los datos del cliente y del préstamo
        nombre = input("Ingrese el nombre del cliente: ").lower().title()
        #Para no permitir números ni símbolos
        while any(chr.isdigit() for chr in nombre) or not nombre.isalpha():
            nombre = input("Error! Ingrese el nombre del cliente: ").lower().title()
            
        #Validacion de DNI
        cedula =input("Ingrese el DNI del cliente: ")
        #Validacion si el DNI tiene solo números          
        while any(chr.isalpha() for chr in cedula) or not cedula.isdigit():
            cedula = input("Error! Ingrese el DNI del cliente:  ")

        #Validación del monto
        monto = input("Ingrese el monto del préstamo: ")
        try:
            if float(monto) < 0:
                raise ValueError
        except ValueError:
            monto = input("Error! Ingrese el monto del prestamo: ")
        while any(chr.isalpha() for chr in monto) or not monto.isdigit():
            monto = input("Error! Ingrese un monto ")

        fecha = datetime.date.today()
        #Busca al cliente en la lista de clientes
        cliente = self.buscar_cliente(nombre, cedula)
        #Si el cliente existe, le crea un nuevo préstamo y lo agrega a la lista de préstamos
        if cliente:
            prestamo = cliente.solicitar_prestamo(monto,fecha)
            print(f"<<<Se ha realizado el préstamo de {monto} a {nombre} con éxito.>>>>")
            print("Estado del prestamo:")
            print(prestamo.obtener_estado())
        #Si el cliente no existe, le avisa al usuario
        else:
            print(f"No se encontró al cliente con nombre {nombre} y cédula {cedula}.")


  # ////// REVISAR NO IMPRIME BIEN ////////
    def revisar_corte(self):
    #Recorre la lista de clientes y muestra el estado de sus préstamos
        for cliente in self.clientes:
            print(f"Cliente: {cliente.nombre}")
            print(f"Cédula: {cliente.cedula}")
            print(f"Saldo: {cliente.saldo}")
            print(f"Prestamos:")
            #Recorre la lista de préstamos de cada cliente y muestra el estado de cada uno
            for prestamo in cliente.prestamos:
                print(f"- Monto: {prestamo.monto}")
                print(f"- Fecha: {prestamo.fecha}")
                print(f"- Estado: {prestamo.obtener_estado()}")
                print("<---------------------------->")


