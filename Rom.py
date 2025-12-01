class Rom:
    def __init__(self, navn: str, beskrivelse: str, lås = "åpen"):
        self._navn = navn
        self._beskrivelse = beskrivelse
        self._gjenstander = []
        self._fiende = None
        self.utganger = []   
        self._låsStatus = lås

    def erLåst(self):
        return self._låsStatus == "låst"

    def låsOpp(self):
        self._låsStatus = "åpen"
        print("Døren åpnes")

    def navn(self):
        return self._navn

    def beskrivelse(self):
        return self._beskrivelse

    def leggTilGjenstander(self, gjenstander):
        for g in gjenstander:
            self._gjenstander.append(g)

    def leggTilGjenstand(self, gjenstand):
        self._gjenstander.append(gjenstand)
            
    def hentGjenstander(self):
        return self._gjenstander

    def settFiende(self, fiende):
        self._fiende = fiende

    def hentFiende(self):
        return self._fiende

    def leggTilUtgang(self, retning: str, rom: "Rom"):
        self.utganger.append((retning, rom))

    def hentUtgang(self, retning: str):
        for r, rom in self.utganger:
            if r == retning:
                return rom
        return None
    
    def visInfo(self):
        print("--------------------------------")
        print(f"Du er i {self._navn}.")
        print(self._beskrivelse)

        if self._fiende is not None and self._fiende.is_alive():
            print(f"Her står det en {self._fiende._navn}.")
            
        if self._gjenstander:
            print("Du ser:")
            for g in self._gjenstander:
                print(g._navn)

        if self.utganger:
            print("Utganger:")
            for retning, rom in self.utganger:
                print(retning)