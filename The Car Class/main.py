# Delera, Aritz B.

from testCar import testCar
import random
from termcolor import colored
from pyfiglet import Figlet

# Create an instance of the testCar class
test_car = testCar()

# Run the testCar program inside a while loop
while True:
    test_car.run()

    # Ask the user if they want to test another car
    choice = input("\n\033[45mWould you like to test another car? (yes/no): \033[0m")
    if choice.lower() != "yes":
        # Make a random quote
        def get_random_goodbye_quote():
            quotes = [
                "Bye and drive safe! 🚗💨",
                "Farewell! Have a great time on the road! 🛣️😄",
                "Take care and have an awesome journey! ✨🌈",
                "Hope you have a safe trip and lots of fun! 🌟🎉",
                "Bye! Hope your car always takes you to awesome places! 🚙💫"
            ]
            return random.choice(quotes)

        print(get_random_goodbye_quote())
        print("\033[35mThank you for using AritzMetic's Car Tester! 💡\033[0m")
        f = Figlet(font='doom')
        print(colored(f.renderText('=THE END='), 'green'))
        break

