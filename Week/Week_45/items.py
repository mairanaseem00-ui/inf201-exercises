from dice import Dice

# Creating the Weapon class

class Weapon:

    def __init__(self, name: str, damage_dice: Dice) -> None:
        
        """
        Create a weapon.

        Args:
            name (str): Name of the weapon.
            damage_dice (Dice): Dice is used for damage.
        """   
    

        # Storing the weapon name and damage dice
        self.name = name
        self.damage_dice = damage_dice
    
    # Rolling the dice to calculate the weapons damage 
    def roll_damage(self) -> int:
        """
        Rolling the dice to get weapon damage.

        Returns:
            int: Damage from the dice rolled.
        """

        return self.damage_dice.roll()