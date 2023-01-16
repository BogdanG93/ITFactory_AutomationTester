# 1. Exercițiu:
# - citește de la tastatură un string de dimensiune impară;
# - afișează caracterul din mijloc.
print('Ex.1 optional:')
palindrom = 'aerisirea'  # we cheat because our_variable > input_from_keyboard
print(f'Cuvantul "{palindrom}" este cel mai lung panlindrom din limba romana si are {len(palindrom)} caractere.')
char_mijloc_palindrom = round((len(palindrom))/2)
print('Singurul caracter care nu se afla in cuvant si se afla in mijlocul acestuia este: ', palindrom[char_mijloc_palindrom])
# print(palindrom[(round((len(palindrom))/2))])
print()
# 2. Folosind assert, verifică dacă un string este palindrom.
print('Ex.2 optional:')
print('Pentru a verifica daca un cuvant este palindrom, trebuie sa-l comparam cu reversul acestuia.')
assert palindrom == palindrom[::-1]
print('Daca vezi acest mesaj, inseamna ca', palindrom, 'este palindrom.')
print()
# 3. Folosind o singură linie de cod :
# - citește un string de la tastatură (ex: 'alabala portocala');
# - salvează fiecare cuvânt într-o variabilă;
# - printează ambele variabile pentru verificare.
print('Ex.3 optional:')
# Prima incercare de aproape o singura linie de cod
#a,b = tuple((input("Scrie o propozitie care iti trece prin minte."), input("Scrie o propozitie care iti trece prin minte.").split()))
#print(a, b)
def o_singura_linie_de_cod():
    l = input("Scrie o propozitie care iti trece prin minte.")
    m = l.split()
    # a, b, c = m
    print(f'Ati introdus propozitia "{l}", iar cu ajutorul acestei "singure linii de cod", am transformat-o in lista {m}')
    # print(f'si variabilele {a}, {b}, {c}.')

o_singura_linie_de_cod()

#4. Exercițiu:
# - citește un string de la tastatură (ex: alabala portocala);
# - salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
# - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.
print('Ex.4 optional:')
string_original = input("Scrie o propozitie random.")
char0 = string_original[0].lower()
char_minus_1 = string_original[-1].lower()
string_modificat = string_original.replace(char0, char0.upper())
lista_string_modificat = list(string_modificat)
lista_string_modificat[0] = char0
lista_string_modificat[-1] = char_minus_1
string_modificat = ''.join(lista_string_modificat)
print('Sirul introdus este', {string_original}, ', acesta transformandu-se in', {string_modificat}, '.')
print()

# 5.Exercițiu:
# - citește un user de la tastatură;
# - citește o parolă;
# - afișează: 'Parola pt user x este ***** și are x caractere';
# - ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
# afișeze corect.
# eg: parola abc => ***
# parola abcd => ****
print('Ex.5 optional:')
username = input('Creati un user.')
parola = input('Setati parola.')
parola_ascunsa = len(parola) * '*'
print('Ati creat user-ul', username, 'cu parola', parola_ascunsa, '.')



