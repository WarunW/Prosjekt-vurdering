class Spill:
    def __init__(self):
        self.spiller = Spiller("Spiller")
        self.setup()

    def setup(self):
        inngang = Rom("Inngang", "Start.")
        gang = Rom("Gang", "En gang.")

        inngang.leggTilUtgang("nord", gang)
        gang.leggTilUtgang("sør", inngang)

        self.nåværendeRom = inngang