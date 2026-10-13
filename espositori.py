class Espositori:
    def __init__(self,codEspositore,nome,cognome):
        self.codEspositore = codEspositore
        self.nome = nome
        self.cognome = cognome
    def __str__(self):
        return f"{self.codEspositore} {self.nome} {self.cognome}