class Vozila:

    def __init__(
            self,
            vid: str,
            model: str,
            broj_na_trkala: str = "Broj na trkala"
    ):
        self.vid = vid
        self.model = model
        self.broj_na_trkala = broj_na_trkala
    
    def tip_na_Vozila(self):
        print(f'Ova vozilo e od vidot {self.vid} i od klasata: {self.model}, Broj na trkala: {self.broj_na_trkala}')


class Moped(Vozila):
    zvuk = "Vroom Vroom vrrrrrrrrrrrr"

    def __init__(
            self,
            boja: str
    ):
        super().__init__('trkacki motor', 'Yamaha R6', broj_na_trkala="2")
        self.boja = boja
    
    def tip_na_Vozila(self):
        super().tip_na_Vozila()
        print(f"Mopedot ima {self.boja} boja.")


class Avtomobil(Vozila):
    zvuk = "voooo voooo"

    def __init__(
            self,
            boja: str
    ):
        super().__init__('trkacki avtomobil', 'Ferrari', broj_na_trkala="4")
        self.boja = boja
    
    def tip_na_Vozila(self):
        super().tip_na_Vozila()
        print(f"Avtomobilot ima {self.boja} boja.")
        
class Trike(Vozila):
    zvuk = "Vr vr vr"

    def __init__(
            self,
            boja: str
    ):
        super().__init__('A trike', 'Slingshot', broj_na_trkala="3")
        self.boja = boja
    
    def tip_na_Vozila(self):
        super().tip_na_Vozila()
        print(f"Trikot ima {self.boja} boja.")


objekt1 = Moped(boja="crna")
objekt2 = Avtomobil(boja="crvena")
objekt3 = Trike(boja="zelena")

objekt1.tip_na_Vozila()
print("Zvuk na mopedot:", objekt1.zvuk)

objekt2.tip_na_Vozila()
print("Zvuk na avtomobilot:", objekt2.zvuk)

objekt3.tip_na_Vozila()
print("Zvik na trikot:", objekt3.zvuk)