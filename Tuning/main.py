#Tema01 Optional fine-tune

# 1. Exercițiu:
# - citește de la tastatură un string de dimensiune impară;
# - afișează caracterul din mijloc.
print('Ex.1 optional:')
def ImparitateString():
    global string_de_afisat
    string_de_afisat = input('Introduce un string de dimensiune impara.')
    if (len(string_de_afisat) == 0):
        print('Nu ai introdus un string de la tastatura.')
        print('Mai incearca o data.')
        ImparitateString()
    elif(len(string_de_afisat)%2 != 0):
        print('Ai introdus string-ul de dimensiune impara:', string_de_afisat)
    else:
        print('Ai introdus un string de dimensiune para.')
        print('Te rog sa reintroduci un string de dimensiune impara.')
        ImparitateString()


ImparitateString()
index_char_mijloc = int(len(string_de_afisat)/2)
print(type(index_char_mijloc))
print('Caracterul din mijlocul string-ului este: ', string_de_afisat[index_char_mijloc])
print()

# # 2. Folosind assert, verifică dacă un string este palindrom.
print('Ex.2 optional:')
print('Pentru a verifica daca un cuvant este palindrom, trebuie sa-l comparam cu reversul acestuia.')
palindrom = 'aerisirea'
assert palindrom == palindrom[::-1]
print(f'Daca vezi acest mesaj, inseamna ca "{palindrom}" este palindrom.')
print()
# 3. Folosind o singură linie de cod :
# - citește un string de la tastatură (ex: 'alabala portocala');
# - salvează fiecare cuvânt într-o variabilă;
# - printează ambele variabile pentru verificare.
print('Ex.3 optional:')
def o_singura_linie_de_cod():
    l = input("Scrie o propozitie care iti trece prin minte.")
    m = l.split()
    i = 0
    o = []
    while i<= len(l)-1:
        o += l[i]
        i+=1
    o = ''.join(o)
    print(type(o))
    print(f'Ati introdus propozitia: "{l}", iar cu ajutorul acestei "singure linii de cod", am transformat-o in lista\n {m}'
          f' si am salvat fiecare cuvant intr-o variabila, recreand string-ul original\n "{o}"')

o_singura_linie_de_cod()

#4. Exercițiu:
# - citește un string de la tastatură (ex: alabala portocala);
# - salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
# - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.
print('Ex.4 optional:')
string_original = input("Scrie o propozitie random.")
char0 = string_original[0].lower()
lista_string_modificat = list(string_original.replace(char0, char0.upper()))
lista_string_modificat[0], lista_string_modificat[-1] = char0, char0
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
username = input('Scrie un username.')
parola = input('Scrie o parola')
parola_ascunsa = len(parola) * '*'
print('Ati creat user-ul', username, 'cu parola', parola_ascunsa, '.')
print('Va rugam sa va logati in cont.')

def VerificareCont():
    i = 1
    incercari = 2
    while(i < 4):
        verify_username = input('username')
        verify_parola = input('parola')
        if username == verify_username and parola == verify_parola:
            print('V-ati logat in cont. Great success!')
            return 0
        else:
            print('Username sau parola introduse incorect.')
            print('Va rugam sa reincercati. Nr. de incercari ramase:', {incercari})
            i += 1
            incercari -=1
            print(i)

    print('Cont blocat din motive de securitate.')
    return 0


VerificareCont()