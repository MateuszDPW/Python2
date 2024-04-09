class Kolejka:
    def __init__(self):
        self.kolejka = []

    # dodaje osobę na koniec kolejki
    def dodaj_do_kolejki(self, osoba):
        self.kolejka.append(osoba)
        print(f"Osoba {self.osoba} została dodana do kolejki")

    # obsługuje (i usuwa) osobę z przodu kolejki
    def obsloz_osobe(self, osoba):
        self.kolejka.pop()
    
    # wyswietla  aktualny stan kolejki
    def pokaz_kolejke(self):
        self.kolejka

    #dodanie kilku osob do kolejki na raz
    def dodaj_grupe(self): 
        osoby=input("Podaj liczbe osób, które chcesz dodać do kolei:\n").split()
        for i in range(len(osoby)):
            try:
                self.kolejka.append(int(osoby[i]))
            except ValueError:
                print ("To nie jest poprawna wartość!")

    #usuwa określoną osobę z kolejki
    def usun_z_kolejki(self, osoba):
        try:
            self.kolejka.remove(osoba)
            print(f"Osoba {self.osoba} została usunięta")
        except: print("Nie ma takiej osoby w kolejce")

kolejka = Kolejka()
