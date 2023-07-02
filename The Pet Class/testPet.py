# Delera, Aritz B.

# Import pet class
import time
import pyfiglet
import random
import datetime
from termcolor import colored
from pyfiglet import Figlet
from pet import Pet

# Once you have written the class, 
# write a program that creates an object of the class and 
class TestPet:
    def __init__(self):
        self.user_pet = Pet()

    # prompts the user to enter the name, type, and age of his or her pet. 
    def user_prompt(self):
        f = Figlet(font='isometric2')
        print(colored(f.renderText('OOP'), 'blue'))

        # Create an introduction
        print("=" * 61)
        print("\033[32m Welcome to AritzMetic's Pet Creator! \033[0m".center(60, "+"))
        print("=" * 61)

            # Ask the user for their name and make a greeting
        user_name = input("\033[30mHi Smart Pipol! what is your name?: \033[0m")
        print("\033[31mHi", user_name, "! AritzMetic is here to help you in making your dream friend!!\033[0m")
        print()

        print("==" * 61)
        print("\033[35mAnswer a few questions to create your unique companion.\033[31m")
        print("==" * 61)
        time.sleep(1)
        print()

        name = input("\033[30mWhat is the name of your pet?: \033[0m")
        animal_type = input("\033[30mWhat type of animal is he/she?(cat/dog/others): \033[0m")
        age = int(input("\033[30mWhat is his/her age?: \033[0m"))

        now = datetime.datetime.now()

        with open("pet_information.txt", "a") as file:
            file.write(f"OWNER: {user_name}\n")
            file.write(f"NAME: {name}\n")
            file.write(f"ANIMAL TYPE: {animal_type}\n")
            file.write(f"AGE: {age}\n")
            file.write(f"DATE: {now}\n")
            file.write("\n")

        # This data should be stored as the object’s attributes. 
        self.user_pet.set_name(name)
        self.user_pet.set_animal_type(animal_type)
        self.user_pet.set_age(age)

    # Use the object’s accessor methods to retrieve the pet’s name, type, and age and display this data on the screen.
    def display_pet_information(self):
        time.sleep(1)
        print(":" * 61)
        print("\033[33mProcessing...\033[0m" .center(70))
        print(":" * 61)
        time.sleep(3)
        print()
        print()
        print("<>" * 30)
        print("*****Your Dream Pet is Ready!*****")
        print("\033[36mNAME:", self.user_pet.get_name(),".\033[0m")
        print("\033[36mANIMAL TYPE:", self.user_pet.get_animal_type(),".\033[0m")
        print("\033[36mAGE:", self.user_pet.get_age(),".\033[0m")
        print("\033[36mEnjoy the magical bond with your dream pet!\033[0m")
        print()
        print("<>" * 30)
        print()
        time.sleep(4)

    def display_random_trivia(self):
        trivia = ["Did you know that having a pet might make you happier and less stressed?",
                "I bet you didn't know that pets make wonderful companions since they adore you no matter what.",
                "Did you know that spending time with your pet encourages you to get moving and adopt a healthier routine?",
                "Did you know that having a pet helps teach kids to be responsible and caring?",
                "Did you know that having a pet can boost your mood and sense of well-being?",
                "Did you know that pets can sense when people are feeling down and offer them support and comfort?"
                ]

        print("\033[31m::\033[0m" * 30)
        random_trivia = random.choice(trivia)
        print("\nRandom Pet Fact:")
        print(random_trivia)
        print()
        print("\033[31m::\033[0m" * 30)
        print()

    def display_current_date(self):
        now = datetime.datetime.now()
        print("\033[32m<>\033[0m" * 30)
        print("\nCurrent Date:")
        print(now.strftime("%Y-%m-%d"))
        print()
        print("\033[32m<>\033[0m" * 30)
        time.sleep(3)
        print()

