class Stand:
    def __init__(self,codStand,metriQuadri,padiglione,prezzo):
        self.codStand = codStand
        self.metriQuadri = float(metriQuadri)
        self.padiglione = int(padiglione)
        self.prezzo = float(prezzo)

    def __str__(self):
        return f"{self.codStand} {self.metriQuadri} {self.padiglione} {self.prezzo}"
