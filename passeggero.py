"""Creo la classe passeggero"""
class Passeggero:
    def __init__(self,cod_pass, nome, cognome):
        self.cod_pass = cod_pass
        self.nome = nome
        self.cognome = cognome
        self.cabina_associata=None

    def __str__(self):
        stato= f'Cabina {self.cabina_associata}' if self.cabina_associata else ''
        return (f"Passeggero {self.cod_pass}: "
                f"{self.nome} {self.cognome}, {stato}")

    def __repr__(self):
        return (f"Passeggero {type(self).__name__}"
                f"cod_pass={self.cod_pass}, nome={self.nome}, cognome={self.cognome}")