def main(): #Definiujemy glowna funkcje
    try: #"Probojemy wywolac funkcje (obsluga bledow). Program wyswietli blad jezeli znajdzie blad"
        from database import keys as avaibleKeys #Importujemy baze danych
        import easydons  #Importujemy wlasnorecznie zrobiona biblioteke Easydons
        while True: #Nieskonczona petla
            isKeyCorrect = False #Definiujemy oraz przypisujemy zmiennej wartosc False
            key = str(input('Wprowadz klucz: ')) #Przyjmujemy dane do uzytkownika i zapisujemy je do zmiennej
            for i in range(len(avaibleKeys)): #Dla '1' w obszarze dostepnych kluczy. // Powtarza instrukcje tyle razy, ile jest kluczy w liscie
                if key == avaibleKeys[i]: #Sprawdzamy czy wprowadzony klucz odpowiada ktoremus z kluczy w liscie
                    isKeyCorrect = True #Zmieniamy wartosc zmiennej isKeyCorrect na True

            if not isKeyCorrect: #Jesli isKeyCorrect jest inne od prawdy (True)
                print('Niepoprawny klucz', 'Code: '+str(isKeyCorrect)) #Wyswietla informacje oraz podaje wartosc IsKeyCorrect
            else: #W przeciwnym razie (Jezeli isKeyCorrect jest prawda)
                print('Poprawny klucz!', 'Code: '+str(isKeyCorrect)) #Wyswietla informacje oraz podaje wartosc IsKeyCorrect
                isKeyCorrect = False #Zmieniamy wartosc zmiennej isKeyCorrect na Falsz (False)
                avaibleKeys.remove(key) #Usuwamy podany klucz z listy zapisanej w pamieci RAM
                database = open('database.py', 'w') #Otwieramy baze danych 
                message = 'keys = ' + str(avaibleKeys); database.write(message); database.close() #Usuwamy podany klucz z listy zapisanej w bazie danych (pliku database.py)
                
    except: #Instrukcje, co sie stanie jezeli wystapi blad
        print('Wystapil nieznany blad.') # Wyswietla informacje, tak samo reszta linijek w tej funkcji
        print()
        print('Program moze nie dzialac z nastepujacych powodow: ')
        print('Brak bazy danych (Brak potrzebnych plikow)')
        print('Brak wygenerowanych kluczy/pusta baza danych')
        print('Brak biblioteki easydons.py (Brak potrzebnych plikow)')
        print()
        print('Sprawdz ponizsze kroki:')
        print('Sprawdz czy plik "database.py" istnieje , a jak nie istnieje to go utworz go w takiej samej lokalizacji jak SprawdzanieKluczy.py, oraz wygeneruj klucze na nowo')
        print('Wygeneruj klucze na nowo')
        print()
        print('Jak powyzsze kroki nie zadzialaja, sproboj pobrac aplikacje od nowa.') 
        input()

if __name__ == '__main__': #Jezeli nazwa to jest '__main__'. Nazwa jest __main__ jezeli program zostal otworzony bezposrednio, a nazwa jest inna od __main__ jezeli program zostal otworzony przy pomocy innego skryptu np. za pomoca funkcji Import (slowami nie potrafie tego wytlumaczyc, o dokladniejsze znaczenie trzeba poszukac w internecie)
    main() #Uruchamiamy Głowna funkcje
 
