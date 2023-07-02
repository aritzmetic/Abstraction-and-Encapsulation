# Delera, Aritz B.

# Import the necessary modules
import time
import pyfiglet
import random
from termcolor import colored
from pyfiglet import Figlet
from car import Car

# make a class testCar
class testCar:
    # Allow the user to input for the card object.
    def __init__(self):

        f = Figlet(font='isometric2')
        print(colored(f.renderText('OOP'), 'blue'))

        # Create an introduction
        print("=" * 61)
        print("\033[32m Welcome to AritzMetic's Car Tester! \033[0m".center(60, "+"))
        print("=" * 61)

        # Ask the user for their name and make a greeting
        name = input("\033[30mHi Smart Pipol! what is your name?: \033[0m")
        print("\033[31mHi", name, "! AritzMetic is here to help you in navigating your Dream Car!!\033[0m")
        print()


    def run(self):
        time.sleep(1)
        print("\033[35mLet's create your dream car.\033[0m")
        time.sleep(1)
        print("\033[35mPlease provide the following details:\033[0m")
        time.sleep(1)
        print()
        print("\033[31m<>\033[0m" * 61)
        year_model = input("\033[30mWhat is the Year Model of your Car?: \033[0m")
        make = input("\033[30mWhat is the Manufacturer of your Car? (Make)?: \033[0m")
        print("\033[31m<>\033[0m" * 61)
        time.sleep(1)
        print("\033[35mGreat! Your car has been created.\033[0m")
        print()
        time.sleep(1)
        # Next, design a program that creates a Car object;
        self.car = Car(year_model, make)

        print("\033[31m==\033[0m" * 61)
        print("\033[36mYour car is ready to go!\033[0m")
        time.sleep(1)
        print("\033[36mLet's test its speed and braking capabilities.\033[0m")
        print("\033[31m==\033[0m" * 61)
        time.sleep(1)

        # then calls the accelerate method five times.
        for i in range(5):
            self.car.accelerate()
            # After each call to the accelerate method, get the current speed of the car and display it.
            print("\033[32m+=\033[0m" * 61)
            print(f"🚀 \033[33mAccelerating... Current speed: {self.car.get_speed()} mph\033[0m")
            time.sleep(0.5 * (i+1))
            print("\033[32m+=\033[0m" * 61)

        print()
        time.sleep(1)
        print("\nNow, let's apply the brakes.")
        time.sleep(1)
        print()

        # Then call the brake method five times.
        for i in range(5):
            self.car.brake()
            # After each call to the brake method, get the current speed of the car and display it.
            print("\033[32m+=\033[0m" * 61)
            print(f"🛑 \033[33mBraking... Current speed: {self.car.get_speed()} mph\033[0m")
            time.sleep(0.5 * (i+1))
            print("\033[32m+=\033[0m" * 61)

        time.sleep(1)
        print("\n\033[34mTest drive complete! It seems like you are ready to Drive. Congratulations!\033[0m")

