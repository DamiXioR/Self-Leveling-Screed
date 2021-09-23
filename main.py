class Worek_Masy_Samopoziomujacej:
    def __init__(self, nazwa_masy, ilosc_powierzni_jaka_pokrywa, wielkosc_powierzni_jaka_pokrywa):
        self.nazwa_masy = nazwa_masy
        self.wielkosc_powierzni_jaka_pokrywa = ilosc_powierzni_jaka_pokrywa
        self.wysokosc_powierzni_jaka_pokrywa = wielkosc_powierzni_jaka_pokrywa

def ile_kupic_workow_masy_samopoziomujacej(worek_masy_samopoziomujacej, powierzchnia_do_wylania, wysokosc_wylania_masy):
    wspolczynnik = worek_masy_samopoziomujacej.wysokosc_powierzni_jaka_pokrywa / wysokosc_wylania_masy
    ilosc_workow_do_kupienia = (powierzchnia_do_wylania / worek_masy_samopoziomujacej.wielkosc_powierzni_jaka_pokrywa) / wspolczynnik 
    return ilosc_workow_do_kupienia
    

nazwa_masy = input("Podaj nazwę masy: ")
wielkosc_powierzni_jaka_pokrywa = float(input("Podaj wielkość powierzchni jaką według producenta pokrywa worek w metrach kwatdratowych: "))
wysokosc_powierzni_jaka_pokrywa = float(input("Podaj wysokość powierzchni jaką według producenta pokrywa worek w centymetrach: "))
    
worek_masy_samopoziomujacej = Worek_Masy_Samopoziomujacej(nazwa_masy, wielkosc_powierzni_jaka_pokrywa, wysokosc_powierzni_jaka_pokrywa)

wielkosc_powierzni_do_pokrycia = float(input("Podaj wielkość powierzchni jaką chcesz pokryć masą samopoziomującą metrach kwatdratowych: "))
wysokosc_powierzni_do_pokrycia = float(input("Podaj wysokość powierzchni jaką chcesz pokryć masą samopoziomującą w centymetrach: "))

wynik = ile_kupic_workow_masy_samopoziomujacej(worek_masy_samopoziomujacej, wielkosc_powierzni_do_pokrycia, wysokosc_powierzni_do_pokrycia)
print("Potrzebujesz: ", wynik, " worków masy samopoziomującej marki", worek_masy_samopoziomujacej.nazwa_masy)
