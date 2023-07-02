import time
import pyfiglet
import random
from termcolor import colored
from pyfiglet import Figlet
from fan import Fan

f = Figlet(font='isometric2')
print(colored(f.renderText('OOP'), 'blue'))

# Create an introduction
print("=" * 61)
print("\033[32m Welcome to AritzMetic's Fan Getter & Setter! \033[0m".center(60, "+"))
print("=" * 61)

    # Ask the user for their name and make a greeting
name = input("\033[30mHi Smart Pipol! what is your name?: \033[0m")
print("\033[31mHi", name, "! AritzMetic👨🏼‍💻 is here to help you in navigating your Fans!!\033[0m")


# create a testfan class
class TestFan:
    def testrun(self):
        # For the first object, 
        # assign the maximum speed, 
        # radius 10, 
        # color yellow, and  
        # turn it on. 
        fan1 = Fan(speed=Fan.FAST, radius=10, color="yellow", on=True)

        # for the second object,
        # Assign medium speed, 
        # radius 5, 
        # color blue, and 
        # turn it off 
        fan2 = Fan(speed=Fan.MEDIUM, radius=5, color="blue", on=False)

        time.sleep(1)
        print(":" * 61)
        print("\033[33mProcessing...\033[0m" .center(70))
        print(":" * 61)
        time.sleep(3)
        print()
        print()
        print("\033[36m<>\033[0m" * 30)

        # Display each object’s speed, radius, color, and on properties.
        # print the fan1
        print("\033[33mHere are the properties of your FAN \033[0m1️⃣")
        print("\033[32mIts Speed ranges to", str(fan1.get_speed()) + ".\033[0m")
        print("\033[32mYour Fan 1 has a radius of", str(fan1.get_radius()) + ".\033[0m")
        print("\033[32mIt also has a color of", fan1.get_color() + ".")
        print("\033[32mand lastly, its power status is", str(fan1.is_on()) + ".\033[0m")

        print("\033[36m<>\033[0m" * 30)
        print()

        print()
        time.sleep(2)

        print("\033[36m<>\033[0m" * 30)


        # print the fan2
        print("\033[33mHere are the properties of your FAN \033[0m2️⃣")
        print("\033[31mIts Speed ranges to", str(fan2.get_speed()) + ".\033[0m")
        print("\033[31mYour Fan 2 has a radius of", str(fan2.get_radius()) + ".\033[0m")
        print("\033[31mIt also has a color of", fan2.get_color() + ".\033[0m")
        print("\033[31mand lastly, its power status is", str(fan2.is_on()) + ".\033[0m")

        print("\033[36m<>\033[0m" * 30)
        print()
        time.sleep(4)

        goodbye_quotes = [
                "Did you know that Fans have been used for centuries by ancient civilizations?👌🏻🤷🏻‍♂️",
                "Did you know that the first electric fan was a game-changer in the late 1800s?👌🏻🤷🏻‍♂️",
                "Did you know that the world's largest ceiling fan is 7.3 meters (24 feet) in diameter?👌🏻🤷🏻‍♂️",
                "Did you know that Japan's 'bladeless fans' use innovative air multiplier technology?👌🏻🤷🏻‍♂️"
             ]

        print("\033[35mThank you for using AritzMetic's Fan Getter & Setter! 💡\033[0m")
        print("{}".format(random.choice(goodbye_quotes)))
        f = Figlet(font='doom')
        print(colored(f.renderText('=THE END='), 'green'))



# Running the TestFan program
test_fan = TestFan()
test_fan.testrun()

