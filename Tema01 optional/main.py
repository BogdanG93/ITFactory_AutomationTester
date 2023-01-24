# 1. Exercițiu:
# - citește de la tastatură un string de dimensiune impară;
# - afișează caracterul din mijloc.
propoz = input("Scrie un string de dimensiune impara.\n")
print("Caracterul din mijlocul string-ului este:", propoz[(len(propoz)//2)])

# 2. Folosind assert, verifică dacă un string este palindrom.
palindrom = "aerisirea"
assert palindrom == palindrom[::-1], "Cuvantul nu este palingdrom."

# 3. Folosind o singură linie de cod :
# - citește un string de la tastatură (ex: 'alabala portocala');
# - salvează fiecare cuvânt într-o variabilă;
# - printează ambele variabile pentru verificare.
string = input("Scrie o propozitie care iti trece prin minte.\n")
x, y = string.split(" ")
print("Primul cuvant este:", x)
print("Al doilea cuvant este:", y)

#4. Exercițiu:
# - citește un string de la tastatură (ex: alabala portocala);
# - salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
# - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.
string = input("Scrie o propozitie random.\n")
prima_litera = string[0]
string_modificat = prima_litera + string[1:(len(string)-1)].replace(prima_litera, prima_litera.upper()) \
                   + string[len(string)-1]
print(string_modificat)

# 5.Exercițiu:
# - citește un user de la tastatură;
# - citește o parolă;
# - afișează: 'Parola pt user x este ***** și are x caractere';
# - ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
# afișeze corect.
# eg: parola abc => ***
# parola abcd => ****
username = input('Creati un user.')
parola = input('Setati parola.')
parola_ascunsa = len(parola) * '*'
print('Ati creat user-ul', username, 'cu parola', parola_ascunsa, '.')
