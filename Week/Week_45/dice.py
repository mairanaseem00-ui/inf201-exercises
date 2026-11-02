

import random

# Creating the Dice class
class Dice:

    def __init__(self, sides: int = 6) -> None:
        """
        Initialise the Dice

        Args:
            sides (int): Number of sides on the dice (default = 6).
                         Must be at least 2.
        """  
        # Checking that the dice has at least 2 sides      
        if sides < 2:
            raise ValueError("Dice needs to have atleast 2 sides")
        
        # Storing the number of sides
        self.sides = sides


# Rolling the dice to generate a random number
    def roll(self) -> int:
        """
        Rolling a dice and return a random number.

        Returns:
            int: A random number between 1 and n number of sides.
        """

        return random.randint(1, self.sides)

# Representing the dice with its number of sides
    def __repr__(self) -> str:
        """
        Return a string that is a representatio of the dice.

        Returns:
            str: The dice and its number of sides.
        """

        return f"Dice(sides={self.sides})"

# Allowing the dice to be called directly like its a function
    def __call__(self) -> int:
        """
        Allows rolling by calling the object: d20() does the same as d20.roll().

        Returns:
            int: The result of rolling the dice
        """

        return self.roll()
