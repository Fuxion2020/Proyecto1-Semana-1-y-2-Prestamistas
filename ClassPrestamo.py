
class Prestamo:    
    def __init__(self, monto, fecha, cliente):
        self.monto = monto
        self.fecha = fecha
        self.cliente = cliente
        self.monto_pagado = 0     


    def calcular_monto_diario(self):     # Calcula el monto diario que debe pagar el cliente por el préstamo
        return self.monto / 24           # Retornar el monto del préstamo dividido entre 24


    def calcular_monto_total(self):      # Calcula el monto total que debe pagar el cliente por el préstamo
        return self.monto * 1.2          # Retornar el monto del préstamo más el 20% de interés





