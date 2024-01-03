# Flashcard program to assist studying / 1st project build

# Import modules and methods
import json, os, sys, time
from random import choice as ch
from time import sleep

# Define flashcard class
class Flashcard:
    # Define set name to allow different sets of flashcards
    def __init__(self):
        self.set_name = 'NA'
        self.flashcards = self.load_flashcards()
        

    # Load json file with terms and definitions
    def load_flashcards(self):
        try:
            with open(f'{self.set_name}.json', 'r') as file:
                return json.load(file)
        # If no file found, return default dictionary
        except FileNotFoundError:
            return {'This is ': 'A test'}

    def save_flashcards(self):
        with open(f'{self.set_name}.json', 'w') as file:
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

    def create_set(self):
        new_set_name = input("Set name: ")
        self.set_name = new_set_name
        self.flashcards = self.load_flashcards()
        self.save_flashcards()
        print(f'Flashcard Set: "{new_set_name}" was created successfully.')
        time.sleep(3)
        os.system('clear')

    def set_selection(self):
        # Add set selection method
        set_names = [filename.split('.')[0] for filename in os.listdir() if filename.endswith('.json')]
    
        if not set_names:
            print("No flashcard sets found.")
            return
        
        print("Available flashcard sets:")
        for i, set_name in enumerate(set_names, 1):
            print(f"{i}. {set_name}")

        set_index = input("\nEnter the number corresponding to the set you want to select: ")

        try:
            selected_set_name = set_names[int(set_index) - 1]
            self.set_name = selected_set_name
            self.flashcards = self.load_flashcards()
            os.system('clear')
            print(f"Selected flashcard set: {selected_set_name}")
            time.sleep(3)
            os.system('clear')
        except (ValueError, IndexError):
            print("Invalid selection.")

    def delete_set(self):
        set_names = [filename.split('.')[0] for filename in os.listdir() if filename.endswith('.json')]
        
        if not set_names:
            print("No flashcard sets found.")
            return

        print("Available flashcard sets:")
        for i, set_name in enumerate(set_names, 1):
            print(f"{i}. {set_name}")

        set_index = input("\nEnter the number corresponding to the set you want to delete: ")

        try:
            selected_set_name = set_names[int(set_index) - 1]
            confirmation = input(f"Are you sure you want to delete the flashcard set '{selected_set_name}'? (y/n): ")

            if confirmation.lower() == 'y':
                os.remove(f"{selected_set_name}.json")
                print(f"Flashcard set '{selected_set_name}' deleted.")
                time.sleep(3)
                os.system('clear')
            else:
                print("Deletion canceled.")
        except (ValueError, IndexError):
            print("Invalid selection.")




if __name__ == '__main__':
    os.system('clear')
    fc = Flashcard()

    while (True):
        print("Welcome to Flashcards by Brix\nEnter 0 at any time to exit.\nWhat would you like to do?\n")

        init_choice = input("1) Select a flashcard set\n2) Create a new flashcard set\n3) Delete flashcard set\n\nInput: ")

        if init_choice == '1':
            os.system('clear')
            fc.set_selection()
            break
            # Add method to select flashcard set     

        elif init_choice == '2':
            os.system('clear')
            fc.create_set()
            continue

        elif init_choice == '3':
            os.system('clear')
            fc.delete_set()
            continue



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
