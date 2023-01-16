import random
print('EXERCITII OBLIGATORII')

# Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
# Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
# X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
# X este un int.
print('1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.\n'
      '"if else" functioneaza in cadrul a (fix) doua ramuri, in ideea de a acoperi \n'
      'mai multe scenarii (ex. scenarii cu True/False)\n'
      'if conditie -> executa cod\n'
      'else (fara conditie)-> executa celalalt cod.')


print('Ex.2 Verifică și afișează dacă x este număr natural sau nu.')

def NrNatural():
    a = input('Introduce un nr. natural.')
    if a.isnumeric():
        print('Ai introdus numarul natural', a)
    else:
        print('Nu ati introdus un numar natural. Te rog sa reincerci.')
        NrNatural()

NrNatural()


print()
print('Ex.3 Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.')

def VerificaNumar():
    try:
        global x
        x = int(input('Introduce un numar.'))
    except ValueError:
        print('Nu ai introdus un numar natural. Te rog sa reincerci.')
        VerificaNumar()

def PozNeNeu():
    VerificaNumar()
    print('Ai introdus numarul', x)
    if x == 0:
        print('Acesta este neutru.')
    elif x > 0:
        print('Acesta este un numar pozitiv.')
    else:
        print('Ati introdus un numar negativ.')

PozNeNeu()


print()
print('Ex.4 Verifică și afișează dacă x este între -2 și 13.')

VerificaNumar()
print('Ai introdus numarul', x)
if -2 <= x <= 13:
    print('x se afla intre valorile "-2" si "13".')
else:
    print('x nu se afla intre valorile "-2" si "13".')


print()
print('Ex.5 Verifică și afișează dacă diferența dintre x și y este mai mică de 5.')

VerificaNumar()
print('Ai introdus numarul', x)
y = 10
print(f'Diferenta dintre {x} si {y} este:', x - y)
if x - y < 5:
    print('Diferenta dintre x si y este mai mica de 5.')
else:
    print('Diferenta dintre x si y este nu este mai mica de 5.')


print()
print('Ex.6 Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.')

VerificaNumar()
print('Ai introdus numarul', x)
if not(5 < x < 27):
    print("x NU este intre 5 si 27.")
else:
    print("x este intre 5 si 27.")


print()
print('Ex.7 x și y (int)\n'
      'Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.')

VerificaNumar()
y = int(input('Introduce un nr. de tipul "int" de la tastatura.'))
if x == y:
    print("x si y sunt nr. egale.")
elif x > y:
    print("x este mai mare decat y.")
else:
    print('x este mai mic decat y.')


print()
print('Ex.8 8. x, y, z - laturile unui triunghi.\n'
      'Afișează dacă triunghiul este isoscel, echilateral sau oarecare.')

def ConstruireTriunghi():
    x = int(input('Alege valoarea lui int(x).'))
    y = int(input('Alege valoarea lui int(y).'))
    z = int(input('Alege valoarea lui int(z).'))
    if (x, y, z > 0) and not (x > y + z) and not (y > x + z) and not (z > x + y):
        if x == y == z:
            print('Triunghiul este echilateral.')
        elif (x == y) or (x == z) or (y == z):
            print('Triunghiul este isoscel.')
        else:
            print('Triunghiul este oarecare.')
    else:
        print('Nu putem construi un triunghi folosind aceste valori ale laturilor.')
        print('Reintrodu alte valori.')
        ConstruireTriunghi()

ConstruireTriunghi()


print()
print('Ex.9 Citește o literă de la tastatură.\n'
      'Verifică și afișează dacă este vocală sau nu')

def OneChar():
    global litera
    litera = input('Introduceti o litera.')
    if (litera.isalpha()) and (litera[0] == litera):
        print('Ai introdus litera', litera)
    else:
        print('Ai introdus una sau mai multe cifre/spatii sau mai mult de o litera, reincearca.')
        OneChar()

def VerificareVocala():
    OneChar()
    if litera[0].lower() in ['a', 'ă', 'â', 'e', 'i', 'î', 'o', 'u']:
        print('Litera introdusa este o vocala.')
    else:
        print('Litera introdusa este o consoana.')

VerificareVocala()


print()
print('Ex.10 Transformă și printează notele din sistem românesc în >\n'
      'Peste 9 => A\n'
      'Peste 8 => B\n'
      'Peste 7 => C\n'
      'Peste 6 => D\n'
      'Peste 4 => E\n'
      '4 sau sub => F')

nota = float(input('Care este ultima nota obtinuta la matematica? (se va salva de tip float)'))
if nota > 10:
    print('Am luat ce nota am vrut eu.')
else:
    if nota > 9:
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

print()
print('EXERCITII OPTIONALE:')

print('Ex.1 Verifică dacă x are minim 4 cifre (x e int).\n'
      '(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)')

def VerificaMinimCifre():
    VerificaNumar()
    if len(str(x)) <= 3:
        print('Numarul introdus este sub minimul de 4 cifre, reincearca.')
        VerificaMinimCifre()
    else:
        print('Ai introdus un numar de minim 4 cifre.')

VerificaMinimCifre()


print()
print('Ex.2 Verifică dacă x are exact 6 cifre.')

def VerificaMinimCifre2():
    VerificaNumar()
    if len(str(x)) == 6:
        print('Numarul introdus este are exact 6 cifre.')

    else:
        print('Ai introdus un numar care nu are exact 6 cifre, reincearca.')
        VerificaMinimCifre2()

VerificaMinimCifre2()


print()
print('Ex.3 Verifică dacă x este număr par sau impar (x e int).')

VerificaNumar()
if x % 2 == 0:
    print('x este numar par.')
else:
    print('x este numar impar.')


print()
print('Ex.4 x, y, z (int)\n'
      'Afișează care este cel mai mare dintre ele?')

def VerificaNumarulCelMaiMare():
    x = int(input('Alege valoarea lui int(x).'))
    y = int(input('Alege valoarea lui int(y).'))
    z = int(input('Alege valoarea lui int(z).'))
    if x > y:
        if x > z:
            print('x este cel mai mare numar.')
        elif x == z:
            print('x si z sunt numere egale si sunt mai mari decat y.')
        else:
            print('z este cel mai mare numar.')
    elif y > z:
        if y > x:
            print('y este cel mai mare numar.')
        elif x == y:
            print('x si y sunt numere egale si sunt mai mari decat z.')
        else:
            print('x este cel mai mare numar.')
    elif z > x:
        if z > y:
            print('z este cel mai mare numar.')
        elif y == z:
            print('y si z sunt numere egale si sunt mai mari decat x.')
        else:
            print('y este cel mai mare numar.')
    else:
        print('Avem 3 numere egale.')


VerificaNumarulCelMaiMare()


print()
print('Ex.5 x, y, z - reprezintă unghiurile unui triunghi\n'
      'Verifică și afișează dacă triunghiul este valid sau nu.')

ConstruireTriunghi()


print()
print('Ex.6 Având stringul: "Coral is either the stupidest animal or the smartest rock"\n '
      '● Citiți de la tastatură un int x\n'
      '● Afișează stringul fără ultimele x caractere\n'
      'Exemplu: daca ati ales 7 => "Coral is either the stupidest animal or the smarte"')

original_string = 'Coral is either the stupidest animal or the smartest rock'
size_string = len(original_string)
print(f'Avem string-ul: "{original_string}"')
cut = int(input('Cate caractere vreti sa taiem din finalul stringului?'))
modified_string = original_string[:size_string - cut]
print(f'String-ul modificat este: "{modified_string}"')


print()
print('Ex.7 Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele')

first_slice, last_slice = slice(0, 5), slice(-5, len(original_string))
new_string = original_string[first_slice] + original_string[last_slice]
print(f'String-ul nou format din primele 5 + ultimele 5 caractere este: "{new_string}"')


print()
print('Ex.8. Același string.\n'
      '● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)\n'
      '● Folosind această variabilă + slicing, afișează tot stringul până la acest cuvant\n'
      '● output: "Coral is either the stupidest animal or the smartest "')

rock_index = original_string.index("rock")
slice_to_rock = slice(0, rock_index)
print('Indexul de start al cuvantului rock este: ', rock_index)
print('Afisam tot string-ul pana la indexul de start al cuvantului rock: ')
print(original_string[slice_to_rock])


print()
print('Ex.9 Citește de la tastatura un string\n'
      'Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert\n'
      'Atentie: se dorește ca programul sa fie case insensitive - "apA" e acceptat')
fraza_random = input('Scrie o propozitie/fraza de la tastatura.')

if (fraza_random[0].lower() == fraza_random[len(fraza_random)-1].lower()):
    print(f'Primul si ultimul caracter din "{fraza_random}" sunt la fel.')
else:
    print(f'Primul si ultimul caracter din "{fraza_random}" nu sunt la fel.')


print()
print('Ex.10 Avand stringul "0123456789"\n'
      '● Afișați doar numerele pare\n'
      '● Afișați doar numerele impare\n'
      '(hint: folositi slicing, controlați din pas)')

string_numere = '0123456789'
print('String-ul format din numere este: ', string_numere)
par, impar = list(string_numere[0::2]), list(string_numere[1::2])
print('Numere pare: ', par)
print('Numere impare: ', impar)

print()
print('BONUS: Joc ghicit zarul\n'
      'Caută pe net și vezi cum se generează un număr random\n'
      'Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll\n'
      'Luați un numărul ghicit de la utilizator\n'
      'Verificați și afișați dacă utilizatorul a ghicit\n'
      'Veți avea 3 opțiuni\n'
      '● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y\n'
      '● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y\n'
      '● Ai ghicit. Felicitari! Ai ales x si zarul a fost y')

score = 0
def AruncaZarul():
    zar_in_mana = input('Dai cu zarul?\n'
                        '1. Da\n'
                        '2. Nu')

    if zar_in_mana == '1' or zar_in_mana == 'da' or zar_in_mana == 'Da' or zar_in_mana == 'ok':
        dice_roll = random.randint(1, 6)
    else:
        print('Good for you. Gambling is bad, \'mkay?')
        print('You sure though? We needz da money.')
        raspuns = input('Continue?\n'
                        '1. Yes, continue.\n'
                        '2. No, I give up.')
        if raspuns == '1' or raspuns == 'Yes' or raspuns == 'yes' or raspuns == 'ok':
            AruncaZarul()
        else:
            exit(0)
    ghiceste_zarul = int(input('Ce numar crezi ca a iesit?'))
    if dice_roll == ghiceste_zarul:
        print(f'Ai ghicit. Felicitari! Ai ales {ghiceste_zarul} si zarul a fost {dice_roll}.')
        global score
        score += 1
        print(f'Scorul actual: ', score)
    elif dice_roll > ghiceste_zarul:
        print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {ghiceste_zarul}, dar a fost {dice_roll}.')
    else:
        print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {ghiceste_zarul}, dar a fost {dice_roll}.')
    next_game = input('Vrei sa incepi o noua runda?\n'
                      '1. Da\n'
                      '2. Nu')
    if next_game == '1' or next_game == 'da' or next_game == 'Da' or next_game == 'ok':
        AruncaZarul()
    else:
        print('NU ne asumam nicio responsabilitate cu privire la starea de dependenta pe care o da acest joc.')
        print('Pentru alte probleme de tip financiar adresati-va bancilor sau "rechinilor".')
        exit(0)

AruncaZarul()