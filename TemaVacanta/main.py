import random
from math import ceil

""" OBLIGATORII
1.1 Creeaza 3 liste care sa contina animale:
a. Mamifere
b. Reptile
c. Pasari
"""
mamifere = ['cartita', 'arici', 'veverita', 'soarece']
reptile = ['limax', 'varan', 'lipitoare', 'gecko']
pasari = ['kiwi', 'sabot', 'cucuveaua', 'flamingo']

print('Avem listele:')
print(f'Mamifere: {mamifere}')
print(f'Reptile: {reptile}')
print(f'Pasari: {pasari}\n')

"""1.2. Sorteaza fiecare lista alphabetic"""
mamifere, reptile, pasari = sorted(mamifere), sorted(reptile), sorted(pasari)

print('Am ordonat listele:')
print(f'Mamifere: {mamifere}')
print(f'Reptile: {reptile}')
print(f'Pasari: {pasari}\n')

"""1.3Creeaza alte 3 liste in care sa salvezi aceleasi elemente din primele 3 liste, 
dar cuvintele sa fie pe dos. Exemplu insect_list = [“greiere”, “musca”] 🡪 insect_list_r = [“ereierg”, “acsum”]"""
mamifere_r, reptile_r, pasari_r = [], [], []

for mamifer in mamifere:
    mamifere_r.append(mamifer[::-1])

for reptila in range(len(reptile)):
    reptile_r.append(reptile[reptila][::-1])

i = 0
while i < len(pasari):
    pasari_r.append(pasari[i][::-1])
    i += 1

print('Listele cu elementele scrise pe dos:')
print(f'mamifere_r: {mamifere_r}')
print(f'reptile_r: {reptile_r}')
print(f'pasari_r: {pasari_r}\n')

"""1.4 Numara caracterele din fiecare element string din fiecare lista si afiseaza lista cu cele mai multe caractere."""


def count_len(lista_vietuitoare):
    len_list = 0
    for x in range(len(lista_vietuitoare)):
        len_list += int(len(lista_vietuitoare[x]))
    return len_list


len_mamifere = count_len(mamifere)
len_reptile = count_len(reptile)
len_pasari = count_len(pasari)

if len_mamifere > len_reptile and len_mamifere > len_pasari:
    print(f"Lista cu cele mai multe caractere este: {mamifere}\n")
elif len_reptile > len_mamifere and len_reptile > len_pasari:
    print(f"Lista cu cele mai multe caractere este: {reptile}\n")
else:
    print(f"Lista cu cele mai multe caractere este: {pasari}\n")

"""1.5 Inlocuieste fiecare al doilea element din fiecare lista cu “I am an intruder”"""
mamifere[1] = reptile[1] = pasari[1] = "I am an intruder"

"""1.6 Sa se amestece toate elementele random din prima lista. Poti folosi .shuffle()"""
random.shuffle(mamifere), random.shuffle(reptile), random.shuffle(pasari)
print('Listele cu elemente amestecate  + intruder:')
print(mamifere)
print(reptile)
print(pasari)

"""Sa se parcurga lista si daca se gaseste elemental “I am an intruder”, 
sa se returneze pozitia lui, sa se stearga din lista si sa se returneze mesajul “The intruder was kicked out”"""


def find_intruder(lista_vietuitoare):
    for element in lista_vietuitoare:
        if element == "I am an intruder":
            elem_index = lista_vietuitoare.index(element)
            return elem_index


def del_intruder(lista_vietuitoare, elem_index):
    lista_vietuitoare.remove(lista_vietuitoare[elem_index])
    print("The intruder was kicked out.")
    print('Noua lista:', lista_vietuitoare)


def find_and_del_intruder(lista_vietuitoare):
    index_intruder = find_intruder(lista_vietuitoare)
    del_intruder(lista_vietuitoare, index_intruder)


find_and_del_intruder(mamifere)
find_and_del_intruder(reptile)
find_and_del_intruder(pasari)

"""
2.1 Creeaza clasa animal cu 4 atribute si 2 metode
2.2 Creeaza alte 3 clase care sa mosteneasca clasa animal si adauga inca o metoda
"""


class Animal:
    def __init__(self, name, habitat, age, weight):
        self.name = name
        self.habitat = habitat
        self.age = age
        self.weight = weight

    def __str__(self):
        return f"{self.name} traieste in {self.habitat}, are {self.age} ani si {self.weight}kg."

    def bad_joke(self):
        print(f"The {self.name} se plimba prin {self.habitat}.")
        gloante = int(input('Cate gloante avem? '))
        if gloante > 0:
            print("Poc!")
            print(f"Care {self.name}?")
        else:
            print("Azi mancam salata.")


urs = Animal("urs", "padure", 3, 60)
Animal.bad_joke(urs)


class Mamifere(Animal):
    def __init__(self, name, habitat, age, weight):
        Animal.__init__(self, name, habitat, age, weight)

    def defineste_mamifer(self):
        print('Mamiferele au sânge cald. Nasc pui vii pe care îi hrănesc cu lapte.')


class Pasari(Animal):
    def __init__(self, name, haitat, age, weight):
        Animal.__init__(self, name, haitat, age, weight)

    def defineste_pasare(self):
        print('Păsările depun ouă. Posedă pene, aripi și ciocuri.')


class Pesti(Animal):
    def __init__(self, name, haitat, age, weight):
        Animal.__init__(self, name, haitat, age, weight)

    def defineste_pesti(self):
        print('Peștii sunt creaturi cu sânge rece. Ei se deplaseaza prin apa cu ajutorul aripioarelor si a cozii.')


"""Ex3. Sa se introduca un cuvant de la tastatura si sa se afiseze ce lungime are, 
cate consoane, cate vocale are si daca are vreun numar in compozitie."""
word = input('Scrie un cuvant de la tastatura: ')
print("Cuvantul are lungimea", len(word))
vocale = consoane = nr_in_char = 0
for char in word:
    if char.isdigit():
        nr_in_char += 1
    if char in ['a', 'e', 'i', 'o', 'u']:
        vocale += 1
    else:
        consoane += 1
print(f'Vocale: {vocale}')
print(f"Consoane: {consoane}")
print(f"Numere in cuvant:{nr_in_char}")

"""4.1 Sa se creeze un dictionar cu 5 carti care sa contina
numele cartii, autorul, nr_pag, mesaj (daca este available sau nu)
4.2 Sa se creeze o functie care sa ii permita bibliotecarului sa poate adauga carti noi in biblioteca (dictionar).
4.3 Sa se creeze o functie care sa ii permita bibliotecarului sa poata sterge carti din biblioteca
4.4 Sa se creeze o functie care sa ii permita bibliotecarului
sa introduca un nume de carte si sa verifice daca este available sau nu"""
book1 = {'numele cartii': 'Animal farm', 'autorul': 'George Orwell', 'nr_pag': 130, 'mesaj': True}
book2 = {'numele cartii': 'The richest man in Babylon', 'autorul': 'George Clason', 'nr_pag': 144, 'mesaj': True}
book3 = {'numele cartii': 'Ghost in the wires', 'autorul': 'Kevin Mitnick', 'nr_pag': 448, 'mesaj': False}
book4 = {'numele cartii': 'Cuvinte care schimba minti', 'autorul': 'Shelle Charvet', 'nr_pag': 324, 'mesaj': False}
book5 = {'numele cartii': 'Winnetou', 'autorul': 'Karl May', 'nr_pag': 874, 'mesaj': True}
carti_in_biblioteca = {'Animal farm': book1, 'The richest man in Babylon': book2, 'Ghost in the wires': book3,
                       'Cuvinte care schimba minti': book4, 'Winnetou': book5}


def create_book(list_of_books, name, author, no_of_pages, message=True):
    new_book = {'numele cartii': name, 'autorul': author, 'nr_pag': no_of_pages, 'mesaj': message}
    book = new_book["numele cartii"]
    list_of_books.update({book: new_book})
    return list_of_books


def del_book(list_of_books, book_to_delete):
    list_of_books.pop(book_to_delete)
    return list_of_books


def find_book(list_of_books, book_to_find):
    if book_to_find in list_of_books:
        availability = list_of_books[book_to_find]["mesaj"]
        return availability


while True:
    try:
        answer = int(input("Ce vrei sa faci?\n1.Adauga carti\n2.Sterge carte\n3.Cauta o carte\n4. Exit\n"))
        if answer == 1:
            carti_de_adaugat = int(input('Cate carti vrei sa adaugi in biblioteca? '))
            i = 0
            if 1 > carti_de_adaugat:
                print('Nu avem carti de adaugat.')
            else:
                while i < carti_de_adaugat:
                    nume = input('Numele cartii: ')
                    autor = input('Numele autorului: ')
                    nr_pag = int(input('Cate pagini are cartea? '))
                    mesaj = True
                    create_book(carti_in_biblioteca, nume, autor, nr_pag, mesaj)
                    i += 1
                print(carti_in_biblioteca, end="\n\n")

        elif answer == 2:
            print('Lista completa a cartilor din biblioteca:')
            print(carti_in_biblioteca)
            carte_de_sters = input('Ce carte vrei sa stergi? Foloseste-te de titlul cartii.\n')
            if carte_de_sters in carti_in_biblioteca:
                del_book(carti_in_biblioteca, carte_de_sters)
                print('Lista completa a cartilor din biblioteca dupa stergerea cartii.')
                print(carti_in_biblioteca, end="\n\n")
            else:
                print("Cartea nu se afla in biblioteca.")

        elif answer == 3:
            carte_cautata = input("Ce carte vrei sa cauti? Foloseste-te de titlul cartii.\n")
            valabilitate_carte = find_book(carti_in_biblioteca, carte_cautata)
            if valabilitate_carte:
                print("Cartea se afla in biblioteca.")
            else:
                print("Cartea nu se afla in biblioteca.")

        else:
            exit(0)

    except ValueError:
        continue

"""Ex5. – Medium
Un user poate sa creeze o rezervare la restaurant care sa contina nume, data, ora, numar persoane, numar mese. 
Numarul de mese se va calcula automat in functie de numarul de persone introdus de utilizator. 
O masa stim ca poate sa aiba 6 locuri.
Cand veti rula programul va aparea prima data un mesaj de genul:
==== “Welcome to our restaurant restaurant_name” ====. 
Puteti alege voi numele restaurantului si mesajul de welcome.
Clientul va fi intrebat daca vrea sa faca o rezervare
Daca raspunde nu, atunci va primi mesajul, “Maybe next time! Have a nice day!”
Daca raspunde da, atunci va fi intrebat numele, data, ora si numarul de persoane.
Dupa ce utilizatorul a introdus datele va fi anuntat ca rezervarea a fost creata:
Reservation was created on the name X, on date Y, at Z hour for N persons.
Sa se foloseasca functii.
Sa se creeze si o functie care apelata va returna lista de rezervari.
"""

reservation_list = {}


def greet_and_reserve():
    while True:
        print("Welcome to The Elusive Tester.")
        make_reservation = input("Do you want to make a reservation?\n1.Yes     2.No\n").lower()
        if make_reservation == "yes" or make_reservation == "1":
            name = input("On which name should the reservation be? ")
            print("When should we be expecting you?")
            date = input("Date: ")
            hour = input("Hour: ")
            no_of_persons = int(input("How many people? "))
            no_of_tables = ceil(no_of_persons / 6)
            print(f"Reservation was created on the name {name}, on date {date}, "
                  f"at {hour} hour for {no_of_persons} persons.")
            new_reservation = {"name": name, "date": date, "hour": hour, "number of persons": no_of_persons,
                               "number of tables": no_of_tables}
            reservation_add = "reservation" + " " + name
            reservation_list[reservation_add] = new_reservation
        else:
            print("Maybe next time! Have a nice day!")
            return False


def where_my_reservations_at():
    for reservation in reservation_list:
        print(f"{reservation}:{reservation_list[reservation]}")


greet_and_reserve()
where_my_reservations_at()

"""OPTIONALE
1. Avem urmatorul quizz de clasificare.
a) Avem o lista de 20 de animale, care continue: mamifere, pasari, reptile, amfibieni.
b) I se va afisa un utilizatorului un animal din lista si I se va cere sa il clasifice 
in una din categoriile: mamifere, pasari, reptile, amfibieni.
c) La sfarsit I se va afisa cate raspunsuri corecte a avut
d) Daca raspunde correct, I se va afisa ca a raspuns correct
e) Daca utilizatorul raspunde gresit, I se va spune ca a raspuns gresit si I se va da raspunsul correct.
f) La sfarsit I se va acorda un rang:
- 20 raspunsuri corecte: rank S 🡪 Congratulations! You got rank S! You are very knowledgeable about animals!
- intre 16 – 19 (inclusiv): rank A 🡪 Congratulations! You got rank A!
- 13 – 15 (inclusiv): rank B 🡪 Congratulations! You got rank B!
- 10 – 12 (inclusiv): rank C 🡪 You got rank C!
- 7 – 9 (inclusiv): rank D 🡪 You got rank D!
- sub 6 (inclusiv): rank F 🡪 Unfortunately you got rank F!
"""


def initializeaza_lista():
    lista = ["lama", "koala", "ras", "liliac", "porc",
             "barza", "lebada", "gasca", "cormoran", "vultur",
             "sarpe", "varan", "aligator", "crocodil", "vipera",
             "broasca", "axolotl", "salamandra", "brotacel", "buhai"]
    return lista


vietati = initializeaza_lista()
print("Bine ati venit la \"Animal Quizz\"!\n"
      " Iti voi afisa un animal, tu trebuie sa-mi spui daca este mamifer, pasare, reptila sau amfibian.")


def clasifica_animal(animal):
    if animal == "lama" or animal == "koala" or animal == "ras" \
            or animal == "liliac" or animal == "porc" or animal == 1:
        animal = "mamifer"
    elif animal == "barza" or animal == "lebada" or animal == "gasca" \
            or animal == "cormoran" or animal == "vultur" or animal == 2:
        animal = "pasare"
    elif animal == "sarpe" or animal == "varan" or animal == "aligator" \
            or animal == "crocodil" or animal == "vipera" or animal == 3:
        animal = "reptila"
    else:
        animal = "amfibian"
    return animal


def sa_ne_jucam(lista, score):
    while lista:
        random_vietate = lista[random.randint(0, len(lista) - 1)]
        clasificare_random_vietate = clasifica_animal(random_vietate)
        print("Scotocim prin joben si scoatem din el un/o", random_vietate)
        clasificare_animal = int(input("Alege un numar pentru a-l clasifica:\n"
                                       "1. Mamifer    2. Pasare   3. Reptila  4. Amfibian\n"))
        animal_clasificat_de_player = clasifica_animal(clasificare_animal)
        if clasificare_random_vietate == animal_clasificat_de_player:
            score += 1
        lista.remove(random_vietate)
    return score


def acordare_rang(score):
    print("Hope you had some fun. Your score is", score)
    if score == 20:
        print("Congratulations! You got rank S! You are very knowledgeable about animals!")
    elif 19 >= score >= 16:
        print("Congratulations! You got rank A!")
    elif 15 >= score >= 13:
        print("Congratulations! You got rank B!")
    elif 12 >= score >= 10:
        print("You got rank C!")
    elif 9 >= score >= 7:
        print("You got rank D!")
    else:
        print("Unfortunately you got rank F!")


# scor = 0
# scor_player = sa_ne_jucam(vietati, scor)
# acordare_rang(scor_player)

"""Aceeasi tema ca mai sus, dar mai dificila.
Sa se inregistreze 2 jucatori cu username si parola.
Sa se logheze cei 2 jucatori cu username si parola
Primul username va incepe quiz-ul
Se aplica aceleasi reguli ca la tema 1.
Dupa ce termina userul 1 si I se aloca un rang, I se va cere user-ului 2 
sa se prezinte la consola ca sa inceapa quizz-ul si I se va da intrebarea 1
La final se vor compara rank-urile celor 2 jucatori si se vor afisa in ordine
Jucatorului de pe locul al doilea I se va spune cate puncta diferenta exista intre el si jucatorul de pe primul loc.
"""


def creaza_cont():
    new_user = input("User-ul dorit: ").lower()
    new_password = input("Parola: ").lower()
    print("Va rugam sa reintroduceti datele.")
    verificare_new_user = input("User: ").lower()
    verificare_new_password = input("Parola: ").lower()
    if new_user == verificare_new_user and new_password == verificare_new_password:
        print("V-ati logat cu succes.")
        return new_user
    else:
        print("User sau parola incorecta.")
        exit(0)


scor = 0
print("Pentru a putea juca in 2, este nevoie de a crea un cont pentru ambii jucatori.")

single_or_double_play = input("Alegeti-va numarul de jucatori.\n"
                              "Apasati \"1\" pentru solo play, \"2\" pentru a juca la dublu. ")

if single_or_double_play == "1":
    creare_cont = input("Doriti sa va creati un cont?\n1. Da    2. Nu\n")
    if creare_cont == "1":
        user = input("User-ul dorit: ").lower()
        parola = input("Parola: ").lower()
        print("Va rugam sa reintroduceti datele.")
        verificare_user = input("User: ").lower()
        verificare_parola = input("Parola: ").lower()
        if user == verificare_user and parola == verificare_parola:
            print("V-ati logat cu succes,", user)
            scor_user = sa_ne_jucam(vietati, scor)
            acordare_rang(scor_user)
        else:
            print("User sau parola incorecta.")
            creare_guest = input("Doriti sa va jucati ca si guest?\n1. Da    2. Nu\n")
            if creare_guest == "1" or creare_guest == "Da":
                guest = "guest" + str(random.randint(1, 1000))
                print("Bun venit", guest)
                scor_guest = sa_ne_jucam(vietati, scor)
                acordare_rang(scor_guest)
            else:
                print("Poate data viitoare.")
                exit(0)
    else:
        creare_guest = input("Doriti sa va jucati ca si guest?\n1. Da    2. Nu\n")
        if creare_guest == "1" or creare_guest == "Da":
            guest = "guest" + str(random.randint(1, 1000))
            print("Bun venit", guest)
            scor_guest = sa_ne_jucam(vietati, scor)
            acordare_rang(scor_guest)
        else:
            print("Poate data viitoare.")
            exit(0)
else:
    if single_or_double_play == "2":
        print("Player 1.")
        user1 = creaza_cont()
        print("Player 2.")
        user2 = creaza_cont()
        scor_user1 = sa_ne_jucam(vietati, scor)
        acordare_rang(scor_user1)
        scor = 0
        vietati = initializeaza_lista()
        scor_user2 = sa_ne_jucam(vietati, scor)
        acordare_rang(scor_user2)
        if scor_user1 > scor_user2:
            print(user1, "a castigat, avand scorul de", scor_user1, "puncte.")
            print("Felicitari si celuilalt player,", user2, "care a fost la diferenta de",
                  str(scor_user1 - scor_user2), "puncte fata de", user1)
        else:
            print(user2, "a castigat, avand scorul de", scor_user2, "puncte.")
            print("Felicitari si celuilalt player,", user1, "care a fost la diferenta de",
                  str(scor_user2 - scor_user1), "puncte fata de", user2)
