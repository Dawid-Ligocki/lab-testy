import pytest
from zamowienie import Zamowienie, Produkt


@pytest.fixture
def zamowienie(mocker):
    zam = Zamowienie()
    zam.pozycje = []
    return zam


def test_dodawanie_pozycji(zamowienie, mocker):
    produkt_mock = mocker.Mock(spec=Produkt)
    produkt_mock.cena = 10
    zamowienie.dodaj_pozycje(produkt_mock, 3)

    assert len(zamowienie.pozycje) == 1
    assert zamowienie.pozycje[0]["produkt"] == produkt_mock
    assert zamowienie.pozycje[0]["ilosc"] == 3


def test_usuwanie_pozycji(zamowienie, mocker):
    produkt_mock = mocker.Mock(spec=Produkt)
    zamowienie.dodaj_pozycje(produkt_mock, 2)
    zamowienie.usun_pozycje(0)

    assert len(zamowienie.pozycje) == 0


def test_obliczanie_kwoty(zamowienie, mocker):
    produkt1_mock = mocker.Mock(spec=Produkt)
    produkt1_mock.cena = 10
    zamowienie.pozycje = [{"produkt": produkt1_mock, "ilosc": 2}]

    assert zamowienie.oblicz_kwote() == 20


def test_liczba_pozycji(zamowienie, mocker):
    zamowienie.pozycje = [{"produkt": mocker.Mock(spec=Produkt), "ilosc": 2},
                          {"produkt": mocker.Mock(spec=Produkt), "ilosc": 3}]

    assert zamowienie.liczba_pozycji() == 2


def test_wyczysc_zamowienie(zamowienie, mocker):
    zamowienie.pozycje = [{"produkt": mocker.Mock(spec=Produkt), "ilosc": 2},
                          {"produkt": mocker.Mock(spec=Produkt), "ilosc": 3}]

    zamowienie.wyczysc_zamowienie()

    assert len(zamowienie.pozycje) == 0


def test_znajdz_pozycje_po_produktcie(zamowienie, mocker):
    produkt1 = mocker.Mock(spec=Produkt)
    produkt2 = mocker.Mock(spec=Produkt)
    zamowienie.pozycje = [{"produkt": produkt1, "ilosc": 2},
                          {"produkt": produkt2, "ilosc": 3}]

    assert zamowienie.znajdz_pozycje_po_produktcie(produkt1) == 0
    assert zamowienie.znajdz_pozycje_po_produktcie(produkt2) == 1
    assert zamowienie.znajdz_pozycje_po_produktcie(mocker.Mock(spec=Produkt)) == -1


def test_zwroc_pozycje(zamowienie, mocker):
    pozycja_mock = {"produkt": mocker.Mock(spec=Produkt), "ilosc": 2}
    zamowienie.pozycje = [pozycja_mock]

    assert zamowienie.zwroc_pozycje(0) == pozycja_mock
    assert zamowienie.zwroc_pozycje(1) == None


def test_aktualizuj_ilosc(zamowienie, mocker):
    pozycja_mock = {"produkt": mocker.Mock(spec=Produkt), "ilosc": 2}
    zamowienie.pozycje = [pozycja_mock]

    zamowienie.aktualizuj_ilosc(0, 5)

    assert pozycja_mock["ilosc"] == 5


def test_oblicz_laczna_ilosc(zamowienie, mocker):
    zamowienie.pozycje = [{"produkt": mocker.Mock(spec=Produkt), "ilosc": 2},
                          {"produkt": mocker.Mock(spec=Produkt), "ilosc": 3}]

    assert zamowienie.oblicz_laczna_ilosc() == 5


def test_oblicz_srednia_cene(zamowienie, mocker):
    produkt1_mock = mocker.Mock(spec=Produkt)
    produkt1_mock.cena = 10

    produkt2_mock = mocker.Mock(spec=Produkt)
    produkt2_mock.cena = 5

    zamowienie.pozycje = [{"produkt": produkt1_mock, "ilosc": 2},
                          {"produkt": produkt2_mock, "ilosc": 3}]

    assert zamowienie.oblicz_srednia_cene() == 7.0
