# Delera, Aritz B.

# Import pet class
from pet import Pet
# Once you have written the class, 
# write a program that creates an object of the class and 
class TestPet:
    def __init__(self):
        self.user_pet = Pet()
    # prompts the user to enter the name, type, and age of his or her pet. 
    def user_prompt(self):
        name = input("What is the name of ypur pet?: ")
        animal_type = input("What type of animal is he/she?(cat/dog/others): ")
        age = int(input("What is his/her age?: "))
# This data should be stored as the object’s attributes. 
# Use the object’s accessor methods to retrieve the pet’s name, type, and age and display this data on the screen.
