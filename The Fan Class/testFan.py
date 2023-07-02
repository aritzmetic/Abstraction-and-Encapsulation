# Delera, Aritz B.

from fan import Fan

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

        
        # Display each object’s speed, radius, color, and on properties.
        # print the fan1
        print("Here are the properties of your FAN 1!")
        print("Its Speed ranges to", str(fan1.get_speed()) + ".")
        print("Your Fan 1 has a radius of", str(fan1.get_radius()) + ".")
        print("It also has a color of", fan1.get_color() + ".")
        print("and lastly, its power status is", str(fan1.is_on()) + ".")

        print() 

        # print the fan2
        print("Here are the properties of your FAN 2!")
        print("Its Speed ranges to", str(fan2.get_speed()) + ".")
        print("Your Fan 2 has a radius of", str(fan2.get_radius()) + ".")
        print("It also has a color of", fan2.get_color() + ".")
        print("and lastly, its power status is", str(fan2.is_on()) + ".")


# Running the TestFan program
test_fan = TestFan()
test_fan.testrun()

