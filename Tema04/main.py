import random

# 1.Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
# 'Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for masina in range(len(masini)):
    print('FOR: Mașina mea preferată este', masini[masina])

for masina in masini:
    print('FOR EACH: Mașina mea preferată este', masina)

i = 0
while i < len(masini):
    print('WHILE: Mașina mea preferată este', masini[i])
    i += 1

# 2. Aceeași listă:
# Folosește un for else
# În for
# - Modifică elementele din listă astfel încât să fie scrie cu majuscule, exceptând primul și ultimul.
# În else:
# - Printează lista.
for masina in range(1, len(masini)-1):
    masini[masina] = masini[masina].upper()
else:
    print(masini)

# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# we override the variable 'masini', because it was modified earlier in the last problem
for masina in range(len(masini)):
    if 'Mercedes' in masini[masina]:
        print('Am găsit masina dorită de dvs.')
        break
    else:
        print('Am găsit mașina', masini[masina], '. Mai căutam.')

# 4. Aceeași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Lăstun:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
# else).
# - Printează S-ar putea să vă placă mașina x.
for masina in range(len(masini)):
    # if 'Trabant' in masini[masina] or 'Lăstun' in masini[masina]:  <-- puteam sa facem si asa
    if masini[masina] == 'Trabant' or masini[masina] == 'Lăstun':
        continue
    print(f'S-ar putea să vă placă mașina {masini[masina]}.')

# 5. Modernizează parcul de mașini:
# ● Crează o listă goală, masini_vechi.
# ● Itereaza prin mașini.
# ● Când găsesti Lăstun sau Trabant:
# - Salvează aceste mașini în masini_vechi.
# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# ● Printează Modele vechi: x.
# ● Modele noi: x.
masini_vechi = []
for masina in range(len(masini)):
    if masini[masina] == 'Trabant' or masini[masina] == 'Lăstun':
        masini_vechi.append(masini[masina])
        masini[masina] = 'Tesla'
print('Modele vechi:', masini_vechi)
print('Modele noi:', masini)

# 6. Având dict:
pret_masini = {
 'Dacia': 6800,
 'Lăstun': 500,
 'Opel': 1100,
 'Audi': 19000,
 'BMW': 23000
}
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
# ● Itereaza prin dict.items() și accesează mașina și prețul.
# ● Printează Pentru un buget de sub 15000 euro puteți alege mașină xLastun
# ● Iterează prin listă.
buget = 15000
for masina, pret in pret_masini.items():
    if pret <= buget:
        print(f'Pentru un buget de pana in {buget} euro puteti alege masina: {masina}')

# 7. Având lista:
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).
i = 0
for numar in range(len(numere)):
    if numere[numar] == 3:
        i += 1
print('Numarul 3 apare in lista de', i, 'ori.')

# 8. Aceeași listă:
# ● Iterează prin ea
# ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
suma_nr = 0
for numar in numere:
    suma_nr += numar
print('Suma numerelor este', suma_nr)

# 9. Aceeași listă:
# ● Iterează prin ea.
# ● Afișază cel mai mare număr (nu ai voie să folosești max).
numar_max = 0
for numar in numere:
    if numar > numar_max:
        numar_max = numar
print('Numarul maxim din lista de numere este', numar_max)

# 10. Aceeași listă:
# ● Iterează prin ea.
# ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# ● Afișază noua listă.
for numar in range(len(numere)):
    if numere[numar] > 0:
        numere[numar] -= numere[numar] * 2  # sau folosim functia -abs()
print(numere)

# OPTIONALE
# Ex.1
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
# Itereaza prin listă alte_numere
# Populează corect celelalte liste
# Afișeaza cele 4 liste la final
for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    else:
        numere_impare.append(numar)
    if numar > 0:
        numere_pozitive.append(numar)
    else:
        numere_negative.append(numar)
print(f'Lista cu numere pare este: {numere_pare}')
print(f'Lista cu numere impare este: {numere_impare}')
print(f'Lista cu numere pozitive este: {numere_pozitive}')
print(f'Lista cu numere negative este: {numere_negative}')

# 2. Aceeași listă:
# Ordonează crescător lista fară să folosești sort.
# Folosim bubble sort conform link
print("Lista neordonata:", alte_numere)
am_schimbat = False
for i in range(len(alte_numere) - 1):
    for j in range(len(alte_numere) - i - 1):
        if alte_numere[j] > alte_numere[j+1]:
            am_schimbat = True
            alte_numere[j], alte_numere[j+1] = alte_numere[j+1], alte_numere[j]
    if not am_schimbat:
        break
print("Lista ordonata:", alte_numere)

# 3. Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
# User alege un număr
# Programul îi spune:
# ● Nr secret e mai mare
# ● Nr secret e mai mic
# ● Felicitări! Ai ghicit!
numar_secret = random.randint(1, 30)
numar_ghicit = None
while numar_ghicit is None:
    nr = int(input('Introdu un numar: '))
    if nr > numar_secret:
        print('Numarul secret este mai mic.')
    elif nr < numar_secret:
        print('Numarul secret este mai mare.')
    else:
        print('Felicitari, ai gasit numarul!')
        break

# # 4. Alege un număr de la tastatură
# # Ex: 7
# # Scrie un program care să genereze în consolă următoarea piramidă
# # 1
# # 22
# # 333
# # 4444
# # 55555
# # 666666
# # 7777777

a = 1
b = ''
numar = int(input('Alege cate niveluri are piramida.'))
for nivel in range(1, numar + 1):
    b = str(a) * nivel
    a += 1
    print(b)

# 5.
tastatura_telefon = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9],
 [0]
]
# Iterează prin listă 2d
# Printează ‘Cifra curentă este x’
# (hint: nested for - adică for în for)
for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print('Cifra curenta este', tastatura_telefon[i][j])
