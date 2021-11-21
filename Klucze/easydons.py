import random #Importujemy biblioteke random
import time #Importujemy biblioteke time


AllCharacters = [ #Definiujemy liste z znakami
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'o',
    'p',
    'r',
    's',
    't',
    'u',
    'w',
    'y',
    'z',
    'x',
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'R',
    'S',
    'T',
    'U',
    'W',
    'Y',
    'Z',
    'X',
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
]
Numbers09 = [ #Definiujemy liste z znakami
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
]

Numbers19 = [ #Definiujemy liste z znakami
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
]


def highlightedPrint(text): #Definiujemy funkcje do pisania wyróżnionych wiadomosci
    print() #Wysyla pustą linijka
    print(text) #Wysyla wiadomosc
    print() #Wysyla pustą linijka

def pickRandomListSubject(list): #Definiujemy funkcję do wybrania losowego obiektu (znaku) z listy // Parametry: list (lista)
    return list[random.randrange(0, len(list))] #Wybieramy losowy znak z listy

def generateRandomKeychain(keychainlenght, list): #Definiujemy funkcje do wygenerowania losowego lancucha znakow // Parametry: keychainlenght (okreslamy dlugosc lancucha znakow), list (lista)
    keychain = '' #Definiujemy zmienna keychain
    while True: #Nieskonczona petla
        character = pickRandomListSubject(list) #Wybieramy losowy znak i zapisujemy go do zmiennej
        keychain += str(character) #Edytujemy zmienna keychain, w taki sposob aby zapisywal sie do niej znak po znaku
        if len(keychain) == keychainlenght: #Jesli dlugosc zmiennej keychain jest taka sama jak zmienna keychainlenght/ Sprawdzamy czy dlugosc lancucha znakow jest taka sama jaka chcemy.
            return keychain #Zwracamy zmienna keychain


def generateKeychainsList(singlekeychainlenght, quantity, list): #Definiujemy funkcje do generowania listy z losowymi lancuchami znakow. // Parametry: singlekeychainlenght (dlugosc pojedynczego lancucha), quantity (ilosc lancuchow), list (lista)
    keychains = [] #Definiujemy pusta liste keychains
    for i in range(quantity): #Dla 'i' w obszarze wszystkich lancuchow znakow // Petla, ktora powtarza tyle, ile jest lancuchow znakow w liscie
        singleKeychain = generateRandomKeychain(singlekeychainlenght, list) #Za pomoca zapisanej wyzej, generujemy losowy lancuch znakow i zapisujemy go do zmiennej
        keychains.append(singleKeychain) #Dodajemy lancuch znakow do listy
        #Tutaj dokladnie nie pamietam dlaczego tak zapisalem, ale nie chce usuwac ze wzgledu na obawe przed bledami. Moze pani sprawdzic czy program bedzie dzialal bez tej linijki. (Obstawiam ze bedzie dzialal)
    return keychains #Zwracamy liste keychains
    