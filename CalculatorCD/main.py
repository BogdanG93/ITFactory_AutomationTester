from datetime import date
from dateutil.relativedelta import relativedelta

# data = input('Intrudce data abaterii ZZ.LL.AAAA:').split('.')
# zi, luna, an = [int(item) for item in data]
# data_abatere = date(an, luna, zi)
# zile_perioada_suspendare = int(input('Introduce perioada de suspendare in zile:'))
# data_ultima_zi_de_suspendare = data_abatere + relativedelta(days=(zile_perioada_suspendare-1))
# print('Perioada de suspendare:')
# print(data_abatere, '-', data_ultima_zi_de_suspendare)

'''
Logica optiunilor se va baza pe pasi
Pasul 1 - Introduce data abaterii
Pasul 2 - Alege contraventia/contraventiile
Pasul 3 - Ai mai facut vreo alta abatere in ultimele 6 luni?
Pasul 4 - Ai/n-ai dreptul la reducere perioadei, esti/nu esti obligat sa dai testare (conform optiunilor alese)
Pas special1 - Cumul puncte
Caz special2 - Alcool

Atentie! Sa nu uitam sa declaram variabila de valabilitate dovada! Aceasta se modifica in functie de abaterile selectate
'''

def menu():
    print('Lista contraventiilor ce au ca masura complementara retinerea permisului de conducere, per perioada zile:')
    print('[1]  30 de zile - art. 100 alin. 3:')

    print('[2]  60 de zile - art. 101 alin. 3:')
          # '101.3.A\n'
          # '101.3.B\n'
          # '101.3.C\n'
          # '101.3.D\n'
          # '101.3.E\n'
          # '101.3.F'
          # '101.3.G\n'
          # '101.3.H\n')

    print('[3]  90 de zile - art. 102 alin. 3:')
          # '102.3.A\n'
          # '102.3.B\n'
          # '102.3.E\n'
          # '102.3.G\n'
          # '102.3.H\n')

    print('[4] 120 de zile - art. 102 alin. 4:')
          # '102.4.A\n'
          # '102.4.B\n'
          # '102.4.C\n')
    print('[5] Cumul puncte.')

    print('[6] Introdu manual nr. total de zile:')

    print('[0] Exit')

def option1():
    alegere_optiune1 = int(input(('Alegeti contraventia:')))
    print('[1] 100.3.A - Depasirea coloanelor de vehicule oprite la culoarea rosie a semaforului\n'
          ' sau la trecerile la nivel cu calea ferata.')
    print('[2] 100.3.D - Nerespectarea semnificatiei culorii rosii a semaforului.')
    print('[3] 100.3.F - Nerespectarea semnalelor, indicatiilor si dispozitiilor politistului rutier\n'
          ' aflat in exercitarea atributiilor de serviciu.')
    print('[4] 100.3.G - Neprezentarea la unitatea de politie competenta pe raza careia s-a produs\n'
          ' un accident de circulatie din care au rezultat numai pagube materiale.')
    print('[5] 100.3.H - Folosirea telefoanelor mobile atunci cand conducatorii de vehicule se afla\n'
          ' in timpul deplasarii pe drumurile publice, cu exceptia celor prevazute cu dispozitive tip\n'
          ' <<maini libere>>, concomitent cu incalcarea unei reguli pentru circulatia vehiculelor.')
    print('[6] 100.3.I - Adoptarea unui comportament agresiv in conducerea vehiculelor pe drumurile publice.\n')

def option2():
    pass

def option3():
    pass

def option4():
    pass

def option5():
    pass

def option6():
    pass

def option0():
    exit(0)

def valabilitate_dovada():
    pass


menu()

