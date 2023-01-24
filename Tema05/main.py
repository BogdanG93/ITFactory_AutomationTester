import math
from datetime import date
from datetime import datetime
import pytz

# OBLIGATORII
# 1. Funcție care să calculeze și să returneze suma a două numere
num1 = int(input("Primul numar: "))
num2 = int(input("Al doilea numar: "))


def calculeaza_suma(first, second):
    suma = first + second
    return f'Suma celor doua numere este {suma}.'


print(calculeaza_suma(num1, num2))


# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar


def par_impar(number):
    if number % 2 == 0:
        return True
    else:
        return False


print(par_impar(205))
print(par_impar(12))


# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)


def caractere_numar_complet(nume, nume_mijlociu, prenume):
    return len(nume + nume_mijlociu + prenume)


print(caractere_numar_complet("Popescu", "Ion", "Ion"))


# 4. Funcție care returnează aria dreptunghiului


def arie_dreptunghi(lungime, latime):
    aria = lungime * latime
    return aria


print(arie_dreptunghi(5, 7))


# 5. Funcție care returnează aria cercului


def arie_cerc(raza):
    return math.pi * raza ** 2


print('%.2f' % arie_cerc(5))


# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.


def search_char_in_string(char):
    string = input('Scrie un string random: ')
    if char in string:
        return True
    else:
        return False


print(search_char_in_string('c'))


# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case este y


def char_lower_upper():
    char_lower, char_upper = 0, 0
    string = input('Introdu un string: ')
    new_string = ''.join(string.split())
    for char in new_string:
        if char.islower():
            char_lower += 1
        else:
            char_upper += 1
    print('Nr. de caractere lower case este:', char_lower)
    print('Nr. de caractere upper case este:', char_upper)


char_lower_upper()


# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu numerele pozitive


def returneaza_nr_pozitive():
    random_list = input('Introduceti cate numere doriti. Separati-le prin spatiu: ').split()
    new_list = []
    for numar in random_list:
        if int(numar) > 0:
            new_list.append(numar)
    return new_list


print("Lista numerelor pozitive:", returneaza_nr_pozitive())


# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.


def compara_2_numere(x, y):
    if x > y:
        print(f'Primul numar "{x}" este mai mare decat al doilea numar "{y}".')
    elif x < y:
        print(f'Al doilea numar "{y}" este mai mare decat primul numar "{x}".')
    else:
        print('Numerele sunt egale.')


compara_2_numere(4, 1)
compara_2_numere(3, 3)


# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False


def adauga_nr_in_set(num1, set_numere):
    if num1 not in set_numere:
        print(f'Am adaugat numărul "{num1}" în set.')
        set_numere.add(num1)
        return True
    else:
        print('Nu am adaugat numărul "num1" în set. Acesta există deja.')
        return False


print(adauga_nr_in_set(33, {54, 42, 712, 33}))
print(adauga_nr_in_set(5, {54, 42, 712, 33}))


# OPTIONALE
# 1. Funcție care primește o lună din an și returnează câte zile are acea luna.


def calendar(luna):
    lunile_anului = {
        'January': 31,
        'February': 28,
        'March': 31,
        'April': 30,
        'May': 31,
        'June': 30,
        'July': 31,
        'August': 31,
        'September': 30,
        'October': 31,
        'November': 30,
        'December': 31
    }
    if luna in lunile_anului:
        return lunile_anului.get(luna)


print(calendar('June'))
print(calendar('January'))
print(calendar('February'))


# 2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.
# În final vei putea face:
# a, b, c, d = calculator(10, 2)
#  ● print("Suma: ", a)
#  ● print("Diferenta: ", b)
#  ● print("Inmultirea: ", c)
#  ● print("Impartirea: ", d)


def calculator(numb1, numb2):
    a = numb1 + numb2
    b = numb1 - numb2
    c = numb1 * numb2
    d = numb1 / numb2
    return a, b, c, d


a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)


# 3. Funcție care primește o lista de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră


def count_cifre(a_list):
    count_dict = {}
    for cifre in a_list:
        if cifre in count_dict:
            count_dict[cifre] += 1
        else:
            count_dict[cifre] = 1
    print(count_dict)


count_cifre([1, 5, 5, 5, 2, 3, 1])


# 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele


def max_number(number1, number2, number3):
    if number1 > number2 and number1 > number3:
        return number1
    elif number2 > number1 and number2 > number3:
        return number2
    else:
        return number3


print("Numarul maxim:", max_number(5, 3, 7))
print("Numarul maxim:", max_number(12, 4, 19))


# 5. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr
# Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)


def range_suma_nr(num):
    suma = 0
    for numar in range(num + 1):
        suma += numar
    return suma


print("Suma tutoror numerelor:", range_suma_nr(5))
print("Suma tutoror numerelor:", range_suma_nr(8))


# OPTIONALE
# 1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune
# Exemplu:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Răspuns: {2, 3}


def numere_comune_in_lista(list1, list2):
    list_numere_comune = []
    for numar in list1:
        if numar in list2:
            list_numere_comune.append(numar)
    list_numere_comune = list(dict.fromkeys(list_numere_comune))
    return list_numere_comune


numere_comune_in_lista([2, 2, 5, 3], [5, 5, 2, 3, 1])


# 2. Funcție care să aplice o reducere de preț.
# Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90.
# Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e invalidă.


def reducere_pret(pret, reducere):
    if reducere <= 0 or reducere >= 100:
        print('Reducerea este invalida.')
    else:
        reducere_in_lei = reducere / 100 * pret
        pret_nou = pret - reducere_in_lei
        print(f'Produsul costa {pret} lei. Dupa ce am aplicat reducerea de {reducere}%, el devine {pret_nou} lei.')


reducere_pret(100, -10)
reducere_pret(525, 10)


# 3. Funcție care să afișeze data și ora curentă din ro
# (bonus: afișați și data și ora curentă din China)


def data_ora():
    data_ora_ro = datetime.now()
    print('Data si ora in Romania:', data_ora_ro.date(), data_ora_ro.hour)
    china_tz = pytz.timezone('Asia/Shanghai')
    data_ora_china = datetime.now(china_tz)
    print('Data si ora in China:', data_ora_china.date(), data_ora_china.hour)


data_ora()

# 4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
# Crăciun dacă nu vrei să ne zici cand e ziua ta :)


def amr_xmas(year):
    christmas_day = date(year=year, month=12, day=25)
    days_til_christmas = (christmas_day - date.today()).days
    return days_til_christmas


print("Days until Christmas: ", amr_xmas(2023))
