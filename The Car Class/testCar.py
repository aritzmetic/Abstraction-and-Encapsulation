# Delera, Aritz B.

# Import the car class
import time
import pyfiglet
import random
import datetime
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


        time.sleep(1)
        print("Let's create your dream car.")
        time.sleep(1)
        print("Please provide the following details:")
        time.sleep(1)
        year_model = input("What is the Year Model of your Car?: ")
        make = input("What is the Manufacturer of your Car? (Make): ")
        time.sleep(1)
        print("Great! Your car has been created.")
        # Next, design a program that creates a Car object;
        self.car = Car(year_model, make)

    def run(self):

        print("\nYour car is ready to go!")
        time.sleep(1)
        print("Let's test its speed and braking capabilities.")
        time.sleep(1)

        # then calls the accelerate method five times. 
        for i in range(5):
            self.car.accelerate()
            # After each call to the accelerate method, get the current speed of the car and display it. 
            print(f"🚀 Accelerating... Current speed: {self.car.get_speed()} mph")
            time.sleep(0.5 * (i+1))

        time.sleep(1)
        print("\nNow, let's apply the brakes.")

    # Then call the brake method five times. 
        for i in range(5):
            self.car.brake()
            # After each call to the brake method, get the current speed of the car and display it.
            print(f"🛑 Braking... Current speed: {self.car.get_speed()} mph")
            time.sleep(0.5 * (i+1))

        time.sleep(1)
        print("\nTest drive complete! It seems like you are ready to Drive. Congratulations!")

test_car = testCar()
test_car.run()
