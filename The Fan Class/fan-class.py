# Delera, Aritz B.

# (The Fan class).  Design a class named Fan to represent a fan. The class contains:
class Fan:
# ■ Three constants named SLOW, MEDIUM, and FAST with the values 1, 2, and 3 to denote the fan speed.
    SLOW = 1
    MEDUIM = 2
    FAST = 3

    # ■ A constructor that creates a fan with the specified speed (default SLOW), radius (default 5), color (default blue), and on (default False).
    def __init__(self, speed=SLOW, radius=5, color="blue", on=False):
        pass
# ■ A private int data field named speed that specifies the speed of the fan.
# ■ A private bool data field named on that specifies whether the fan is on (the default is False).
# ■ A private float data field named radius that specifies the radius of the fan.
# ■ A private string data field named color that specifies the color of the fan.
# ■ The accessor(getters)  and mutator(setters)  methods for all four data fields.
# ■ A constructor that creates a fan with the specified speed (default SLOW), radius (default 5), color (default blue), and on (default False).

# For the first object, 
# assign the maximum speed, 
# radius 10, 
# color yellow, and 
# turn it on. 

# for the second object,
# Assign medium speed, 
# radius 5, 
# color blue, and 
# turn it off 
# Display each object’s speed, radius, color, and on properties.
