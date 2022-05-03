from random import randint

class My_action:
    """A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        die_number (int): The number of spots on the side facing up.
        one_five_point (int): The value of 1 and 5.
    """

    def __init__(self):

        """Constructs a new instance of Die.

        Args:
            self (Die): An instance of Die.
        """

        self.die_number = 0
        self.one_five_point = 0

    def die_action(self):
        """Generates a new random value and calculates the points for the die.
        
        Args:
            self (Die): An instance of Die.
        """

        self.die_number = randint(1,6)
        self.one_five_point = 100 if self.die_number == 1 else 50 if self.die_number == 5 else 0