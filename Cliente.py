import pickle
from ClassPrestamo import Prestamo
from ClassPrestamo import * 

class Cliente:
    def __init__(self, nombre, cedula, saldo, prestamos):
        self.nombre = nombre
        self.cedula = cedula
        self.saldo = saldo
        self.prestamos = []  # lista para guardar los préstamos
        
    def show(self):
        #Esto es para que el programa puede leer los clientes que haya, básicamente cuando vayamos hacerle print esto ayuda
        return f"""
        Nombre: {self.nombre}
        Cedula: {self.cedula}
        Saldo: {self.saldo}
        Prestamos: {self.prestamos}
        """

    def solicitar_prestamo(self, monto, fecha):
        """Crea un nuevo préstamo para el cliente y lo agrega a la lista de préstamos."""
        prestamo = Prestamo(monto, fecha, self)
        self.prestamos.append(prestamo)
        self.saldo += monto
        return prestamo
    
    