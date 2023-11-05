import pickle
from ClassPrestamo import * 


class Cliente:
    def __init__(self, nombre, cedula, saldo):
        self.nombre = nombre
        self.cedula = cedula
        self.saldo = saldo
        self.prestamos = {}  # Diccionario para guardar los préstamos 

    def solicitar_prestamo(self, monto, fecha):
        """Crea un nuevo préstamo para el cliente y lo agrega al diccionario de préstamos."""
        prestamo = Prestamo(monto, fecha, self)
        self.prestamos[self.cedula] = prestamo  
        self.saldo += monto
        return prestamo

