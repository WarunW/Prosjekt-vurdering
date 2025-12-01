from klasser import *
from Rom import *

lobby = Rom("lobby", "En stille lobby.")
kontor = Rom("kontor", "Et lite kontor.")
hvelv = Rom("hvelv", "Et stort bankhvelv. Inne i rommet står selve hvelvkassen du må åpne for å stikke av.", lås="låst")

lobby.leggTilUtgang("kontor", kontor)
kontor.leggTilUtgang("lobby", lobby)
kontor.leggTilUtgang("hvelv", hvelv)
hvelv.leggTilUtgang("kontor", kontor)

lobby.leggTilGjenstand(EnergyBar())
kontor.leggTilGjenstand(AccessCard())
kontor.settFiende(Sikkerhetsvakt())

spiller = Spiller("Bankraner")
rom = lobby
spiller.settRom(rom)

print("Velkommen til bankran-spillet!")
print("Skriv: gå [rom], ta [item], bruk [item], angrip, inventory, slutt")

while True:
    rom.visInfo()
    kommando = input(">").lower().strip()
    
    if kommando == "slutt":
        print("Spillet avsluttes.")
        break

    elif kommando.startswith("gå "):
        retning = kommando[3:]
        nytt = rom.hentUtgang(retning)
        if nytt is None:
            print("Du kan ikke gå dit.")
        elif nytt.erLåst():
            print("Døren er låst.")
        else:
            rom = nytt
            spiller.settRom(rom)

    elif kommando.startswith("ta "):
        navn = kommando[3:]
        funnet = None
        for g in rom.hentGjenstander():
            if g._navn == navn:
                funnet = g

        if funnet:
            rom.hentGjenstander().remove(funnet)
            spiller._inventar.addItem(funnet)
            print(f"Du tok {navn}.")
        else:
            print("Den gjenstanden finnes ikke her.")

    elif kommando.startswith("bruk "):
        navn = kommando[5:]
        spiller.useItem(navn)

    elif kommando == "inventar":
        spiller._inventar.listItem()

    elif kommando == "angrip":
        fiende = rom.hentFiende()
        if fiende and fiende.is_alive():
            spiller.attack(fiende)
            if fiende.is_alive():
                fiende.attack(spiller)
        else:
            print("Det er ingen fiende her.")

    elif kommando == "åpne hvelv":
        if rom._navn == "hvelv" and spiller._inventar.hasItem("kodekort"):
            print("Du åpner hvelvet og rømmer! Du vant!")
            break
        else:
            print("Du kan ikke åpne hvelvet nå.")
    else:
        print("Ukjent kommando.")
        print("Mulige kommandoer: gå [rom], ta [item], bruk [item], angrip, inventory, slutt, åpne hvelv.")