"""
1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.

Variabila este informatia pe care o stocam intr-un spatiu alocat de memorie, in scopul manipularii acesteia.

Practic ne putem gandi la spatiu ca fiind un dulap, spatiul alocat variabilei ca fiind un obiect care sa contina
informatia, de genul o cutie, numele variabilei ar fi labelul de pe cutie, iar in interiorul cutiei s-ar afla informatia.
"""

# 2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă :

tema = 'Azi ne facem tema.'   # str
exercitii = 10 # int
ora = 18.23 # float
facem_toata_tema = False # bool

# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
#                               +
# 5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
print('Ex. 3 + 5:')
print()
print('Variabilele declarate anterior sunt de tipul: ')
print(f'tema: {tema}--> ', type(tema))
print(f'exercitii: {exercitii}-->', type(exercitii))
print(f'ora: {ora}-->', type(ora))
print(f'facem_toata_tema: {facem_toata_tema}-->', type(facem_toata_tema))
print(tema + ' Avem ' + str(exercitii) + ' exercitii de rezolvat. Avand in vedere faptul ca este ora ' + str(ora) +
      ', credeti ca intr-o ora le putem rezolva pe toate? R: ' + str(facem_toata_tema))
print()
print()

# 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
# - Verifică tipul acesteia.
print('Ex. 4:')
print()
print(f'Variabila "ora" are valoarea de: {ora}')
ora = round(ora)
print(f'Dupa rotunjire, ea are valoarea: {ora} si este de tipul-->', type(ora))
print()
print()

# 6. Citește de la tastatură:
# - numele;
# - prenumele.
# Afișează: 'Numele complet are x caractere'.
print('Ex. 6:')
print()
numele = input(print('Scrie-ti numele: '))
prenumele = input(print('Scrie-ti prenumele: '))
nume_complet = numele + ' ' + prenumele
print('Nume complet: ', nume_complet)
length_nume_complet = len(nume_complet)
print(f"Numele complet are {length_nume_complet} caractere")
print()
print()

# 7. Citește de la tastatură:
# - lungimea;
# - lățimea.
# Afișează: 'Aria dreptunghiului este x'.
print('Ex. 7:')
print()
print('Calculam aria dreptunghiului.')
L = input('Alege lungimea dreptunghiului.')
l = input('Alege latimea dreptunghiului.')
print ('Aria dreptunghiului este: ', int(L) * int(l))
print()
print()

# 8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
# - afișează de câte ori apare cuvântul 'the';
#           +
# 9. Același string.
# ● Afișează de câte ori apare cuvântul 'the';
# ● Printează rezultatul.
print('Ex. 8 + 9:')
print()
random_philosophy = 'Coral is either the stupidest animal or the smartest rock'
print('Avem string-ul: ', random_philosophy,'.')
print('Acesta are ', len(random_philosophy), ' de caractere.')
print('Avand aceasta informatie, putem folosi functia .count pentru a afisa de cate ori se repeta cuvantul "the".')
string_counted = random_philosophy.count('the', 0, len(random_philosophy))
print('String-ul contine cuvantul "the" de ', string_counted, ' ori.')
print()
print()

# 10. Același string.
# ● Folosiți un assert ca să verificați dacă acest string conține doar numere.
print('Ex. 10:')
print()
string_has_numbers = random_philosophy.isnumeric()
print(string_has_numbers)
assert random_philosophy.isnumeric() == False
print('Acest string nu conține doar numere.')
assert random_philosophy.isnumeric() == True
print('Acest string conține doar numere.')


