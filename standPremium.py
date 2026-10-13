from stand import Stand
class StandPremium(Stand):
    def __init__(self,codStand,metriQuadri,padiglione,prezzo,posizione):
        super().__init__(codStand,metriQuadri,padiglione,prezzo)
        self.posizione = posizione