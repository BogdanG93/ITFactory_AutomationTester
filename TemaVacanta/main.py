# import random
#
# print('Ex. 1')
# mamifere = ['cartita', 'arici', 'veverita', 'soarece']
# reptile = ['limax', 'varan', 'lipitoare', 'gecko']
# pasari = ['kiwi', 'sabot', 'cucuveaua', 'flamingo']
#
# print('Avem listele:')
# print(f'Mamifere: {mamifere}')
# print(f'Reptile: {reptile}')
# print(f'Pasari: {pasari}\n')
#
# mamifere, reptile, pasari = sorted(mamifere), sorted(reptile), sorted(pasari)
#
# print('Am ordonat listele:')
# print(f'Mamifere: {mamifere}')
# print(f'Reptile: {reptile}')
# print(f'Pasari: {pasari}\n')
#
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
#
#
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
#
# mamifere[1] = reptile[1] = pasari[1] = "I am an intruder"
# random.shuffle(mamifere), random.shuffle(reptile), random.shuffle(pasari)
# print('Listele cu elemente amestecate  + intruder:')
# print(mamifere)
# print(reptile)
# print(pasari)
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
# print("Ex. 2")
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

# print("Ex. 3")
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
1.   Sa se creeze un dictionar cu 5 carti care sa contina
numele cartii, autorul, nr_pag, mesaj (daca este available sau nu)
2.   Sa se creeze o functie care sa ii permita bibliotecarului sa poate adauga carti noi in biblioteca (dictionar).
3.   Sa se creeze o functie care sa ii permita bibliotecarului sa poata sterge carti din biblioteca
4.   Sa se creeze o functie care sa ii permita bibliotecarului
sa introduca un nume de carte si sa verifice daca este available sau nu
"""
# book1 = {'numele cartii': 'Animal farm', 'autorul': 'George Orwell', 'nr_pag': 130, 'mesaj': True}
# book2 = {'numele cartii': 'The richest man in Babylon', 'autorul': 'George Samuel Clason', 'nr_pag': 144, 'mesaj': True}
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
