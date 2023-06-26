from pracownik import Pracownik
from zarzadzanie_pracownikami import ZarzadzaniePracownikami

def test_dodaj_pracownika():
    zarzadzanie = ZarzadzaniePracownikami()
    pracownik = Pracownik("Jan", "Kowalski", 5000)
    zarzadzanie.dodaj_pracownika(pracownik)
    assert len(zarzadzanie.pracownicy) == 1

def test_usun_pracownika():
    zarzadzanie = ZarzadzaniePracownikami()
    pracownik = Pracownik("Jan", "Kowalski", 5000)
    zarzadzanie.dodaj_pracownika(pracownik)
    zarzadzanie.usun_pracownika(pracownik)
    assert len(zarzadzanie.pracownicy) == 0

def test_srednia_pensja():
    zarzadzanie = ZarzadzaniePracownikami()
    pracownik1 = Pracownik("Jan", "Kowalski", 5000)
    pracownik2 = Pracownik("Anna", "Nowak", 7000)
    zarzadzanie.dodaj_pracownika(pracownik1)
    zarzadzanie.dodaj_pracownika(pracownik2)
    assert zarzadzanie.srednia_pensja() == 6000

def test_pracownicy_aktywni():
    zarzadzanie = ZarzadzaniePracownikami()
    pracownik1 = Pracownik("Jan", "Kowalski", 5000)
    pracownik2 = Pracownik("Anna", "Nowak", 7000)
    pracownik3 = Pracownik("Adam", "Malinowski", 4500)
    zarzadzanie.dodaj_pracownika(pracownik1)
    zarzadzanie.dodaj_pracownika(pracownik2)
    zarzadzanie.dodaj_pracownika(pracownik3)
    pracownik2.zwolnij()
    aktywni = zarzadzanie.pracownicy_aktywni()
    assert len(aktywni) == 2
    assert pracownik1 in aktywni
    assert pracownik3 in aktywni

def test_pracownicy_zwolnieni():
    zarzadzanie = ZarzadzaniePracownikami()
    pracownik1 = Pracownik("Jan", "Kowalski", 5000)
    pracownik2 = Pracownik("Anna", "Nowak", 7000)
    pracownik3 = Pracownik("Adam", "Malinowski", 4500)
    zarzadzanie.dodaj_pracownika(pracownik1)
    zarzadzanie.dodaj_pracownika(pracownik2)
    zarzadzanie.dodaj_pracownika(pracownik3)
    pracownik1.zwolnij()
    zwolnieni = zarzadzanie.pracownicy_zwolnieni()
    assert len(zwolnieni) == 1
    assert pracownik1 in zwolnieni

def test_pracownicy_z_pensja_wieksza_niz():
    zarzadzanie = ZarzadzaniePracownikami()
    pracownik1 = Pracownik("Jan", "Kowalski", 5000)
    pracownik2 = Pracownik("Anna", "Nowak", 7000)
    pracownik3 = Pracownik("Adam", "Malinowski", 4500)
    zarzadzanie.dodaj_pracownika(pracownik1)
    zarzadzanie.dodaj_pracownika(pracownik2)
    zarzadzanie.dodaj_pracownika(pracownik3)
    pensja_wieksza = zarzadzanie.pracownicy_z_pensja_wieksza_niz(5000)
    assert len(pensja_wieksza) == 1
    assert pracownik2 in pensja_wieksza

def test_pracownik_z_imieniem():
    zarzadzanie = ZarzadzaniePracownikami()
    pracownik1 = Pracownik("Jan", "Kowalski", 5000)
    pracownik2 = Pracownik("Anna", "Nowak", 7000)
    zarzadzanie.dodaj_pracownika(pracownik1)
    zarzadzanie.dodaj_pracownika(pracownik2)
    assert zarzadzanie.pracownik_z_imieniem("Jan") == pracownik1
    assert zarzadzanie.pracownik_z_imieniem("Adam") is None

def test_pracownik_z_nazwiskiem():
    zarzadzanie = ZarzadzaniePracownikami()
    pracownik1 = Pracownik("Jan", "Kowalski", 5000)
    pracownik2 = Pracownik("Anna", "Nowak", 7000)
    zarzadzanie.dodaj_pracownika(pracownik1)
    zarzadzanie.dodaj_pracownika(pracownik2)
    assert zarzadzanie.pracownik_z_nazwiskiem("Kowalski") == pracownik1
    assert zarzadzanie.pracownik_z_nazwiskiem("Malinowski") is None

def test_podwyzka_wszystkim():
    zarzadzanie = ZarzadzaniePracownikami()
    pracownik1 = Pracownik("Jan", "Kowalski", 5000)
    pracownik2 = Pracownik("Anna", "Nowak", 7000)
    zarzadzanie.dodaj_pracownika(pracownik1)
    zarzadzanie.dodaj_pracownika(pracownik2)
    zarzadzanie.podwyzka_wszystkim(10)
    assert pracownik1.pensja == 5500
    assert pracownik2.pensja == 7700

def test_testy_integracyjne():
    zarzadzanie = ZarzadzaniePracownikami()
    pracownik1 = Pracownik("Jan", "Kowalski", 5000)
    pracownik2 = Pracownik("Anna", "Nowak", 7000)
    zarzadzanie.dodaj_pracownika(pracownik1)
    zarzadzanie.dodaj_pracownika(pracownik2)
    assert len(zarzadzanie.pracownicy) == 2
    assert zarzadzanie.srednia_pensja() == 6000
    pracownik1.zwolnij()
    zwolnieni = zarzadzanie.pracownicy_zwolnieni()
    assert len(zwolnieni) == 1
    assert pracownik1 in zwolnieni


def test_dodaj_i_usun_pracownika():
    zarzadzanie = ZarzadzaniePracownikami()

    # Test dodawania pracownika
    zarzadzanie.dodaj_pracownika(Pracownik("Jan", "Kowalski", 5000))
    assert len(zarzadzanie.pracownicy) == 1

    # Test usunięcia pracownika
    pracownik = zarzadzanie.pracownicy[0]
    zarzadzanie.usun_pracownika(pracownik)
    assert len(zarzadzanie.pracownicy) == 0

def test_srednia_pensja_po_podwyzce():
    zarzadzanie = ZarzadzaniePracownikami()

    # Dodanie pracowników
    zarzadzanie.dodaj_pracownika(Pracownik("Jan", "Kowalski", 5000))
    zarzadzanie.dodaj_pracownika(Pracownik("Anna", "Nowak", 7000))

    # Awansowanie jednego pracownika (z podwyżką)
    pracownik = zarzadzanie.pracownik_z_imieniem("Jan")
    pracownik.awansuj()

    # Sprawdzenie średniej pensji po podwyżce
    assert zarzadzanie.srednia_pensja() == 6250

def test_pracownicy_aktywni_po_zwolnieniu():
    zarzadzanie = ZarzadzaniePracownikami()

    # Dodanie pracowników
    zarzadzanie.dodaj_pracownika(Pracownik("Jan", "Kowalski", 5000))
    zarzadzanie.dodaj_pracownika(Pracownik("Anna", "Nowak", 7000))
    zarzadzanie.dodaj_pracownika(Pracownik("Adam", "Malinowski", 4500))

    # Zwolnienie jednego pracownika
    pracownik = zarzadzanie.pracownik_z_imieniem("Anna")
    pracownik.zwolnij()

    # Sprawdzenie listy aktywnych pracowników
    aktywni = zarzadzanie.pracownicy_aktywni()
    assert len(aktywni) == 2
    assert zarzadzanie.pracownik_z_imieniem("Jan") in aktywni
    assert zarzadzanie.pracownik_z_imieniem("Adam") in aktywni
