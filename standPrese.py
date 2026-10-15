from stand import Stand
class StandPrese (Stand):
    def __init__(self,codStand,metriQuadri,padiglione,prezzo,numeroPrese):
        super().__init__(codStand,metriQuadri,padiglione,prezzo)
        self.numeroPrese = int(numeroPrese)
        self.prezzo = prezzo *(1+0.07*numeroPrese)
