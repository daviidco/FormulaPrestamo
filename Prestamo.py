import decimal

class Prestamo:
    def __init__(self, cantprestamo, numcuotas, interes):
        self.cantPrestamo = cantprestamo
        self.numcuotas = numcuotas
        self.interes = decimal.Decimal(interes)
        #self.valCuota = self.cantPrestamo * ((self.interes * ((1 + self.interes) ** self.numcuotas)) /
        #                                     (((1 + self.interes) ** self.numcuotas) - 1))

        term1 = decimal.Decimal((1 + self.interes)) ** self.numcuotas
        term2 = (decimal.Decimal(1 + self.interes) ** self.numcuotas) - 1
        self.valCuota = self.cantPrestamo * ((self.interes * term1 /term2))
        self.totalCuotas = self.valCuota * self.numcuotas
        self.costofinanciero = self.totalCuotas - self.cantPrestamo
