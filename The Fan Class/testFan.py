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
        # Display each object’s speed, radius, color, and on properties.
        fan2 = Fan(speed=Fan.MEDIUM, radius=5, color="blue", on=False)

        

