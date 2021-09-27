# Program do wyliczania pozostalej kwoty kredytu.
# Miesieczna kapitalizacja odsetek.
# Program powinien przyjmowac z terminala:
#       - kwote kredytu
#       - oprocentowanie (w procentach) powyzej inflacji
#       - wysokosc stalej miesiecznej raty
# Wartosci inflacji w kazdym miesiacu program powinien przyjmowac z pliku.
# Program zwraca wartosci dla 24 kolejnych miesiecznych rat w postaci:
#   <miesiac>: Twoja pozostala kwota kredytu: <X>. To o <Y> mniej niz
#   w poprzednim miesiacu."
#   -------------------------------------------------------------------------
#
#  utworzenie zmiennej string dla outputu:
output = '{} - {}:\n\t\tPozostala kwota kredytu: {}.\n\t\t To o {} mniej niz w poprzedm ' \
         'miesiacu.'
#
# utworzenie i zainicjowanie numeru kolejnego
# nr = 0  # - to juz nie jest potrzebne

#  Utworzenie i zainicjowanie zmiennych potrzebnych do obliczenia pozostalego
#  kredytu
# inflacja = float(0) # - inicjalizacja zmiennej nie jest potrzebna
# pozostaly_kredyt = float(0) # - inicjalizacja zmiennej nie jest potrzebna


#  przyjecie danych kredytu:
wys_kredytu = float(input('Podaj wysokosc kredytu: '))
wys_oprocentowania = float(input('Podaj oprocentowanie ponad inflacje: '))
wys_stalej_raty = float(input('Podaj wysokosc raty: '))

# wypisanie danych startowych kredytu
print('\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('\nINFO:\n  Twoj kredyt: {} PLN\n  Oprocentowanie: {}%\n  Rata: {} PLN'
      .format(wys_kredytu, wys_oprocentowania, wys_stalej_raty))
print('\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

# otwarcie pliku 'wersja_2_0.txt'
dane = open('wersja_2_0.txt','r')

# zamkniecie pliku 'wersja_2_0.txt'
dane.close()
