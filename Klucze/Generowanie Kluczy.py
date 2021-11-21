import easydons #Importujemy wlasnorecznie zrobiona biblioteke Easydons

database = open('database.py', 'w') #Otwieramy plik do pisania (nie do edycji)

keyQuantity = 10 #Ilosc kluczy, może pani zedytować ta wartosc (jezeli wartosc bedzie ciagiem znakow (np. 'asd' albo 'jeden') to wtedy program sie zatrzyma poniewaz uznalem ze do tego skryptu nie potrzeba zbytnio obslugi bledow, poniewaz nie jest to plik strikte pod edycje)
singleKeyLenght = 30 #Dlugosc pojedynczego klucza, moze pani zedytowac ta wartosc (jezeli wartosc bedzie ciagiem znakow (np. 'asd' albo 'jeden') to wtedy program sie zatrzyma poniewaz uznalem ze do tego skryptu nie potrzeba zbytnio obslugi bledow, poniewaz nie jest to plik strikte pod edycje)

def main(): #Definiujemy głowna funkcje
    keys = easydons.generateKeychainsList(singleKeyLenght, keyQuantity, easydons.AllCharacters) #Generujemy klucz i zapisujemy go do zmiennej
    print('Wygenerowano klucze. Nacisnij ENTER') #Wyswietlamy informacje o wygenerowanym kluczu
    message = 'keys = '+str(keys); database.write(message) #Zapisujemy klucze w bazie danych.
    print(keys) #Wyswietlamy klucze
    input() #Oczekiwanie na ENTERs

if __name__ == '__main__': #Jezeli nazwa to jest '__main__'. Nazwa jest __main__ jezeli program zostal otworzony bezposrednio, a nazwa jest inna od __main__ jezeli program zostal otworzony przy pomocy innego skryptu np. za pomoca funkcji Import (slowami nie potrafie tego wytlumaczyc, o dokladniejsze znaczenie trzeba poszukac w internecie)
    main() #Uruchamiamy Głowna funkcje