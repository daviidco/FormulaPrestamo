class Prestamo:
    def __init__(self, cantprestamo, numcuotas, interes):
        self.cantPrestamo = cantprestamo
        self.numcuotas = numcuotas
        self.interes = interes
        self.valCuota = self.cantPrestamo * ((self.interes * ((1 + self.interes) ** self.numcuotas)) /
                                             (((1 + self.interes) ** self.numcuotas) - 1))
        self.totalCuotas = self.valCuota * self.numcuotas
        self.costofinanciero = self.totalCuotas - self.cantPrestamo
