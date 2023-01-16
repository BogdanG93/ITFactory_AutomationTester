# # 1.Funcție care să calculeze și să returneze suma a două numere
# suma = 0
#
#
# def calculeaza_suma(num1, num2):
#     suma = num1 + num2
#     return suma
#
#
# calculeaza_suma(5, 7)

# # 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
#
#
# def par_impar(num1):
#     if num1 % 2 == 0:
#         return True
#     else:
#         return False
#
#
# par_impar(205)

# # 3. Funcție care returnează numărul total de caractere din numele tău complet.
# # (nume, prenume, nume_mijlociu)
# def caractere_numar_complet():
#     print('Introduceti de la tastatura, in ordinea afisarii')
#     nume = input('Nume:')
#     nume_mijlociu = input('Nume mijlociu:')
#     prenume = input('Prenume:')
#     return len(nume + nume_mijlociu + prenume)
#
#
# caractere_numar_complet()


# # 4. Funcție care returnează aria dreptunghiului
# def calculeaza_arie_dreptunghi():
#     print('Pentru a calcula aria dreptunghiului, introdu lungimea si latimea acestuia.')
#     lungimea = int(input('Lungimea:'))
#     latimea = int(input('latimea:'))
#     return lungimea * latimea
#
#
# calculeaza_arie_dreptunghi()

# # 5. Funcție care returnează aria cercului
# import math
#
#
# def calculeaza_arie_cerc(raza):
#     return math.pi*raza**2
#
#
# calculeaza_arie_cerc(5)

# # 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.
# def search_char_in_string(char):
#     string = input('Scrie un string random:')
#     if char in string:
#         return True
#     else:
#         return False
#
#
# search_char_in_string('c')

# # 7. Funcție fără return, primește un string și printează pe ecran:
# # ● Nr de caractere lower case este x
# # ● Nr de caractere upper case este y
# def char_lower_upper():
#     char_lower, char_upper = 0, 0
#     string = input('Introdu un string.')
#     new_string = ''.join(string.split())
#     for char in new_string:
#         if char.islower():
#             char_lower += 1
#         else:
#             char_upper += 1
#     print('Nr de caractere lower case este: ', char_lower)
#     print('Nr de caractere upper case este: ', char_upper)
#
#
# char_lower_upper()

# # 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu numerele pozitive
# def returneaza_nr_pozitive():
#     list = input('Introduceti cate numere doriti. Separati-le prin spatiu: ').split()
#     new_list = []
#     for numar in list:
#         if int(numar) > 0:
#             new_list.append(numar);
#     return new_list
#
# returneaza_nr_pozitive()

# # 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# # ● Primul număr x este mai mare decat al doilea nr y
# # ● Al doilea nr y este mai mare decat primul nr x
# # ● Numerele sunt egale.
# def compara_2_numere(num1, num2):
#     if num1 > num2:
#         print(f'Primul numar {num1} este mai mare decat al doilea nr {num2}.')
#     else:
#         print(f'Al doilea nr {num2} este mai mare decat primul nr {num1}.')
#
#
# compara_2_numere(4, 1)
# compara_2_numere(3, 5)

# # 10. Funcție care primește un număr și un set de numere.
# # # ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# # # ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False
# # def adauga_nr_in_set(num1, set_numere):
# #     if num1 not in set_numere:
# #         print('Am adaugat numărul în set.')
# #         set_numere.add(num1)
# #         print(set_numere)
# #         return True
# #     else:
# #         print('Nu am adaugat numărul nou în set. Acesta există deja.')
# #         return False
# #
# #
# # adauga_nr_in_set(33, {54, 42, 712, 33})
# # adauga_nr_in_set(5, {54, 42, 712, 33})

''' Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google. '''

# # 1. Funcție care primește o lună din an și returnează câte zile are acea luna.
# from calendar import monthrange
# def calc_zile_in_luna(luna):
#     zile_in_luna = monthrange(2022, luna)[1]
#     return zile_in_luna
#
# calc_zile_in_luna(2)

# # 2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.
# # În final vei putea face:
# # a, b, c, d = calculator(10, 2)
# #  ● print("Suma: ", a)
# #  ● print("Diferenta: ", b)
# #  ● print("Inmultirea: ", c)
# #  ● print("Impartirea: ", d)
# def calculator(num1, num2):
#     a = num1 + num2
#     b = num1 - num2
#     c = num1 * num2
#     d = num1 / num2
#     print("Suma: ", a)
#     print("Diferenta: ", b)
#     print("Inmultirea: ", c)
#     print("Impartirea: ", d)
#     return a, b, c, d
#
#
# a, b, c, d = calculator(10, 2)

# 3. Funcție care primește o lista de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# def count_cifre(list):
#     count_dict = {}
#     for cifre in list:
#         if cifre in count_dict:
#             count_dict[cifre] += 1
#         else:
#             count_dict[cifre] = 1
#     print(count_dict)
#
#
# count_cifre([1, 5, 5, 5, 2, 3, 1])

# # 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
#
#
# def max_number(num1, num2, num3):
#     # return max(num1, num2, num3)
#     if num1 > num2 and num1 > num3:
#         return num1
#     elif num2 > num1 and num2 > num3:
#         return num2
#     else:
#         return num3
#
#
# max_number(5, 3, 7)

# # 5. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr
# # Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)
# def range_suma_nr(num1):
#     suma = 0
#     for numere in range(num1 + 1):
#         suma += numere
#     return suma
#
# range_suma_nr(5)

''' Exerciții Opționale - Bonus '''

# # 1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune
# # Exemplu:
# # list1 = [1, 1, 2, 3]
# # list2 = [2, 2, 3, 4]
# # Răspuns: {2, 3}
#
#
# def numere_comune_in_lista(list1, list2):
#     list_numere_comune = []
#     for numar in list1:
#         if numar in list2:
#             list_numere_comune.append(numar)
#     list_numere_comune = list(dict.fromkeys(list_numere_comune))
#     return list_numere_comune
#
#
# numere_comune_in_lista([2, 2, 5, 3], [5, 5, 2, 3, 1])

# # 2. Funcție care să aplice o reducere de preț.
# # Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90.
# # Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e invalidă.
#
#
# def reducere_pret(pret, reducere):
#     if reducere <= 0 or reducere >= 100:
#         print('Reducerea este invalida.')
#     else:
#         reducere_in_lei = reducere / 100 * pret
#         pret_nou = pret - reducere_in_lei
#         print(f'Produsul costa {pret} lei. Dupa ce am aplicat reducerea de {reducere}%, el devine {pret_nou} lei.')
#
#
# reducere_pret(100, -10)
# reducere_pret(525, 10)

# # 3. Funcție care să afișeze data și ora curentă din ro
# # (bonus: afișați și data și ora curentă din China)
#
#
#
# def data_ora():
#     data_ora_ro = datetime.now()
#     print('Data si ora in Romania:', data_ora_ro.date(), data_ora_ro.hour)
#     china_tz = pytz.timezone('Asia/Shanghai')
#     data_ora_china = datetime.now(china_tz)
#     print('Data si ora in China:', data_ora_china.date(), data_ora_china.hour)
#
#
# data_ora()

# # 4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
# # Crăciun dacă nu vrei să ne zici cand e ziua ta :)
# import datetime
#
#
# def countdown_days_left():
#     data_nasterii = datetime.date(1993, 10, 7)
#     data_de_azi = datetime.date.today()
#     if data_de_azi.month == data_nasterii.month\
#             and data_de_azi.day >= data_nasterii.day\
#             or data_de_azi.month > data_nasterii.month:
#         an_de_sarbatorit = data_de_azi.year + 1
#     else:
#         an_de_sarbatorit = data_de_azi.year
#     data_de_sarbatorit = datetime.date(an_de_sarbatorit, data_nasterii.month, data_nasterii.day)
#     zile_ramase = data_de_sarbatorit - data_de_azi
#     print('Zile ramase pana la ziua de nastere:', zile_ramase.days)
#
#
# countdown_days_left()