import random
import time
import os
import easydons

letters = [
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
    'n',
    'o',
    'p',
    'r',
    's',
    't',
    'u',
    'w',
    'y',
    'z'
]


def main():
    def pickRandomListSubject(list):
        randomSubject = list[random.randrange(0, len(list))]
        return randomSubject
    while True:
        os.system('cls')
        print('Liczba wczytanych obiektów w liście:', len(letters))
        wordChars = int(input('Podaj dlugosc hasla: '))

        for i in range(0, wordChars):
            word = ''
            word = word + pickRandomListSubject(easydons.AllCharacters)
            print(word, end='')
            
        print('')
        print('Kliknij Enter aby kontynuowac!')
        input()


try:
    if __name__ == '__main__':
        main()
except ValueError:
    os.system('cls')
    print('Podana wartość musi być Intem (cyfrą)!')
    time.sleep(2)
    main()
