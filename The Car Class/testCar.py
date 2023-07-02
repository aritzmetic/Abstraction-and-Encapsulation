# Delera, Aritz B.

# Import the car class
from car import Car

# make a class testCar
class testCar:
    # Allow the user to input for the card object.
    def __init__(self):
        year_model = input("What is the Year Model of your Car?: ")
        make = input("What is the Manufacturer of your Car? (Make): ")
        # Next, design a program that creates a Car object;
        self.car = Car(year_model, make)

    def run(self):
        # then calls the accelerate method five times. 
        for _ in range(5):
            self.car.accelerate()
            # After each call to the accelerate method, get the current speed of the car and display it. 
            print("Current speed:", self.car.get_speed())

    # Then call the brake method five times. 
        for _ in range(5):
            self.car.brake()
            # After each call to the brake method, get the current speed of the car and display it.
            print("Current speed:", self.car.get_speed())

test_car = testCar()
test_car.run()
