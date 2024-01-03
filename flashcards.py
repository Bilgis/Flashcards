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

    # Save current flashcard set into a JSON file
    def save_flashcards(self):
        with open(f'{self.set_name}.json', 'w') as file:
            json.dump(self.flashcards, file)

    # Provide key and answer with a value
    def quiz(self):
        while True:
            term, definition = ch(list(self.flashcards.items()))

            print('Press Enter to continue | Press 1 to go back to menu\n')

            print(term)
            answer = input()

            if answer == '0':
                fc.exit_program()

            elif answer == '1':
                os.system('clear')
                return 

            else:
                os.system('clear')
                print('Press Enter to continue | Press 1 to go back to menu\n')
                print(f'{term} : {definition}')
                input()
                os.system('clear')

            #elif answer.lower() == definition.lower():
                #print('\nCorrect')
                #sleep(1)
                #os.system('clear')
            #else:
                #print('\nIncorrect')
                #sleep(1)
                #os.system('clear')

    # Add a new item to the flashcard set
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

    # Show the items in the selected flashcard list
    def show_hand(self):
        count = 1
        for key, value in self.flashcards.items():
            print(f'({count}) {key} : {value}')
            count += 1

    # Create new flashcard sets
    def create_set(self):
        new_set_name = input("Set name: ")
        if new_set_name == '0':
            fc.exit_program()

        self.set_name = new_set_name
        self.flashcards = self.load_flashcards()
        self.save_flashcards()
        print(f'Flashcard Set: "{new_set_name}" was created successfully.')
        time.sleep(2)
        os.system('clear')

    # Select set if there are some available; If not provide error message
    def set_selection(self):
        set_names = [filename.split('.')[0] for filename in os.listdir() if filename.endswith('.json')]
    
        if not set_names:
            print("No flashcard sets found.")
            time.sleep(2)
            os.system('clear')
            fc.main_menu()
            return
        
        print("Available flashcard sets:")
        for i, set_name in enumerate(set_names, 1):
            print(f"{i}. {set_name}")

        set_index = input("\nEnter the number corresponding to the set you want to select: ")

        if set_index == '0':
            fc.exit_program()

        try:
            selected_set_name = set_names[int(set_index) - 1]
            self.set_name = selected_set_name
            self.flashcards = self.load_flashcards()
            os.system('clear')
            print(f"Selected flashcard set: {selected_set_name}")
            time.sleep(1)
            os.system('clear')
        except (ValueError, IndexError):
            print("Invalid selection.")
            time.sleep(1)
            os.system('clear')

    # Remove flashcard list 
    def delete_set(self):
        set_names = [filename.split('.')[0] for filename in os.listdir() if filename.endswith('.json')]
        
        if not set_names:
            print("No flashcard sets found.")
            os.system('clear')
            return

        print("Available flashcard sets:")
        for i, set_name in enumerate(set_names, 1):
            print(f"{i}. {set_name}")

        set_index = input("\nEnter the number corresponding to the set you want to delete: ")
        if set_index == '0':
            fc.exit_program()

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

    def exit_program(self):
        os.system('clear')
        print('Exiting program')
        time.sleep(1)
        os.system('clear')
        sys.exit()

    def main_menu(self):
        while (True):
            print("Welcome to Flashcards by Brix\nEnter 0 at any time to exit.\nWhat would you like to do?\n")

            init_choice = input("1) Select a flashcard set\n2) Create a new flashcard set\n3) Delete flashcard set\n\nInput: ")

            # Exit program
            if init_choice == '0':
                fc.exit_program()

            # Select flashcard set
            elif init_choice == '1':
                os.system('clear')
                fc.set_selection()
                break
           
            # Create new flashcard set
            elif init_choice == '2':
                os.system('clear')
                fc.create_set()
                continue

            # Delete flashcard set
            elif init_choice == '3':
                os.system('clear')
                fc.delete_set()
                continue

            else:
                print("Invalid input")
                time.sleep(1)
                os.system('clear')
                continue 


# If flashcards.py is called through a CLI 
if __name__ == '__main__':
    os.system('clear')
    fc = Flashcard()
    fc.main_menu()

    while True:
        choice = input("1) Quiz yourself\n2) Add a term and definition\n3) View flashcards\n4) Back to main menu\n\nInput: ")

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

        elif choice == '4':
            os.system('clear')
            fc.main_menu()
            
        elif choice == '0':
            print("Exiting program.")
            break

        else:
            print("Inavlid input")
            time.sleep(1)
            os.system('clear')
            continue
