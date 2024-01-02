# Flashcard program to assist studying / 1st project build

from random import choice as ch
from time import sleep
import os

class Flashcard:
    def __init__(self):
        self.flashcards={'IP' : 'Internet Protocol',
                         'TCP' : 'Transmission Control Protocol',
                         'UDP' : 'User Datagram Protocol'}

    def quiz(self):
        while (True):
            term, definition = ch(list(self.flashcards.items()))

            print(term)
            answer = input('')
            if answer == '1':
                break

            elif (answer == definition.lower()):
                print('\nCorrect')
                sleep(1)
                os.system('clear')

            elif (answer != definition.lower()):
                print('\nIncorrect')
                sleep(1)
                os.system('clear')

            
os.system('clear')
fc = Flashcard()
print("Welcome to your flashcards, Brix\nEnter 0 at any time to exit.\nWhat would you like to do?\n")
choice = input("1) Quiz yourself\n2) Add a term and definition\nInput: ")

if choice == '1':
    os.system('clear')
    fc.quiz()
