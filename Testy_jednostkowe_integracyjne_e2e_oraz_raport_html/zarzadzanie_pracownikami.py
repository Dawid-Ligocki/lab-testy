class ZarzadzaniePracownikami:
    def __init__(self):
        self.pracownicy = []

    def dodaj_pracownika(self, pracownik):
        self.pracownicy.append(pracownik)

    def usun_pracownika(self, pracownik):
        self.pracownicy.remove(pracownik)

    def srednia_pensja(self):
        if len(self.pracownicy) > 0:
            suma_pensji = sum(pracownik.pensja for pracownik in self.pracownicy)
            return suma_pensji / len(self.pracownicy)
        else:
            return 0

    def pracownicy_aktywni(self):
        return [pracownik for pracownik in self.pracownicy if pracownik.status == "Aktywny"]

    def pracownicy_zwolnieni(self):
        return [pracownik for pracownik in self.pracownicy if pracownik.status == "Zwolniony"]

    def pracownicy_z_pensja_wieksza_niz(self, kwota):
        return [pracownik for pracownik in self.pracownicy if pracownik.pensja > kwota]

    def pracownik_z_imieniem(self, imie):
        for pracownik in self.pracownicy:
            if pracownik.imie == imie:
                return pracownik
        return None

    def pracownik_z_nazwiskiem(self, nazwisko):
        for pracownik in self.pracownicy:
            if pracownik.nazwisko == nazwisko:
                return pracownik
        return None

    def podwyzka_wszystkim(self, procent):
        for pracownik in self.pracownicy:
            pracownik.podwyzka(procent)
