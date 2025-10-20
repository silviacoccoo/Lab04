import csv
from cabina import Cabina
from cabinaDeluxe import CabinaDeluxe
from cabinaPetFriendly import CabinaPetFriendly
from passeggero import Passeggero

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""

        self._nome = nome # attributo della nave

        # inizializzo le strutture dati
        self.cabine = {}
        self.passeggeri={}

    def __str__(self): # per stampare una versione leggibile
        return f"{self.nome}"

    def __repr__(self): # stamapa per il debug
        return (f"{type(self).__name__}"
                f"nome={self.nome}")

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        try:
            with open(file_path, "r", newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for riga in reader:
                        if riga: #verifichiamo che la riga esista, non sia vuota
                            if riga[0].startswith('CAB'):
                                cod_cab=riga[0]
                                num_letti=int(riga[1])
                                ponte=riga[2]
                                prezzo=int(riga[3])

                                if riga[4]=='<unset>':
                                    cabina=Cabina(cod_cab, num_letti, ponte, prezzo) # creo oggetto
                                    self.cabine[cod_cab] = cabina # aggiungo al dizionario con chiave cod_cab
                                else:
                                    if riga[4]=='Lussuosa' or riga[4]=='Moderna' or riga[4]=='Classica':
                                        tipo=riga[4]
                                        cabina1=CabinaDeluxe(cod_cab, num_letti, ponte, prezzo, tipo)
                                        self.cabine[cod_cab] = cabina1
                                    else:
                                        animali=int(riga[4])
                                        cabina2=CabinaPetFriendly(cod_cab, num_letti, ponte, prezzo, animali)
                                        self.cabine[cod_cab] = cabina2
                            else:
                                cod_pass=riga[0]
                                nome=riga[1]
                                cognome=riga[2]
                                passeggero=Passeggero(cod_pass, nome, cognome) # creo oggetto passeggero
                                self.passeggeri[cod_pass]=passeggero # aggiungo al dizionario
        except FileNotFoundError:
            print("File non trovato")
        # TODO

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

