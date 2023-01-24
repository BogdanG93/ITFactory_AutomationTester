import random

# OBLIGATORII
# Ex:1 Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else
print('"if else" functioneaza in cadrul a (fix) doua ramuri, in ideea de a acoperi mai multe scenarii\n'
      'if conditie is True -> executa acest bloc de cod\nelse conditie -> executa celalalt bloc de cod')

# Ex.2 Verifică și afișează dacă x este număr natural sau nu.
a = 5
if a >= 0 and type(a) == int:
    print('Ai introdus numarul natural', a)
else:
    print('Nu ati introdus un numar natural. Te rog sa reincerci.')

# Ex.3 Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
x = 12
if x > 0:
    print('Numarul este pozitiv.')
elif x < 0:
    print('Numarul este negativ.')
else:
    print('Numarul este neutru.')

# Ex.4 Verifică și afișează dacă x este între -2 și 13
x = 7
if -2 <= x <= 13:
    print('x se afla intre valorile "-2" si "13".')
else:
    print('x nu se afla intre valorile "-2" si "13".')

# Ex.5 Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
x = 7
y = 4
if x - y < 5:
    print('Diferenta dintre x si y este mai mica de 5.')
else:
    print('Diferenta dintre x si y nu este mai mica de 5.')

# Ex.6 Verifică dacă x NU este între 5 și 27 - (a se folosi ‘not’)
x = 3
if not (5 < x < 27):
    print(x, "nu este intre 5 si 27.")

# Ex.7 Declara o noua variabila y de tip int si apoi verifica si afiseaza
# daca x si y sunt egale, daca nu, afiseaza care din ele este mai mare
x = int(input('Alege valoarea lui x. '))
y = int(input('Alege valoarea lui y. '))
if x == y:
    print("x si y sunt nr. egale.")
elif x > y:
    print("x este mai mare decat y.")
else:
    print('x este mai mic decat y.')

# Ex.8 Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca triunghiul
# este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau oarecare (nicio latura nu e egala).
x = int(input('Alege valoarea lui x. '))
y = int(input('Alege valoarea lui y. '))
z = int(input('Alege valoarea lui z. '))
if (x, y, z > 0) and not (x > y + z) and not (y > x + z) and not (z > x + y):
    if x == y == z:
        print('Triunghiul este echilateral.')
    elif (x == y) or (x == z) or (y == z):
        print('Triunghiul este isoscel.')
    else:
        print('Triunghiul este oarecare.')
else:
    print('Nu putem construi un triunghi folosind aceste valori ale laturilor.')

# Ex.9 - Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu
litera = input('Introduceti o litera. ')
if (litera.isalpha()) and (litera[0] == litera):
    if litera[0].lower() in ['a', 'ă', 'â', 'e', 'i', 'î', 'o', 'u']:
        print('Litera introdusa este o vocala.')
    else:
        print('Litera introdusa este o consoana.')
else:
    print('Ai introdus una sau mai multe cifre/spatii sau mai mult de o litera, reincearca.')

# Ex. 10 Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza:
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F
nota = float(input('Care este nota primita? '))
if 10 >= nota > 9:
    print('Am luat nota A.')
elif nota > 8:
    print('Am luat nota B.')
elif nota > 7:
    print('Am luat nota C.')
elif nota > 6:
    print('Am luat nota D.')
elif nota > 4:
    print('Am luat nota E.')
elif nota <= 4:
    print('Am luat nota F.')
else:
    print("Nu ati introdus o nota de la 0 la 10.")

# OPTIONALE
# Ex:1 - Verifica daca x are minim 4 cifre (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
x = int(input('Alege valoarea lui x. '))
if abs(x) <= 3:
    print('Numarul introdus nu are 4 cifre.')
else:
    print('Numarul introdus are 4 cifre.')

# Ex.2 Verifică dacă x are exact 6 cifre.
x = 542176
if len(str(x)) == 6:
    print('Are 6 cifre.')
else:
    print('Nu are 6 cifre.')

# Ex.3 Verifică dacă x este număr par sau impar
x = 23
if x % 2 == 0:
    print('Numarul este par.')
else:
    print('Numarul este impar.')

# Ex:4 Avand trei variabile x, y, z (toate int) afiseaza in consola care este cel mai mare dintre ele
x = int(input('Alege valoarea lui x. '))
y = int(input('Alege valoarea lui y. '))
z = int(input('Alege valoarea lui z. '))
if x >= y and x >= z:
    print(f'{x} este cel mai mare numar.')
elif y >= x and y >= z:
    print(f'{y} este cel mai mare numar.')
else:
    print(f'{z} este cel mai mare numar.')

# # Ex.5 - Presupunand ca x, y, z - reprezinta unghiurile unui triunghi,
# verifica si afiseaza daca triunghiul este valid sau nu
# (un triunghi este valid daca suma tuturor unghiurilor este de 180 de grade
# sau daca suma lungimilor a oricare doua laturi este mai mare decat lungimea celei de-a treia laturi)
x = int(input('Alege valoarea primului unghi. '))
y = int(input('Alege valoarea celui de-al doilea unghi. '))
z = int(input('Alege valoarea celui de-al treilea unghi. '))
if x + y + z == 180 and x > 0 and y > 0 and z > 0:
    print('Triunghiul este valid.')
else:
    print('Triunghiul nu este valid.')

'''Ex.6 Avand stringul: 'Coral is either the stupidest animal or the smartest rock' 
citește de la tastatura un număr x de tip int și afișează stringul fără ultimele x caractere. 
ex: dacă ați ales 7 se va afisa urmatorul string: 'Coral is either the stupidest animal or the smarte' '''
original_string = 'Coral is either the stupidest animal or the smartest rock'
cut = int(input('Cate caractere vreti sa taiem din finalul stringului? '))
print(original_string[0:-cut])

# Ex. 7 Folosindu-te de același string de la exercițiul 6,
# declara un string nou care sa fie format din primele 5 caractere + ultimele 5
string = 'Coral is either the stupidest animal or the smartest rock'
new_string = string[0:5] + string[-5:]
print(f'String-ul nou format din primele 5 + ultimele 5 caractere este: "{new_string}"')

'''Ex:8 Folosindu-te de același string de la exercițiul 6, salvează într-o variabila și afiseaza indexul de start 
al cuvântului rock - adică poziția in string la care începe cuvântul rock 
(hint: este o funcție care te ajuta sa faci asta). 
Folosind aceasta variabila + slicing, afișează tot stringul pana la acest cuvant. 
Output asteptat: 'Coral is either the stupidest animal or the smartest ' '''
string = 'Coral is either the stupidest animal or the smartest rock'
rock_index = string.index("rock")
print(string[:rock_index])

# Ex.9 Citeste de la tastatura un string si verifica daca primul și ultimul caracter sunt la fel.
# Se va folosi un assert.
# Atentie: se dorește ca programul sa fie case insensitive,
# adica 'apA' e acceptat ca un string in care primul si ultimul caracter este la fel
# (hint, te poti folosi de o functie pentru a face string-ul case insensitive)
string = input('Scrie o propozitie/fraza de la tastatura. ')
assert string[0].lower() ==string[len(string)-1].lower(), 'Primul si ultimul caracter sunt diferite'

# Ex: 10 Avand stringul '0123456789' afiseaza doar numerele pare si apoi doar numerele impare
# (hint: foloseste slicing si controleaza afisarea in slicing cu slicing step)
string_numere = '0123456789'
print('Numere pare: ', string_numere[0::2])
print('Numere impare: ', string_numere[1::2])

# Ex.1 - Vrem sa cream o aplicatie pentru achizitionare bilete de avion
# care sa primeasca drept inputuri urmatoarele informatii:
# Varsta
# Insotit de mama
# Insotit de tata
# Pasaport
# Act permisiune mama
# Act permisiune tata
#
# Conditii de imbarcare:
# Daca pers are varsta peste 18 ani si are pasaport
# Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
# Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte
# si are permisiune in scris de la celalat parinte
#
# Scrie codul care implementeaza conditiile de imbarcare de mai sus si testeaza-l
# cu toate variantele care crezi ca ar trebui testate.
# Genereaza scenarii de testare cu expected results si apoi ruleaza codul pentru a verifica
# daca expected results sunt egale cu actual results.
#
# Exemple:
# Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
# Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca

varsta = int(input("Va rugam sa introduceti varsta pasagerului. "))
pasaport_valid = input("E pasaportul valid? Da/Nu ").lower()
if varsta >= 18 and pasaport_valid == "da":
    print("Va puteti imbarca")
elif varsta < 18 and pasaport_valid == "da":
    ambii_parinti = input("E copilul insotit de ambii parinti? Da/Nu ").lower()
    if ambii_parinti == "da":
        print("Va puteti imbarca.")
    else:
        permisiune = input("Aveti ermisiunea celuilalt parinte? Da/Nu ").lower()
        if permisiune == "da":
            print("Va puteti imbarca.")
        else:
            print("Nu va puteti imbarca.")
else:
    print("Nu va puteti imbarca.")

""" Scenarii de testare:
1. Adult >= 18 ani cu pasaport valid => Se poate imbarca
2. Adult >= 18 ani cu pasaport invalid => Nu se poate imbarca
3. Copil cu pasaport valid si ambii parinti => Se poate imbarca
4. Copil cu pasaport valid si un singur parinte - permisiune parinte lipsa => Se poate imbarca
5. Copil cu pasaport valid si un singur parinte - fara permisiune parinte lipsa => Nu se poate imbarca
6. Copil fara pasaport valid => Nu se poate imbarca
"""

""" Ex.2 Joc de noroc
- Cauta pe net si vezi cum se genereaza un numar random
- Imagineaza-ti ca dai cu zarul si salvezi acest numar intr-o variabila numita dice_roll.
Numarul salvat va fi generat random cu metoda gasita in online
- Introdu un numar de la tastatura care sa reprezinte numarul ales de la utilizator
- Verifica si afiseaza daca utilizatorul a ghicit numarul
- Vor exista 3 optiuni care vor trebui tratate:
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
● Ai ghicit. Felicitari? Ai ales x si zarul a fost y"""
zar_in_mana = input('Dai cu zarul?\n'
                    '1. Da      2. Nu\n').lower()

if zar_in_mana == '1' or zar_in_mana == 'da':
    dice_roll = random.randint(1, 6)
else:
    print('Ok. Bye!')
    exit(0)

ghiceste_zarul = int(input('Ce numar crezi ca a iesit? '))
if dice_roll == ghiceste_zarul:
    print(f'Ai ghicit. Felicitari! Ai ales {ghiceste_zarul} si zarul a fost {dice_roll}.')
elif dice_roll > ghiceste_zarul:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {ghiceste_zarul}, dar a fost {dice_roll}.')
else:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {ghiceste_zarul}, dar a fost {dice_roll}.')
