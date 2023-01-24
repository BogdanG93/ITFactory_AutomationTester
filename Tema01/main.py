"""
1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.

Variabila este informatia pe care o stocam intr-un spatiu alocat de memorie, in scopul manipularii acesteia.

Practic ne putem gandi la spatiu ca fiind un dulap, spatiul alocat variabilei ca fiind un obiect care sa
contina informatia, de genul o cutie, numele variabilei ar fi labelul de pe cutie, iar in interiorul cutiei
s-ar afla informatia.
"""

# 2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă :
tema = 'Azi ne facem tema.'   # str
exercitii = 10                # int
ora = 18.23                   # float
facem_toata_tema = False      # bool

# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
#                               +
# 5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
print('Variabilele declarate anterior sunt de tipul: ')
print(f'tema: {tema}--> ', type(tema))
print(f'exercitii: {exercitii}-->', type(exercitii))
print(f'ora: {ora}-->', type(ora))
print(f'facem_toata_tema: {facem_toata_tema}-->', type(facem_toata_tema))
print(tema + ' Avem ' + str(exercitii) + ' exercitii de rezolvat. Avand in vedere faptul ca este ora ' + str(ora) +
      ', credeti ca intr-o ora le putem rezolva pe toate? R: ' + str(facem_toata_tema))

# 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
# - Verifică tipul acesteia.
print(f'Variabila "ora" are valoarea de: {ora}')
ora = round(ora)
print(f'Dupa rotunjire, ea are valoarea: {ora} si este de tipul-->', type(ora))

# 6. Citește de la tastatură:
# - numele;
# - prenumele.
# Afișează: 'Numele complet are x caractere'.
numele = input('Scrie-ti numele: ')
prenumele = input('Scrie-ti prenumele: ')
print(f"Numele complet are {len(numele) + len(prenumele)} caractere")

# 7. Citește de la tastatură:
# - lungimea;
# - lățimea.
# Afișează: 'Aria dreptunghiului este x'.
print('Calculam aria dreptunghiului.')
lungimea = input('Alege lungimea dreptunghiului: ')
latimea = input('Alege latimea dreptunghiului: ')
print('Aria dreptunghiului este: ', int(lungimea) * int(latimea))

# 8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
# - afișează de câte ori apare cuvântul 'the';
#           +
# 9. Același string.
# ● Afișează de câte ori apare cuvântul 'the';
# ● Printează rezultatul.
propoztie = 'Coral is either the stupidest animal or the smartest rock'
print('String-ul contine cuvantul "the" de ', propoztie.count(' the '), ' ori.')

# 10. Același string.
# ● Folosiți un assert ca să verificați dacă acest string conține doar numere.
propoztie = 'Coral is either the stupidest animal or the smartest rock'
assert propoztie.isnumeric() is True, "Propozitia nu contine doar cifre"
