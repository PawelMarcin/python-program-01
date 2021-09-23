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
#  przyjecie danych kredytu:
wys_kredytu = input('Podaj wysokosc kredytu: ')
wys_oprocentowania = input('Podaj oprocentowanie ponad inflacje: ')
wys_stalej_raty = input('Podaj wysokosc raty: ')

# wypisanie danych startowych kredytu
print('\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('\nINFO:\n  Twoj kredyt: {} PLN\n  Oprocentowanie: {}%\n  Rata: {} PLN'
      .format(wys_kredytu, wys_oprocentowania, wys_stalej_raty))
print('\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

#-----------------------------------------------------------------------------
# wersja 1.0, wszystkie dane z pliku, wzor na obliczenia wg danych z zadania,
# calkiem od czapy
print('wersja 1.0')

