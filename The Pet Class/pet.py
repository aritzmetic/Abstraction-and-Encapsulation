# Delera, Aritz B.

# B. Pet Class
# Write a class named Pet, which should have the following data attributes:
class Pet:
    # • _ _name (for the name of a pet)
    # • _ _animal_type (for the type of animal that a pet is. Example values are ‘Dog’, ‘Cat’, and ‘Bird’)
    # • _ _age (for the pet’s age)
    # The Pet class should have an _ _init_ _ method that creates these attributes. It should also have the following methods:
    def __init__(self, name="", animal_type="", age=0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

# • set_name() This method assigns a value to the _ _name field.
    def set_name(self, name):
        self.__name = name
# • set_animal_type() This method assigns a value to the _ _animal_type field.
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
# • set_age() This method assigns a value to the _ _age field.
    def set_age(self, age):
        self.__age = age
# • get_name() This method returns the value of the _ _ name field.
    def get_name(self):
        return self.__name
# • get_animal_type() This method returns the value of the _ _animal_type field.
    def get_animal_type(self):
        return self.__animal_type
# • get_age() This method returns the value of the _ _age field.
    def get_age(self):
        return self.__age
