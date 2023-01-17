# import random
#
"""1.1 Creeaza 3 liste care sa contina animale:
a. Mamifere
b. Reptile
c. Pasari
"""
from math import ceil

# mamifere = ['cartita', 'arici', 'veverita', 'soarece']
# reptile = ['limax', 'varan', 'lipitoare', 'gecko']
# pasari = ['kiwi', 'sabot', 'cucuveaua', 'flamingo']
#
# print('Avem listele:')
# print(f'Mamifere: {mamifere}')
# print(f'Reptile: {reptile}')
# print(f'Pasari: {pasari}\n')
"""1.2. Sorteaza fiecare lista alphabetic"""
# mamifere, reptile, pasari = sorted(mamifere), sorted(reptile), sorted(pasari)
#
# print('Am ordonat listele:')
# print(f'Mamifere: {mamifere}')
# print(f'Reptile: {reptile}')
# print(f'Pasari: {pasari}\n')
"""1.3Creeaza alte 3 liste in care sa salvezi aceleasi elemente din primele 3 liste, 
dar cuvintele sa fie pe dos. Exemplu insect_list = [“greiere”, “musca”] 🡪 insect_list_r = [“ereierg”, “acsum”]"""
# mamifere_r, reptile_r, pasari_r = [], [], []
#
# for mamifer in mamifere:
#     mamifere_r.append(mamifer[::-1])
#
# for reptila in range(len(reptile)):
#     reptile_r.append(reptile[reptila][::-1])
#
# i = 0
# while i < len(pasari):
#     pasari_r.append(pasari[i][::-1])
#     i += 1
#
# print('Listele cu elementele scrise pe dos:')
# print(f'mamifere_r: {mamifere_r}')
# print(f'reptile_r: {reptile_r}')
# print(f'pasari_r: {pasari_r}\n')
"""1.4 Numara caracterele din fiecare element string din fiecare lista si afiseaza lista cu cele mai multe caractere."""
# def count_len(lista_vietuitoare):
#     len_list = 0
#     for x in range(len(lista_vietuitoare)):
#         len_list += int(len(lista_vietuitoare[x]))
#     return len_list
#
#
# len_mamifere = count_len(mamifere)
# len_reptile = count_len(reptile)
# len_pasari = count_len(pasari)
#
# if len_mamifere > len_reptile and len_mamifere > len_pasari:
#     print(f"Lista cu cele mai multe caractere este: {mamifere}\n")
# elif len_reptile > len_mamifere and len_reptile > len_pasari:
#     print(f"Lista cu cele mai multe caractere este: {reptile}\n")
# else:
#     print(f"Lista cu cele mai multe caractere este: {pasari}\n")
"""1.5 Inlocuieste fiecare al doilea element din fiecare lista cu “I am an intruder”"""
# mamifere[1] = reptile[1] = pasari[1] = "I am an intruder"
"""1.6 Sa se amestece toate elementele random din prima lista. Poti folosi .shuffle()"""
# random.shuffle(mamifere), random.shuffle(reptile), random.shuffle(pasari)
# print('Listele cu elemente amestecate  + intruder:')
# print(mamifere)
# print(reptile)
# print(pasari)
"""Sa se parcurga lista si daca se gaseste elemental “I am an intruder”, 
sa se returneze pozitia lui, sa se stearga din lista si sa se returneze mesajul “The intruder was kicked out”"""
#
#
# def find_intruder(lista_vietuitoare):
#     global elem_index
#     for element in lista_vietuitoare:
#         if element == "I am an intruder":
#             elem_index = lista_vietuitoare.index(element)
#             return elem_index
#
#
# def del_intruder(lista_vietuitoare):
#     lista_vietuitoare.remove(lista_vietuitoare[elem_index])
#     print("The intruder was kicked out.")
#     print('Noua lista:', lista_vietuitoare)
#
#
# def find_and_del_intruder(lista_vietuitoare):
#     find_intruder(lista_vietuitoare)
#     del_intruder(lista_vietuitoare)
#
#
# find_and_del_intruder(mamifere)
# find_and_del_intruder(reptile)
# find_and_del_intruder(pasari)
#
"""
2.1 Creeaza clasa animal cu 4 atribute si 2 metode
2.2 Creeaza alte 3 clase care sa mosteneasca clasa animal si adauga inca o metoda
"""
#
#
# class Animal:
#     def __init__(self, name, habitat, age, weight):
#         self.name = name
#         self.habitat = habitat
#         self.age = age
#         self.weight = weight
#
#     def __str__(self):
#         return f"{self.name} traieste in {self.habitat}, are {self.age} ani si {self.weight}kg."
#
#     def bad_joke(self):
#         print(f"The {self.name} se plimba prin {self.habitat}.")
#         gloante = int(input('Cate gloante avem?'))
#         if gloante > 0:
#             print("Poc!")
#             print(f"Care {self.name}?")
#         else:
#             print("Azi mancam salata.")
#
#
# urs = Animal("urs", "padure", 3, 60)
# Animal.bad_joke(urs)
#
#
# class Mamifere(Animal):
#     def __init__(self,  name, habitat, age, weight):
#         Animal.__init__(self, name, habitat, age, weight)
#
#     def defineste_mamifer(self):
#         print('Mamiferele au sânge cald. Nasc pui vii pe care îi hrănesc cu lapte.')
#
#
# class Pasari(Animal):
#     def __init__(self, name, haitat, age, weight):
#         Animal.__init__(self, name, haitat, age, weight)
#
#     def defineste_pasare(self):
#         print('Păsările depun ouă. Posedă pene, aripi și ciocuri.')
#
#
# class Pesti(Animal):
#     def __init__(self, name, haitat, age, weight):
#         Animal.__init__(self, name, haitat, age, weight)
#
#     def defineste_pesti(self):
#         print('Peștii sunt creaturi cu sânge rece. Ei se deplaseaza prin apa cu ajutorul aripioarelor si a cozii.')

"""Ex3. Sa se introduca un cuvant de la tastatura si sa se afiseze ce lungime are, 
cate consoane, cate vocale are si daca are vreun numar in compozitie."""
# word = input('Scrie un cuvant de la tastatura.')
# print("Cuvantul are lungimea", len(word))
# vocale = consoane = nr_in_char = 0
# for char in word:
#     if char.isdigit():
#         nr_in_char +=1
#     if char in ['a', 'e', 'i', 'o', 'u']:
#         vocale += 1
#     else:
#         consoane += 1
# print(f'Vocale: {vocale}')
# print(f"Consoane: {consoane}")
# print(f"Numere in cuvant:{nr_in_char}")

"""
Ex4.
4.1 Sa se creeze un dictionar cu 5 carti care sa contina
numele cartii, autorul, nr_pag, mesaj (daca este available sau nu)
4.2 Sa se creeze o functie care sa ii permita bibliotecarului sa poate adauga carti noi in biblioteca (dictionar).
4.3 Sa se creeze o functie care sa ii permita bibliotecarului sa poata sterge carti din biblioteca
4.4 Sa se creeze o functie care sa ii permita bibliotecarului
sa introduca un nume de carte si sa verifice daca este available sau nu
"""
# book1 = {'numele cartii': 'Animal farm', 'autorul': 'George Orwell', 'nr_pag': 130, 'mesaj': True}
# book2 = {'numele cartii': 'The richest man in Babylon', 'autorul': 'George Clason', 'nr_pag': 144, 'mesaj': True}
# book3 = {'numele cartii': 'Ghost in the wires', 'autorul': 'Kevin Mitnick', 'nr_pag': 448, 'mesaj': False}
# book4 = {'numele cartii': 'Cuvinte care schimba minti', 'autorul': 'Shelle Charvet', 'nr_pag': 324, 'mesaj': False}
# book5 = {'numele cartii': 'Winnetou', 'autorul': 'Karl May', 'nr_pag': 874, 'mesaj': True}
# carti_in_biblioteca = {'Animal farm': book1, 'The richest man in Babylon': book2, 'Ghost in the wires': book3,
#                        'Cuvinte care schimba minti': book4, 'Winnetou': book5}
#
#
# def create_book(list_of_books, name, author, no_of_pages, message=True):
#     new_book = {'numele cartii': name, 'autorul': author, 'nr_pag': no_of_pages, 'mesaj': message}
#     book = new_book["numele cartii"]
#     list_of_books.update({book: new_book})
#     return list_of_books
#
#
# def del_book(list_of_books, book_to_delete):
#     list_of_books.pop(book_to_delete)
#     return list_of_books
#
#
# def find_book(list_of_books, book_to_find):
#     if book_to_find in list_of_books:
#         availability = list_of_books[book_to_find]["mesaj"]
#         return availability
#
#
# while True:
#     try:
#         answer = int(input("Ce vrei sa faci?\n1.Adauga carti\n2.Sterge carte\n3.Cauta o carte\n4. Exit\n"))
#         if answer == 1:
#             carti_de_adaugat = int(input('Cate carti vrei sa adaugi in biblioteca? '))
#             i = 0
#             if 1 > carti_de_adaugat:
#                 print('Nu avem carti de adaugat.')
#             else:
#                 while i < carti_de_adaugat:
#                     nume = input('Numele cartii: ')
#                     autor = input('Numele autorului: ')
#                     nr_pag = int(input('Cate pagini are cartea? '))
#                     mesaj = True
#                     create_book(carti_in_biblioteca, nume, autor, nr_pag, mesaj)
#                     i += 1
#                 print(carti_in_biblioteca, end="\n\n")
#
#         elif answer == 2:
#             print('Lista completa a cartilor din biblioteca:')
#             print(carti_in_biblioteca)
#             carte_de_sters = input('Ce carte vrei sa stergi? Foloseste-te de titlul cartii.\n')
#             if carte_de_sters in carti_in_biblioteca:
#                 del_book(carti_in_biblioteca, carte_de_sters)
#                 print('Lista completa a cartilor din biblioteca dupa stergerea cartii.')
#                 print(carti_in_biblioteca, end="\n\n")
#             else:
#                 print("Cartea nu se afla in biblioteca.")
#
#         elif answer == 3:
#             carte_cautata = input("Ce carte vrei sa cauti? Foloseste-te de titlul cartii.\n")
#             valabilitate_carte = find_book(carti_in_biblioteca, carte_cautata)
#             if valabilitate_carte:
#                 print("Cartea se afla in biblioteca.")
#             else:
#                 print("Cartea nu se afla in biblioteca.")
#
#         else:
#             exit(0)
#
#     except ValueError:
#         continue

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


# reservation_list = {}
#
#
# def greet_and_reserve():
#     while True:
#         print("Welcome to The Elusive Tester.")
#         make_reservation = input("Do you want to make a reservation?\n1.Yes     2.No\n").lower()
#         if make_reservation == "yes" or make_reservation == "1":
#             name = input("On which name should the reservation be? ")
#             print("When should we be expecting you?")
#             date = input("Date: ")
#             hour = input("Hour: ")
#             no_of_persons = int(input("How many people? "))
#             no_of_tables = ceil(no_of_persons / 6)
#             print(f"Reservation was created on the name {name}, on date {date}, "
#                   f"at {hour} hour for {no_of_persons} persons.")
#             new_reservation = {"name": name, "date": date, "hour": hour, "number of persons": no_of_persons,
#                                "number of tables": no_of_tables}
#             reservation_add = "reservation" + " " + name
#             reservation_list[reservation_add] = new_reservation
#         else:
#             print("Maybe next time! Have a nice day!")
#             return False
#
#
# def where_my_reservations_at():
#     for reservation in reservation_list:
#         print(f"{reservation}:{reservation_list[reservation]}")
#
#
# greet_and_reserve()
# where_my_reservations_at()
