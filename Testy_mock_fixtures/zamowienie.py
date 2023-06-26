class Zamowienie:
    def __init__(self):
        self.pozycje = []

    def dodaj_pozycje(self, produkt, ilosc):
        self.pozycje.append({"produkt": produkt, "ilosc": ilosc})

    def usun_pozycje(self, indeks):
        if indeks >= 0 and indeks < len(self.pozycje):
            del self.pozycje[indeks]

    def oblicz_kwote(self):
        kwota = 0
        for pozycja in self.pozycje:
            produkt = pozycja["produkt"]
            ilosc = pozycja["ilosc"]
            kwota += produkt.cena * ilosc
        return kwota

    def liczba_pozycji(self):
        return len(self.pozycje)

    def wyczysc_zamowienie(self):
        self.pozycje = []

    def znajdz_pozycje_po_produktcie(self, produkt):
        for i, pozycja in enumerate(self.pozycje):
            if pozycja["produkt"] == produkt:
                return i
        return -1

    def zwroc_pozycje(self, indeks):
        if indeks >= 0 and indeks < len(self.pozycje):
            return self.pozycje[indeks]
        return None

    def aktualizuj_ilosc(self, indeks, nowa_ilosc):
        if indeks >= 0 and indeks < len(self.pozycje):
            self.pozycje[indeks]["ilosc"] = nowa_ilosc

    def oblicz_laczna_ilosc(self):
        ilosc = 0
        for pozycja in self.pozycje:
            ilosc += pozycja["ilosc"]
        return ilosc

    def oblicz_srednia_cene(self):
        if len(self.pozycje) == 0:
            return 0
        suma_cen = sum(pozycja["produkt"].cena * pozycja["ilosc"] for pozycja in self.pozycje)
        suma_ilosci = sum(pozycja["ilosc"] for pozycja in self.pozycje)
        return suma_cen / suma_ilosci


class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena
