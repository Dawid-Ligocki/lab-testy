class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja
        self.status = "Aktywny"

    def podwyzka(self, procent):
        self.pensja += self.pensja * (procent / 100)

    def zwolnij(self):
        self.pensja = 0
        self.status = "Zwolniony"

    def awansuj(self):
        self.podwyzka(10)
        self.status = "Kierownik"

    def __str__(self):
        return f"{self.imie} {self.nazwisko} - {self.pensja}, {self.status}"
