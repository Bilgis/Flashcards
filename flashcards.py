# Flashcard program to assist studying / 1st project build

# Import modules and methods
import json, os, sys, time
from random import choice as ch
from time import sleep

# Define flashcard class
class Flashcard:
    def __init__(self):
        self.flashcards = self.load_flashcards()

    # Load json file with terms and definitions
    def load_flashcards(self):
        try:
            with open('flashcards.json', 'r') as file:
                return json.load(file)
        # If no file found, return default dictionary
        except FileNotFoundError:
            return {'IP': 'Internet Protocol',
                    'TCP': 'Transmission Control Protocol',
                    'UDP': 'User Datagram Protocol'}

    def save_flashcards(self):
        with open('flashcards.json', 'w') as file:
            json.dump(self.flashcards, file)

    def quiz(self):
        while True:
            term, definition = ch(list(self.flashcards.items()))

            print(term)
            answer = input('')
            if answer == '1':
                break
            elif answer.lower() == definition.lower():
                print('\nCorrect')
                sleep(1)
                os.system('clear')
            else:
                print('\nIncorrect')
                sleep(1)
                os.system('clear')

    def new_entry(self, key, value):
        self.flashcards[key] = value
        self.save_flashcards()

    # Add method to delete an entry
    def delete_entry(self, pick):
        if pick in self.flashcards:
            del self.flashcards[pick]
            print(f'Entry "{pick}" deleted.')
            self.save_flashcards()
            time.sleep(1)
            os.system('clear')

        else:
            print(f'Entry "{pick}" not found.')
            os.system('clear')

    def show_hand(self):
        count = 1
        for key, value in self.flashcards.items():
            print(f'({count}) {key} : {value}')
            count += 1

if __name__ == '__main__':
    fc = Flashcard()

    if len(sys.argv) == 3:
        # If there are 3 arguments (file, key, value), they may be added in through the command line
        new_key = sys.argv[1]
        new_value = sys.argv[2]

        fc.new_entry(new_key, new_value)
        print(fc.flashcards)
        os.system('clear')

    os.system('clear')

    print("Welcome to Flashcards by Brix\nEnter 0 at any time to exit.\nWhat would you like to do?\n")

    while True:
        choice = input("1) Quiz yourself\n2) Add a term and definition\n3) View flashcards\n\nInput: ")

        if choice == '1':
            os.system('clear')
            fc.quiz()
        elif choice == '2':
            while True:
                os.system('clear')
                key = input("Enter side A: ")
                value = input("Enter side B: ")
                fc.new_entry(key, value)

                more = input('\n1) Add another\n2) Go back\n\n')

                if more == '1':
                    continue
                else:
                    print("Invalid input")
                    os.system('clear')
                    break

        elif choice == '3':
            os.system('clear')
            fc.show_hand()

            back_choice = input("\n\n1) Go back\n2) Delete Entry\n")

            if back_choice == '1':
                os.system('clear')
                continue

            elif back_choice == '2':
                os.system('clear')
                fc.show_hand()
                entry_to_delete = input("\n\nEnter the term you want to delete: ")
                fc.delete_entry(entry_to_delete)

            else:
                print('Not valid choice. Returning to main menu.')
                time.sleep(1)
                os.system('clear')
                
        

        elif choice == '0':
            print("Exiting program.")
            break

        else:
            print("Inavlid input")
            time.sleep(1)
            os.system('clear')
            continue
