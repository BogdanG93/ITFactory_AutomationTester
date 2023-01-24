import math
from datetime import datetime

"""1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()"""


class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print("Culoarea cercului:", self.culoare + ",", "raza cercului:", self.raza)

    def aria(self):
        aria = math.pi * self.raza ** 2
        print("Aria cercului este: %.2f" % aria)

    def diametru(self):
        diametru = 2 * self.raza
        print("Diametrul cercului este:", diametru)

    def circumferinta(self):
        circumferinta = 2 * math.pi * self.raza
        print("Circumferinta cercului este: %.2f" % circumferinta)


cerc1 = Cerc(3, "albastru")
cerc2 = Cerc(5, "galben")

cerc1.descrie_cerc()
cerc1.aria()
cerc1.diametru()
cerc1.circumferinta()

cerc2.descrie_cerc()
cerc2.aria()
cerc2.diametru()
cerc2.circumferinta()

"""2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul

self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie()."""


class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f"Descriere dreptunghi: lungime = {self.lungime}, latime = {self.latime}, culoare = {self.culoare}")

    def aria(self):
        print("Aria dreptunghiului este:", self.lungime * self.latime)

    def perimetrul(self):
        print("Perimetrul dreptunghiului este:", 2 * (self.lungime + self.latime))

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare
        print("Am schimbat culoarea cercului, acum este", self.culoare)


d1 = Dreptunghi(15, 10, "albastru")
d1.descrie()
d1.aria()
d1.perimetrul()
d1.schimba_culoarea("rosu")
d1.descrie()
print()
d2 = Dreptunghi(12, 6, "portocaliu")
d2.descrie()
d2.aria()
d2.perimetrul()
d2.schimba_culoarea("verde")
d2.descrie()

"""3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)"""


class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(self.nume, "vrea sa lucreze in IT.")

    def nume_complet(self):
        print("Nume complet:", self.nume + " " + self.prenume)

    def salariu_lunar(self):
        print(self.nume + " " + self.prenume, "are un salariu lunar de", self.salariu, "lei.")

    def salariu_anual(self):
        print("Salariul anual este de %.2f" % (self.salariu * 12), "lei.")

    def marire_salariu(self, procent):
        self.salariu = procent / 100 * self.salariu + self.salariu
        print("Incepem bine anul. Ti-am marit salariul cu", procent, "% (nu uita sa scazi inflatia).")
        return self.salariu


angajat1 = Angajat("Geagu", "Bogdan", 2700.52)
angajat1.descrie()
angajat1.nume_complet()
angajat1.salariu_lunar()
angajat1.salariu_anual()
angajat1.marire_salariu(10)
angajat1.salariu_lunar()
print()
angajat2 = Angajat("Pop", "Octavian", 3500.85)
angajat2.descrie()
angajat2.nume_complet()
angajat2.salariu_lunar()
angajat2.salariu_anual()
angajat2.marire_salariu(14)
angajat2.salariu_lunar()

"""4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)"""


class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f"Titularul contului, {self.titular_cont}, are in contul \"{self.iban}\" suma de {self.sold} lei.")

    def debitare_cont(self, suma):
        self.sold -= suma
        print(f"Titularului {self.titular_cont} i s-a debitat din contul \"{self.iban}\" suma de {suma} lei. "
              f"Sold curent: {self.sold} lei.")

    def creditare_cont(self, suma):
        self.sold += suma
        print(f"Titularului {self.titular_cont} i s-a adaugat in contul \"{self.iban}\" suma de {suma} lei. "
              f"Sold curent: {self.sold} lei.")


cont1 = Cont(542855, "Geagu Bogdan", 1500)
cont1.afisare_sold()
cont1.debitare_cont(500)
cont1.creditare_cont(1500)
print()
cont2 = Cont(854241, "Pop Octavian Marius", 8200)
cont2.afisare_sold()
cont2.debitare_cont(2700)
cont2.creditare_cont(5000)

"""Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google.
1. Clasa Factura
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)

● generează_factura() - va printa tabelar dacă reușiți
Factura seria x numar y
Data: generați automat data de azi
Produs | cantitate | preț bucată | Total
Telefon | 7 | 700 | 49000"""


def i_like_underscores():
    print(" ________________________________________________ ")


class Factura:
    seria = '5442'

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate
        return self.cantitate

    def schimba_pretul(self, pret):
        self.pret_buc = pret
        return self.pret_buc

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume
        return self.nume_produs

    def genereaza_factura(self):
        data = datetime.today().strftime('%d.%m.%Y')
        nume = self.nume_produs
        cantitate = self.cantitate
        pret = self.pret_buc
        total = self.cantitate * self.pret_buc
        print("Data:", data)
        print(f"Factura seria {self.seria} nr. {self.numar}")
        i_like_underscores()
        print("{:<20} {:<10} {:<5} {:<5}".format("| Produs", "| Cantitate", "| Preț", "| Total  |"))
        i_like_underscores()
        print("{:<20} {:<11} {:<6} {:<5}".format("| " + str(nume), "|    " + str(cantitate),
                                                 "| " + str(pret), "| " + str(total) + " |"))
        i_like_underscores()


factura1 = Factura(5425, "ciocolata", 413, 5)
factura1.schimba_cantitatea(350)
factura1.schimba_pretul(4.8)
factura1.schimba_nume_produs("Ciocolata cu alune")
factura1.genereaza_factura()
print()
factura2 = Factura(5426, "inghetata", 2500, 3)
factura2.schimba_cantitatea(1875)
factura2.schimba_pretul(2.5)
factura2.schimba_nume_produs("Inghetata ITF")
factura2.genereaza_factura()

"""2.Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate mașinile cand ies din fabrica sunt gri
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
Culori disponibile = alegeți voi 5-7 culori
Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
● descrie() - se vor printa toate atributele, în afară de culori_disponibile
● înmatriculare() - va schimba atributul înmatriculată în True
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
culoare e în opțiunea de culori disponibile, altfel afișați o eroare
● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
accelera până la viteza maximă
● franeaza() - mașina se va opri și va avea viteza 0"""


class Masina:
    marca = "Dacia"
    culoare = "gri"
    viteza_actuala = 0
    culori_disponibile = {"rosu", "verde", "albastru", "oranj", "galben"}
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        print(f"Masina:\nmarca:{self.marca}, model: {self.model}, culoare:{self.culoare}, "
              f"viteza actuala: {self.viteza_actuala},inmatriculata: {self.inmatriculata},"
              f" viteza maxima: {self.viteza_maxima}")

    def inmatriculare(self):
        self.inmatriculata = True

    def vopseste(self, culoare):
        if culoare in self.culori_disponibile:
            print("Ai vopsit masina in culoarea", culoare)
            self.culoare = culoare
        else:
            print("ERROR. Nu avem disponibila aceasta culoare.")

    def acceleaza(self, viteza):
        if viteza <= 0:
            print("ERROR. Ai gresit pedala baiatul sau fata mea.")
        else:
            if viteza < self.viteza_maxima:
                print(f"Am accelerat masina si am ajuns la viteza de {viteza} km/h.")
                self.viteza_actuala = viteza
            else:
                print(f"Am accelerat masina si am ajuns la viteza de {self.viteza_maxima} km/h.")
                self.viteza_actuala = self.viteza_maxima

    def franeaza(self):
        print("Am apasat pedala de frana.")
        self.viteza_actuala = 0
        print("Viteza actuala:", self.viteza_actuala)


masina1 = Masina("Duster", 220)
masina1.descrie()
masina1.inmatriculare()
masina1.vopseste("alb")
masina1.acceleaza(230)
masina1.franeaza()

masina2 = Masina("Logan", 180)
masina2.descrie()
masina2.inmatriculare()
masina2.vopseste("rosu")
masina2.acceleaza(-5)
masina2.franeaza()

"""3. Clasa TodoList
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
Metode:

● adauga_task(nume, descriere) - se va adauga in dict
● finalizează_task(nume) - se va sterge din dict
● afișează_todo_list() - doar cheile
● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
printăm detalii suplimentare.
○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
adauge.
○ Dacă acesta răspunde nu - la revedere
○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în dict"""


class TodoList:
    todo = {}

    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere
        print("Todo list, dupa adaugarea noului task: ", self.todo)

    def finalizeaza_task(self, nume):
        print(f"Task done:\"{nume}\", descriere: \"{self.todo[nume]}\"")
        self.todo.pop(nume)
        print("Todo list, dupa stergerea task-ului: ", self.todo)

    def afiseaza_todo_list(self):
        print("Todo list curent:")
        for keys in self.todo.items():
            print(keys)

    def afiseaza_detalii_suplimentare(self, nume):
        if nume not in self.todo.keys():
            add_new_task = input(f"Task-ul cautat \"{nume}\" nu este in todo list. Vrei sa-l adaugam?\n"
                                 f"1.Da     2.Nu\n").lower()
            if add_new_task == "da" or add_new_task == "1":
                descriere = input("Adauga o descriere task-ului: ")
                self.adauga_task(nume, descriere)
            else:
                print("Ok, bye bye!")
        else:
            print(f"Task-ul pe care-l cauti, \"{nume}\" este deja in todo list cu descrierea: \"{self.todo[nume]}\"")


dict1 = TodoList()
dict1.adauga_task("scrie cod", "Azi, 16.01.2023, trebuie sa rezolvi tema06 de la curs.")
dict1.adauga_task("bea o bere", "Dupa ce-ti faci tema scoate una rece din frigider.")
dict1.finalizeaza_task("bea o bere")
dict1.afiseaza_todo_list()
dict1.afiseaza_detalii_suplimentare("fa sport")
dict1.afiseaza_detalii_suplimentare("scrie cod")
dict1.afiseaza_todo_list()
# ar trebui sa golim dictionarul la adaugarea unui alt obiect, ca sa nu intercaleze cu task-urile de la primul
dict1.todo.clear()
print()
dict2 = TodoList()
dict2.adauga_task("recapitulare OOP", "Repeta notiunea de clasa, atribute, metode si OOP pillars.")
dict2.adauga_task("make coffee", "Dry your tears in coffee.")
dict2.adauga_task("watch cute cats", "Take a break and watch videos with cutie-pies cats.")
dict2.finalizeaza_task("make coffee")
dict2.afiseaza_todo_list()
dict2.afiseaza_detalii_suplimentare("make more coffee")
dict2.afiseaza_detalii_suplimentare("make more coffee")
dict2.afiseaza_todo_list()
