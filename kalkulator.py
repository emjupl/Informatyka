import os
import time

def mnozenie(x, y):
    wynik = x * y
    return wynik

def dzielenie(x, y):
    wynik = x // y
    return wynik

def odejmowanie(x, y):
    wynik = x - y
    return wynik


def dodawanie(x, y):
    wynik = x + y
    return wynik

def error(text):
    print(text, 'Poczekaj 2 sekundy na wznowienie programu')
    time.sleep(2)
    os.system('cls')
    main()


def main():
    os.system('cls')
    print('1. Mnozenie')
    print('2. Dzielenie')
    print('3. Odejmowanie')
    print('4. Dodawanie')

    wybor = int(input('Wybierz opcje: '))
    if (wybor > 0 and wybor <= 4):
        try:
            int1 = int(input('Pierwsza liczba: '))
            int2 = int(input('Druga liczba: '))
        except: 
            error('Podaj liczbe, a nie ciag znakow!')
    else:
        error('Podaj jakas z opcji podanych powyzej!')

    if wybor == 1:
        print(int1, '*', int2, '=', mnozenie(int1, int2))
    elif wybor == 2:
        print(int1, '%', int2, '=', dzielenie(int1, int2))
    elif wybor == 3:
        print(int1, '-', int2, '=', odejmowanie(int1, int2))
    elif wybor == 4:
        print(int1, '+', int2, '=', dodawanie(int1, int2))
    print('Kliknij enter aby kontynuowac!')
    input()


if __name__ == '__main__':
    while True:
        try:
            main()
        except ValueError:
            error('Podaj liczbe, a nie ciag znakow!')
        except ZeroDivisionError:
            error('Nie mozna dzielic przez zero!')