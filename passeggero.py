"""Creo la classe passeggero"""
class Passeggero:
    def __init__(self,cod_pass, nome, cognome):
        self.cod_pass = cod_pass
        self.nome = nome
        self.cognome = cognome

    def __str__(self):
        return (f"Passeggero {self.cod_pass}: "
                f"{self.nome} {self.cognome}")

    def __repr__(self):
        return (f"Passeggero {type(self).__name__}"
                f"cod_pass={self.cod_pass}, nome={self.nome}, cognome={self.cognome}")