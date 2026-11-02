# Importing the Weapon class
from items import Weapon

class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int, damage: int, weapon: Weapon | None = None) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points of character.
            damage (int): Damage delt when character attacks.
            weapon (Weapon): Weapon used by sharacter.
            
        """
        self.name = name
        self._hp = hp_max  # Assume the character is created with max hp
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon
    
    # Reducing the character´s HP when taking damage
    def take_damage(self, amount:int) -> None:
        self._hp -= amount
        
        # Making sure HP does not go below 0
        self._hp = max(self._hp, 0)

    # Increasing the character´s HP when healing
    def heal(self, amount:int) -> None:
       self._hp += amount
       
       # Making sure HP does exceed max HP
       self._hp = min(self._hp, self.hp_max)

    # Attacking other character using take_damage
    def attack(self, target) -> None:

        # Checking if the character has a weapon
        if self.weapon is not None:
            
            # Rolling the weapon dice to calculate damage
            damage = self.weapon.roll_damage()
        
        # Checking if the character has no weapon
        else:   
            # Using the character's normal damage  
            damage = self.damage 
        
        # Reducing the target's HP based on the damage           
        target.take_damage(damage)

    # Introducing the character
    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    # Representing the character object
    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self._hp} damage={self.damage}>)"

    # Returning a readable description of the character
    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self._hp} HP and {self.damage} damage"
    
    # Getting the character's current HP
    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp
    
    # Checking if the character is alive
    @property
    def is_alive(self) -> bool:
        """Public read-only property to check if the character is alive."""
        return self._hp > 0
    
# Creating the Warrior subclass

class Warrior(Character):
    def __init__(self, name: str, hp_max: int, damage: int, weapon: Weapon | None = None, armor: int = 5) -> None:
        """
        Create the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points of character.
            damage (int): Damage delt when character attacks.
            weapon (Weapon): Weapon used by character.
            armor (int): Armor that reduces incoming damage. 
        """
        # Using the attributes from Character
        super().__init__(name, hp_max, damage, weapon)
        
        # Storing the warrior´s armor
        self.armor = armor

# Redusing damage using armor

    def take_damage(self, amount: int) -> None:
        """
        Reducing damage using armor.

        Args:
            amount (int): The incoming damage.
        """ 

        # Calculating the damage after armor
        damage = max(0, amount - self.armor)

        # Reducing Character´s HP using this method
        super().take_damage(damage)



# Creating the Mage subclass

class Mage(Character):
    def __init__(self, name: str, hp_max: int, damage: int, weapon: Weapon | None = None, mana: int = 30, mana_max: int = 30) -> None:
        """
        Create the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points of character.
            damage (int): Damage delt when character attacks.
            weapon (Weapon): Weapon used by character.
            mana (int): Mana that is avalible.
            mana_max (int): Maximum mana.
        """
        # Using the attributes from Character
        super().__init__(name, hp_max, damage, weapon)
        
        # Storing the mage's mana
        self.mana = mana
        self.mana_max = mana_max

    
# Redusing damage using armor

    def attack(self, target) -> None:
        """
       Using magic to attack if mana is available.

       Args:
            target (character): Character is being attacked
       """ 

        # Checking if mage has mana for magic and if we have enough
        
        if self.mana >= 10:
            # Using 10 mana
            self.mana -= 10

            # Calculating double damage 
            damage = self.damage * 2

            # Attack not using weapon
            target.take_damage(damage)

        # Using attack without mana if to low
        else:
            
            # Using Character´s attack methid
            super().attack(target)

            # Restoring 5 mana, without it going over maximum
            self.mana = min(self.mana + 5, self.mana_max)


# Creating the Battle class

class Battle:
    def __init__(self, hero: Character, enemy: Character) -> None:
        """
        Creating the Battle.

        Args:
            hero (Character): The hero in the battle.
            enemy (Character): The enemy in the battle.
        """
        
        # Storing the hero and enemy
        self.hero = hero
        self.enemy = enemy
    
    # Playing one round of the battle 
    def play_round(self) -> None:
        """
        Play one round of the battle.
        """

        # Hero attacks enemy
        self.hero.attack(self.enemy)
        
        # Enemy attacks hero if still alive
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)
    
    # Running the battle until one dies  
    def simulate_battle(self) -> None:
        """
        Running the battle until one character is dead.
        """
       
        # Continuing while both characters are alive
        while self.hero.is_alive and self.enemy.is_alive:

            self.play_round()
