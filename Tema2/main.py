# import random

'''
Exerciții obligatorii - grad de dificultate: Ușor spre Mediu .

Pentru toate exercițiile se va folosi noțiunea de if în rezolvare.
Indirect vei exersa și operatorii în cadrul condițiilor ramurilor din if.
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.
'''
# 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
'''
if else sunt operatori conditionali, care functioneaza in baza unui argument dat, valoarea lui de adevar fiind evaluata
IF conditie este adevarata --> executa codul
In cazul in care nu se indeplineste conditia de adevar, blocul de cod in IF este ignorat, trecandu-se la blocul ELSE
ELSE va rula numai in cazul in care nu este indeplinita conditia de adevara regasita la IF, altfel va fi ignorata
IF/ELSE este impartit in 2 ramuri, dar daca avem nevoie de mai multe conditii, putem adauga ELIF de cate ori avem nevoie
'''

# # 2. Verifică și afișează dacă x este număr natural sau nu.
# x = input('Alege un numar.')
# if x.isnumeric():
#     print(x, 'este numar natural.')
# else:
#     print(x, 'nu este numar natural.')

# # 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
# x = int(input('Alege un numar natural.'))
# if x == 0:
#     print(x, 'este numar neutru.')
# elif x > 0:
#     print(x, 'este numar pozitiv.')
# else:
#     print(x, 'este numar negativ.')

# # 4. Verifică și afișează dacă x este între -2 și 13.
# x = int(input('Alege un numar natural.'))
# if (-2 < x < 13):
#     print(x, 'se afla intre -2 si 13.')
# else:
#     print(x, 'nu se afla intre -2 si 13.')

# # 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
# x = int(input('Alege o valoare pentru x.'))
# y = int(input('Alege o valoare pentru y.'))
# if x - y < 5:
#     print(f'Diferenta dintre {x} si {y} este {x-y}, aceasta fiind mai mica de 5.')
# else:
#     print(f'Diferenta dintre {x} si {y} este {x-y}, aceasta fiind mai mare de 5 sau egala cu 5.')

# # 6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
# x = int(input('Alege o valoare pentru x.'))
# if not(5 < x < 27):
#     print(x, 'NU este între 5 și 27.')
# else:
#     print(x, 'este între 5 și 27.')

# # 7.x și y (int). Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
# x = int(input('Alege o valoare pentru x.'))
# y = int(input('Alege o valoare pentru y.'))
# if x == y:
#     print(x, 'este egal cu', y, '.')
# elif x > y:
#     print(x, '>', y)
# else:
#     print(x, '<', y)

# # 8. x, y, z - laturile unui triunghi.
# # Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
# x = int(input('Alege o valoare pentru x.'))
# y = int(input('Alege o valoare pentru y.'))
# z = int(input('Alege o valoare pentru z.'))
# if x == y == z:
#     print('Triunghiul este echilateral.')
# elif (x == y) or (x == z) or (y == z):
#     print('Triunghiul este isoscel.')
# else:
#     print('Triunghiul este oarecare.')


# # 9. Citește o literă de la tastatură.
# # Verifică și afișează dacă este vocală sau nu
# litera = input('Introduceti o litera.')
# if litera[0].lower() in ['a', 'ă', 'â', 'e', 'i', 'î', 'o', 'u']:
#     print('Litera introdusa este o vocala.')
# else:
#     print('Litera introdusa este o consoana.')

# # 10.Transformă și printează notele din sistem românesc în >
# # Peste 9 => A
# # Peste 8 => B
# # Peste 7 => C
# # Peste 6 => D
# # Peste 4 => E
# # 4 sau sub => F
# nota = int(input('Ce nota ai luat?'))
# if nota > 9:
#     print('Am luat nota A.')
# elif nota > 8:
#     print('Am luat nota B.')
# elif nota > 7:
#     print('Am luat nota C.')
# elif nota > 6:
#     print('Am luat nota D.')
# elif nota > 4:
#     print('Am luat nota E.')
# elif nota <= 4:
#     print('Am luat nota F.')


''' Exerciții Opționale - grad de dificultate: Mediu spre greu - might need Google. '''

# # 1.Verifică dacă x are minim 4 cifre (x e int).
# # (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
# x = input('Introduceti un numar.')
# if len(x) > 3:
#     print(x, 'are minim 4 cifre.')
# else:
#     print(x, 'nu are minim 4 cifre.')

# # 2.Verifică dacă x are exact 6 cifre.
# x = input('Introduceti un numar.')
# if len(x) == 6:
#     print(x, 'are exact 6 cifre.')
# else:
#     print(x, 'nu are exact 6 cifre.')

# # 3.Verifică dacă x este număr par sau impar (x e int).
# x = int(input('Introduceti un numar.'))
# if x % 2 == 0:
#     print(x, 'este un numar par.')
# else:
#     print(x, 'este un numar impar.')

# # 4. x, y, z (int)
# # Afișează care este cel mai mare dintre ele?
# x = int(input('Alege o valoare pentru x.'))
# y = int(input('Alege o valoare pentru y.'))
# z = int(input('Alege o valoare pentru z.'))
# if x > y > z or x > z > y:
#     print(x, 'este cel mai mare numar.')
# elif y > x > z or y > z > x:
#     print(y, 'este cel mai mare numar.')
# else:
#     print(z, 'este cel mai mare numar.')
'''
cel_mai_mare = max(x, y, z)
print(cel_mai_mare)
'''

# # 5. x, y, z - reprezintă unghiurile unui triunghi
# # Verifică și afișează dacă triunghiul este valid sau nu.
# x = int(input('Alege o valoare numerica in grade pentru x.'))
# y = int(input('Alege o valoare numerica in grade pentru y.'))
# z = int(input('Alege o valoare numerica in grade pentru z.'))
# if (x + y + z == 180) and x > 0 and y > 0 and z > 0 and (x < y + z) and (y < x + z) and (z < x + y):
#     print('Triunghiul este valid.')
# else:
#     print('Triunghiul nu este valid.')

# # 6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# # ● Citiți de la tastatură un int x
# # ● Afișează stringul fără ultimele x caractere
# # Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
# string_original = 'Coral is either the stupidest animal or the smartest rock'
# x = int(input('Cate caractere vrei sa stergi din finalul stringului?'))
# print(string[:len(string)-x])

# 7.Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5
# string_nou = string_original[slice(0, 5)] + string_original[slice(-5, len(string_original))]


# # 8. Același string.
# # ● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
# # este o funcție care te ajuta sa faci asta)
# # ● Folosind această variabilă + slicing, afișează tot stringul până la acest
# # cuvant
# # ● output: 'Coral is either the stupidest animal or the smartest '
# index_rock = string_original.index('rock')
# print('Indexul cuvantului "rock" este', index_rock)
# print(string_original[slice(0, index_rock)])

# # 9. Citește de la tastatura un string
# # Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
# # Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat
# string_random = input('Introduce de la tastatura un string.')
# if string_random[0].lower() == string_random[len(string_random)-1].lower():
#     print('Primul si ultimul caracter sunt la fel.')
# else:
#     print('Primul si ultimul caracter sunt diferite.')

# # 10. Avand stringul '0123456789'
# # ● Afișați doar numerele pare
# # ● Afișați doar numerele impare
# # (hint: folositi slicing, controlați din pas)
# string_numere = '0123456789'
# print('Numere pare', string_numere[slice(0, len(string_numere), 2)])
# print('Numere impare', string_numere[slice(1, len(string_numere), 2)])

'''
Exerciții Bonus (may need google) .
11. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll

Luați un numărul ghicit de la utilizator
Verificați și afișați dacă utilizatorul a ghicit
Veți avea 3 opțiuni
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
● Ai ghicit. Felicitari! Ai ales x si zarul a fost y
'''

# ghiceste_zarul = int(input('Ghiceste pe ce numar va pica zarul. Alege un numar de la 1 la 6.'))
# numar_zar = random.randint(1, 6)
# if ghiceste_zarul == numar_zar:
#     print(f'Ai ghicit. Felicitari! Ai ales {ghiceste_zarul} si zarul a fost {numar_zar}')
# elif ghiceste_zarul < numar_zar:
#     print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {ghiceste_zarul} dar a fost {numar_zar}')
# else:
#     print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {ghiceste_zarul} dar a fost {numar_zar}')