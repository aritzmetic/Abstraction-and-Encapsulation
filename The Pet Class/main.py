# Delera, Aritz B.

import time
from termcolor import colored
from pyfiglet import Figlet
from testPet import TestPet

def main():
    testPet = TestPet()

    while True:
        testPet.user_prompt()
        testPet.display_pet_information()
        testPet.display_random_trivia()
        testPet.display_current_date()

        choice = input("Do you want to have another pet? (yes/no): ")
        if choice.lower() != "yes":
            time.sleep(1)
            print("\033[35mThank you for using the AritzMetic Pet Creator. Your Dream Pet Information has been stored to another file! May your dreams be filled with extraordinary pets!💡\033[0m")
            print()
            f = Figlet(font='doom')
            print(colored(f.renderText('=THE END='), 'green'))
            break

if __name__ == "__main__":
    main()
