# OBLIGATORII

# 1. Declară o listă note_muzicale în care să pui do re mi etc până la do
# ● Afișeaz-o
# ● Inversează ordinea folosind slicing și suprascrie această listă.
# ● Printează varianta actuală (inversată).
# ● Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea.
# Nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat.
# ● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print('a. Lista de note muzicale:\n', note_muzicale)
note_muzicale = note_muzicale[::-1]
print('b. Lista inversata de note muzicale:\n', note_muzicale)
note_muzicale.reverse()
print('c. Lista de note muzicale aplicand functia reverse:\n', note_muzicale)

# # 2. De câte ori apare ‘do’?
print('Nota muzicala "do" apare de', note_muzicale.count('do'), 'ori in lista.')

# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# Găsește 2 variante să le unești într-o singură listă.
list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
print("Lista noua formata din prima si a doua lista:", list1 + list2)
list1.extend(list2)
print("Prima lista unita cu lista a doua, folosing functia extend:", list1)

# 4. Sorteaza si afiseaza lista generata la exercitiul anterior. Sterge numarul 0 din lista
# folosind o functie si apoi afiseaza din nou lista
list1.sort()
print(f"Lista sortata este: {list1}")
list1.remove(0)
print(f"Lista sortata dupa stergerea numarului 0 este: {list1}")

# 5. Folosind un if, verifica lista generata la exercitiul 3 si afiseaza pe fiecare ramura urmatoarele:
# Lista este goala (IF)
# Lista nu este goala (ELSE)
if list1:
    print('Lista nu este goala.')
else:
    print('Lista este goala.')

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.
list1.clear()

# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.
if list1:
    print('Lista nu este goala.')
else:
    print('Lista este goala.')

#  8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)
dict1 = {'Ana': 8,
         'Gigel': 10,
         'Dorel': 5}
print(dict1.keys())

# 9. Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie
print('Ana a luat nota', dict1['Ana'])
print('Gigel a luat nota', dict1['Gigel'])
print('Dorel a luat nota', dict1['Dorel'])

# 10. Dorel a făcut contestație și a primit 6
# ● Modifică nota lui Dorel în 6
# ● Printează nota după modificare
dict1.update({'Dorel': 6})
print('Dorel a luat nota', dict1['Dorel'])

# 11. Gigel se transferă din clasă
# ● Căuta o funcție care să îl șteargă
# ● Vine un coleg nou. Adaugă Ionică, cu nota 9
# ● Printează noii elevi
dict1.pop('Gigel')
dict1['Ionica'] = 9
print(dict1)

# 12. Set
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# ● Adaugă în zilele_sapt ‘luni’
# ● Afișeaza zile_sapt
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbătă', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')       # un set nu poate contine duplicate => linia de cod este redundanta
print(zile_sapt)

# 13.Folosește un if și verifică dacă:
# ● Weekend este un subset al zilelor din săptămânii.
# ● Weekend nu este un subset al zilelor din săptămânii.
if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor săptămânii.')
else:
    print('Weekend nu este un subset al zilelor săptămânii.')

# 14. Afișează diferențele dintre aceste 2 seturi.
print(zile_sapt.difference(weekend))

# 15. Afișază intersecția elementelor din aceste 2 seturi.
print(zile_sapt.intersection(weekend))

# OPTIONALE
'''
1. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise
● Declară o Listă cu 5 jucători
● Schimbari_efectuate = te joci tu cu valori diferite
● Schimbari_max = 3

Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție:
- Efectuează schimbarea
- Șterge jucătorul scos din listă
- Adaugă jucătorul intrat
- Afișaza a intra x, a ieșit y, mai ai z schimbări

Dacă jucătorul nu e în teren:
- Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
teren’
- Afișază ‘mai ai z schimbări’
Testează codul cu diferite valori

Google search hint: “how to check if item îs în list python”
'''
schimbari_max_admise = 3
jucatori_in_teren = ['77 Barbu Gabriela Theodora', '12 Barbu Mădălina', '35 Popescu Ionela Diana',
                   '10 Sandu Gabriela Sorina', '27 Șandru Mihaela']
rezerve = ['22 Balogh Alexandru', '13 Geagu Bogdan', '33 Pop Octavian Marius']
print('Jucatorii din teren sunt:', jucatori_in_teren)
print('Rezervele sunt:', rezerve)

while schimbari_max_admise > 0:
    schimbare_jucator = int(input('Schimba jucatorul din teren folosindu-te de numarul de pe tricou.'))
    if schimbare_jucator == 77:
        jucator_schimbat = '77 Barbu Gabriela Theodora'
    elif schimbare_jucator == 12:
        jucator_schimbat = '12 Barbu Mădălina'
    elif schimbare_jucator == 35:
        jucator_schimbat = '35 Popescu Ionela Diana'
    elif schimbare_jucator == 10:
        jucator_schimbat = '10 Sandu Gabriela Sorina'
    elif schimbare_jucator == 27:
        jucator_schimbat = '27 Șandru Mihaela'
    else:
        print('Nu se poate efectua schimbarea deoarece jucătorul nu este în teren.')
        print('Mai ai', schimbari_max_admise, 'schimbari.')
        schimbare_jucator = int(input('Schimba jucatorul din teren folosindu-te de numarul de pe tricou.'))
        if schimbare_jucator == 77:
            jucator_schimbat = '77 Barbu Gabriela Theodora'
        elif schimbare_jucator == 12:
            jucator_schimbat = '12 Barbu Mădălina'
        elif schimbare_jucator == 35:
            jucator_schimbat = '35 Popescu Ionela Diana'
        elif schimbare_jucator == 10:
            jucator_schimbat = '10 Sandu Gabriela Sorina'
        elif schimbare_jucator == 27:
            jucator_schimbat = '27 Șandru Mihaela'

    jucator_introdus = int(input('Introdu un jucator in teren folosindu-te de numarul de pe tricou.'))
    if jucator_introdus == 22:
        jucator_introdus = '22 Balogh Alexandru'
    elif jucator_introdus == 13:
        jucator_introdus = '13 Geagu Bogdan'
    elif jucator_introdus == 33:
        jucator_introdus = '33 Pop Octavian Marius'
    else:
        print('Jucatorul pe care vrei sa-l introduci in teren nu este pe banca de rezerve.')
        jucator_introdus = int(input('Introdu un jucator in teren folosindu-te de numarul de pe tricou.'))
        if jucator_introdus == 22:
            jucator_introdus = '22 Balogh Alexandru'
        elif jucator_introdus == 13:
            jucator_introdus = '13 Geagu Bogdan'
        elif jucator_introdus == 33:
            jucator_introdus = '33 Pop Octavian Marius'

    if jucator_schimbat in jucatori_in_teren:
        if jucator_introdus in rezerve:
            jucatori_in_teren.remove(jucator_schimbat)
            jucatori_in_teren.extend([jucator_introdus])
            rezerve.remove(jucator_introdus)
            schimbari_max_admise-=1
            print(f'A intrat jucatorul cu nr. {jucator_introdus}.\n'
                  f'A ieșit jucatorul cu nr. {jucator_schimbat}.\n'
                  f'Mai ai {schimbari_max_admise} schimbări')
            print('Jucatorii din teren sunt:', jucatori_in_teren)
            print('Rezervele sunt:', rezerve)

        else:
            print('Nu s-a putut face schimbarea.')
    else:
        print('Reincearca.')
